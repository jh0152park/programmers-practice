import sys
import math


sun_before, sun_back = map(int, sys.stdin.readline().strip().split())
moon_before, moon_back = map(int, sys.stdin.readline().strip().split())

sun_year = sun_back - sun_before
moon_year = moon_back - moon_before

while sun_year != moon_year:
    if sun_year < moon_year:
        sun_year += sun_back
    else:
        moon_year += moon_back

print(sun_year)