from playsound import playsound


def speakNumber(x):
    if x == 0:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/0.wav")
    elif x == 1:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/1.wav")
    elif x == 2:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/2.wav")
    elif x == 3:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/3.wav")
    elif x == 4:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/4.wav")
    elif x == 5:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/5.wav")
    elif x == 6:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/6.wav")
    elif x == 7:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/7.wav")
    elif x == 8:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/8.wav")
    elif x == 9:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/9.wav")
    elif x == 10:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/10.wav")
    elif x == 11:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/11.wav")
    elif x == 12:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/12.wav")
    elif x == 13:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/13.wav")
    elif x == 14:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/14.wav")
    elif x == 15:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/15.wav")
    elif x == 16:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/16.wav")
    elif x == 17:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/17.wav")
    elif x == 18:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/18.wav")
    elif x == 19:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/19.wav")
    elif x == 20:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/20.wav")
    elif x == 30:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/30.wav")
    elif x == 40:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/40.wav")
    elif x == 50:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/50.wav")
    elif x == 60:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/60.wav")
    elif x == 70:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/70.wav")
    elif x == 80:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/80.wav")
    elif x == 90:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/90.wav")
    elif x == 100:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/hundred.wav")
    elif x == 1000:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/thousand.wav")
    elif x == 1000000:
        playsound("/home/irondev/PycharmProjects/python_projects_udemy/audio-numbers/million.wav")



def proOnes(x):
    if x != 0:
        playsound(x)

def proTens(x):
    y = str(x)
    if x[0] != 0:
        if int(y[0]) == 0:
            proOnes(int(y[1]))
        elif 10 <= x <= 19:
            playsound(x)
        else:
            x = str(x)
            playsound(int(x[0]) * 10)
            playsound(x[1])


def proHundred(x):
    if x != 0:
        playsound(x)
        playsound(100)

def proThousand(x):
    y = str(x)
    if x != 0:
        if x <= 9:
            proOnes(x)
            playsound(1000)
        elif 100>x>9:
            proTens(x)
            playsound(1000)
        elif x >= 100:
            proHundred(int(y[0]))
            proOnes(int(y[1:]))



def