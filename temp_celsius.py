import sys


if len(sys.argv) != 2:
    print("Usage: python temp_check.py <temperature_in_celsius>")
else:
    T = float(sys.argv[1]) 

    if T < 15:
        print("Weather condition: Cold ")
    elif 15 <= T <= 30:
        print("Weather condition: Normal ")
    else:
        print("Weather condition: Hot ")
