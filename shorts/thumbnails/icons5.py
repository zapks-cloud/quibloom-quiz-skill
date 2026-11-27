from icons4 import *
import icons4
def castle():
    im,d=new()
    d.rectangle((150,420,850,900),fill=GRAY)
    for x in (150,290,430,570,710):
        d.rectangle((x,360,x+100,420),fill=GRAY)
    d.rectangle((90,300,290,900),fill=(150,160,170));d.rectangle((710,300,910,900),fill=(150,160,170))
    for x in (90,170,250,710,790,870):
        d.rectangle((x,250,x+40,300),fill=(150,160,170))
    d.pieslice((400,600,600,1000),180,360,fill=BR) if False else None
    d.rectangle((420,640,580,900),fill=BR);d.ellipse((420,580,580,700),fill=BR)
    d.rectangle((170,400,210,470),fill=(40,60,80));d.rectangle((790,400,830,470),fill=(40,60,80))
    d.line((500,150,500,300),fill=WHITE,width=8) if False else None
    d.polygon([(500,100),(500,180),(600,140)],fill=RED);d.line((500,100,500,260),fill=WHITE,width=10)
    return im
icons4.ICONS.update(castle=castle); ICONS=icons4.ICONS
