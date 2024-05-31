from __future__ import annotations
import logging
from WazeRouteCalculator import WazeRouteCalculator

from utils import time_to_minutes, time_to_minutes_after_midnight, minutes_after_midnight_to_time

class TripCalculator():
    """Calculate trip duration and departure time"""

    def __init__(self, from_address: str, to_address: str, stops: list[tuple], arrival_time: str, region: str = "IL") -> None:
        """Inits Trip Calculator Class.

        Args:
            from_address: Source City Name (str).
            to_address: Destination City Name (str).
            stops: Optional Stops (List of tuples(city name, duration in minutes)).
            arrival_time: Arrival Time At Destination City (str)
            region: Optional Region (defaults to "IL")
        """
        
        # set up logger
        logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        logger.addHandler(handler)

        self.stops = stops
        self.region = region
        self.to_address = to_address
        self.from_address = from_address
        self.arrival_time = arrival_time

        self.duration_per_stop = dict((x, time_to_minutes(y)) for x, y in stops)

        self.total_trip_time = self.calc_trip_duration()
        
    def calc_trip_duration(self) -> tuple():
        '''Calculate trip duration in minutes'''

        duration_per_stop = self.duration_per_stop

        total_trip_time = 0

        all_trip_locations = self.get_all_trip_locations()

        for i in range(0, len(all_trip_locations) - 1):
            src = all_trip_locations[i]
            dst = all_trip_locations[i + 1]

            info = self.calc_route_between_two_points(src, dst)

            duration_in_minutes = info[0]

            total_trip_time += duration_in_minutes

            # check if dst is one of the stops
            if dst in duration_per_stop:
                stop_duration = self.duration_per_stop[dst]

                print(f'stopping at {dst} for {stop_duration} minutes')

                total_trip_time += stop_duration

        return total_trip_time

    def calc_route_between_two_points(self, src: str, dst: str, region: str = "IL") -> tuple():
        '''Calculate route time using Waze API'''
        
        try:
            route = WazeRouteCalculator(src, dst, region)
            
            return route.calc_route_info()
        except:
            raise Exception("Failed To Calculate Route!")
    
    def calc_trip_departure_time(self):
        '''Calculate trip departure time in HH:mm format'''

        arrival_time, total_trip_time = self.arrival_time, self.total_trip_time

        # Convert arrival_time to number of minutes
        arrival_time_in_minutes = time_to_minutes_after_midnight(arrival_time)

        res = arrival_time_in_minutes - total_trip_time

        # Convert minutes to HH:mm format
        return minutes_after_midnight_to_time(res)

    def get_all_trip_locations(self):
        '''Return list of all trip locations'''
        
        from_address, to_address, stops = self.from_address, self.to_address, self.stops

        stops_locations: list[str] = []

        for stop in stops:
            location = stop[0]

            stops_locations.append(location)

        return [from_address, *stops_locations, to_address]
