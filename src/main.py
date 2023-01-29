import psutil
import schedule
import datetime
from time import sleep

interval = 60
output_file = "battery.csv"

def task():
    with open(output_file, "a") as f:
        btr = psutil.sensors_battery()
        print(f"{datetime.datetime.today()},{btr.percent},{btr.power_plugged}", file=f)
        print(f"{datetime.datetime.today()}\t{btr.percent}\t\t{btr.power_plugged}")

if __name__ == "__main__":
    print("########################################")
    print("##########   Battery  Watch   ##########")
    print("########################################")
    print(f"interval: {interval}[sec]")
    print(f"output_file: {output_file}")
    print("Use Ctrl-C to exit")
    print("")
    print(f"Executing...")
    print("[date]\t\t\t\t[percent]\t[power_plugged]")
    task()
    schedule.every(interval).seconds.do(task)
    while True:
        schedule.run_pending()
        sleep(1)
