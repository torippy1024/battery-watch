import psutil
import schedule
import datetime
from time import sleep

interval = 60

def task():
    with open("battery.csv", "a") as f:
        btr = psutil.sensors_battery()
        print(f"{datetime.datetime.today()},{btr.percent},{btr.power_plugged}", file=f)

schedule.every(interval).seconds.do(task)

while True:
    schedule.run_pending()
    sleep(1)
