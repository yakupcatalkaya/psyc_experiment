# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 02:22:54 2020

@author: yakupcatalkaya
"""

#####################IMPORT #####################

import pygame as pyg
# import os
import random

#####################CONSTANTS #####################

running = True
# _image_library = {}

#######################################get the images#######################################

# def get_image(path):
#         global _image_library
#         image = _image_library.get(path)
#         if image == None:
#                 canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#                 image = pyg.image.load(canonicalized_path)
#                 _image_library[path] = image
#         return image
    
#####################################get windows size################################
def get_windows_size():    
    width,height=pyg.display.Info().current_w,pyg.display.Info().current_h
    return width,height

#####################################waiting################################

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
                    pyg.quit()
        pyg.time.delay(95)
    return False
            
#####################################stimuli scaler################################
def stimuli_scaler(size):
    width,height=size
    scale_w,scale_h=width/default_w,height/default_h
    return (scale_w,scale_h)

#####################################load the fonts################################
    
def get_font(font_type="comicsansms",size=14):
    font = pyg.font.SysFont(font_type,size)
    return font

#####################################create text################################

def create_text(texts,color=(255, 255, 255),size=14,font_type="comicsansms"):
    size=int(size*((scale_x*scale_y)**(1/2)))
    texts= get_font(font_type,size).render(str(texts), True, (255, 255, 255))
    return texts

#####################################create image################################

# def create_image(path):
#     scale_ratio=(scale_x*scale_y)**(1/2)
#     image=get_image(path)
#     newimage=pyg.transform.scale(image,(int(image.get_width()*scale_ratio),int(image.get_height()*scale_ratio)))
#     return newimage
    
#####################################show stimuli################################

def show_stimuli(source,up=0,left=0): 
    w,h=default_w,default_h
    up,left=up*scale_y,left*scale_x
    x,y=source.get_width(),source.get_height()
    area=(-(int(left*scale_x))+int(w*scale_x)//2- x//2,-(int(up*scale_y))+int(h*scale_y)//2- y//2)
    screen.blit(source,area)
    
#####################################first screen################################

def first_screen():
    text2=create_text(texts="Welcome to the experiment",size=54)
    text3=create_text(texts="The experiment is designed by mrjacob")
    # image=create_image('C:/Users/yakupcatalkaya/Desktop/experiment/umram_logo_1.png')
    screen.fill(black)  
    show_stimuli(text2)
    show_stimuli(text3,up=-520,left=-820)
    # show_stimuli(image,up=200,left=0)
    update_screen()
    pyg.time.delay(1000)

#####################################empty screen################################

def empty_screen():
    global background
    background = pyg.Surface(win_size)
    screen.fill(black)
    update_screen()
    
#####################################checker################################

def checking():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_p:
                waiting()
                return None
            elif event.key == pyg.K_ESCAPE:
                pyg.quit()

#####################################starter and scaler################################

def start_and_scale():
    global scale_x,scale_y,win_size,screen,title,black,white,default_w,default_h
    pyg.init()    
    pyg.display.set_caption('Experiment')
    title="mrjacob"
    black=(0,0,0)
    white=(255,255,255)
    default_w,default_h=1920,1080
    # clock = pyg.time.Clock()
    # clock.tick(60)
    win_size=get_windows_size()
    # win_size=(1920,1080)
    screen = pyg.display.set_mode(win_size)
    screen = pyg.display.set_mode(win_size,pyg.FULLSCREEN)  #  (win_size,pyg.FULLSCREEN)   #(672,378)
    scale_x,scale_y=stimuli_scaler(win_size)
    
#####################################screen updater################################

def update_screen():
    pyg.display.update()

#####################################randomized list creator################################

def random_number_list():
    list1=[]
    alphabet="A B C D E F G H I K L M N O P Q R S T V X Y Z"
    alph_list=alphabet.split()
    word="D A T"
    letters=word.split()
    for letter in letters:
        alph_list.remove(letter)
    old_num=45
    for number in range(40):
        ran_num=random.randrange(0,20)
        if not old_num==ran_num:
            list1.append(alph_list[ran_num])
        old_num=ran_num
    templist=[]
    for a in range(3):
        ran_num=random.randrange(0,23)
        templist.append(ran_num)
    templist.sort()
    for a in range(3):
        list1.insert(templist[a],letters[a])
    return list1

#####################################experiment screen################################

def experiment_screen():
    score=0
    real=0
    word="D A T"
    first,second,third=word.split()
    first_check,second_check,third_check=0,0,0
    a_list=random_number_list()
    screen.fill(black)
    show_stimuli(create_text(texts="D A T",size=154))
    update_screen()
    pyg.time.delay(3500)
    for a_num in a_list:
        checking()
        screen.fill(black)
        show_stimuli(create_text(texts=str(a_num),size=154))
        update_screen()
        condition=is_true()
        if condition==True:
            if first==a_num:
                first_check=1
            if second==a_num and first_check==1:
                second_check=1
            if third==a_num and second_check==1:
                third_check=1
    screen.fill(black)
    show_stimuli(create_text(texts="Is all three appeared?",size=154))
    update_screen()
    pyg.time.delay(500)
    condition=is_true()
    if condition==True:
        if third_check==1:
            score+=1
    return real,score

#####################################keyboard press################################

def is_true():
    onestimuli=88
    for trial in range(onestimuli):
        for event in pyg.event.get():
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    pyg.quit()
                elif event.key == pyg.K_s:
                    pyg.time.delay((onestimuli-trial)*10+1)
                    return True
        pyg.time.delay(10)
    
#####################################instruction screen################################

def instruction_screen():
    global running
    screen.fill(black)
    show_stimuli(create_text(texts="The Instructions",size=54),up=200)
    show_stimuli(create_text(texts="-------------------------------------------",size=54),up=160,left=-25)
    show_stimuli(create_text(texts="1)  The first screen will show the three letter",size=24),up=100,left=175)
    show_stimuli(create_text(texts="that should be remembered by the end of the experiment.",size=24),up=50,left=70)
    show_stimuli(create_text(texts="2)  When experiment starts, the letters will show up one by one.",size=24),up=0,left=70)
    show_stimuli(create_text(texts="For that matter, the participant will press S when the first letter is matched.",size=24),up=-50,left=-50)
    show_stimuli(create_text(texts="3)  When the all three letters are found, a question will be asked.",size=24),up=-100,left=65)
    show_stimuli(create_text(texts="In order to say yes, the participant should press S. Otherwise, do nothing.",size=24),up=-150,left=-30)
    show_stimuli(create_text(texts="4)  Press S, ESC, P to initiate, terminate, or pause the experiment respectively.",size=24),up=-200,left=-15)
    show_stimuli(create_text(texts="-------------------------------------------",size=54),up=-250,left=-25)
    update_screen()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_s:
                running=False
            elif event.key == pyg.K_ESCAPE:
                pyg.quit()
            elif event.key == pyg.K_p:
                waiting()
                running=False
    
#####################################main program ################################

def main():
    start_and_scale()
    empty_screen()
    checking()
    first_screen()
    pyg.time.delay(1000)
    while running:
        checking()
        instruction_screen()
    experiment_screen()
    empty_screen()
    pyg.time.delay(1000)
    pyg.quit()

#####################################initiate program ################################

main()
pyg.quit()