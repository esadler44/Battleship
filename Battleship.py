#Battleship

#Pygame stuff
from pygame import *
init()
mixer.init()
size = 452,727
screen = display.set_mode(size)
myClock = time.Clock()
fontHello = font.SysFont("Times New Roman",57)

#Importing instructions
Instructions = image.load("Instructions.png")

#Keeping it at menu until ready
menu = 0

#Menu
while menu == 0:
    screen.blit(Instructions, Rect(0,0,0,0))
    display.flip()
    for evnt in event.get():
        if evnt.type == MOUSEBUTTONDOWN:
            menu = 1   

#Setting up board
screen.fill((112,128,144))

text = fontHello.render("BATTLESHIP" ,1, (255,0,0))
screen.blit(text,Rect(0,328,0,0))

fontHello = font.SysFont("Times New Roman",15)
text = fontHello.render("  Your boats:" ,1, (0,0,0))
screen.blit(text,Rect(328,30,0,0))
text = fontHello.render("   Aircraft Carrier" ,1, (0,0,0))
screen.blit(text,Rect(328,60,0,0))
text = fontHello.render("   Battleship" ,1, (0,0,0))
screen.blit(text,Rect(328,110,0,0))
text = fontHello.render("   Cruiser" ,1, (0,0,0))
screen.blit(text,Rect(328,160,0,0))
text = fontHello.render("   Submarine" ,1, (0,0,0))
screen.blit(text,Rect(328,210,0,0))
text = fontHello.render("   Destroyer" ,1, (0,0,0))
screen.blit(text,Rect(328,260,0,0))
text = fontHello.render("  Computer boats:" ,1, (0,0,0))
screen.blit(text,Rect(328,430,0,0))
text = fontHello.render("   Aircraft Carrier" ,1, (0,0,0))
screen.blit(text,Rect(328,460,0,0))
text = fontHello.render("   Battleship" ,1, (0,0,0))
screen.blit(text,Rect(328,510,0,0))
text = fontHello.render("   Cruiser" ,1, (0,0,0))
screen.blit(text,Rect(328,560,0,0))
text = fontHello.render("   Submarine" ,1, (0,0,0))
screen.blit(text,Rect(328,610,0,0))
text = fontHello.render("   Destroyer" ,1, (0,0,0))
screen.blit(text,Rect(328,660,0,0))

fontHello = font.SysFont("Times New Roman",29)

text = fontHello.render("1  2  3  4  5  6  7  8  9  10" ,1, (0,0,0))
screen.blit(text,Rect(43,0,0,0))
screen.blit(text,Rect(43,390,0,0))
text = fontHello.render("A" ,1, (0,0,0))
screen.blit(text,Rect(0,30,0,0))
screen.blit(text,Rect(0,420,0,0))
text = fontHello.render("B" ,1, (0,0,0))
screen.blit(text,Rect(0,60,0,0))
screen.blit(text,Rect(0,450,0,0))
text = fontHello.render("C" ,1, (0,0,0))
screen.blit(text,Rect(0,90,0,0))
screen.blit(text,Rect(0,480,0,0))
text = fontHello.render("D" ,1, (0,0,0))
screen.blit(text,Rect(0,120,0,0))
screen.blit(text,Rect(0,510,0,0))
text = fontHello.render("E" ,1, (0,0,0))
screen.blit(text,Rect(0,150,0,0))
screen.blit(text,Rect(0,540,0,0))
text = fontHello.render("F" ,1, (0,0,0))
screen.blit(text,Rect(0,180,0,0))
screen.blit(text,Rect(0,570,0,0))
text = fontHello.render("G" ,1, (0,0,0))
screen.blit(text,Rect(0,210,0,0))
screen.blit(text,Rect(0,600,0,0))
text = fontHello.render("H" ,1, (0,0,0))
screen.blit(text,Rect(0,240,0,0))
screen.blit(text,Rect(0,630,0,0))
text = fontHello.render("I" ,1, (0,0,0))
screen.blit(text,Rect(0,270,0,0))
screen.blit(text,Rect(0,660,0,0))
text = fontHello.render("J" ,1, (0,0,0))
screen.blit(text,Rect(0,300,0,0))
screen.blit(text,Rect(0,690,0,0))
display.flip()

BLUE = (28,107,160)

def boarddraw(screen):
    draw.rect(screen,BLUE,(32,32,297,297),0)
    draw.rect(screen,BLUE,(32,422,297,297),0)
    
    for x in range(1,11):
        draw.line(screen,(255,255,255),(0,30*x),(328,30*x),3)
        draw.line(screen,(255,255,255),(30*x,0),(30*x,328),3)
        draw.line(screen,(0,0,0),(0,(400+30*x)-10),(328,(400+30*x)-10),3)
        draw.line(screen,(0,0,0),(30*x,390),(30*x,718),3)
    display.flip()

boarddraw(screen)

def bottomboard(screen):
    draw.rect(screen,BLUE,(32,422,297,297),0)
    for x in range(1,11):
        draw.line(screen,(0,0,0),(0,(400+30*x)-10),(328,(400+30*x)-10),3)
        draw.line(screen,(0,0,0),(30*x,390),(30*x,718),3)
    display.flip()

import random

#Variables
xA = []
yA = []
xB = []
yB = []
xC = []
yC = []
xS = []
yS = []
xD = []
yD = []
missx = []
missy = []
hitx = []
hity = []
defcountx = 0
defcounto = 0
xallow = 0
oallow = 0
answer = "maybe"

running = True
menu = True
computerspaces = []
userspaces = []
userACspaces = []
userBSspaces = []
userCRspaces = []
userSBspaces = []
userDSspaces = []
ACspaces = []
BSspaces = []
CRspaces = []
SBspaces = []
DSspaces = []
ACdeath = []
BSdeath = []
CRdeath = []
SBdeath = []
DSdeath = []
alreadyguessed = []
userguesses = []
guesses = 0
turncycle = 1
redoboard = 0
rowletters = ["A","B","C","D","E","F","G","H","I","J"]
directions = ["up","down","left","right"]
leftnonos = [1,11,21,31,41,51,61,71,81,91]
rightnonos = [10,20,30,40,50,60,70,80,90,100]
leftnonos2 = [1,11,21,31,41,51,61,71,81,91]
rightnonos2 = [10,20,30,40,50,60,70,80,90,100]
x = 0
y = 0
z = 0
w = 0
v = 0

