from icons5 import *
import icons5
def ziggurat():
    im,d=new()
    for i,(w,y) in enumerate(((700,740),(540,590),(380,440),(220,290))):
        d.rectangle((500-w/2,y,500+w/2,y+150),fill=SAND if i%2==0 else (214,196,160))
    d.rectangle((460,160,540,290),fill=BR);d.polygon([(450,160),(550,160),(500,90)],fill=YEL)
    d.rectangle((460,740+30,540,890),fill=BR);d.rectangle((120,890,880,930),fill=GRAY);return im
icons5.ICONS.update(ziggurat=ziggurat);ICONS=icons5.ICONS
