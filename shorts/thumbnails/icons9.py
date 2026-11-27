from icons8 import *
import icons7
def mosque():
    im,d=new()
    d.rectangle((300,520,700,780),fill=(240,232,214))
    d.pieslice((300,330,700,710),180,360,fill=(70,140,170))
    d.pieslice((410,250,590,430),180,360,fill=(60,120,150))
    d.rectangle((495,200,505,260),fill=(200,170,60))
    d.ellipse((488,180,512,204),fill=(230,190,60))
    for x in (190,770):
        d.rectangle((x,360,x+40,780),fill=(232,222,200))
        d.polygon([(x-6,360),(x+46,360),(x+20,290)],fill=(200,70,60))
        d.rectangle((x-8,470,x+48,482),fill=(200,170,60))
    for x in (350,470,590):
        d.pieslice((x,600,x+60,680),180,360,fill=(90,90,110)); d.rectangle((x,640,x+60,780),fill=(90,90,110))
    d.rectangle((150,780,850,810),fill=(120,160,90))
    return im
icons7.ICONS.update(mosque=mosque);ICONS=icons7.ICONS