board = [" "]*100
yourboard = ["_"]*100

#Computer setting up it's boats
#AI for board set-up in here
while redoboard == 0:
    computerspaces = []
    ACspaces = []
    BSspaces = []
    CRspaces = []
    SBspaces = []
    DSspaces = []
    defineddirection = 0
    directions = ["up","down","left","right"]
    leftnonos = [1,11,21,31,41,51,61,71,81,91]
    rightnonos = [10,20,30,40,50,60,70,80,90,100]
    for count in range(0,5):
        if count == 0:
            AC = random.randint(1,100)
            computerspaces.append(AC)
            ACspaces.append(AC)
            ACadd = AC
            wwtg = random.randint(0,3)
            direction = directions[wwtg]
            for ACcount in range(0,4):
                if direction == "left":
                    ACadd -= 1
                    if ACadd in rightnonos or ACadd < 1 or x == 1:
                        ACadd = AC+1
                        AC += 1
                        x = 1  
                    ACspaces.append(ACadd)
                    computerspaces.append(ACadd)
                elif direction == "right":
                    ACadd += 1
                    if ACadd in leftnonos or ACadd > 100 or x == 1:
                        ACadd = AC-1
                        AC -= 1
                        x = 1
                    ACspaces.append(ACadd)
                    computerspaces.append(ACadd)
                elif direction == "up":
                    ACadd -= 10
                    if AC < 1 or ACadd < 1 or x == 1:
                        ACadd = AC+10
                        AC += 10
                        x = 1 
                    ACspaces.append(ACadd)
                    computerspaces.append(ACadd)
                else:
                    ACadd += 10
                    if AC > 100 or ACadd > 100 or x == 1:
                        ACadd = AC-10
                        AC -= 10
                        x = 1
                    ACspaces.append(ACadd)
                    computerspaces.append(ACadd)
        if count == 1:
            wwtg = random.randint(0,3)
            direction = directions[wwtg]
            leftnonos+=computerspaces
            rightnonos+=computerspaces
            BS = random.randint(1,100)
            while BS in computerspaces:
                BS = random.randint(1,100)
            if direction == "left" or direction == "right":
                while ((BS - 1 in rightnonos or BS - 1 == 0) and (BS + 1 in computerspaces or BS + 2 in computerspaces or BS + 3 in computerspaces)) or ((BS + 1 in leftnonos or BS + 1 == 101) and (BS - 1 in computerspaces or BS - 2 in computerspaces or BS - 3 in computerspaces)) or ((BS - 2 in rightnonos  or BS - 2 == 0) and (BS + 1 in computerspaces or BS + 2 in computerspaces)) or ((BS + 2 in leftnonos or BS + 2 == 101) and (BS - 1 in computerspaces or BS - 2 in computerspaces)) or ((BS - 3 in rightnonos or BS - 3 == 0) and BS + 1 in computerspaces) or ((BS + 3 in leftnonos or BS + 3 == 101) and BS - 1 in computerspaces):
                    BS = random.randint(1,100)
            if direction == "up" or direction == "down":
                while ((BS + 10 > 100 or BS + 10 in computerspaces) and (BS - 10 in computerspaces or BS - 20 in computerspaces or BS - 30 in computerspaces)) or ((BS - 10 < 1 or BS - 10 in computerspaces) and (BS + 10 in computerspaces or BS + 20 in computerspaces or BS + 30 in computerspaces)) or ((BS + 20 > 100 or BS + 20 in computerspaces) and (BS - 10 in computerspaces or BS - 20 in computerspaces)) or ((BS - 20 < 1 or BS - 20 in computerspaces) and (BS + 10 in computerspaces or BS + 20 in computerspaces)) or ((BS + 30 > 100 or BS + 30 in computerspaces) and BS - 10 in computerspaces) or ((BS - 30 < 1 or BS - 30 in computerspaces) and BS + 10 in computerspaces):
                    BS = random.randint(1,100)
            computerspaces.append(BS)
            BSspaces.append(BS)
            BSadd = BS    
            for BScount in range(0,3):
                if direction == "left":
                    BSadd -= 1
                    if BSadd in rightnonos or BSadd < 1 or y == 1:
                        BSadd = BS+1
                        BS += 1                        
                        y = 1
                    BSspaces.append(BSadd)
                    computerspaces.append(BSadd)
                elif direction == "right":
                    BSadd += 1
                    if BSadd in leftnonos or BSadd > 100 or y == 1:
                        BSadd = BS-1
                        BS -= 1
                        y = 1
                    BSspaces.append(BSadd)
                    computerspaces.append(BSadd)
                elif direction == "up":
                    BSadd -= 10
                    if BS < 1 or BSadd < 1 or BSadd in computerspaces or y == 1:
                        BSadd = BS+10
                        BS += 10
                        y = 1
                    BSspaces.append(BSadd)
                    computerspaces.append(BSadd)
                elif direction == "down":
                    BSadd += 10
                    if BS > 100 or BSadd > 100 or BSadd in computerspaces or y == 1:
                        BSadd = BS-10
                        BS -= 10
                        y = 1
                    BSspaces.append(BSadd)
                    computerspaces.append(BSadd)
        if count == 2:
            wwtg = random.randint(0,3)
            direction = directions[wwtg]
            leftnonos+=computerspaces
            rightnonos+=computerspaces
            CR = random.randint(1,100)
            while CR in computerspaces:
                CR = random.randint(1,100)
            if direction == "left" or direction == "right":
                while ((CR - 1 in rightnonos or CR - 1 == 0) and (CR + 1 in computerspaces or CR + 2 in computerspaces)) or ((CR + 1 in leftnonos or CR + 1 == 101) and (CR - 1 in computerspaces or CR - 2 in computerspaces)) or ((CR - 2 in rightnonos  or CR - 2 == 0) and CR + 1 in computerspaces) or ((CR + 2 in leftnonos or CR + 2 == 101) and CR - 1 in computerspaces):
                    CR = random.randint(1,100)
            if direction == "up" or direction == "down":
                while ((CR + 10 > 100 or CR + 10 in computerspaces) and (CR - 10 in computerspaces or CR - 20 in computerspaces)) or ((CR - 10 < 1 or CR - 10 in computerspaces) and (CR + 10 in computerspaces or CR + 20 in computerspaces)) or ((CR + 20 > 100 or CR + 20 in computerspaces) and CR - 10 in computerspaces) or ((CR - 20 < 1 or CR - 20 in computerspaces) and CR + 10 in computerspaces):
                    CR = random.randint(1,100)
            computerspaces.append(CR)
            CRspaces.append(CR)
            CRadd = CR
            for CRcount in range(0,2):
                if direction == "left":
                    CRadd -= 1
                    if CRadd in rightnonos or CRadd < 1 or z == 1:
                        CRadd = CR+1
                        CR += 1                        
                        z = 1
                    CRspaces.append(CRadd)
                    computerspaces.append(CRadd)
                elif direction == "right":
                    CRadd += 1
                    if CRadd in leftnonos or CRadd > 100 or z == 1:
                        CRadd = CR-1
                        CR -= 1
                        z = 1
                    CRspaces.append(CRadd)
                    computerspaces.append(CRadd)
                elif direction == "up":
                    CRadd -= 10
                    if CR < 1 or CRadd < 1 or CRadd in computerspaces or z == 1:
                        CRadd = CR+10
                        CR += 10
                        z = 1
                    CRspaces.append(CRadd)
                    computerspaces.append(CRadd)
                elif direction == "down":
                    CRadd += 10
                    if CR > 100 or CRadd > 100 or CRadd in computerspaces or z == 1:
                        CRadd = CR-10
                        CR -= 10
                        z = 1
                    CRspaces.append(CRadd)
                    computerspaces.append(CRadd)
        if count == 3:
            wwtg = random.randint(0,3)
            direction = directions[wwtg]
            leftnonos+=computerspaces
            rightnonos+=computerspaces
            SB = random.randint(1,100)
            while SB in computerspaces:
                SB = random.randint(1,100)
            if direction == "left" or direction == "right":
                while ((SB - 1 in rightnonos or SB - 1 == 0) and (SB + 1 in computerspaces or SB + 2 in computerspaces)) or ((SB + 1 in leftnonos or SB + 1 == 101) and (SB - 1 in computerspaces or SB - 2 in computerspaces)) or ((SB - 2 in rightnonos  or SB - 2 == 0) and SB + 1 in computerspaces) or ((SB + 2 in leftnonos or SB + 2 == 101) and SB - 1 in computerspaces):
                    SB = random.randint(1,100)
            if direction == "up" or direction == "down":
                while ((SB + 10 > 100 or SB + 10 in computerspaces) and (SB - 10 in computerspaces or SB - 20 in computerspaces)) or ((SB - 10 < 1 or SB - 10 in computerspaces) and (SB + 10 in computerspaces or SB + 20 in computerspaces)) or ((SB + 20 > 100 or SB + 20 in computerspaces) and SB - 10 in computerspaces) or ((SB - 20 < 1 or SB - 20 in computerspaces) and SB + 10 in computerspaces):
                    SB = random.randint(1,100)
            computerspaces.append(SB)
            SBspaces.append(SB)
            SBadd = SB
            for SBcount in range(0,2):
                if direction == "left":
                    SBadd -= 1
                    if SBadd in rightnonos or SBadd < 1 or w == 1:
                        SBadd = SB+1
                        SB += 1                        
                        w = 1
                    SBspaces.append(SBadd)
                    computerspaces.append(SBadd)
                elif direction == "right":
                    SBadd += 1
                    if SBadd in leftnonos or SBadd > 100 or w == 1:
                        SBadd = SB-1
                        SB -= 1
                        w = 1
                    SBspaces.append(SBadd)
                    computerspaces.append(SBadd)
                elif direction == "up":
                    SBadd -= 10
                    if SB < 1 or SBadd < 1 or SBadd in computerspaces or w == 1:
                        SBadd = SB+10
                        SB += 10
                        w = 1
                    SBspaces.append(SBadd)
                    computerspaces.append(SBadd)
                elif direction == "down":
                    SBadd += 10
                    if SB > 100 or SBadd > 100 or SBadd in computerspaces or w == 1:
                        SBadd = SB-10
                        SB -= 10
                        w = 1
                    SBspaces.append(SBadd)
                    computerspaces.append(SBadd)
        if count == 4:
            wwtg = random.randint(0,3)
            direction = directions[wwtg]
            leftnonos+=computerspaces
            rightnonos+=computerspaces
            DS = random.randint(1,100)
            while DS in computerspaces:
                DS = random.randint(1,100)
            if direction == "left" or direction == "right":
                while ((DS - 1 in rightnonos or DS - 1 == 0) and DS + 1 in computerspaces) or ((DS + 1 in leftnonos or DS + 1 == 101) and DS - 1 in computerspaces):
                    DS = random.randint(1,100)
            if direction == "up" or direction == "down":
                while ((DS + 10 > 100 or DS + 10 in computerspaces) and DS - 10 in computerspaces) or ((DS - 10 < 1 or DS - 10 in computerspaces) and DS + 10 in computerspaces):
                    DS = random.randint(1,100)
            computerspaces.append(DS)
            DSspaces.append(DS)
            DSadd = DS
            if direction == "left":
                DSadd -= 1
                if DSadd in rightnonos or DSadd < 1 or v == 1:
                    DSadd = DS+1
                    DS += 1                        
                    v = 1
                DSspaces.append(DSadd)
                computerspaces.append(DSadd)
            elif direction == "right":
                DSadd += 1
                if DSadd in leftnonos or DSadd > 100 or v == 1:
                    DSadd = DS-1
                    DS -= 1
                    v = 1
                DSspaces.append(DSadd)
                computerspaces.append(DSadd)
            elif direction == "up":
                DSadd -= 10
                if DS < 1 or DSadd < 1 or DSadd in computerspaces or v == 1:
                    DSadd = DS+10
                    DS += 10
                    v = 1
                DSspaces.append(DSadd)
                computerspaces.append(DSadd)
            elif direction == "down":
                DSadd += 10
                if DS > 100 or DSadd > 100 or DSadd in computerspaces or v == 1:
                    DSadd = DS-10
                    DS -= 10
                    v = 1
                DSspaces.append(DSadd)
                computerspaces.append(DSadd)

    for ACboat in range(0,5):
        board[ACspaces[ACboat]-1] = " "
    for BSboat in range(0,4):
        board[BSspaces[BSboat]-1] = " "
    for CRboat in range(0,3):
        board[CRspaces[CRboat]-1] = " "
    for SBboat in range(0,3):
        board[SBspaces[SBboat]-1] = " "
    for DSboat in range(0,2):
        board[DSspaces[DSboat]-1] = " "
        
    if board.count(" ") == 100:
        redoboard = 1
   
