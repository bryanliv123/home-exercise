from handlers import CmdArgsParser, RouteCalculator

if __name__ == "__main__":
    args_parser = CmdArgsParser()

    route_calculator_handler = RouteCalculator()

    args = args_parser.get_arguments()

    from_address = args.src

    to_address = args.dst

    result = route_calculator_handler.calc_route(from_address, to_address)

    print(result)
