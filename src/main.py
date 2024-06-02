from scripts import CmdArgsParser, TripCalculator

if __name__ == "__main__":
    args_parser = CmdArgsParser()

    src, dst, stops, arrival_time = args_parser.get_arguments()

    trip_calculator = TripCalculator(
        from_address=src, to_address=dst, stops=stops, arrival_time=arrival_time
    )

    departure_time = trip_calculator.calc_trip_departure_time()

    print(f"leave {src} at {departure_time} to reach {dst} by {arrival_time}")