#User making their boats
direction = "right"        
for usercount in range(0,5):
    if usercount == 0:
        while len(userspaces) != 5:
            
            if mouse.get_pressed()[2] and direction == "right":
                direction = "down"
            elif mouse.get_pressed()[2] and direction == "down":
                direction = "right"
            
            hmx,hmy = mouse.get_pos()
            hspacex = hmx/30
            hspacey = hmy/30
            hx = (30*hspacex)+2
            hy = (30*hspacey)+2
            
            if hspacex == 10:
                hspace = (hspacey)*(hspacex)
            else:
                hspace = str(hspacey-1)+str(hspacex)
                hspace = int(hspace)
                
            if (direction == "right" and hmy > 33 and hmy < 328 and hmx > 33 and hmx < 210) or (direction == "down" and hmy > 33 and hmy < 210 and hmx > 33 and hmx < 328):
                check = "green"
                for hACplacing in range(0,5):
                    if direction == "down":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        hy += 30
                    
                    elif direction == "right":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        hx += 30
                display.flip()        
                myClock.tick(10)
                boarddraw(screen)
                
            elif (direction == "right" and hmy > 33 and hmy < 328 and hmx > 209) or (direction == "down" and hmx > 33 and hmx < 328 and hmy > 209):
                check = "red"
                for hACplacing in range(0,5):
                    if direction == "down":
                        if hy < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                        hy += 30
                    
                    elif direction == "right":
                        if hx < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                        hx += 30
                display.flip()
                myClock.tick(10)
                boarddraw(screen)
                
            for evnt in event.get():                    
                if evnt.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                    mx, my = evnt.pos
                    if my < 328 and mx < 328 and check == "green":            
                        spacex = mx/30
                        spacey = my/30
                        x = (30*spacex)+2
                        y = (30*spacey)+2
                        if spacex == 10:
                            space = (spacey)*(spacex)
                        else:
                            space = str(spacey-1)+str(spacex)
                            space = int(space)
                        for ACplacing in range(0,5):
                            if direction == "down":
                                yourboard[space-1] = "A"
                                xA.append(x)
                                yA.append(y)
                                userspaces.append(space)
                                userACspaces.append(space)
                                space += 10
                                y += 30
                            
                            elif direction == "right":
                                yourboard[space-1] = "A"
                                xA.append(x)
                                yA.append(y)
                                display.flip()
                                userspaces.append(space)
                                userACspaces.append(space)
                                space += 1
                                x += 30
                                
                        def drawA(screen):
                            for drawcount in range(0,5):
                                x = xA[drawcount]
                                y = yA[drawcount]
                                draw.rect(screen,(0,255,255),(x,y,27,27),0)
                                display.flip()
                        drawA(screen)
                if evnt.type == QUIT:
                    quit()
                    
    if usercount == 1:
        while len(userspaces) != 9:
            
            if mouse.get_pressed()[2] and direction == "right":
                direction = "down"
            elif mouse.get_pressed()[2] and direction == "down":
                direction = "right"
            
            hmx,hmy = mouse.get_pos()
            hspacex = hmx/30
            hspacey = hmy/30
            hx = (30*hspacex)+2
            hy = (30*hspacey)+2
            if hspacex == 10:
                hspace = (hspacey)*(hspacex)
            else:
                hspace = str(hspacey-1)+str(hspacex)
                hspace = int(hspace)
                
            if (direction == "right" and hmy > 33 and hmy < 328 and hmx > 239) or (direction == "right" and (hspace in userspaces or hspace+1 in userspaces or hspace+2 in userspaces or hspace+3 in userspaces)) or (direction == "down" and hmx > 33 and hmx < 328 and hmy > 239) or (direction == "down" and (hspace in userspaces or hspace+10 in userspaces or hspace+20 in userspaces or hspace+30 in userspaces)):
                check = "red"
                for hACplacing in range(0,4):
                    if direction == "down":
                        if hy < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        if hx < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                
            elif (direction == "right" and hmy > 33 and hmy < 328 and hmx > 33 and hmx < 240) or (direction == "down" and hmy > 33 and hmy < 240 and hmx > 33 and hmx < 328):
                check = "green"
                for hACplacing in range(0,4):
                    if direction == "down":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                    
            for evnt in event.get():                    
                if evnt.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                    mx, my = evnt.pos
                    if my < 328 and mx < 328 and check == "green":            
                        spacex = mx/30
                        spacey = my/30
                        x = (30*spacex)+2
                        y = (30*spacey)+2
                        if spacex == 10:
                            space = (spacey)*(spacex)
                        else:
                            space = str(spacey-1)+str(spacex)
                            space = int(space)
                        for ACplacing in range(0,4):
                            if direction == "down":
                                yourboard[space-1] = "B"
                                xB.append(x)
                                yB.append(y)
                                userspaces.append(space)
                                userBSspaces.append(space)
                                space += 10
                                y += 30
                            
                            elif direction == "right":
                                yourboard[space-1] = "B"
                                xB.append(x)
                                yB.append(y)
                                userspaces.append(space)
                                userBSspaces.append(space)
                                space += 1
                                x += 30
                                
                        def drawB(screen):
                            for drawcount in range(0,4):
                                x = xB[drawcount]
                                y = yB[drawcount]
                                draw.rect(screen,(255,0,255),(x,y,27,27),0)
                                display.flip()
                        drawB(screen)
                if evnt.type == QUIT:
                    quit()
            
    if usercount == 2:
        while len(userspaces) != 12:
            
            if mouse.get_pressed()[2] and direction == "right":
                direction = "down"
            elif mouse.get_pressed()[2] and direction == "down":
                direction = "right"
            
            hmx,hmy = mouse.get_pos()
            hspacex = hmx/30
            hspacey = hmy/30
            hx = (30*hspacex)+2
            hy = (30*hspacey)+2
            if hspacex == 10:
                hspace = (hspacey)*(hspacex)
            else:
                hspace = str(hspacey-1)+str(hspacex)
                hspace = int(hspace)
            
            if (direction == "right" and hmy > 33 and hmy < 328 and hmx > 269) or (direction == "down" and hmx > 33 and hmx < 328 and hmy > 269) or (direction == "right" and (hspace in userspaces or hspace+1 in userspaces or hspace+2 in userspaces)) or (direction == "down" and (hspace in userspaces or hspace+10 in userspaces or hspace+20 in userspaces)):
                check = "red"
                for hACplacing in range(0,3):
                    if direction == "down":
                        if hy < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        if hx < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                drawB(screen)
                
            elif (direction == "right" and hmy > 33 and hmy < 328 and hmx > 33 and hmx < 270) or (direction == "down" and hmy > 33 and hmy < 270 and hmx > 33 and hmx < 328):
                check = "green"
                for hACplacing in range(0,3):
                    if direction == "down":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                drawB(screen)
                
            for evnt in event.get():                    
                if evnt.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                    mx, my = evnt.pos
                    if my < 328 and mx < 328 and check == "green":            
                        spacex = mx/30
                        spacey = my/30
                        x = (30*spacex)+2
                        y = (30*spacey)+2
                        if spacex == 10:
                            space = (spacey)*(spacex)
                        else:
                            space = str(spacey-1)+str(spacex)
                            space = int(space)
                        for ACplacing in range(0,3):
                            if direction == "down":
                                yourboard[space-1] = "C"
                                xC.append(x)
                                yC.append(y)
                                userspaces.append(space)
                                userCRspaces.append(space)
                                space += 10
                                y += 30
                            
                            elif direction == "right":
                                yourboard[space-1] = "C"
                                xC.append(x)
                                yC.append(y)
                                userspaces.append(space)
                                userCRspaces.append(space)
                                space += 1
                                x += 30
                                
                        def drawC(screen):
                            for drawcount in range(0,3):
                                x = xC[drawcount]
                                y = yC[drawcount]
                                draw.rect(screen,(255,255,0),(x,y,27,27),0)
                                display.flip()
                        drawC(screen)
                
                if evnt.type == QUIT:
                    quit()
    if usercount == 3:
        while len(userspaces) != 15:
            
            if mouse.get_pressed()[2] and direction == "right":
                direction = "down"
            elif mouse.get_pressed()[2] and direction == "down":
                direction = "right"
            
            hmx,hmy = mouse.get_pos()
            hspacex = hmx/30
            hspacey = hmy/30
            hx = (30*hspacex)+2
            hy = (30*hspacey)+2
            if hspacex == 10:
                hspace = (hspacey)*(hspacex)
            else:
                hspace = str(hspacey-1)+str(hspacex)
                hspace = int(hspace)
                
            if (direction == "right" and hmy > 33 and hmy < 328 and hmx > 269) or (direction == "down" and hmx > 33 and hmx < 328 and hmy > 269)  or (direction == "right" and (hspace in userspaces or hspace+1 in userspaces or hspace+2 in userspaces)) or (direction == "down" and (hspace in userspaces or hspace+10 in userspaces or hspace+20 in userspaces)):
                check = "red"
                for hACplacing in range(0,3):
                    if direction == "down":
                        if hy < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        if hx < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                drawB(screen)
                drawC(screen)
                
            elif (direction == "right" and hmy > 33 and hmy < 328 and hmx > 33 and hmx < 270) or (direction == "down" and hmy > 33 and hmy < 270 and hmx > 33 and hmx < 328):
                check = "green"
                for hACplacing in range(0,3):
                    if direction == "down":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                drawB(screen)
                drawC(screen)
                
            for evnt in event.get():                    
                if evnt.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                    mx, my = evnt.pos
                    if my < 328 and mx < 328 and check == "green":            
                        spacex = mx/30
                        spacey = my/30
                        x = (30*spacex)+2
                        y = (30*spacey)+2
                        if spacex == 10:
                            space = (spacey)*(spacex)
                        else:
                            space = str(spacey-1)+str(spacex)
                            space = int(space)
                        for ACplacing in range(0,3):
                            if direction == "down":
                                yourboard[space-1] = "S"
                                xS.append(x)
                                yS.append(y)
                                userspaces.append(space)
                                userSBspaces.append(space)
                                space += 10
                                y += 30
                            
                            elif direction == "right":
                                yourboard[space-1] = "S"
                                xS.append(x)
                                yS.append(y)
                                userspaces.append(space)
                                userSBspaces.append(space)
                                space += 1
                                x += 30
                                
                        def drawS(screen):
                            for drawcount in range(0,3):
                                x = xS[drawcount]
                                y = yS[drawcount]
                                draw.rect(screen,(194,14,254),(x,y,27,27),0)
                                display.flip()
                        drawS(screen)
                
                if evnt.type == QUIT:
                    quit()
    if usercount == 4:
        while len(userspaces) != 17:
            
            if mouse.get_pressed()[2] and direction == "right":
                direction = "down"
            elif mouse.get_pressed()[2] and direction == "down":
                direction = "right"
            
            hmx,hmy = mouse.get_pos()
            hspacex = hmx/30
            hspacey = hmy/30
            hx = (30*hspacex)+2
            hy = (30*hspacey)+2
            if hspacex == 10:
                hspace = (hspacey)*(hspacex)
            else:
                hspace = str(hspacey-1)+str(hspacex)
                hspace = int(hspace)
                
            if (direction == "right" and hmy > 33 and hmy < 328 and hmx > 299) or (direction == "down" and hmx > 33 and hmx < 328 and hmy > 299)  or (direction == "right" and (hspace in userspaces or hspace+1 in userspaces)) or (direction == "down" and (hspace in userspaces or hspace+10 in userspaces)):
                check = "red"
                for hACplacing in range(0,2):
                    if direction == "down":
                        if hy < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        if hx < 328:
                            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
                            display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                drawB(screen)
                drawC(screen)
                drawS(screen)
                
            elif (direction == "right" and hmy > 33 and hmy < 328 and hmx > 33 and hmx < 300) or (direction == "down" and hmy > 33 and hmy < 300 and hmx > 33 and hmx < 328):
                check = "green"
                for hACplacing in range(0,2):
                    if direction == "down":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hy += 30
                    
                    elif direction == "right":
                        draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
                        display.flip()
                        hx += 30
                myClock.tick(10)
                boarddraw(screen)
                drawA(screen)
                drawB(screen)
                drawC(screen)
                drawS(screen)
                
            for evnt in event.get():                    
                if evnt.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                    mx, my = evnt.pos
                    if my < 328 and mx < 328 and check == "green":            
                        spacex = mx/30
                        spacey = my/30
                        x = (30*spacex)+2
                        y = (30*spacey)+2
                        if spacex == 10:
                            space = (spacey)*(spacex)
                        else:
                            space = str(spacey-1)+str(spacex)
                            space = int(space)
                        for ACplacing in range(0,2):
                            if direction == "down":
                                yourboard[space-1] = "D"
                                xD.append(x)
                                yD.append(y)
                                userspaces.append(space)
                                userDSspaces.append(space)
                                space += 10
                                y += 30
                            
                            elif direction == "right":
                                yourboard[space-1] = "D"
                                xD.append(x)
                                yD.append(y)
                                userspaces.append(space)
                                userDSspaces.append(space)
                                space += 1
                                x += 30
                                
                        def drawD(screen):
                            for drawcount in range(0,2):
                                x = xD[drawcount]
                                y = yD[drawcount]
                                draw.rect(screen,(255,0,0),(x,y,27,27),0)
                                display.flip()
                        drawD(screen)
                
                if evnt.type == QUIT:
                    quit()
                
