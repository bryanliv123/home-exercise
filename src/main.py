from route_calculator import RouteCalculator

if __name__ == "__main__":
    route_calculator_handler = RouteCalculator()
    result = route_calculator_handler.calc_route(from_address="haifa", to_address='tel aviv')
    print(result)
