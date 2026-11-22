def main():
    x = convert(input("What time is it? "))

    if 7.0 <= x <= 8.0 :
        print("Breakfast Time")
    elif 12.00 <= x <= 13.0 :
        print("Lunch Time")
    elif 18.00 <= x <= 19.00:
        print("Dinner Time")


def convert(time):
    time = time.split(":")
    hour = float(time[0])
    mins = float(time[1]) / 60

    return hour + mins

if __name__ == "__main__":
    main()
