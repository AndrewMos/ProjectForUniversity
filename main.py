import operator
import time
from help import *
import threading
from apscheduler.schedulers.blocking import BlockingScheduler

citizens_list = []

def job_function():
    rewrite_result(citizens_list)

def cron_function():
    sched = BlockingScheduler()
    sched.add_job(job_function, 'cron', second='0, 30')
    sched.start()

t = threading.Thread(target=cron_function)
t.start()

print ("ddd")
while 1:
    citizen = add_sitizen()
    if (citizen != 0):
        for i in citizens_list:
            if (i.pesel == citizen.pesel):
                citizens_list.remove(i)
        citizens_list.append(citizen)
