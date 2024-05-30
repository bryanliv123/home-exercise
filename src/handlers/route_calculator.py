import logging
from WazeRouteCalculator import WazeRouteCalculator

class RouteCalculator():
    def __init__(self) -> None:
        # set up logger
        logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')

        logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()

        logger.addHandler(handler)

    def calc_total_trip(self, from_address: str, to_address: str, stops, region: str = "IL") -> tuple():
        # try:
        #     route = WazeRouteCalculator(from_address, to_address, region)

        #     return route.calc_route_info()
        # except:
        #     raise Exception("Failed To Calculate Route!")
        pass

    def calc_route_between_two_points(self, from_address: str, to_address: str, region: str = "IL") -> tuple():
        try:
            route = WazeRouteCalculator(from_address, to_address, region)

            return route.calc_route_info()
        except:
            raise Exception("Failed To Calculate Route!")

