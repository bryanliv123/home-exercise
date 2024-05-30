import argparse

class CmdArgsParser():
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog='home-exercise')

        self.parser.add_argument('--src', help='Source City Name')
        self.parser.add_argument('--dst', help='Destination City Name')
        self.parser.add_argument('--stops', help='List of stops')
        self.parser.add_argument('--arrival_time', help='Arrival Time')

        self.parser.print_help()

    def get_arguments(self):
        return self.parser.parse_args()