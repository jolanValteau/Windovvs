import pygame
from datetime import datetime
import time
from PIL import Image




x=1300
y=720
couleur_fenetre=(0,0,0)

pygame.init()

police=pygame.font.Font("police/policeApex.ttf",20)
pygame.display.set_caption("Jeu vidéo")
fenetre=pygame.display.set_mode()
x,y=fenetre.get_size()
fenetre=pygame.display.set_mode((x,y), pygame.FULLSCREEN)
background=pygame.image.load("img/Desktop/Windows10_fond_ecran.jpg")
barN=pygame.image.load("img/Desktop/barre_des_taches_windows.PNG")
barM=pygame.image.load("img/Desktop/barre_des_taches_windows_click.PNG")
logoapex=pygame.image.load("img/Desktop/logo_apex_raccourcit_click.jpg")
winN=pygame.image.load("img/Desktop/menu_windows.png")
winApex=pygame.image.load("img/Desktop/winApex.png")

apexN=pygame.image.load("img/Desktop/apex.png")
apexM=pygame.image.load("img/Desktop/logo_apex_raccourcit_click.jpg")
apex=apexN



lB={}
lBAbs={}
bar=barN
win=winN
carre=False

winApexAbs = winApex

# Static button only
def addB(nom,coo,coomilieu,conrect):
    global lB
    lB[nom]={"coo":coo,"coomilieu":coomilieu,"rect":conrect}

# Absolute button only
def addBAbs(nom,coo,coomilieu,conrect):
    global lBAbs
    lBAbs[nom]={"coo":coo,"coomilieu":coomilieu,"rect":conrect}


addB("bar" , (0,y-bar.get_height()) , (bar.get_height()/2 , y-bar.get_height()+bar.get_height()/2 ) , (bar.get_rect(center=(0-bar.get_width()/2+bar.get_height() , y-bar.get_height()+bar.get_height()/2))))

addB("win" , (0, y-bar.get_height()-win.get_height()) , (win.get_width()/2 , y-win.get_height()-win.get_height()+win.get_height()/2 ) , (bar.get_rect(center=(win.get_width()/2 , y-win.get_height()-win.get_height()+win.get_height()/2))))

addB("quit" , (0, y-bar.get_height()*2) , (bar.get_height()/2 , y-bar.get_height()-bar.get_height()/2 ) , pygame.Rect(0, y-bar.get_height()*2, 0+bar.get_height(), y-bar.get_height()*2 +bar.get_height()) )


# Apps :

xapex,yapex = 100,100
addBAbs("apex" , (xapex,yapex) , (xapex+(apex.get_width()/2) , yapex+(apex.get_height()/2) ) , (apex.get_rect(center=( xapex+(apex.get_width()/2) , yapex+(apex.get_height()/2)  ))))

# Apps windows carre :

winApps = []

xwinapex,ywinapex = 50,700
addBAbs("winApex" , (xwinapex,ywinapex) , (xwinapex+(winApex.get_width()/2) , ywinapex+(winApex.get_height()/2) ) , (winApex.get_rect(center=( xwinapex+(winApex.get_width()/2) , ywinapex+(winApex.get_height()/2)  ))))
doubleClickApex = 0

winApps.append( [pygame.image.load("img/Desktop/winApex.png"), "winApex"])

winAppsAbs = winApps

#  END Apps

game = "Desktop"
bg = pygame.transform.scale(background, (x,y))
black=(0,0,0)

run=True

