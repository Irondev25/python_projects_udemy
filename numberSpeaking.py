from playsound import playsound


number = str(input("Enter a number: "))


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



def speakHundred(x):
    y = int(x)

    if 0 <= y <= 9:
        speakNumber(y)
    elif 10 <= y <= 19:
        speakNumber(y)
    elif 19 <= y <= 99:
        speakNumber(int(y / 10) * 10)
        if (y % 10) != 0:
            speakNumber(y % 10)
    elif 100 <= y <= 999:
        speakNumber(int(y / 100))
        speakNumber(100)
        z = y - int(y / 100) * 100
        if 0 < z <= 9:
            speakNumber(z)
        elif 10 <= y <= 19:
            speakNumber(z)
        elif 20 <= z <= 99:
            speakNumber(int(z / 10) * 10)
            if (z % 10) != 0:
                speakNumber(z % 10)



if 0 <= int(number) <= 999:
    speakHundred(number)
elif 1000 <= int(number) <= 999000:
    speakHundred(number[0:len(number)-3])
    speakNumber(1000)
    speakHundred(number[len(number)-3:])
elif 1000000 <= int(number) <= 999999999:
    speakHundred(number[0:len(number)-6])
    speakNumber(1000000)
    speakHundred(number[len(number)-6:len(number)-3])
    speakNumber(1000)
    speakHundred(number[len(number)-3:])



