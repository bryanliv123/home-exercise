import argparse

from utils import split_array_into_tuples


class CmdArgsParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog="home-exercise")

        self.parser.add_argument("--src", help="Source City Name")
        self.parser.add_argument("--dst", help="Destination City Name")
        self.parser.add_argument("--stops", help="List of stops")
        self.parser.add_argument("--arrival_time", help="Arrival Time")

    def get_arguments(self):
        args = self.parser.parse_args()

        src, dst, stops, arrival_time = (
            args.src,
            args.dst,
            args.stops,
            args.arrival_time,
        )

        parsed_stops = split_array_into_tuples(stops.split(",")) if stops else []

        return src, dst, parsed_stops, arrival_time
