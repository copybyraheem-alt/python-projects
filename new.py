import datetime
import time


def validate_alarm_time(alarm_time_str: str) -> datetime.time:
    """Validate that the alarm time string follows the 'HH:MM:SS' format.

    Args:
        alarm_time_str: Time string in 'HH:MM:SS' (24-hour) format.

    Returns:
        datetime.time: The parsed time object.

    Raises:
        ValueError: If the format or time values are invalid.
    """
    try:
        return datetime.datetime.strptime(alarm_time_str, "%H:%M:%S").time()
    except ValueError:
        raise ValueError(
            f"Invalid time format '{alarm_time_str}'. Please use HH:MM:SS (24-hour format, e.g., 07:30:00)."
        )


def set_alarm(alarm_time_str: str) -> None:
    """Set an alarm and wait until the target time is reached.

    Args:
        alarm_time_str: Target alarm time formatted as 'HH:MM:SS'.
    """
    alarm_time = validate_alarm_time(alarm_time_str)

    # Determine target datetime (today or tomorrow if the time has already passed)
    now = datetime.datetime.now()
    target_datetime = datetime.datetime.combine(now.date(), alarm_time)

    if target_datetime <= now:
        target_datetime += datetime.timedelta(days=1)
        print(f"Alarm set for tomorrow at {alarm_time_str}.")
    else:
        print(f"Alarm set for today at {alarm_time_str}.")

    print("Alarm active. Press Ctrl+C to cancel.\n")

    try:
        # Loop until current time reaches or passes the target time
        while datetime.datetime.now() < target_datetime:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            # Update the current line in terminal to avoid spamming the screen
            print(f"\rCurrent Time: {current_time} | Alarm Time: {alarm_time_str}", end="", flush=True)
            time.sleep(1)

        # Trigger alarm
        final_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\rCurrent Time: {final_time} | Alarm Time: {alarm_time_str}")
        print("\n" + "=" * 35)
        print("  WAKE UP!! Alarm ringing!  \a")
        print("=" * 35)

    except KeyboardInterrupt:
        print("\n\nAlarm cancelled by user.")


# Backward compatibility alias for the previous typo
set_alaram = set_alarm


if __name__ == "__main__":
    while True:
        try:
            user_alarm = input("Enter alarm time (HH:MM:SS): ").strip()
            validate_alarm_time(user_alarm)
            set_alarm(user_alarm)
            break
        except ValueError as err:
            print(f"Error: {err}\nPlease try again.\n")
        except KeyboardInterrupt:
            print("\nExiting.")
            break
