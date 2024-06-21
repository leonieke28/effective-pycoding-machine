from datetime import datetime, timedelta

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime("2018-02-26 23:24:04", "%Y-%m-%d %H:%M:%S")


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
    left on Planet Earth (calculated from start_date)"""
    time_left_earth = PY2_DEATH_DT - start_date
    earth_hours_left = time_left_earth.total_seconds() / 3600
    return round(earth_hours_left, 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
    left on Planet Miller (calculated from start_date)"""
    earth_hours_left = py2_earth_hours_left(start_date)
    miller_minutes_left = earth_hours_left * 60 / (7 * 365 * 24)
    return round(miller_minutes_left, 2)
