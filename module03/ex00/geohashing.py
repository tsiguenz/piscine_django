#!/usr/bin/python3

import sys


def usage():
    print("Usage: python3 geohashing.py <latitude> <longitude> <date>")
    print(
        'Exemple: python3 geohashing.py "37.421542" "122.085589" "2005-05-26010458.68"'
    )


def main():
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3].encode()

        import antigravity

        antigravity.geohash(latitude, longitude, date)
    except Exception as e:
        print("Error:", e)
        usage()


if __name__ == "__main__":
    main()
