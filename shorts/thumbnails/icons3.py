from icons2 import *
def ship():
    im,d=new();d.polygon([(80,600),(920,600),(780,780),(220,780)],fill=BR);d.polygon([(80,600),(40,470),(110,470),(150,600)],fill=BR);d.polygon([(920,600),(960,470),(890,470),(850,600)],fill=BR)
    d.rectangle((485,150,515,600),fill=(120,75,40));d.polygon([(500,170),(820,560),(500,560)],fill=RED);d.polygon([(500,170),(180,560),(500,560)],fill=WHITE)
    for x in (300,500,700): d.ellipse((x-30,660,x+30,720),fill=YEL)
    return im
def pyramid():
    im,d=new();d.polygon([(500,120),(960,800),(40,800)],fill=SAND);d.polygon([(500,120),(960,800),(560,800)],fill=(214,190,140))
    d.ellipse((420,200,580,360),fill=YEL) if False else None
    for y in (330,480,630):d.line((500-(y-120)*0.68,y,500+(y-120)*0.68,y),fill=(200,175,125),width=10)
    d.ellipse((700,100,860,260),fill=YEL);return im
def butterfly():
    im,d=new();d.ellipse((130,160,490,520),fill=PURP);d.ellipse((510,160,870,520),fill=PURP);d.ellipse((190,480,490,820),fill=PINK);d.ellipse((510,480,810,820),fill=PINK)
    d.rounded_rectangle((470,260,530,820),30,fill=NAVY);d.line((490,260,380,110),fill=NAVY,width=12);d.line((510,260,620,110),fill=NAVY,width=12)
    for x,y in((310,340),(690,340)):d.ellipse((x-50,y-50,x+50,y+50),fill=WHITE)
    return im
def bird():
    im,d=new();d.ellipse((200,330,760,760),fill=BLUE);d.ellipse((600,200,860,460),fill=BLUE);d.polygon([(840,300),(960,340),(840,380)],fill=ORG)
    d.ellipse((730,270,780,320),fill=WHITE);d.ellipse((745,285,765,305),fill=NAVY);d.polygon([(200,450),(40,380),(80,560),(200,560)],fill=(50,110,200));d.ellipse((320,420,620,640),fill=(110,170,250))
    d.line((440,760,440,880),fill=ORG,width=18);d.line((560,760,560,880),fill=ORG,width=18);return im
def cat():
    im,d=new();d.polygon([(190,420),(200,120),(400,290)],fill=ORG);d.polygon([(810,420),(800,120),(600,290)],fill=ORG);d.ellipse((150,230,850,830),fill=ORG)
    for x in(350,650):d.ellipse((x-55,460,x+55,570),fill=WHITE);d.ellipse((x-22,480,x+22,550),fill=NAVY)
    d.polygon([(470,610),(530,610),(500,660)],fill=PINK)
    for s in(-1,1):
        for k in(0,40,80):d.line((500+s*90,660+k//2,500+s*330,630+k),fill=WHITE,width=8)
    return im
def compass():
    im,d=new();d.ellipse((90,90,910,910),fill=YEL,outline=ORG,width=40);d.ellipse((200,200,800,800),fill=WHITE)
    d.polygon([(500,230),(570,500),(430,500)],fill=RED);d.polygon([(500,770),(570,500),(430,500)],fill=BLUE);d.ellipse((470,470,530,530),fill=NAVY);return im
def gamepad():
    im,d=new();d.rounded_rectangle((90,300,910,720),200,fill=PURP);d.rectangle((230,440,400,490),fill=WHITE);d.rectangle((290,380,340,550),fill=WHITE)
    for x,y,c in((700,420,RED),(780,500,YEL),(620,500,GREEN),(700,580,BLUE)):d.ellipse((x-38,y-38,x+38,y+38),fill=c)
    return im
def gem():
    im,d=new();d.polygon([(280,200),(720,200),(900,420),(500,880),(100,420)],fill=CYAN);d.polygon([(280,200),(400,420),(100,420)],fill=(100,220,240));d.polygon([(720,200),(900,420),(600,420)],fill=(20,150,180))
    d.polygon([(400,420),(600,420),(500,880)],fill=(60,200,225));d.polygon([(280,200),(720,200),(600,420),(400,420)],fill=(160,235,250));return im
def cross():
    im,d=new();d.rounded_rectangle((90,90,910,910),120,fill=WHITE);d.rectangle((390,200,610,800),fill=RED);d.rectangle((200,390,800,610),fill=RED);return im
def moonbed():
    im,d=new();d.ellipse((560,80,860,380),fill=YEL);d.ellipse((620,60,920,340),fill=NAVY) if False else None
    d.rounded_rectangle((60,560,940,700),30,fill=BLUE);d.rectangle((60,700,110,840),fill=BR);d.rectangle((890,700,940,840),fill=BR);d.rounded_rectangle((100,440,420,570),50,fill=WHITE)
    for x,y in((180,200),(400,130),(300,330)):d.ellipse((x-14,y-14,x+14,y+14),fill=YEL)
    return im
def clapper():
    im,d=new();d.rounded_rectangle((90,380,910,880),40,fill=GRAY);d.rectangle((90,380,910,470),fill=NAVY)
    d.polygon([(90,250),(910,150),(930,290),(110,390)],fill=WHITE)
    for x in range(150,900,160):d.polygon([(x,265),(x+80,255),(x+30,370),(x-50,380)],fill=NAVY)
    d.polygon([(480,560),(480,780),(670,670)],fill=YEL);return im
def mathsym():
    im,d=new();d.ellipse((60,60,940,940),fill=BLUE);d.rectangle((200,300,420,350),fill=WHITE);d.rectangle((285,215,335,435),fill=WHITE)
    d.rectangle((580,300,800,350),fill=WHITE);d.line((220,700,420,560),fill=WHITE,width=40);d.line((420,700,220,560),fill=WHITE,width=40) if False else None
    d.line((230,720,410,560),fill=YEL,width=36);d.line((410,720,230,560),fill=YEL,width=36);d.rectangle((580,610,800,650),fill=WHITE);d.ellipse((665,540,715,590),fill=WHITE);d.ellipse((665,680,715,730),fill=WHITE);return im
ICONS.update(ship=ship,pyramid=pyramid,butterfly=butterfly,bird=bird,cat=cat,compass=compass,gamepad=gamepad,gem=gem,cross=cross,moonbed=moonbed,clapper=clapper,mathsym=mathsym)
