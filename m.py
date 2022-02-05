# imports things
import time
import pygame
import threading

pygame.init()
# gives time
time_obj = time.localtime()
# n is number of glasses
n = 1

stuff = True

timer_run = True  # it's used to count time in "mintimer_5" function
no_adding = True
# they are threads for starting functions
threads = []  # 5 min timer
threads2 = []  # input for water drunk
threads3 = []  # time left query
threads4 = []  # 1 hour timer
second_thr_pair = True
# used to locate the new thread and start it. It adds everytime those four
# threads finish
thread_num = 0
user_input = True

# alarm sound
pygame.mixer.music.load('alarm sound.wav')


def hourtimer_1():
    global minutes  # for knowing the number of minutes passed in the hour timer
    global query_func  # it's related to 'timeLeft_query' function. It's a boolean and is only true when the hour timer
    # has not ended

    minutes =\
        0

    print('Hour Timer has started')
    # ----------------------------#
    for i in range(0, 60):
        time.sleep(60)
        minutes += 1

    query_func = False

    print('<--------------------->')
    print('<  An hour has passed  >')


# Its used to ask how many minutes left for the hour timer to finish
# just press anything during the hour timer to get output
def timeLeft_query():
    global query_func
    query_func = True
    print('asking for input now')
    # query func is no more "True" after the hour timer ends 
    while query_func:
        user_query = input()
        print(f'<-----{minutes} have passed----->')
        print(f'<-----{60 - minutes} are left------->')


def mintimer_5():
    global timer_run  # its used to count time in this function.It ends after input giver
    global stuff  # this variable is used to find if 5 minutes has ended and should the input
    # be counted as water drunk
    # if found true then it subtracts 1 from n for 1 glass of water deducted

    timer_run = True
    stuff = True
    # gets time
    time_obj = time.localtime()
    target_time = time_obj.tm_sec

    print('<--------------------->')
    print('5 min timer has started')
    pygame.mixer.music.play(-1)  # plays the music

    # loops 60 seconds waiting for 5 times
    for i in range(1, 6):
        while timer_run:
            time.sleep(60)
            print(f'{i} min has passed')
            break

    pygame.mixer.music.stop()  # stops the music after the 5 min

    stuff = False


def ask_input():
    global n
    global timer_run
    global no_adding  # one glass is added or not added after one loop of the task in the while loop
    global user_input  # having user input assumes that all water has been drunk
    # else n gets added by 1

    no_adding = True
    user_input = False

    the_Input = input()
    print('The user is assumed to have drunk due amount of water')
    print('<--------------------------------------------------->')

    if not stuff:
        n = n + 1
        no_adding = True
    else:
        n = n - 1
        no_adding = False

    timer_run = False  # turned false to stop the timer of 5 minutes
    pygame.mixer.music.stop()  # music also stoped

    user_input = True  # user input comes true


print(f'Assalamualaikum nibba, you have {n} glass/glasses of water to drink')

while True:
    print('<-------------------------------------------->')
    print(f'You got {n} glass/glasses of wah-ter to drink')

    # hourtimer_1()
    t3 = threading.Thread(target=hourtimer_1, args=(),)
    threads3.append(t3)
    threads3[thread_num].start()

    # user query
    t4 = threading.Thread(target=timeLeft_query, args=(),)
    threads4.append(t4)
    threads4[thread_num].start()

    threads3[thread_num].join()
    threads4[thread_num].join(timeout=0.1)  # this thread cant get joined

    # 5 min timer        
    t1 = threading.Thread(target=mintimer_5, args=(),)
    threads.append(t1)
    threads[thread_num].start()

    # input for water drunk
    t2 = threading.Thread(target=ask_input, args=(),)
    threads2.append(t2)
    threads2[thread_num].start()

    threads[thread_num].join()
    threads2[thread_num].join(timeout=0.3)

    print("PROCESSNIG NIBBAS . . . . ")
    pygame.mixer.music.stop()

    if not user_input:
        n = n + 1
    elif user_input:
        n = 1
    elif no_adding:
        pass
    else:
        n = n + 1

    thread_num += 1
