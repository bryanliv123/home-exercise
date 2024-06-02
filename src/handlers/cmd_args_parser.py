import argparse
from typing import List

from utils import split_array_into_tuples


class CmdArgsParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog="home-exercise")

        self.parser.add_argument("--src", help="Source City Name")
        self.parser.add_argument("--dst", help="Destination City Name")
        self.parser.add_argument("--stops", help="List of stops")
        self.parser.add_argument("--arrival_time", help="Arrival Time")

    def validate_stops_pattern(self, argument: List[str]):
        """Validate that stops argument in correct format"""

        if len(argument) % 2 != 0:
            raise argparse.ArgumentTypeError("Invalid number of stops arguments.")

        for i in range(0, len(argument), 2):
            location = argument[i]
            duration = argument[i + 1]

            if not isinstance(location, str) or not (
                duration.endswith("h") or duration.endswith("m")
            ):
                raise argparse.ArgumentTypeError(
                    f"Invalid stops argument types at position {i+1} and {i+2}. Must be str, duration"
                )

    def get_arguments(self):
        args = self.parser.parse_args()

        src, dst, stops, arrival_time = (
            args.src,
            args.dst,
            args.stops,
            args.arrival_time,
        )

        stops_list: List[str] = stops.split(",") if stops else []

        try:
            self.validate_stops_pattern(stops_list)
        except argparse.ArgumentTypeError as e:
            self.parser.error(str(e))

        parsed_stops = split_array_into_tuples(stops_list)

        return src, dst, parsed_stops, arrival_time
