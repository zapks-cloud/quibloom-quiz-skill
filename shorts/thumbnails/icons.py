from PIL import Image,ImageDraw
import math
NAVY=(16,46,68);CARD=(24,61,82);CARDB=(38,86,108);CYAN=(38,190,217);YEL=(255,208,48);WHITE=(255,255,255)
GREEN=(110,190,70);RED=(236,92,84);ORG=(250,150,60);SAND=(240,226,196);BLUE=(70,140,230);PINK=(240,120,160);GRAY=(150,175,195);BR=(150,100,60);PURP=(150,110,220)
S=1000  # canvas; drawn at 1000 then downscaled
def new(): 
    im=Image.new('RGBA',(S,S),(0,0,0,0));return im,ImageDraw.Draw(im)
def temple():
    im,d=new()
    d.polygon([(70,330),(500,70),(930,330)],fill=SAND);d.polygon([(150,330),(500,120),(850,330)],fill=(214,196,160))
    d.rectangle((90,340,910,400),fill=SAND)
    for i in range(6):
        x=130+i*148;d.rectangle((x,400,x+90,780),fill=WHITE);d.rectangle((x+22,400,x+30,780),fill=(215,225,235));d.rectangle((x-14,400,x+104,430),fill=SAND);d.rectangle((x-14,760,x+104,790),fill=SAND)
    d.rectangle((50,790,950,850),fill=SAND);d.rectangle((20,850,980,920),fill=(214,196,160))
    d.ellipse((450,190,550,290),fill=YEL)
    return im
def bridge():
    im,d=new()
    d.rectangle((0,560,1000,610),fill=GRAY)
    d.rectangle((0,610,1000,640),fill=(110,140,160))
    for x in (230,770):
        d.rectangle((x-35,120,x+35,800),fill=ORG);d.rectangle((x-55,110,x+55,160),fill=RED)
    # cables
    import math
    for (a,b) in ((230,770),):
        pts=[(x,120+ (x-500)**2/ (270**2)*(560-120)*0.0) for x in range(a,b)]
    def cat(x0,x1,xm,y0,ym,w):
        pts=[]
        for x in range(x0,x1+1,4):
            t=(x-xm)/((x1-x0)/2); pts.append((x,ym+(y0-ym)*t*t))
        d.line(pts,fill=WHITE,width=w)
    cat(230,770,500,120,430,14); cat(0,230,230,560,120,14) if False else None
    d.line([(0,540),(230,130)],fill=WHITE,width=14);d.line([(770,130),(1000,540)],fill=WHITE,width=14)
    for x in range(260,760,45):
        t=(x-500)/270; y=430+(120-430)*t*t
        d.line((x,y,x,560),fill=WHITE,width=7)
    for x in range(30,230,45):
        y=540-(x/230)*410;d.line((x,y,x,560),fill=WHITE,width=7)
    for x in range(790,1000,45):
        y=130+((x-770)/230)*410;d.line((x,y,x,560),fill=WHITE,width=7)
    # water
    d.rectangle((0,780,1000,1000),fill=BLUE)
    for i in range(4): d.arc((i*260-60,800,i*260+140,880),0,180,fill=WHITE,width=8)
    return im
def wave():
    im,d=new()
    d.ellipse((150,60,850,760),fill=(255,226,120))
    d.rectangle((0,520,1000,1000),fill=BLUE)
    for i in range(5): d.ellipse((i*210-60,470,i*210+150,590),fill=BLUE)
    for i in range(5): d.arc((i*210-40,520,i*210+170,640),180,360,fill=WHITE,width=10)
    # fish
    d.ellipse((330,640,640,820),fill=ORG);d.polygon([(620,730),(760,640),(760,820)],fill=ORG);d.ellipse((380,700,420,740),fill=WHITE);d.ellipse((392,712,408,728),fill=NAVY)
    d.polygon([(470,645),(520,590),(570,650)],fill=RED)
    return im
def heart():
    im,d=new()
    d.ellipse((130,190,530,590),fill=RED);d.ellipse((470,190,870,590),fill=RED);d.polygon([(150,500),(850,500),(500,900)],fill=RED)
    d.ellipse((230,270,330,370),fill=(250,160,150))
    pts=[(80,560),(300,560),(380,430),(480,700),(580,380),(660,560),(920,560)]
    d.line(pts,fill=WHITE,width=26,joint='curve')
    return im
def globe():
    im,d=new()
    d.ellipse((100,100,900,900),fill=BLUE)
    d.polygon([(250,280),(420,230),(480,330),(400,430),(300,420),(230,360)],fill=GREEN)
    d.polygon([(520,500),(700,460),(760,600),(660,780),(560,700)],fill=GREEN)
    d.polygon([(560,230),(720,250),(780,350),(640,380)],fill=GREEN)
    for r in (200,):
        d.ellipse((500-r*1.0,100,500+r*1.0,900),outline=(255,255,255,150),width=8)
    d.line((100,500,900,500),fill=(255,255,255,150),width=8)
    d.ellipse((100,100,900,900),outline=WHITE,width=14)
    d.polygon([(500,40),(540,110),(460,110)],fill=RED);d.ellipse((470,100,530,160),fill=RED)
    return im
