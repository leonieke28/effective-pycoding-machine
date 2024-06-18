import os
import re
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def get_unique_dates_from_logs(logs):
    return set(re.search(r"\d{2}-\d{2}", line).group() for line in logs)


def populate_books_by_date(logs, unique_dates):
    books_by_date = {date: "" for date in unique_dates}

    for i, line in enumerate(logs):
        if "sending to slack channel" in line:
            date = re.search(r"\d{2}-\d{2}", line).group()
            if "Python" in logs[i - 1]:
                books_by_date[date] += PY_BOOK
            else:
                books_by_date[date] += OTHER_BOOK

    return books_by_date


def print_books_by_date(books_by_date):
    for date in sorted(books_by_date.keys()):
        print(date, books_by_date[date])


def create_chart():
    with open(SAFARI_LOGS) as f:
        logs = f.readlines()

    unique_dates = get_unique_dates_from_logs(logs)
    books_by_date = populate_books_by_date(logs, unique_dates)

    print_books_by_date(books_by_date)


create_chart()