#Everybody's Moves
while True:
    while guesses != turncycle:
        #User moves
        hmx,hmy = mouse.get_pos()
        hspacex = hmx/30
        hspacey = hmy/30
        hx = (30*hspacex)+2
        hy = (30*hspacey)+2
        hspacey = hspacey-14
        if hspacex == 10:
            hspace =(hspacey+1)*(hspacex)
        else:
            hspace = str(hspacey)+str(hspacex)
            hspace = int(hspace)
        
        if hmy > 421 and hmy < 720 and hmx > 33 and hmx < 329 and hspace in userguesses:
            check = "red"
            draw.rect(screen,(255,0,0),(hx,hy,27,27),0)
            display.flip()
                    
            myClock.tick(10)
            bottomboard(screen)
            
            if xallow == 1:
                X_hits(screen)
            if oallow == 1:
                O_hits(screen)
            
        elif hmy > 421 and hmy < 720 and hmx > 33 and hmx < 329:
            check = "green"
            draw.rect(screen,(0,255,0),(hx,hy,27,27),0)
            display.flip()
                
            myClock.tick(10)
            bottomboard(screen)
            
            if xallow == 1:
                X_hits(screen)
            if oallow == 1:
                O_hits(screen)
            
        for evnt in event.get():                    
            if evnt.type == MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                mx, my = evnt.pos
                if my > 421 and mx < 329 and mx > 33 and check == "green":            
                    spacex = mx/30
                    spacey = my/30
                    x = (30*spacex)+2
                    y = (30*spacey)+2
                    spacey = spacey-14
                    if spacex == 10:
                        space =(spacey+1)*(spacex)
                    else:
                        space = str(spacey)+str(spacex)
                        space = int(space)
                    userguesses.append(space)
                    
                    if space in computerspaces:
                        
                        mixer.music.load('GrenadeSound.wav')
                        mixer.music.play()
                        
                        hitx.append(x)
                        hity.append(y)
                        
                        if defcountx == 0:
                            xallow = 1
                            defcountx = 1
                            def X_hits(screen):
                                text = fontHello.render("X" ,1, (0,0,0))
                                for count in range(0,len(hitx)):
                                    x = hitx[count]
                                    y = hity[count]
                                    screen.blit(text,Rect(x+5,y,0,0))
                                display.flip()
                        X_hits(screen)
                    else:
                        
                        mixer.music.load('Miss plop.wav')
                        mixer.music.play()
                        
                        missx.append(x)
                        missy.append(y)
                        if defcounto == 0:
                            oallow = 1
                            defcounto = 1
                            def O_hits(screen):
                                text = fontHello.render("O" ,1, (0,0,0))
                                for count in range(0,len(missx)):
                                    x = missx[count]
                                    y = missy[count]
                                    screen.blit(text,Rect(x+5,y,0,0))
                                display.flip()
                        O_hits(screen)
                            
                    guesses += 1
            
            if evnt.type == QUIT:                
                quit()
    
    if space in computerspaces:
        computerspaces[computerspaces.index(space)] = "X"
        if space in ACspaces:
            ACspaces[ACspaces.index(space)] = "X"
            board[space-1] = "X"
            if ACspaces == ["X","X","X","X","X"]:
                text = fontHello.render("X" ,1, (255,0,0))
                screen.blit(text,Rect(350,480,0,0))
        if space in BSspaces:
            BSspaces[BSspaces.index(space)] = "X"
            board[space-1] = "X"
            if BSspaces == ["X","X","X","X"]:
                text = fontHello.render("X" ,1, (255,0,0))
                screen.blit(text,Rect(350,530,0,0))
        if space in CRspaces:
            CRspaces[CRspaces.index(space)] = "X"
            board[space-1] = "X"
            if CRspaces == ["X","X","X"]:
                text = fontHello.render("X" ,1, (255,0,0))
                screen.blit(text,Rect(350,580,0,0))
        if space in SBspaces:
            SBspaces[SBspaces.index(space)] = "X"
            board[space-1] = "X"
            if SBspaces == ["X","X","X"]:
                text = fontHello.render("X" ,1, (255,0,0))
                screen.blit(text,Rect(350,630,0,0))
        if space in DSspaces:
            DSspaces[DSspaces.index(space)] = "X"
            board[space-1] = "X"
            if DSspaces == ["X","X"]:
                text = fontHello.render("X" ,1, (255,0,0))
                screen.blit(text,Rect(350,680,0,0))
    else:
        board[space-1] = "O"
    #User win check and print
    if computerspaces == ["X"]*17:
        mixer.music.load('Clapping.wav')
        mixer.music.play()
        screen.fill((0,0,0))
        text = fontHello.render("CONGRATS, YOU WIN!!!" ,1, (255,255,255))
        screen.blit(text,Rect(70,328,0,0))
        display.flip()
        time.wait(2000)
        break
        
    #Computer's guesses
    #AI Guessing in here
    direction = "nowhere"
    directions = ["up","down","left","right"]
    
    if ("X" in ACdeath and ACdeath != ["X"]*5) or ("X" in BSdeath and BSdeath != ["X"]*4) or ("X" in CRdeath and CRdeath != ["X"]*3) or ("X" in SBdeath and SBdeath != ["X"]*3) or ("X" in DSdeath and DSdeath != ["X"]*2):
        
        if defineddirection == 0:
            if comspace - 10 in alreadyguessed or comspace - 10 < 1 or (comspace in userACspaces and ((comspace - 10 in userspaces and comspace - 10 not in userACspaces) or (comspace - 20 in userspaces and comspace - 20 not in userACspaces) or (comspace - 30 in userspaces and comspace - 30 not in userACspaces) or (comspace - 40 in userspaces and comspace - 40 not in userACspaces))) or (comspace in userBSspaces and ((comspace - 10 in userspaces and comspace - 10 not in userBSspaces) or (comspace - 20 in userspaces and comspace - 20 not in userBSspaces) or (comspace - 30 in userspaces and comspace - 30 not in userBSspaces))) or (comspace in userCRspaces and ((comspace - 10 in userspaces and comspace - 10 not in userCRspaces) or (comspace - 20 in userspaces and comspace - 20 not in userCRspaces))) or (comspace in userSBspaces and ((comspace - 10 in userspaces and comspace - 10 not in userSBspaces) or (comspace - 20 in userspaces and comspace - 20 not in userSBspaces))) or (comspace in userDSspaces and ((comspace - 10 in userspaces and comspace - 10 not in userDSspaces))):
                del directions[directions.index("up")]
                
            if comspace + 10 in alreadyguessed or comspace + 10 > 100 or (comspace in userACspaces and ((comspace + 10 in userspaces and comspace + 10 not in userACspaces) or (comspace + 20 in userspaces and comspace + 20 not in userACspaces) or (comspace + 30 in userspaces and comspace + 30 not in userACspaces) or (comspace + 40 in userspaces and comspace + 40 not in userACspaces))) or (comspace in userBSspaces and ((comspace + 10 in userspaces and comspace + 10 not in userBSspaces) or (comspace + 20 in userspaces and comspace + 20 not in userBSspaces) or (comspace + 30 in userspaces and comspace + 30 not in userBSspaces))) or (comspace in userCRspaces and ((comspace + 10 in userspaces and comspace + 10 not in userCRspaces) or (comspace + 20 in userspaces and comspace + 20 not in userCRspaces))) or (comspace in userSBspaces and ((comspace + 10 in userspaces and comspace + 10 not in userSBspaces) or (comspace + 20 in userspaces and comspace + 20 not in userSBspaces))) or (comspace in userDSspaces and ((comspace + 10 in userspaces and comspace + 10 not in userDSspaces))):
                del directions[directions.index("down")]
            
            if comspace - 1 in alreadyguessed or comspace - 1 in rightnonos2 or comspace - 1 < 1 or (comspace in userACspaces and ((comspace - 1 in userspaces and comspace - 1 not in userACspaces) or (comspace - 2 in userspaces and comspace - 2 not in userACspaces) or (comspace - 3 in userspaces and comspace - 3 not in userACspaces) or (comspace - 4 in userspaces and comspace - 4 not in userACspaces))) or (comspace in userBSspaces and ((comspace - 1 in userspaces and comspace - 1 not in userBSspaces) or (comspace - 2 in userspaces and comspace - 2 not in userBSspaces) or (comspace - 3 in userspaces and comspace - 3 not in userBSspaces))) or (comspace in userCRspaces and ((comspace - 1 in userspaces and comspace - 1 not in userCRspaces) or (comspace - 2 in userspaces and comspace - 2 not in userCRspaces))) or (comspace in userSBspaces and ((comspace - 1 in userspaces and comspace - 1 not in userSBspaces) or (comspace - 2 in userspaces and comspace - 2 not in userSBspaces))) or (comspace in userDSspaces and ((comspace - 1 in userspaces and comspace - 1 not in userDSspaces))):
                del directions[directions.index("left")]
            
            if comspace + 1 in alreadyguessed or comspace + 1 in leftnonos2 or comspace + 1 > 100 or (comspace in userACspaces and ((comspace + 1 in userspaces and comspace + 1 not in userACspaces) or (comspace + 2 in userspaces and comspace + 2 not in userACspaces) or (comspace + 3 in userspaces and comspace + 3 not in userACspaces) or (comspace + 4 in userspaces and comspace + 4 not in userACspaces))) or (comspace in userBSspaces and ((comspace + 1 in userspaces and comspace + 1 not in userBSspaces) or (comspace + 2 in userspaces and comspace + 2 not in userBSspaces) or (comspace + 3 in userspaces and comspace + 3 not in userBSspaces))) or (comspace in userCRspaces and ((comspace + 1 in userspaces and comspace + 1 not in userCRspaces) or (comspace + 2 in userspaces and comspace + 2 not in userCRspaces))) or (comspace in userSBspaces and ((comspace + 1 in userspaces and comspace + 1 not in userSBspaces) or (comspace + 2 in userspaces and comspace + 2 not in userSBspaces))) or (comspace in userDSspaces and ((comspace + 1 in userspaces and comspace + 1 not in userDSspaces))):
                del directions[directions.index("right")]
            
                
            if len(directions) == 1:
                direction = directions[0]
            elif len(directions) > 1:
                wwtg = random.randint(0,len(directions)-1)
                direction = directions[wwtg]
            
        #When it has already found one going up
        if defineddirection == 1:
            newspace -= 10
            if newspace < 1 or newspace in alreadyguessed:
                defineddirection = 2
                newspace = comspace
            
        #Choosing to go up first
        elif direction == "up":
            newspace = comspace - 10
            if newspace in userspaces:
                defineddirection = 1
            if newspace not in userspaces:
                definedirection = 0
                
        #When it has found one going down
        if defineddirection == 2:
            newspace += 10
            if newspace > 100 or newspace in alreadyguessed:
                defineddirection = 1
                newspace = comspace - 10
                
        #Choosing to go down first
        elif direction == "down":
            newspace = comspace + 10
            if newspace in userspaces:
                defineddirection = 2
            if newspace not in userspaces:
                definedirection = 0
                
        #When it has found one going left
        if defineddirection == 3:
            newspace -= 1
            if newspace in rightnonos2 or newspace in alreadyguessed or newspace < 1:
                defineddirection = 4
                newspace = comspace
        
        #Choosing to try left first
        elif direction == "left":
            newspace = comspace - 1
            if newspace in userspaces:
                defineddirection = 3
            if newspace not in userspaces:
                definedirection = 0
                
        #When it has found one going right
        if defineddirection == 4:
            newspace += 1
            if newspace in leftnonos2 or newspace in alreadyguessed or newspace > 100:
                defineddirection = 3
                newspace = comspace - 1
                
        #Choosing to go right first
        elif direction == "right":
            newspace = comspace + 1
            if newspace in userspaces:
                defineddirection = 4
            if newspace not in userspaces:
                definedirection = 0
        
        #Making new hits after found one first
        alreadyguessed.append(newspace)
                
        if newspace in userspaces:
            text = fontHello.render("X" ,1, (0,0,0))
            newspace = str(newspace)
            if int(newspace) == 100:
                screen.blit(text,Rect(307,302,0,0))
            elif int(newspace) < 11:
                screen.blit(text,Rect((int(newspace)*30)+7,33,0,0))
            elif newspace[-1] == "0":
                screen.blit(text,Rect(307,(int(newspace[0]))*30+2,0,0))
            else:
                screen.blit(text,Rect((int(newspace[1:])*30)+7,((int(newspace[0]))+1)*30+2,0,0))
            display.flip()
            newspace = int(newspace)
            if newspace in userACspaces:
                ACdeath.append("X")
                yourboard[newspace-1] = "X"
                
                if ACdeath == ["X","X","X","X","X"]:
                    text = fontHello.render("X" ,1, (255,0,0))
                    screen.blit(text,Rect(350,80,0,0))
                    
            if newspace in userBSspaces:
                BSdeath.append("X")
                yourboard[newspace-1] = "X"
                
                if BSdeath == ["X","X","X","X"]:
                    text = fontHello.render("X" ,1, (255,0,0))
                    screen.blit(text,Rect(350,130,0,0))
                    
            if newspace in userCRspaces:
                CRdeath.append("X")
                yourboard[newspace-1] = "X"
                    
                if CRdeath == ["X","X","X"]:
                    text = fontHello.render("X" ,1, (255,0,0))
                    screen.blit(text,Rect(350,180,0,0))
                    
            if newspace in userSBspaces:
                SBdeath.append("X")
                yourboard[newspace-1] = "X"
                    
                if SBdeath == ["X","X","X"]:
                    text = fontHello.render("X" ,1, (255,0,0))
                    screen.blit(text,Rect(350,230,0,0))
                    
            if newspace in userDSspaces:
                DSdeath.append("X")
                yourboard[newspace-1] = "X"
                
                if DSdeath == ["X","X"]:
                    text = fontHello.render("X" ,1, (255,0,0))
                    screen.blit(text,Rect(350,280,0,0))
            
        else:
            yourboard[newspace-1] = "O"
            text = fontHello.render("O" ,1, (0,0,0))
            newspace = str(newspace)
            if int(newspace) == 100:
                screen.blit(text,Rect(307,302,0,0))
            elif int(newspace) < 11:
                screen.blit(text,Rect((int(newspace)*30)+7,33,0,0))
            elif newspace[-1] == "0":
                screen.blit(text,Rect(307,(int(newspace[0]))*30+2,0,0))
            else:
                screen.blit(text,Rect((int(newspace[1:])*30)+7,((int(newspace[0]))+1)*30+2,0,0))
            display.flip()
            
            newspace = int(newspace)
            if defineddirection == 1:
                defineddirection = 2
                newspace = comspace
            if defineddirection == 2:
                defineddirection = 1
                newspace = comspace
            if defineddirection == 3:
                defineddirection = 4
                newspace = comspace
            if defineddirection == 4:
                defineddirection = 3
                newspace = comspace
    
    #Guessing randomly when no leads are made.
            
    else:
        comspace = random.randint(1,100)
        while comspace in alreadyguessed:
            comspace = random.randint(1,100)
        defineddirection = 0
       
        alreadyguessed.append(comspace)
        
        if comspace in userspaces:
            text = fontHello.render("X" ,1, (0,0,0))
            comspace = str(comspace)
            if int(comspace) == 100:
                screen.blit(text,Rect(307,302,0,0))
            elif int(comspace) < 11:
                screen.blit(text,Rect((int(comspace)*30)+7,33,0,0))
            elif comspace[-1] == "0":
                screen.blit(text,Rect(307,(int(comspace[0]))*30+2,0,0))
            else:
                screen.blit(text,Rect((int(comspace[1:])*30)+7,((int(comspace[0]))+1)*30+2,0,0))
            display.flip()
            
            comspace = int(comspace)
            if comspace in userACspaces:
                if comspace in userACspaces:
                    ACdeath.append("X")
                    yourboard[comspace-1] = "X"
                    
            if comspace in userBSspaces:
                if comspace in userBSspaces:
                    BSdeath.append("X")
                    yourboard[comspace-1] = "X"
                    
            if comspace in userCRspaces:
                if comspace in userCRspaces:
                    CRdeath.append("X")
                    yourboard[comspace-1] = "X"
                    
            if comspace in userSBspaces:
                if comspace in userSBspaces:
                    SBdeath.append("X")
                    yourboard[comspace-1] = "X"
                    
            if comspace in userDSspaces:
                if comspace in userDSspaces:
                    DSdeath.append("X")
                    yourboard[comspace-1] = "X"
            
        else:
            yourboard[comspace-1] = "O"
            comspace = str(comspace)
            text = fontHello.render("O" ,1, (0,0,0))
            if int(comspace) == 100:
                screen.blit(text,Rect(307,302,0,0))
            elif int(comspace) < 11:
                screen.blit(text,Rect((int(comspace)*30)+7,33,0,0))
            elif comspace[-1] == "0":
                screen.blit(text,Rect(307,(int(comspace[0]))*30+2,0,0))
            else:
                screen.blit(text,Rect((int(comspace[1:])*30)+7,((int(comspace[0]))+1)*30+2,0,0))
            display.flip()
            comspace = int(comspace)
    #Computer win check and print
    if ACdeath == ["X","X","X","X","X"] and BSdeath == ["X","X","X","X"] and CRdeath == ["X","X","X"] and SBdeath == ["X","X","X"] and DSdeath == ["X","X"]:
        mixer.music.load('TPIRLOSS.wav')
        mixer.music.play()
        screen.fill((0,0,0))
        text = fontHello.render("THE COMPUTER BEAT YOU!!!" ,1, (255,255,255))
        screen.blit(text,Rect(30,328,0,0))
        display.flip()
        time.wait(2000)
        break
    
    turncycle += 1
quit()