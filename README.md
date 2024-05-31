# Home Exercise

Home Exercise is a Python project for calculating trip start time.

## Example

```bash
$ python .\main.py --src eilat --dst Haifa --stops tel-aviv,1h,hadera,15m --arrival_time 20:30
```

* src - Trip Start Location
* dst - Trip Destination Location
* stops - Optional Stops Locations, And Duration In Each One
* arrival_time - Desired Arrival Time At Destination

## Output

```bash
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
