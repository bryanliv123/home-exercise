from handlers import CmdArgsParser, TripCalculator
from utils import split_array_into_tuples

if __name__ == "__main__":
    args_parser = CmdArgsParser()

    args = args_parser.get_arguments()

    src, dst, stops, arrival_time = args.src, args.dst, args.stops, args.arrival_time
    
    stops_tuples = split_array_into_tuples(stops.split(','))

    trip_calculator = TripCalculator(from_address=src, to_address=dst, stops=stops_tuples, arrival_time=arrival_time)

    departure_time = trip_calculator.calc_trip_departure_time()

    print(f"leave {src} at {departure_time} to reach {dst} by {arrival_time}")
