def add_time(start, duration, starting_day=None):
    # Helper function to convert 12-hour time format to 24-hour time format
    def to_24_hour_format(hour, period):
        if period == "PM" and hour != 12:
            hour += 12
        if period == "AM" and hour == 12:
            hour = 0
        return hour

    # Helper function to convert 24-hour time format to 12-hour time format
    def to_12_hour_format(hour):
        period = "AM" if hour < 12 else "PM"
        hour = hour % 12
        if hour == 0:
            hour = 12
        return hour, period

    # Days of the week in order
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start time to 24-hour format
    start_hour = to_24_hour_format(start_hour, period)

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calculate the new time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute = end_minute % 60
    days_later = end_hour // 24
    end_hour = end_hour % 24

    # Convert back to 12-hour format
    end_hour, end_period = to_12_hour_format(end_hour)

    # Format the time string
    end_time = f"{end_hour}:{end_minute:02d} {end_period}"

    # Determine the new day of the week if starting day is provided
    if starting_day:
        starting_day = starting_day.capitalize()
        start_day_index = days_of_week.index(starting_day)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        end_time += f", {end_day}"

    # Append the number of days later
    if days_later == 1:
        end_time += " (next day)"
    elif days_later > 1:
        end_time += f" ({days_later} days later)"

    return end_time
