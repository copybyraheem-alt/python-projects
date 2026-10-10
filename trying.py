import datetime

flight_time_str = "2026-11-20 18:30"

flight_datetime = datetime.datetime.strptime(flight_time_str, "%Y-%m-%d %H:%M")
now = datetime.datetime.now()

time_until_flight = flight_datetime - now

if time_until_flight.total_seconds() < 0:
    print("The flight has already departed.")
else:
    days = time_until_flight.days
    hours = time_until_flight.seconds // 3600
    minutes = (time_until_flight.seconds % 3600) // 60
    seconds = time_until_flight.seconds % 60

    print(f"Days left: {days}")
    print(f"Hours left: {hours}")
    print(f"Minutes left: {minutes}")
    print(f"Seconds left: {seconds}")

    formatted_date = flight_datetime.strftime("%A, %B %d, %Y")
    formatted_time = flight_datetime.strftime("%I:%M %p")
    print(f"Boarding on: {formatted_date} at {formatted_time}")
    print(f"Time remaining: {days}d {hours}h {minutes}m {seconds}s")