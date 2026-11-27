from icons10 import *
import icons10
def moons():
    im,d=new()
    # big cratered moon
    d.ellipse((120,120,800,800),fill=(222,224,228))
    d.pieslice((120,120,800,800),300,60,fill=(205,208,214))
    for (x,y,r) in [(300,260,90),(520,200,55),(560,460,110),(280,520,70),(420,680,50),(690,330,45),(650,640,40),(200,380,38)]:
        d.ellipse((x-r,y-r,x+r,y+r),fill=(176,180,190)); d.ellipse((x-r+10,y-r+10,x+r-6,y+r-6),fill=(192,196,205))
    # small planet with moon dot beside
    d.ellipse((700,620,960,880),fill=(252,150,60)); d.ellipse((790,640,880,730),fill=(255,190,110))
    d.ellipse((620,560,690,630),fill=(222,224,228),outline=(120,130,145),width=5)
    return im
icons10.ICONS['moons']=moons
def dino():
    im,d=new()
    G=(92,184,92);GD=(60,140,70);W=(255,255,255)
    # tail
    d.polygon([(60,640),(300,470),(420,520),(380,640),(220,700)],fill=G)
    # body
    d.ellipse((260,330,640,700),fill=G)
    # neck+head
    d.polygon([(560,380),(700,230),(760,170),(960,200),(970,330),(900,350),(780,380),(690,520)],fill=G)
    # lower jaw
    d.polygon([(780,350),(960,340),(930,420),(790,400)],fill=GD)
    # teeth
    for x in (800,840,880,920): d.polygon([(x,348),(x+16,348),(x+8,376)],fill=W)
    # eye
    d.ellipse((780,210,830,260),fill=W); d.ellipse((800,222,822,246),fill=(20,30,40))
    # tiny arm
    d.polygon([(620,470),(710,500),(700,525),(610,505)],fill=GD)
    # legs
    d.polygon([(380,620),(520,620),(540,830),(420,830)],fill=GD)
    d.polygon([(330,820),(560,820),(560,880),(300,880)],fill=GD)
    d.polygon([(430,620),(560,640),(600,830),(500,830)],fill=G)
    # belly spots / spikes
    for (x,y) in ((300,420),(360,360),(430,330),(500,330)): d.polygon([(x,y),(x+30,y-50),(x+60,y)],fill=GD)
    return im
icons10.ICONS['dino']=dino
def chemflask():
    im,d=new()
    W=(255,255,255);G=(92,200,150);B=(200,225,240)
    d.polygon([(420,120),(580,120),(580,400),(880,860),(120,860),(420,400)],fill=B)
    d.polygon([(290,640),(710,640),(880,860),(120,860)],fill=G)
    d.rectangle((390,90,610,140),fill=W)
    for (x,y,r) in ((420,560,34),(560,500,26),(500,600,20)): d.ellipse((x-r,y-r,x+r,y+r),fill=W)
    # atom
    d.ellipse((780,160,900,280),fill=(255,208,48)); d.ellipse((90,200,160,270),fill=(38,190,217))
    return im
icons10.ICONS['chemflask']=chemflask
