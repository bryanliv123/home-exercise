# Home Exercise

Home Exercise is a Python project for various trip calculations.

## Installation
```bash
$ pip install -r requirements.txt
```


## Usage

```bash
$ python .\main.py --src eilat --dst Haifa --stops tel-aviv,1h,hadera,15m --arrival_time 20:30
From: eilat - to: tel-aviv
Time 208.08 minutes, distance 340.90 km.
Stopping at tel-aviv for 60 minutes
From: tel-aviv - to: hadera        
Time 47.82 minutes, distance 50.40 km.
Stopping at hadera for 15 minutes
From: hadera - to: Haifa
Time 38.83 minutes, distance 50.72 km.
leave eilat at 14:20 to reach Haifa by 20:30
```
* --src - Trip Start Location
* --dst - Trip Destination Location
* --stops - Stops Locations, And Duration In Each One
* --arrival_time - Desired Arrival Time At Destination

### Trip without stops
```bash
$ python .\main.py --src ariel --dst tel-aviv --arrival_time 09:00
From: ariel - to: tel-aviv
Time 35.93 minutes, distance 48.19 km.
leave ariel at 08:24 to reach tel-aviv by 09:00
```

## Architecture
![image](https://github.com/bryanliv123/home-exercise/assets/60899499/807c3a5f-73b3-4d9c-8cd4-0e4221e58eff)

The program uses a class called TripCalculator which exposes several methods.

* calc_trip_departure_time - Calculate trip departure time in HH:mm format
* calc_trip_duration- Calculate trip duration in minutes
* calc_route_between_two_points - Calculate route info (duration, distance) between two locations
* get_all_trip_locations - Returns list of all trip locations

Under the hood, TripCalculator makes use of a package called WazeRouteCalculator.
TripCalculator provides a level of abstraction above this package, and added new features like stops and departure time calculation. 

```bash
trip_calculator = TripCalculator(from_address=src, to_address=dst, stops=stops, arrival_time=arrival_time)

departure_time = trip_calculator.calc_trip_departure_time()

print(f"leave {src} at {departure_time} to reach {dst} by {arrival_time}")
```

