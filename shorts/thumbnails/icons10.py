from icons import *
import icons
def liner():
    im,d=new()
    d.polygon([(40,610),(960,610),(900,740),(150,740)],fill=(30,36,48));d.rectangle((40,590,960,625),fill=RED)
    d.rectangle((120,500,880,590),fill=WHITE);d.rectangle((250,420,760,500),fill=(235,240,245))
    for x in range(160,860,50): d.ellipse((x,530,x+24,554),fill=(60,100,130))
    for x in (290,420,550,680):
        d.rectangle((x,250,x+70,420),fill=(235,170,70));d.rectangle((x,250,x+70,290),fill=(25,25,30))
        d.ellipse((x+8,180,x+62,230),fill=(210,220,230,150))
    d.rectangle((95,470,125,500),fill=WHITE);d.line((850,500,920,430),fill=(120,75,40),width=10)
    for i,x in enumerate(range(-20,1000,120)): d.pieslice((x,700,x+160,820),180,360,fill=BLUE)
    d.rectangle((0,760,1000,900),fill=BLUE)
    for x in range(40,1000,160): d.arc((x,780,x+120,830),180,360,fill=WHITE,width=8)
    return im
def helmet():
    im,d=new();G=(110,125,95)
    d.pieslice((140,200,860,820),180,360,fill=G)
    d.ellipse((60,520,940,680),fill=(90,104,78));d.rectangle((140,520,860,545),fill=G)
    d.pieslice((140,200,860,820),180,360,fill=G)
    d.ellipse((60,500,940,640),fill=(95,110,82))
    d.pieslice((300,230,620,420),200,300,fill=(150,165,135))
    d.line((250,640,300,820),fill=BR,width=18);d.line((750,640,700,820),fill=BR,width=18);d.line((300,820,700,820),fill=BR,width=18)
    d.ellipse((470,240,530,300),fill=(70,84,60))
    return im
def kepi():
    im,d=new();B=(40,80,150)
    d.polygon([(160,520),(840,520),(790,300),(220,230)],fill=B)
    d.ellipse((150,200,800,330),fill=(55,100,175))
    d.rectangle((160,500,840,600),fill=(30,62,120))
    d.pieslice((80,520,900,860),0,180,fill=(20,34,52))
    d.ellipse((400,360,520,480),fill=YEL);d.ellipse((430,390,490,450),fill=B)
    return im
def stovepipe():
    im,d=new();K=(30,30,38)
    d.rounded_rectangle((260,120,740,700),30,fill=K);d.ellipse((260,90,740,200),fill=(55,55,66))
    d.rectangle((260,560,740,660),fill=(150,40,50))
    d.ellipse((90,640,910,860),fill=K);d.ellipse((260,600,740,720),fill=K);d.rectangle((260,560,740,660),fill=(150,40,50))
    d.rounded_rectangle((300,160,350,540),20,fill=(70,70,84))
    return im
def moonlander():
    im,d=new()
    d.ellipse((60,520,940,1250),fill=(190,196,206))
    for x,y,r in ((220,640,60),(520,600,40),(760,700,70),(380,780,50),(640,860,45)):
        d.ellipse((x-r,y-r*0.6,x+r,y+r*0.6),fill=(150,158,170))
    d.polygon([(350,200),(650,200),(720,330),(650,440),(350,440),(280,330)],fill=YEL)
    d.rectangle((420,260,580,360),fill=(190,200,215));d.ellipse((440,275,560,345),fill=(120,170,220))
    d.rectangle((330,440,670,480),fill=(220,160,40))
    for a,b in (((350,480),(230,580)),((650,480),(770,580)),((430,480),(380,590)),((570,480),(620,590))): d.line((a,b),fill=GRAY,width=18)
    for x in (230,380,620,770): d.rectangle((x-45,575,x+45,600),fill=GRAY)
    d.line((500,200,500,120),fill=WHITE,width=8);d.ellipse((470,90,530,140),fill=WHITE)
    return im
def mic():
    im,d=new()
    d.rounded_rectangle((340,80,660,520),150,fill=(160,172,186))
    for y in range(150,500,50): d.line((350,y,650,y),fill=(110,122,138),width=8)
    for x in range(380,640,50): d.line((x,100,x,500),fill=(110,122,138),width=6)
    d.rounded_rectangle((330,330,670,390),20,fill=(190,200,215))
    d.arc((250,300,750,720),0,180,fill=(190,200,215),width=40)
    d.rectangle((480,700,520,830),fill=(190,200,215));d.rounded_rectangle((330,830,670,890),25,fill=(190,200,215))
    return im
icons.ICONS.update(liner=liner,helmet=helmet,kepi=kepi,stovepipe=stovepipe,moonlander=moonlander,mic=mic)
ICONS=icons.ICONS
