# Home Exercise

Home Exercise is a Python project for calculating trip start time.

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
stops is an optional list
```bash
$ python .\main.py --src ariel --dst tel-aviv --arrival_time 09:00
From: ariel - to: tel-aviv
Time 35.93 minutes, distance 48.19 km.
leave ariel at 08:24 to reach tel-aviv by 09:00
```
