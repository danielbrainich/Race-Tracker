from datetime import timedelta

def calculate_percentile(result):
    finishers = result.finishers
    place = result.place

    try:
        if finishers > 0:
            return round(100 - place / finishers * 100)
    except (ValueError, ZeroDivisionError):
        return 0

def calculate_pace(result):
    try:
        distance = float(result.race.distance)
        time = result.time

        if isinstance(time, timedelta) and time.total_seconds() > 0:
            pace_seconds_per_mile = time.total_seconds() / distance
            minutes, seconds = divmod(pace_seconds_per_mile, 60)
            return f"{int(minutes):02d}:{round(seconds):02d}"
    except (ValueError, ZeroDivisionError):
        pass

    return "00:00"
