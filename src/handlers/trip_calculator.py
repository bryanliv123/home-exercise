from __future__ import annotations

import logging
from typing import Dict, List, Tuple

from WazeRouteCalculator import WazeRouteCalculator

from utils import subtract_minutes_from_time, time_to_minutes

from .trip_calculator_types import RouteInfo


class TripCalculator:
    def __init__(
        self,
        from_address: str,
        to_address: str,
        stops: List[Tuple[str, str]],
        arrival_time: str,
        region: str = "IL",
    ) -> None:
        """Calculate trip duration and departure time

        Args:
            from_address: Source City Name (str).
            to_address: Destination City Name (str).
            stops: Optional Stops (List of tuples (Location, Duration)).
            arrival_time: Arrival Time At Destination City (str)
            region: Optional Region (defaults to "IL")
        """
        self.__setup_logger__()

        self.region = region
        self.to_address = to_address
        self.from_address = from_address
        self.arrival_time = arrival_time

        # Store each stop and duration
        # {"stop_name": duration, ...}
        self.stops = dict((x, time_to_minutes(y)) for x, y in stops)

        # Save each route and its calculated result
        self.previous_routes: Dict[str, RouteInfo] = {}

    def calc_trip_departure_time(self):
        """Calculate trip departure time in HH:mm format"""

        # Calculate total trip duration in minutes
        total_trip_time = self.calc_trip_duration()

        # Subtract total trip time from desired arrival time
        return subtract_minutes_from_time(total_trip_time, self.arrival_time)

    def calc_trip_duration(self) -> float:
        """Calculate trip duration in minutes"""

        stops = self.stops

        total_trip_time: float = 0

        all_trip_locations = self.get_all_trip_locations()

        for i in range(len(all_trip_locations) - 1):
            src = all_trip_locations[i]
            dst = all_trip_locations[i + 1]

            info = self.calc_route_between_two_points(src, dst)

            duration_in_minutes = info[0]

            total_trip_time += duration_in_minutes

            # check if dst is one of the stops
            if dst in stops:
                stop_duration = stops[dst]

                print(f"Stopping at {dst} for {stop_duration} minutes")

                total_trip_time += stop_duration

        return total_trip_time

    def calc_route_between_two_points(
        self, src: str, dst: str, region: str = "IL"
    ) -> RouteInfo:
        """Calculate route time using Waze API"""

        key = f"{src.lower()}-{dst.lower()}"

        if key in self.previous_routes:
            # Route has already been calculated
            return self.previous_routes[key]

        try:
            route = WazeRouteCalculator(src, dst, region)

            route_info = route.calc_route_info()

            # Save route info
            self.previous_routes[key] = route_info

            return route_info
        except:
            raise Exception("Failed To Calculate Route!")

    def get_all_trip_locations(self) -> list[str]:
        """Return list of all trip locations"""

        from_address, stops, to_address = self.from_address, self.stops, self.to_address

        stops_locations = list(stops.keys())

        return [from_address, *stops_locations, to_address]

    def __setup_logger__(self):
        # set up logger
        logger = logging.getLogger("WazeRouteCalculator.WazeRouteCalculator")

        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()

        logger.addHandler(handler)
