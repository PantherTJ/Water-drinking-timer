# imports things
import time
import pygame
from pygame import mixer
import threading

pygame.init()
# gives time
time_obj = time.localtime()

# n is number of glasses
n = 1

secs_min = 60  # how many seconds in minutes
min_hr = 60  # how many mins in hour

res_in_time = True  # used to find if the input is given during or after 5 minutes

timer_run = True  # it's used to count time in "mintimer_5" function
# they store threads for starting functions
threads1 = []  # 5 min timer
threads2 = []  # time left query and input for water drunk function:'input_management'
threads3 = []  # 1 hour timer
second_thr_pair = True
# used to locate the new thread and start it. It adds everytime those four
# threads finish
thread_num = 0

# alarm sound
music = pygame.mixer.music.load('alarm sound.wav')


def hourtimer_1():
    global minutes  # for knowing the number of minutes passed in the hour timer
    global query_func  # it's related to 'timeLeft_query' function. Its a boolean and is only true when the hour timer
    # has not ended

    minutes = 0

    print('Hour Timer has started')
    # ----------------------------#
    for i in range(0, min_hr):
        time.sleep(secs_min)
        minutes += 1

    query_func = False

    print('<--------------------->')
    print('< An hour has passed >')


# It's used to ask how many minutes left for the hour timer to finish
# just press anything during the hour timer to get output
def input_management():
    global query_func
    query_func = True
    res_in_time = True
    # query func is no more "True" after the hour timer ends

    global n
    global timer_run

    while True:

        user_query = input()

        if query_func:

            print(f'<-----{minutes} have passed----->')
            print(f'<-----{60 - minutes} are left------->')

        elif res_in_time:

            print('The user is assumed to have drunk due amount of water')
            print('<--------------------------------------------------->')

            timer_run = False  # turned false to stop the timer of 5 minutes

            if res_in_time:
                n = 0

            break


def mintimer_5():
    global timer_run  # its used to count time in this function.It ends after input giver
    global res_in_time  # this variable is used to find if 5 minutes has ended and should the input

    # be counted as water drunk
    # if found true then it subtracts 1 from n for 1 glass of water deducted

    timer_run = True
    res_in_time = True

    print('<--------------------->')
    print('5 min timer has started')
    pygame.mixer.music.play(-1)  # plays the music

    # loops 60 seconds waiting for 5 times
    for i in range(1, (secs_min * 5) + 1):
        time.sleep(1)

        if i % 60 == 0:
            print(f'{i / 60} Minutes have passed')

        if not timer_run:
            pygame.mixer.music.stop()  # stops the music
            print('broken')
            break

    res_in_time = False
    pygame.mixer.music.stop()

print(f'"Greeting message", you have {n} glass/glasses of water to drink')

while True:
    print('<-------------------------------------------->')
    print(f'You got {n} glass/glasses of wah-ter to drink')

    # 'hourtimer_1'()
    t3 = threading.Thread(target=hourtimer_1, args=(), )
    threads3.append(t3)
    threads3[thread_num].start()

    # input management
    t2 = threading.Thread(target=input_management, args=(), )
    threads2.append(t2)
    threads2[thread_num].start()
    # hour timer being joined so that 5-min timer only starts after the hour ends
    threads3[thread_num].join()
    # thread2 can't get joined because there is still running of the 5-min timer

    # 5 min timer
    t1 = threading.Thread(target=mintimer_5)
    threads1.append(t1)
    threads1[thread_num].start()

    threads1[thread_num].join()
    # input management will finish after 5 minutes timer
    threads2[thread_num].join(timeout=0.1)

    print("PROCESSING NIBBAS . . . . ")
    pygame.mixer.music.stop()

    n += 1
    thread_num += 1

# should have used tkinter
