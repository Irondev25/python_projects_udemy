import time
from playsound import playsound

#function for getting their alarm input
def get_alarm_time():
    hours = float(input("Enter hour(24 hour system): "))
    minute = float(input("Enter minute: "))
    second = float(input("Enter second: "))

    return (hours*60*60) + (minute*60) + second

#function for getting current time
def get_current_time():
    return time.time()


#fuction to play audio
def for_ringing_the_bell():
    playsound("/home/irondev/Downloads/alarm.mp3")


def stopwatch():
    total_time = get_alarm_time() + get_current_time()
    while total_time >= time.time():
        continue

    for_ringing_the_bell()




stopwatch()



