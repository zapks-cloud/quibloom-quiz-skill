from icons11 import *
import icons10
from PIL import ImageFont
def mathicon():
    im,d=new()
    W=(255,255,255);Y=(255,208,48);C=(38,190,217);G=(92,200,150);P=(255,120,160)
    # right triangle with right-angle mark
    d.polygon([(130,860),(130,330),(700,860)],fill=C)
    d.polygon([(190,800),(190,480),(530,800)],fill=(18,48,70))
    d.rectangle((130,760,230,860),outline=W,width=10)
    # hexagon
    import math
    cx,cy,r=700,300,190
    d.polygon([(cx+r*math.cos(math.radians(60*i)),cy+r*math.sin(math.radians(60*i))) for i in range(6)],fill=Y)
    # pi
    f=None
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf'):
        try: f=ImageFont.truetype(p,260);break
        except Exception: pass
    if f: d.text((cx-90,cy-175),'\u03c0',font=f,fill=(18,48,70))
    # plus / equals marks
    d.rectangle((760,700,940,730),fill=W); d.rectangle((845,615,855,815),fill=W)
    d.rectangle((560,880,720,905),fill=P)
    return im
icons10.ICONS['mathicon']=mathicon
