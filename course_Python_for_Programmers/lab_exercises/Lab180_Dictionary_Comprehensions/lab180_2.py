#!/usr/bin/env python3
"""lab180_2.py
temperatures at noon Mon - Fri: 80, 82, 85, 87, 76
percent chance of precipitation at noon Mon - Fri: 0, 2, 44, 100, 0
wind speed and direction at noon Mon - Fri: 2SW, 7SW, 3S, 10S, 2W
create dictionary with keys being each day’s names,
values are a tuple of (temp, precip, wind)
"""


def PrintWeather(*sequences):
    days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
    forecasts = {data[0]: data[1:] for data in zip(days, *sequences)}
    # print(forecasts)
    for day in sorted(forecasts, key=lambda d: days.index(d)):
        print(f"{day:>20}:", '\t'.join(f"{num:>10}" for num in forecasts[day]))


def main():
    temps = [80, 82, 85, 87, 76]
    precip = [0, 2, 44, 100, 0]
    wind = ["2SW", "7SW", "3S", "10S", "2W"]
    PrintWeather(temps, precip, wind)


if __name__ == "__main__":
    main()
