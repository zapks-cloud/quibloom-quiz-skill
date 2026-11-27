import sys,os
os.environ['QUIBLOOM_LOGO']='/tmp/t/r/quibloom-logo.png'
sys.path.insert(0,'/tmp/t/r'); sys.argv=['x']
import r
from r import *
from PIL import Image,ImageDraw,ImageFilter
TW,TH=1280,720
def wrapl(s,f,mw):
    ws=s.split();ls=[];c=''
    for w in ws:
        t=(c+' '+w).strip()
        if f.getlength(t)<=mw: c=t
        else: ls.append(c);c=w
    ls.append(c);return ls
def make(topic,cat,out,icon='temple',bt0='15 QUESTIONS  |  SCORE 15/15?'):
    im=Image.new('RGB',(TW,TH),NAVY);d=ImageDraw.Draw(im,'RGBA')
    d.ellipse((-220,-260,420,380),outline=(38,86,108,120),width=36)
    d.ellipse((880,420,1500,1040),outline=(38,86,108,120),width=36)
    for (x,y,rad) in [(560,90,10),(700,640,12),(60,640,9),(1210,60,10),(520,520,8)]:
        d.ellipse((x-rad,y-rad,x+rad,y+rad),fill=(255,208,48,70))
    # logo + brand
    lg=logo.copy(); lg=lg.resize((84,84),Image.LANCZOS); im.paste(lg,(60,48),lg)
    d.text((160,62),'Quibloom',font=F(50),fill=WHITE)
    # category pill
    pf=F(34); pw=int(pf.getlength(cat))+56
    d.rounded_rectangle((60,176,60+pw,236),16,fill=(25,66,88))
    d.text((60+28,182),cat,font=pf,fill=CYAN)
    # title
    t=topic.upper(); sz=132
    while True:
        f=F(sz); ls=wrapl(t,f,670)
        if (len(ls)+1)*sz*1.06<=318 and all(f.getlength(l)<=670 for l in ls): break
        sz-=4
    y=252
    for l in ls:
        d.text((60,y),l,font=f,fill=WHITE); y+=int(sz*1.06)
    d.text((60,y),'QUIZ',font=f,fill=YEL)
    # bottom badge
    bf=F(40); bt=bt0
    bw=int(bf.getlength(bt))+56
    d.rounded_rectangle((60,TH-120,60+bw,TH-52),20,fill=YEL)
    d.text((60+28,TH-112),bt,font=bf,fill=NAVY)
    import icons
    ic=icons.ICONS[icon]().resize((460,460),Image.LANCZOS)
    d.ellipse((780,130,1240,590),fill=(25,66,88,255),outline=(38,86,108,255),width=6)
    im.paste(ic,(780,130),ic)
    d.rounded_rectangle((60,TH-120,60+bw,TH-52),20,fill=YEL) if False else None
    im.save(out,'JPEG',quality=92)
if __name__=='__main__':
    make(sys.argv[1] if len(sys.argv)>1 else 'Ancient Greece','HISTORY','/tmp/th/t.jpg')
