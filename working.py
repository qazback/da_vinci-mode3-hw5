import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(1[0-2]|0?[1-9])\s?(AM|PM)\s?to\s(1[0-2]|0?[1-9])\s?(AM|PM)$"
    match = re.search(pattern, s)
    if match:
        start_hour = int(match.group(1))
        start_meridiem = match.group(2)
        end_hour = int(match.group(3))
        end_meridiem = match.group(4)
        if start_meridiem == "PM" and start_hour != 12:
            start_hour += 12
        if end_meridiem == "PM" and end_hour != 12:
            end_hour += 12
        if start_hour >= 24 or end_hour >= 24 or start_hour > end_hour:
            raise ValueError("Invalid time range")
        return f"{start_hour:02}:00 to {end_hour:02}:00"
    else:
        raise ValueError("Invalid time format")


if __name__ == "__main__":
    main()