# Apex Legends
def Apex():
    global lB

    game="Apex"
    conM=pygame.image.load("img/Apex Legends/bouton continuer - Modifié.png")
    conN=pygame.image.load("img/Apex Legends/bouton continuer.png")
    annM=pygame.image.load("img/Apex Legends/bouton echap - Modifié.png")
    annN=pygame.image.load("img/Apex Legends/bouton echap.png")
    leavePopup=pygame.image.load("img/Apex Legends/leave popup.png")
    lobbyapex=pygame.image.load("img/Apex Legends/Apex lobby.jpg")

    bg = pygame.transform.scale(lobbyapex, (x,y))

    con=conN
    ann=annN

    leavePopup=pygame.transform.scale(leavePopup, ( x , int(leavePopup.get_height() * (x/leavePopup.get_width()) ) ))
    leaveupcoo=(x/2-leavePopup.get_width()/2 , y/2-leavePopup.get_height()/2 )

    addB("con" , (x*0.4,y*0.52) , (x*0.4+con.get_width()/2 , y*0.52+con.get_height()/2 ) , con.get_rect(center=(x*0.4+con.get_width()/2 , y*0.52+con.get_height()/2 )))
    addB("ann" , (x*0.5,y*0.52) , (x*0.5+ann.get_width()/2 , y*0.52+ann.get_height()/2 ) , ann.get_rect(center=(x*0.5+ann.get_width()/2 , y*0.52+ann.get_height()/2 )))



    while game == "Apex":
        fenetre.blit(bg, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_F4 and pygame.key.get_mods() & pygame.KMOD_ALT:
                    game="Desktop"
                    bg = pygame.transform.scale(background, (x,y))
                    exit_=False
                    break
                if event.key==pygame.K_ESCAPE:

                    exit_=True

                    while exit_:
                        fenetre.blit(leavePopup, leaveupcoo)
                        fenetre.blit(con, lB["con"]["coo"])
                        fenetre.blit(ann, lB["ann"]["coo"])
                        pygame.display.flip()

                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEMOTION:
                                coo=event.pos
                                if lB["con"]["rect"].collidepoint(coo[0],coo[1]):
                                    con=conM
                                    ann=annN
                                elif lB["ann"]["rect"].collidepoint(coo[0],coo[1]):
                                    ann=annM
                                    con=conN
                                else:
                                    con=conN
                                    ann=annN
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                if con==conM:
                                    game="Desktop"
                                    exit_=False
                                    break
                                elif ann==annM:
                                    exit_=False
                                    ann=annN
                                    break
                            fenetre.blit(bg, (0, 0))
                            fenetre.blit(leavePopup, leaveupcoo)
                            fenetre.blit(con, lB["con"]["coo"])
                            fenetre.blit(ann, lB["ann"]["coo"])
                            pygame.display.flip()
# End Apex Legends

# WINDOVVS 12 mac for SYSTEM 128x linux edition
while run:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    heure = police.render ( dt_string, 1 , (255,255,255) )
    bg = pygame.transform.scale(background, (x,y))
    fenetre.blit(bg, (0, 0))
    fenetre.blit(apex, (xapex,yapex))
    fenetre.blit(bar,(0,y-bar.get_height()))
    fenetre.blit(heure,(x-162,y-31))
    if carre:
        fenetre.blit(win, (0, y-bar.get_height()-win.get_height()))
        for app in winApps:
            fenetre.blit(app[0], (lBAbs[app[1]]["coo"] ))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                Apex()
            if event.key == pygame.K_F4 and pygame.key.get_mods() & pygame.KMOD_ALT:
                run=False

        if event.type==pygame.MOUSEMOTION:
            coo=event.pos
            if lB["bar"]["rect"].collidepoint(coo[0],coo[1]):
                bar=barM
                apex=apexN
            elif lBAbs["apex"]["rect"].collidepoint(coo[0],coo[1]) or doubleClickApex == 1:
                apex=apexM
                bar=barN
            else:
                bar=barN
                apex=apexN
            if carre==True:
                if lBAbs["winApex"]["rect"].collidepoint(coo[0],coo[1]):

                    src = Image.open("img/Desktop/winApex.png")
                    largeurI, hauteurI = src.size
                    dest = Image.open("img/Desktop/winApexChange.png")

                    for xI in range(largeurI):
                        for yI in range(hauteurI):
                            color = src.getpixel((xI,yI))
                            dest.putpixel((xI,yI),( color[0]+100 ,color[1]+10,color[2]+10 ))

                    dest.save("img/Desktop/winApexChange.png")

                    for app in winApps:
                        if app[1] == "winApex":
                            app[0] = pygame.image.load("img/Desktop/winApexChange.png")
                else:
                    win = winN
                    winApps == winAppsAbs

        if event.type==pygame.MOUSEBUTTONDOWN:
            coo=event.pos

            if apex == apexM:
                cu = time.monotonic()
                if doubleClickApex == 0:
                    doubleClickApexCu = time.monotonic()
                event = pygame.event.wait()
                while event.type!=pygame.MOUSEBUTTONUP:
                    event = pygame.event.wait()
                    if  event.type==pygame.MOUSEMOTION and time.monotonic()-cu>0.2:
                        doubleClickApex = 0
                        (xapex,yapex)=event.pos[0]-(apex.get_width()/2),event.pos[1]-(apex.get_height()/2)
                        addBAbs("apex" , (xapex,yapex) , (xapex+(apex.get_width()/2) , yapex+(apex.get_height()/2) ) , (apex.get_rect(center=( xapex+(apex.get_width()/2) , yapex+(apex.get_height()/2)  ))))
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        heure = police.render ( dt_string, 1 , (255,255,255) )
                        bg = pygame.transform.scale(background, (x,y))
                        fenetre.blit(bg, (0, 0))
                        fenetre.blit(apex, (xapex,yapex))
                        fenetre.blit(bar,(0,y-bar.get_height()))
                        fenetre.blit(heure,(x-162,y-31))
                        if carre:
                            fenetre.blit(win, (0, y-bar.get_height()-win.get_height()))
                        pygame.display.flip()

                if time.monotonic()- doubleClickApexCu > 0.2:
                    doubleClickApex = 0
                if time.monotonic()- doubleClickApexCu < 0.2 and doubleClickApex != 1:
                    doubleClickApex=1
                elif time.monotonic()- doubleClickApexCu < 0.2 and doubleClickApex == 1:
                    Apex()
                    doubleClickApex = 0
            if carre==True:
                if not(win.get_rect(center=(win.get_width()/2 , y-bar.get_height()-win.get_height()/2)).collidepoint(coo[0],coo[1])):
                    carre=False
                if lB["quit"]["rect"].collidepoint(coo[0],coo[1]):
                    run = False
            elif bar==barM:
                carre=True


pygame.quit()
# END