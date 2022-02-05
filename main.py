# imports things
import time
import pygame
from pygame import mixer
import threading

pygame.init()

time_obj = time.localtime()
n = 1
stuff = True
timer_run = True
no_adding = True
threads = []
threads2 = []
thread_num = 0
user_input = True


# alarm sound
alarm = pygame.mixer.music.load('alarm sound.wav')

def hourtimer_1 ():
    print('Hour Timer has started')
    time.sleep(360)
    print('<--------------------->')
    print('An hour has passed')


def mintimer_5 ():
    global timer_run
    global stuff

    timer_run = True
    stuff = True
    time_obj = time.localtime()
    target_time = time_obj.tm_sec

    print('<--------------------->')
    print('5 min timer has started')
    pygame.mixer.music.play(-1)
    
    for i in range(1,6):
        while timer_run:
            time.sleep(10)
            print(f'{i} min has passed')
            break
        
    pygame.mixer.music.stop()
    
    stuff = False


def ask_input():
    global n
    global timer_run
    global no_adding
    global user_input

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
    
    timer_run = False
    pygame.mixer.music.stop()
    
    user_input = True


print(f'Assalamualaikum nibba, you have {n} glass/glasses of water to drink')

while True: 
    print('<-------------------------------------------->')
    print(f'You got {n} glass/glasses of wah-ter to drink')
    


    hourtimer_1()
    t1 = threading.Thread(target=mintimer_5)
    threads.append(t1)
    threads[thread_num].start()
    

    t2 = threading.Thread(target=ask_input)
    threads2.append(t2)
    threads2[thread_num].start()
    
    threads[thread_num].join()
    threads2[thread_num].join(timeout=0.3)

    print("PROCESSNIG NIBBAS . . . . ")
    

    if not user_input:
        n = n + 1
    elif user_input:
        n = 1
    elif no_adding:
        pass
    else:
        n = n + 1

  


    thread_num += 1
    




    

    