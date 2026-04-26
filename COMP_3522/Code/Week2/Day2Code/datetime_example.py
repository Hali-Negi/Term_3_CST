"""This module depicts the datetime module in use"""
from datetime import datetime
import time


def main():
    """Some common operations using the datetime module"""

    # Accessing system time
    print("Accessing System Time")
    print("---------------------")
    local_time_now = datetime.now()
    utc_time_now = datetime.utcnow()
    print(f"Local Now: {local_time_now}")
    print(f"Local Date: {local_time_now.date()}")
    print(f"Local Time: {local_time_now.time()}")
    print(f"Local Timestamp (epoch): {local_time_now.timestamp()}")
    print(f"UTC Now: {utc_time_now}")
    print(f"UTC Date: {utc_time_now.date()}")
    print(f"UTC Time: {utc_time_now.time()}")
    print(f"UTC Timestamp (epoch): {utc_time_now.timestamp()}")
    print(type(utc_time_now), end="\n\n")

    # Accessing individual attributes
    print("Accessing individual attributes")
    print("-------------------------------")
    print(f"Local (Hours): {local_time_now.hour}")
    print(f"Local (Minutes): {local_time_now.minute}")
    print(f"Local (Seconds): {local_time_now.second}")
    print(f"Local (microseconds): {local_time_now.microsecond}")

    # Putting system to sleep
    print("\nSleeping for 2 seconds..", end="\n\n")
    time.sleep(2)

    # Datetime time arithmetic
    print("DateTime Arithmetic")
    print("-------------------")
    deltatime = utc_time_now - local_time_now
    print(f"Time Difference: {deltatime}")
    print(f"Time Diff in seconds: {deltatime.total_seconds()}")
    print(f"Time Diff in days: {deltatime.days}")
    print(f"Time Diff in minutes: {deltatime.total_seconds()/60}")
    print(type(deltatime), end = "\n\n")

    # Datetime formatting display
    print("Date Time Formatting")
    print("--------------------")
    utc_formatted = utc_time_now.strftime("%H:%M:%S")
    utc_formatted_date = utc_time_now.strftime("%d/%m/%Y")
    print(f"UTC Time Formatted: {utc_formatted}")
    print(f"UTC Date formatted: {utc_formatted_date}")




if __name__ == '__main__':
    main()