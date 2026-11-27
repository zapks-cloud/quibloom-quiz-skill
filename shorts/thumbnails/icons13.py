from icons12 import *
import icons10, math
def landmark():
    im,d=new()
    W=(255,255,255);Y=(255,208,48);C=(38,190,217);G=(92,200,150);P=(255,120,160)
    # tower (lattice-like): tall triangle with arch
    d.polygon([(500,100),(380,860),(620,860)],fill=C)
    d.polygon([(500,230),(450,560),(550,560)],fill=(18,48,70))
    d.pieslice((440,700,560,980),180,360,fill=(18,48,70))
    d.rectangle((400,520,600,550),fill=W); d.rectangle((420,330,580,355),fill=W)
    # dome building left
    d.rectangle((90,640,330,860),fill=Y); d.pieslice((120,500,300,780),180,360,fill=P)
    d.rectangle((60,640,360,660),fill=W)
    # arch building right
    d.rectangle((680,560,940,860),fill=G)
    for x in (710,780,850): d.pieslice((x,640,x+60,720),180,360,fill=(18,48,70)); d.rectangle((x,680,x+60,780),fill=(18,48,70))
    return im
icons10.ICONS['landmark']=landmark
