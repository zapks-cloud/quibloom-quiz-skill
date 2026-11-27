from icons import *
def briefcase():
    im,d=new();d.rounded_rectangle((340,200,660,340),50,outline=BR,width=44)
    d.rounded_rectangle((100,300,900,800),70,fill=BR);d.rectangle((100,500,900,540),fill=(120,75,40));d.rounded_rectangle((440,470,560,590),20,fill=YEL);return im
def book():
    im,d=new();d.polygon([(500,240),(120,200),(120,780),(500,820)],fill=BLUE);d.polygon([(500,240),(880,200),(880,780),(500,820)],fill=(90,165,250))
    for i in range(4):
        y=330+i*90;d.line((190,y,440,y+14),fill=WHITE,width=22);d.line((560,y+14,810,y),fill=WHITE,width=22)
    d.polygon([(500,240),(500,820),(470,830),(470,250)],fill=NAVY);return im
def note():
    im,d=new();d.ellipse((140,640,420,860),fill=PINK);d.ellipse((560,560,840,780),fill=PINK)
    d.rectangle((380,200,430,760),fill=PINK);d.rectangle((790,120,840,680),fill=PINK);d.polygon([(380,200),(840,120),(840,260),(380,340)],fill=PINK);return im
def trophy():
    im,d=new();d.pieslice((250,100,750,700),0,180,fill=YEL);d.rectangle((250,380,750,400),fill=YEL)
    d.arc((90,160,330,420),90,270,fill=YEL,width=40);d.arc((670,160,910,420),270,90,fill=YEL,width=40)
    d.rectangle((460,560,540,740),fill=YEL);d.rounded_rectangle((300,740,700,840),30,fill=ORG)
    d.polygon([(500,230),(530,310),(610,310),(545,360),(570,440),(500,390),(430,440),(455,360),(390,310),(470,310)],fill=WHITE);return im
def palette():
    im,d=new();d.ellipse((80,160,920,840),fill=SAND);d.ellipse((560,560,760,760),fill=CARD)
    for (x,y,c) in ((260,360,RED),(430,260,YEL),(620,290,GREEN),(750,430,BLUE)): d.ellipse((x-60,y-60,x+60,y+60),fill=c)
    return im
def tree():
    im,d=new();d.rectangle((450,560,550,900),fill=BR)
    for (x,y,r) in ((500,300,230),(320,460,180),(680,460,180)): d.ellipse((x-r,y-r,x+r,y+r),fill=GREEN)
    d.ellipse((400,260,500,360),fill=(140,215,100));return im
def atom():
    im,d=new()
    for a in (0,60,120):
        t=Image.new('RGBA',(S,S),(0,0,0,0));td=ImageDraw.Draw(t);td.ellipse((60,300,940,700),outline=CYAN,width=26);im.alpha_composite(t.rotate(a,center=(500,500)))
    d=ImageDraw.Draw(im);d.ellipse((410,410,590,590),fill=YEL);return im
def camera():
    im,d=new();d.rounded_rectangle((90,260,910,800),90,fill=GRAY);d.rounded_rectangle((330,170,670,290),30,fill=GRAY);d.rectangle((90,380,910,430),fill=NAVY)
    d.ellipse((290,320,710,740),fill=NAVY);d.ellipse((350,380,650,680),fill=BLUE);d.ellipse((420,450,520,550),fill=(190,225,255));d.ellipse((780,300,860,360),fill=YEL);return im
def clock():
    im,d=new();d.ellipse((90,90,910,910),fill=WHITE,outline=CYAN,width=50)
    for i in range(12):
        a=i*math.pi/6;d.line((500+330*math.sin(a),500-330*math.cos(a),500+390*math.sin(a),500-390*math.cos(a)),fill=NAVY,width=18)
    d.line((500,500,500,260),fill=NAVY,width=34);d.line((500,500,680,580),fill=RED,width=26);d.ellipse((470,470,530,530),fill=NAVY);return im
def plane():
    im,d=new();d.polygon([(100,520),(260,470),(660,470),(900,380),(920,420),(780,520),(920,620),(900,660),(660,570),(260,570)],fill=WHITE)
    d.polygon([(380,470),(250,150),(330,150),(560,470)],fill=GRAY);d.polygon([(380,570),(250,890),(330,890),(560,570)],fill=GRAY)
    d.polygon([(100,520),(60,380),(140,380),(250,490)],fill=CYAN);return im
def train():
    im,d=new();d.rounded_rectangle((200,100,800,720),90,fill=RED);d.rounded_rectangle((260,190,740,430),40,fill=(170,215,250));d.line((500,190,500,430),fill=RED,width=20)
    d.ellipse((290,540,390,640),fill=YEL);d.ellipse((610,540,710,640),fill=YEL);d.line((250,880,400,720),fill=GRAY,width=30);d.line((750,880,600,720),fill=GRAY,width=30);d.line((150,820,850,820),fill=GRAY,width=30);return im
def pawn():
    im,d=new();d.ellipse((380,100,620,340),fill=WHITE);d.polygon([(420,320),(580,320),(640,700),(360,700)],fill=WHITE);d.ellipse((330,300,670,380),fill=WHITE)
    d.rounded_rectangle((260,690,740,800),40,fill=WHITE);d.rounded_rectangle((200,800,800,880),30,fill=GRAY);return im
def magnet():
    im,d=new();d.arc((160,130,840,810),180,360,fill=RED,width=150);d.rectangle((160,470,310,720),fill=RED);d.rectangle((690,470,840,720),fill=RED)
    d.rectangle((160,640,310,740),fill=WHITE);d.rectangle((690,640,840,740),fill=WHITE)
    for x in (230,770):
        d.line((x-30,860,x+30,800),fill=YEL,width=14);d.line((x+30,860,x-30,800),fill=YEL,width=14)
    return im
def coin():
    im,d=new();d.ellipse((120,120,880,880),fill=YEL,outline=ORG,width=50);d.ellipse((230,230,770,770),outline=ORG,width=24)
    d.line((500,330,500,670),fill=ORG,width=40);d.arc((380,330,620,500),90,270,fill=ORG,width=40);d.arc((380,500,620,670),270,90,fill=ORG,width=40);return im
ICONS.update(briefcase=briefcase,book=book,note=note,trophy=trophy,palette=palette,tree=tree,atom=atom,camera=camera,clock=clock,plane=plane,train=train,pawn=pawn,magnet=magnet,coin=coin)
