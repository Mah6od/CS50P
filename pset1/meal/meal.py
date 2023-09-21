def main():
    time_input = input("what time is it? ")

    try:
        times = convert(time_input)

        if 7.0 <= times <= 8.0:
            print("breakfast time")
        elif 12.0 <= times <= 13.0:
            print("lunch time")
        elif 18.0 <= times <= 19.0:
            print("dinner time")

    except ValueError:
        print("Invalid time format. Please use hh:mm format.")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    total_time = hours + (minutes / 60)
    return total_time

if __name__ == "__main__":
    main()
