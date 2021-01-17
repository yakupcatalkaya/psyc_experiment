# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 02:22:54 2020

@author: yakupcatalkaya
"""

import pygame as pyg
import csv
import random
import hashlib
import time
import os
running = True
id_num=""
global_list=[]
program_clock=time.time()
directory=os.getcwd()
def get_windows_size():    
    width,height=pyg.display.Info().current_w,pyg.display.Info().current_h
    return width,height

def waiting():
    for attempt in range(99):
        screen.fill(black)
        text1=create_text(texts="Press ESC to terminate the experiment!",size=54)
        show_stimuli(text1)
        show_stimuli(create_text(texts="Experiment continue in "+str(10-attempt//10)+" seconds...",size=54),up=-200)
        update_screen()
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_r:
                    break
                elif event.key == pyg.K_ESCAPE:
                    exit_screen()
        pyg.time.delay(95)
    return False
            
def stimuli_scaler(size):
    width,height=size
    scale_w,scale_h=width/default_w,height/default_h
    return (scale_w,scale_h)

    
def get_font(font_type="comicsansms",size=14):
    font = pyg.font.SysFont(font_type,size)
    return font


def create_text(texts,color=(255, 255, 255),size=14,font_type="comicsansms"):
    size=int(size*((scale_x*scale_y)**(1/2)))
    texts= get_font(font_type,size).render(str(texts), True, color)
    return texts


def show_stimuli(source,up=0,left=0): 
    w,h=default_w,default_h
    up,left=up*scale_y,left*scale_x
    x,y=source.get_width(),source.get_height()
    area=(-(int(left*scale_x))+int(w*scale_x)//2- x//2,-(int(up*scale_y))+int(h*scale_y)//2- y//2)
    screen.blit(source,area)
    

def first_screen():
    text2=create_text(texts="Welcome to the experiment",size=54)
    text3=create_text(texts="The experiment is build by UMRAM Farooqui's Lab")
    screen.fill(black)  
    show_stimuli(text2)
    show_stimuli(text3,up=-520,left=-820)
    update_screen()
    pyg.time.delay(1000)


def empty_screen():
    global background
    background = pyg.Surface(win_size)
    screen.fill(black)
    update_screen()
    

def checking():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_p:
                waiting()
                return None
            elif event.key == pyg.K_ESCAPE:
                exit_screen()
            elif event.key == pyg.K_SPACE:
                return False


def start_and_scale():
    global scale_x,scale_y,win_size,screen,title,black,white,default_w,default_h
    pyg.init()    
    pyg.display.set_caption('Experiment')
    title="mrjacob"
    black=(0,0,0)
    white=(255,255,255)
    default_w,default_h=1920,1080
    win_size=get_windows_size()
    screen = pyg.display.set_mode(win_size)
    screen = pyg.display.set_mode(win_size,pyg.FULLSCREEN)  #  (win_size,pyg.FULLSCREEN)   #(672,378)
    scale_x,scale_y=stimuli_scaler(win_size)
    

def update_screen():
    pyg.display.update()


def random_number_list():
    number_list=[]
    letter_list=[]
    letters="A B C D E F G H I K L M N P Q R S T V X Y Z".split()
    numbers="1 2 3 4 5 6 7 8 9".split()
    for step in range(32):
        ran_num=random.randint(0,4)
        number_list.append(numbers[ran_num])
    for step in range(121):
        ran_num=random.randint(0,19) 
        letter_list.append(letters[ran_num])
    templist=number_list+letter_list
    random.shuffle(templist)
    atemplist=templist[:]
    
    indexlist=list(range(9,153,9))
    count=0
    for index in indexlist:
        templist.insert(index+count,"gap")
        count+=1
    
    indexlist=[]
    for step in range(16):
        index=random.randrange(1,151)
        while index in indexlist:
            index=random.randrange(1,151)
        indexlist.append(index)
    count=0  
    for index in indexlist:
        atemplist.insert(index+count,"gap")
        count+=1
        
    count=0
    for letter in templist:
        if count%10==0 and count!=0:
            if letter in numbers:
                ran_num=random.randint(1,168)
                while (templist[ran_num] in numbers) or templist[ran_num]=="gap" or ran_num%10==0:
                    ran_num=random.randint(1,168)
                templist[count],templist[ran_num]=templist[ran_num],templist[count]
        count+=1 
        
    count=0
    for letter in atemplist:
        if 0<count<len(atemplist)-1:
            if (letter in numbers and atemplist[count-1]=="gap") or (letter=="gap" and (atemplist[count-1]=="gap" or atemplist[count+1]=="gap")):
                ran_num=random.randint(2,167)
                while (atemplist[ran_num] in numbers) or atemplist[ran_num]=="gap" or (atemplist[ran_num+1]=="gap" or atemplist[ran_num-1]=="gap" or atemplist[ran_num-1] in numbers or atemplist[ran_num+1] in numbers):
                    ran_num=random.randint(2,167)
                atemplist[count],atemplist[ran_num]=atemplist[ran_num],atemplist[count]
        count+=1 
    return templist,atemplist

def again_again(item_i,error_i,score_i,miss_i):
    letters="A B C D E F G H I K L M N P Q R S T V X Y Z".split()
    done=False
    stimuli_start=time.time()
    for step in range(39):
        screen.fill(black)        
        show_stimuli(create_text(texts=str(item_i),size=154))
        update_screen()
        state=is_true(item_i,1)
        if state==True:
            error_i+=1
            stimuli_stop=time.time()
            step=step
            done=True
            break
        elif state==False:
            score_i+=1
            stimuli_stop=time.time()
            step=step
            done=True
            break
    if done:
        screen.fill(black)        
        show_stimuli(create_text(texts=str(item_i),size=154))
        update_screen()
        pyg.time.delay(int(18-step)*10+1)
        show_fixation(item_i,just=False)
    elif not done:
        for a in range(69):
            countiii=a
            state=show_fixation(item_i)
            if state==True:
                error_i+=1
                stimuli_stop=time.time()
                break
            elif state==False:
                score_i+=1
                stimuli_stop=time.time()
                break
        if state=="None":
            if item_i in letters:
                miss_i+=1
            if item_i not in letters:
                error_i+=1
            stimuli_stop=time.time()
        pyg.time.delay((68-countiii)*10+1)
    react_time_i=str(int((stimuli_stop-stimuli_start)*1000)) 
    if int(react_time_i)<100:
        if state==True:error_i-=1
        elif state==False:score_i-=1
        elif state=="None" and item_i not in letters: error_i-=1
        elif state=="None" and item_i in letters: miss_i-=1
        state,error_i,score_i,miss_i,react_time_i=again_again(item_i,error_i,score_i,miss_i)
    return state,error_i,score_i,miss_i,react_time_i


def experiment_screen(ready=True):
    letters="A B C D E F G H I K L M N P Q R S T V X Y Z".split()
    count_session_regular=1
    count_session_random=1
    global global_list
    exp1,exp2=random_number_list()
    score,error,miss=0,0,0
    timelist=[]
    pyg.time.delay(1000)   
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                exit_screen()
            elif event.key == pyg.K_SPACE:
                break
    for item in exp1:
        if item=="gap":
            count_session_regular+=1
            repeat=break_screen(typo="set")
            if repeat>=300:repeat=300
            timelist.append(repeat)
            global_list.append(["gap","gap","gap","gap","gap",str(repeat*10)+" ms has been spend."])
        else:
            done=False
            stimuli_start=time.time()
            for step in range(39):
                screen.fill(black)        
                show_stimuli(create_text(texts=str(item),size=154))
                update_screen()
                state=is_true(item,1)
                if state==True:
                    error+=1
                    stimuli_stop=time.time()
                    step=step
                    done=True
                    break
                elif state==False:
                    score+=1
                    stimuli_stop=time.time()
                    step=step
                    done=True
                    break
            if done:
                screen.fill(black)        
                show_stimuli(create_text(texts=str(item),size=154))
                update_screen()
                pyg.time.delay(int(18-step)*10+1)
                show_fixation(item,just=False)
            elif not done:
                for a in range(69):
                    countiii=a
                    state=show_fixation(item)
                    if state==True:
                        error+=1
                        stimuli_stop=time.time()
                        break
                    elif state==False:
                        score+=1
                        stimuli_stop=time.time()
                        break
                if state=="None":
                    if item in letters:
                        miss+=1
                    if item not in letters:
                        error+=1
                    stimuli_stop=time.time()
                pyg.time.delay((68-countiii)*10+1)
            react_time=str(int((stimuli_stop-stimuli_start)*1000))
            if int(react_time)<100:
                if state==True:error-=1
                elif state==False:score-=1
                elif state=="None" and item not in letters: error-=1
                elif state=="None" and item in letters: miss-=1
                state,error,score,miss,react_time=again_again(item,error,score,miss)
            global_list.append([item,state,error,score,miss,react_time,"regular",count_session_regular])
    break_screen()
    counti=0
    for item in exp2:
        if item=="gap":
            count_session_random+=1
            for a in range(timelist[counti]):
                screen.fill(black)
                update_screen()
                checking()
                pyg.time.delay(10)
            global_list.append(["gap",str(timelist[counti]*10)+" ms (predetermined) has been spend."])
            counti+=1
        else:
            done=False
            stimuli_start=time.time()
            for step in range(39):
                screen.fill(black)        
                show_stimuli(create_text(texts=str(item),size=154))
                update_screen()
                state=is_true(item,1)
                if state==True:
                    error+=1
                    stimuli_stop=time.time()
                    step=step
                    done=True
                    break
                elif state==False:
                    score+=1
                    stimuli_stop=time.time()
                    step=step
                    done=True
                    break
            if done:
                screen.fill(black)        
                show_stimuli(create_text(texts=str(item),size=154))
                update_screen()
                pyg.time.delay(int(18-step)*10+1)
                show_fixation(item,just=False)
            elif not done:
                for a in range(69):
                    countiii=a
                    state=show_fixation(item)
                    if state==True:
                        error+=1
                        stimuli_stop=time.time()
                        break
                    elif state==False:
                        score+=1
                        stimuli_stop=time.time()
                        break
                if state=="None":
                    if item in letters:
                        miss+=1
                    if item not in letters:
                        error+=1
                    stimuli_stop=time.time()
                pyg.time.delay((68-countiii)*10+1)
            react_time=str(int((stimuli_stop-stimuli_start)*1000))   
            if int(react_time)<100:
                if state==True:error-=1
                elif state==False:score-=1
                elif state=="None" and item not in letters: error-=1
                elif state=="None" and item in letters: miss-=1
                state,error,score,miss,react_time=again_again(item,state,error,score,miss)
            global_list.append([item,state,error,score,miss,react_time,"random",count_session_random])
                

def show_fixation(item,colour=(255,255,255),just=True):
    screen.fill(black)        
    show_stimuli(create_text(texts=str("+"),color=colour,size=154))
    update_screen()
    if not just:
        pyg.time.delay(690)
    if just:
        state=is_true(item,1)
        return state
    

def is_true(item,onestimuli):
    letters="A B C D E F G H I K L M N P Q R S T V X Y Z".split()
    # wait_time=0
    for trial in range(onestimuli):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    exit_screen()
                elif event.key == pyg.K_p:
                    waiting()
                    continue
                elif event.key == pyg.K_DOWN:
                    if item in letters:
                        return True
                        break
                    else:
                        return False
                        break
        pyg.time.delay(7)
    return "None"


def exit_screen():
    global global_list
    done=False
    for attempt in range(29):
        screen.fill(black)
        show_stimuli(create_text(texts="Please do not close the experiment!",size=54))
        show_stimuli(create_text(texts="Experiment will close in "+str(3-attempt//8)+" seconds...",size=54),up=-200)
        update_screen()
        if done==False:
            create_csv_file(global_list)
            done=True
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    pyg.quit()
        pyg.time.delay(95)
    pyg.quit()


def break_screen(typo="session"):
    screen.fill(black)
    if typo=="session":
        show_stimuli(create_text(texts="Another long session is going to start!",size=54),up=50)
        show_stimuli(create_text(texts="Press space to continue to the long "+str(typo),size=34),up=-50)
        update_screen()
    else:
        show_stimuli(create_text(texts="Press down arrow key button to everything except numbers",size=54),up=50)
        show_stimuli(create_text(texts="Press space to continue to "+str(typo),size=34),up=-50)
        update_screen()
    repeat=0
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    exit_screen()
                elif event.key == pyg.K_SPACE:
                    pyg.time.delay(300)
                    return int(repeat)
                    break
        pyg.time.delay(9)
        repeat+=1
        

def instruction_screen():
    screen.fill(black)
    show_stimuli(create_text(texts="The Instructions",size=54),up=190)
    show_stimuli(create_text(texts="-------------------------------------------",size=54),up=150,left=0)
    show_stimuli(create_text(texts="1)  In experiment, there are 17 set and in each set there are 9 stimuli.",size=24),up=90,left=10)
    show_stimuli(create_text(texts="2)  Participant should press down arrow key when a letter is appeared in the screen.",size=24),up=30,left=-65)
    show_stimuli(create_text(texts="3)  For numbers,do nothing. ",size=24),up=-30,left=250)
    show_stimuli(create_text(texts="4)  There are 10 sessions [5 from each type] in the experiment. ",size=24),up=-90,left=50)
    show_stimuli(create_text(texts="5)  Press space button to continue the experiment . ",size=24),up=-150,left=120)
    update_screen()
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    exit_screen()
                elif event.key == pyg.K_SPACE:
                    return None
                

def subject_sign():
    global signed,id_num
    num = ''
    done = False
    while not done:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                done = True
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    done= True
                if event.key == pyg.K_RETURN or event.key == pyg.K_KP_ENTER:
                    id_num=str(num)
                    num=''
                    print(id_num)
                    signed= True
                    done= True
                if event.key == pyg.K_BACKSPACE:
                    num=num[:-1]
                else: 
                    num += event.unicode
        screen.fill(black)
        text1=create_text(texts='ENTER YOUR SUBJECT ID:',color=white,size=34)
        text3=create_text(texts='Then, press enter',color=white,size=34)
        text2=create_text(texts=str(num),color=white,size=34)
        show_stimuli(text1,left=200)
        show_stimuli(text2,left=-200)
        show_stimuli(text3,up=-100,left=280)
        update_screen()


def create_csv_file(global_list):
    global signed,id_num
    print("The data file is at: "+str(directory))
    if signed is True:
        pass
    else:
        id_num=str(1111)
        signed= True
    day=""
    for item in time.localtime()[:3]: day+=str(item)+"/"
    program_end=time.time()
    program_time=str(int(program_end-program_clock))+" s "
    with open('data.csv', 'w', newline='') as data:
        rw= csv.writer(data, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rw.writerow(["ID NUM:",id_num,day[:-1],program_time,"0","0",hashlib.md5(id_num.encode()).hexdigest()])
        for line in global_list:
            string=""
            for a in line:
                string+=str(a)
            checksum=hashlib.md5(string.encode()).hexdigest()
            line.append(checksum)          
            rw.writerow(line)
            

def main():
    start_and_scale()
    subject_sign()
    empty_screen()
    checking()
    first_screen()
    pyg.time.delay(1000)
    instruction_screen()
    ready=True
    for trial in range(5):
        break_screen()
        experiment_screen(ready)
        ready=False
    pyg.time.delay(1000)
    exit_screen()

main()
pyg.quit()