def flask():
    im,d=new()
    d.rectangle((400,100,600,400),fill=(200,225,240));d.rectangle((370,80,630,130),fill=WHITE)
    d.polygon([(400,380),(600,380),(880,860),(120,860)],fill=(200,225,240))
    d.polygon([(250,640),(750,640),(880,860),(120,860)],fill=GREEN)
    d.polygon([(400,380),(600,380),(600,400),(400,400)],fill=(200,225,240))
    for (x,y,r) in ((400,540,30),(540,470,24),(480,580,18)): d.ellipse((x-r,y-r,x+r,y+r),fill=WHITE)
    # atom sparkle
    d.ellipse((80,160,140,220),fill=YEL);d.ellipse((860,300,920,360),fill=CYAN)
    return im
def hourglass_scroll():
    im,d=new()
    # castle for history
    d.rectangle((150,420,850,880),fill=SAND)
    for x in (150,310,470,630,790): d.rectangle((x,340,x+60,420),fill=SAND)
    for x in (80,780): d.rectangle((x,250,x+140,880),fill=(214,196,160)); 
    for x in (60,160,260): pass
    for x in (80,160,780,860): d.rectangle((x,200,x+60,260),fill=(214,196,160))
    d.polygon([(70,250),(150,150),(230,250)],fill=RED);d.polygon([(770,250),(850,150),(930,250)],fill=RED)
    d.rectangle((400,620,600,880),fill=BR);d.ellipse((400,540,600,700),fill=BR)
    d.rectangle((250,480,290,560),fill=NAVY);d.rectangle((710,480,750,560),fill=NAVY)
    return im
def chip():
    im,d=new()
    d.rounded_rectangle((220,220,780,780),50,fill=(40,60,90),outline=CYAN,width=14)
    d.rounded_rectangle((340,340,660,660),30,fill=CYAN)
    for i in range(5):
        p=270+i*115
        for (a,b,c,e) in ((p,120,p+36,220),(p,780,p+36,880),(120,p,220,p+36),(780,p,880,p+36)): d.rectangle((a,b,c,e),fill=YEL)
    d.text((500,500),"AI",fill=NAVY,anchor='mm',font=__import__('PIL.ImageFont',fromlist=['x']).truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf',180))
    return im
def weather():
    im,d=new()
    d.ellipse((560,70,860,370),fill=YEL)
    for a in range(0,360,45):
        x=710+math.cos(math.radians(a))*210;y=220+math.sin(math.radians(a))*210;d.ellipse((x-16,y-16,x+16,y+16),fill=YEL)
    d.ellipse((130,330,430,630),fill=WHITE);d.ellipse((330,260,650,640),fill=WHITE);d.ellipse((500,380,820,660),fill=WHITE);d.rectangle((260,500,700,650),fill=WHITE)
    d.polygon([(470,620),(380,800),(470,790),(420,950),(600,740),(500,750),(560,620)],fill=YEL)
    return im
def food():
    im,d=new()
    d.pieslice((120,200,880,900),180,360,fill=ORG)
    for (x,y) in ((300,340),(420,290),(560,320),(680,360),(500,380)): d.ellipse((x-14,y-8,x+14,y+8),fill=SAND)
    d.rounded_rectangle((100,500,900,570),30,fill=GREEN)
    d.rounded_rectangle((130,570,870,680),40,fill=BR)
    d.rounded_rectangle((100,680,900,750),30,fill=YEL)
    d.pieslice((120,640,880,960),0,180,fill=ORG)
    return im
def paw():
    im,d=new()
    d.ellipse((290,480,710,880),fill=BR)
    for (x,y,r) in ((190,400,90),(380,250,100),(620,250,100),(810,400,90)):
        d.ellipse((x-r,y-r*1.25,x+r,y+r*1.25),fill=BR)
    return im
def planet():
    im,d=new()
    d.ellipse((260,260,740,740),fill=ORG);d.arc((260,260,740,740),200,330,fill=(220,110,50),width=40)
    d.ellipse((330,330,420,420),fill=(255,190,110))
    d.ellipse((60,400,940,600),outline=SAND,width=34)
    d.pieslice((260,260,740,740),0,180,fill=ORG) if False else None
    for (x,y,r) in ((120,150,16),(880,180,12),(820,820,18),(160,780,10),(500,80,12)): d.ellipse((x-r,y-r,x+r,y+r),fill=YEL)
    return im
ICONS=dict(temple=temple,bridge=bridge,wave=wave,heart=heart,globe=globe,flask=flask,castle=hourglass_scroll,chip=chip,weather=weather,food=food,paw=paw,planet=planet)
