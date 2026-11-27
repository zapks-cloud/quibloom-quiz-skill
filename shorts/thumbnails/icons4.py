from icons3 import *
def dino():
    im,d=new();d.ellipse((150,380,700,760),fill=GREEN);d.polygon([(650,430),(940,330),(900,480),(700,560)],fill=GREEN);d.ellipse((700,240,950,440),fill=GREEN)
    d.polygon([(160,520),(30,700),(200,640)],fill=GREEN);d.ellipse((840,290,880,330),fill=WHITE)
    for x in (270,350,430,510):d.polygon([(x,400),(x+40,300),(x+80,390)],fill=ORG)
    d.rectangle((290,700,370,880),fill=(80,150,50));d.rectangle((520,700,600,880),fill=(80,150,50));return im
def landmark():
    im,d=new();d.polygon([(500,60),(560,160),(440,160)],fill=GRAY);d.polygon([(440,160),(560,160),(640,880),(360,880)],fill=SAND)
    d.rectangle((300,540,700,600),fill=(214,196,160));d.rectangle((250,880,750,930),fill=(214,196,160));d.polygon([(430,600),(570,600),(600,880),(400,880)],fill=(190,170,130))
    d.ellipse((460,260,540,340),fill=NAVY);return im
def mask():
    im,d=new();d.ellipse((150,100,850,880),fill=SAND);d.polygon([(220,350),(400,380),(340,470),(220,430)],fill=NAVY);d.polygon([(780,350),(600,380),(660,470),(780,430)],fill=NAVY)
    d.arc((300,520,700,820),20,160,fill=RED,width=40);d.polygon([(500,420),(550,560),(450,560)],fill=(214,196,160));d.line((500,100,500,10),fill=YEL,width=40);return im
def letters():
    im,d=new();d.rounded_rectangle((60,160,640,700),90,fill=BLUE);d.polygon([(160,700),(300,700),(160,860)],fill=BLUE)
    d.rounded_rectangle((380,300,940,820),90,fill=ORG);d.polygon([(840,820),(700,820),(840,940)],fill=ORG)
    d.polygon([(210,560),(350,260),(490,560)],fill=WHITE);d.polygon([(280,560),(350,380),(420,560)],fill=BLUE);d.rectangle((250,500,450,540),fill=WHITE)
    d.line((530,420,820,420),fill=WHITE,width=36);d.line((530,540,820,540),fill=WHITE,width=36);d.line((530,660,720,660),fill=WHITE,width=36);return im
def crown():
    im,d=new();d.polygon([(100,760),(60,300),(300,520),(500,200),(700,520),(940,300),(900,760)],fill=YEL);d.rectangle((100,760,900,860),fill=ORG)
    for x,y in((60,300),(500,200),(940,300)):d.ellipse((x-45,y-45,x+45,y+45),fill=RED)
    for x in(300,500,700):d.ellipse((x-35,670,x+35,740),fill=BLUE)
    return im
def dress():
    im,d=new();d.polygon([(380,120),(500,250),(620,120),(660,300),(600,380),(900,880),(100,880),(400,380),(340,300)],fill=PINK)
    d.rectangle((400,380,600,440),fill=RED);d.polygon([(300,880),(500,540),(700,880)],fill=(220,95,140));return im
def shoes():
    im,d=new();d.ellipse((260,130,560,430),fill=RED);d.polygon([(260,260),(260,600),(380,600),(380,260)],fill=RED)
    d.polygon([(100,640),(100,540),(380,420),(900,620),(900,740),(100,740)],fill=RED);d.rectangle((90,740,910,820),fill=WHITE);d.rectangle((90,740,300,830),fill=WHITE);return im
def pot():
    im,d=new();d.rounded_rectangle((180,360,820,800),70,fill=GRAY);d.rectangle((120,420,180,490),fill=GRAY);d.rectangle((820,420,880,490),fill=GRAY);d.rounded_rectangle((200,300,800,360),30,fill=(190,205,220))
    d.ellipse((460,240,540,300),fill=WHITE);d.arc((280,60,500,300),270,70,fill=WHITE,width=24);d.arc((500,60,720,300),90,290,fill=WHITE,width=24) if False else None
    for x in(330,500,670):d.line((x,260,x-40,150),fill=WHITE,width=24)
    return im
def lantern():
    im,d=new();d.rectangle((470,40,530,170),fill=YEL);d.ellipse((130,150,870,810),fill=RED);d.ellipse((330,150,670,810),fill=(200,50,50));d.rectangle((400,760,600,830),fill=YEL)
    d.rectangle((120,330,880,380),fill=YEL) if False else None
    for x in(420,500,580):d.line((x,830,x,950),fill=YEL,width=22)
    d.ellipse((300,420,700,540),fill=YEL) if False else None;return im
def fireworks():
    im,d=new()
    for cx,cy,c in((500,420,RED),(250,300,YEL),(760,280,CYAN)):
        for k in range(12):
            a=k*math.pi/6;d.line((cx+60*math.cos(a),cy+60*math.sin(a),cx+190*math.cos(a),cy+190*math.sin(a)),fill=c,width=22)
        d.ellipse((cx-30,cy-30,cx+30,cy+30),fill=WHITE)
    return im
def dragon():
    im,d=new();d.ellipse((120,300,520,640),fill=RED);d.ellipse((400,250,860,600),fill=RED);d.polygon([(780,330),(960,380),(780,440)],fill=ORG)
    d.polygon([(560,260),(640,100),(680,280)],fill=YEL);d.ellipse((650,330,700,380),fill=YEL);d.arc((100,500,600,900),180,360,fill=RED,width=90);d.polygon([(100,640),(40,820),(220,720)],fill=ORG);return im
ICONS.update(dino=dino,landmark=landmark,mask=mask,letters=letters,crown=crown,dress=dress,shoes=shoes,pot=pot,lantern=lantern,fireworks=fireworks,dragon=dragon)
def pagoda():
    im,d=new()
    for i,(w,y) in enumerate(((620,700),(500,520),(380,340),(260,180))):
        d.polygon([(500-w/2-60,y+60),(500+w/2+60,y+60),(500+w/2,y),(500-w/2,y)],fill=RED)
        d.rectangle((500-w/2+30,y+60,500+w/2-30,y+160),fill=SAND if i%2==0 else (214,196,160)) if i<3 else None
    d.polygon([(480,170),(520,170),(500,70)],fill=YEL);d.rectangle((250,880,750,930),fill=GRAY);d.rectangle((440,760,560,880),fill=BR);return im
def dancer():
    im,d=new();d.ellipse((430,80,570,220),fill=ORG);d.polygon([(450,220),(550,220),(560,500),(440,500)],fill=PINK)
    d.polygon([(440,420),(560,420),(900,720),(100,720)],fill=PINK);d.line((470,250,200,150),fill=ORG,width=44);d.line((530,250,800,330),fill=ORG,width=44)
    d.line((470,720,430,900),fill=ORG,width=40);d.line((540,720,600,900),fill=ORG,width=40);return im
ICONS.update(pagoda=pagoda,dancer=dancer)
