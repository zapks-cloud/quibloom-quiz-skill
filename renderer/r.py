import math, sys, json, random, os
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1080,1920,30
NAVY=(16,46,68); CARD=(24,61,82); CARDB=(38,86,108); CYAN=(38,190,217); YEL=(255,208,48)
WHITE=(255,255,255); GREEN=(110,190,70); GREENBG=(38,87,44); GREENL=(175,240,150); DIM=(120,150,170)
_FD_CAND=['/usr/share/fonts/truetype/noto/NotoSans-%s.ttf','/usr/share/fonts/noto/NotoSans-%s.ttf',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','NotoSans-%s.ttf')]
def _fp(w):
    for c in _FD_CAND:
        p=c%w
        if os.path.exists(p): return p
    return _FD_CAND[0]%w
def F(sz,w='Bold'): return ImageFont.truetype(_fp(w),sz)
SS=3
def spr(w,h,fn):
    im=Image.new('RGBA',(w*SS,h*SS),(0,0,0,0)); d=ImageDraw.Draw(im); fn(d,SS)
    return im.resize((w,h),Image.LANCZOS)
def text(s,sz,fill,w='Bold'):
    f=F(sz,w); l,t,r,b=f.getbbox(s); 
    im=Image.new('RGBA',(r+8,int(sz*1.5)),(0,0,0,0)); ImageDraw.Draw(im).text((2,0),s,font=f,fill=fill+(255,)); 
    bb=im.getbbox(); return im.crop((0,bb[1]-2 if bb else 0,im.width,(bb[3]+2) if bb else im.height)) if False else im
def clamp(x): return 0 if x<0 else 1 if x>1 else x
def pr(t,t0,d): return clamp((t-t0)/d)
def eo(x): return 1-(1-x)**3
def eb(x):
    c1=1.70158;c3=c1+1; return 1+c3*(x-1)**3+c1*(x-1)**2
def put(fr,s,x,y,a=1.0,sc=1.0,center=False):
    if a<=0.01 or sc<=0.01: return
    if sc!=1.0: s=s.resize((max(1,int(s.width*sc)),max(1,int(s.height*sc))),Image.BILINEAR)
    if a<1.0:
        al=s.getchannel('A').point(lambda v:int(v*a)); s=s.copy(); s.putalpha(al)
    if center: x-=s.width//2; y-=s.height//2
    fr.paste(s,(int(x),int(y)),s)
def rr(w,h,r,fill,border=None,bw=3):
    def fn(d,S):
        if border: d.rounded_rectangle((0,0,w*S-1,h*S-1),r*S,fill=border); d.rounded_rectangle((bw*S,bw*S,w*S-1-bw*S,h*S-1-bw*S),(r-bw)*S,fill=fill)
        else: d.rounded_rectangle((0,0,w*S-1,h*S-1),r*S,fill=fill)
    return spr(w,h,fn)
def circ(r,fill):
    return spr(2*r,2*r,lambda d,S:d.ellipse((0,0,2*r*S-1,2*r*S-1),fill=fill))
def ring(R,wd,col,a0,a1):
    n=2*R+4
    def fn(d,S): d.arc((2*S,2*S,(n-2)*S,(n-2)*S),a0,a1,fill=col,width=wd*S)
    return spr(n,n,fn)
import os as _os
_LOGO=_os.environ.get('QUIBLOOM_LOGO') or _os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'..','assets','quibloom-logo.png')
logo=Image.open(_LOGO).convert('RGBA')
# make navy bg of logo transparent
lp=logo.load()
def logo_t(sz):
    im=logo.resize((sz,sz),Image.LANCZOS); px=im.load()
    for y in range(sz):
        for x in range(sz):
            r,g,b,a=px[x,y]; d=abs(r-16)+abs(g-46)+abs(b-68)
            px[x,y]=(r,g,b,int(255*clamp(d/60)))
    return im
L_BIG=logo_t(360); L_SM=logo_t(96)
# static sprites
RING1=ring(330,56,(23,61,83),0,250); RING2=ring(290,52,(23,61,83),40,300)
PARTS=[circ(r,c) for r,c in [(8,(38,190,217,70)),(12,(255,208,48,60)),(16,(38,190,217,45)),(6,(255,255,255,50))]]
random.seed(4)
PART=[(random.uniform(0,W),random.uniform(0,H),random.choice(range(4)),random.uniform(18,45),random.uniform(0,6.28)) for _ in range(18)]
def bg(t):
    fr=Image.new('RGB',(W,H),NAVY)
    a1=RING1.rotate(-(t*7)%360,resample=Image.BICUBIC); put(fr,a1,70,330,1,1+0.03*math.sin(t*0.9),True)
    a2=RING2.rotate((t*-9+90)%360,resample=Image.BICUBIC); put(fr,a2,1010,1640,1,1+0.03*math.sin(t*0.8+1),True)
    for x,y,k,v,ph in PART:
        yy=(y-t*v)%(H+60)-30; xx=x+30*math.sin(t*0.7+ph)
        put(fr,PARTS[k],xx,yy,1,1,True)
    return fr
# header
WM=text('Quibloom',46,WHITE)
def header(fr,t,idx,tot,a=1.0):
    pass
    return _header(fr,t,idx,tot,a)
def _header(fr,t,idx,tot,a=1.0):
    k=eo(pr(t,0,0.5)); dy=(1-k)*-40
    wob=math.sin(t*2.2)*4
    put(fr,L_SM.rotate(wob,resample=Image.BICUBIC),44+48,118+dy+48-8,a*k,1+0.03*math.sin(t*3),True)
    put(fr,WM,160,120+dy,a*k)
    c=text('%02d / %02d'%(idx,tot),36,CYAN); put(fr,c,W-64-c.width,128+dy,a*k)
PILL=rr(240,60,16,(25,66,88))
CHOOSE=text('CHOOSE YOUR ANSWER',30,(170,195,210),'Bold'); CORR=text('CORRECT ANSWER',30,GREEN)
BAR_BG=rr(952,10,5,(30,70,95)); 
def bar(w): return rr(max(10,int(952*w)),10,5,YEL) 
CARDS={'n':rr(952,140,24,CARD,CARDB),'h':rr(952,140,24,(30,80,104),CYAN),'g':rr(952,140,24,GREENBG,GREEN)}
BADGE={'y':rr(86,86,16,YEL),'g':rr(86,86,16,GREEN)}
def badge_txt(l,col): return text(l,50,col)
CHK_CACHE={}
def check(p):
    def fn(d,S):
        pts=[(14,40),(36,62),(78,16)]
        # draw progressively
        L1=((pts[1][0]-pts[0][0])**2+(pts[1][1]-pts[0][1])**2)**.5; L2=((pts[2][0]-pts[1][0])**2+(pts[2][1]-pts[1][1])**2)**.5
        tot=L1+L2; cur=p*tot
        def pt(a,b,f): return (a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f)
        if cur<=L1: e=pt(pts[0],pts[1],cur/L1); seg=[pts[0],e]
        else: e=pt(pts[1],pts[2],(cur-L1)/L2); seg=[pts[0],pts[1],e]
        d.line([(x*S,y*S) for x,y in seg],fill=GREENL,width=10*S,joint='curve')
        for x,y in seg: d.ellipse(((x-5)*S,(y-5)*S,(x+5)*S,(y+5)*S),fill=GREENL)
    return spr(96,80,fn)
def wrap(s,font,maxw):
    out=[];cur=''
    for w in s.split():
        c=(cur+' '+w).strip()
        if font.getlength(c)<=maxw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
QF=F(88)
NQ=[3]
HT=dict(w=[0.24,1.35,2.84,4.72])
class Q: pass
def build_q(cat,q,opts,correct):
    o=Q(); o.cat=cat; o.correct=correct
    o.pill=rr(int(F(28).getlength(cat))+56,60,16,(25,66,88)); o.cattxt=text(cat,28,CYAN)
    qs=88
    while len(wrap(q,F(qs),900))>3: qs-=4
    o.lines=[text(l,qs,WHITE) for l in wrap(q,F(qs),900)]
    o.opts=[]
    for i,s in enumerate(opts):
        fs=56
        while F(fs).getlength(s)>760: fs-=2
        o.opts.append((text(s,fs,WHITE),text(s,fs,DIM),badge_txt('ABCD'[i],NAVY),badge_txt('ABCD'[i],NAVY)))
    return o
CD=[circ(96,(24,61,82))]
CDTXT=[text(str(n),110,WHITE) for n in range(6)]
def cd_ring(frac):
    n=216
    def fn(d,S):
        d.ellipse((6*S,6*S,(n-6)*S,(n-6)*S),outline=(30,70,95),width=12*S)
        if frac>0: d.arc((6*S,6*S,(n-6)*S,(n-6)*S),-90,-90+360*frac,fill=YEL,width=12*S)
    return spr(n,n,fn)
def draw_q(fr,t,Qo,idx,T):
    # T: dict with opt_t[4], opt_e[4], cd0, rev, end
    header(fr,t,idx,NQ[0])
    k=eo(pr(t,0.05,0.5)); put(fr,Qo.pill,64,282+(1-k)*-30,k)
    put(fr,Qo.cattxt,64+28,282+8+(1-k)*-30,k)
    y=400
    for i,l in enumerate(Qo.lines):
        k=eo(pr(t,0.2+0.14*i,0.55)); put(fr,l,64,y+(1-k)*60,k); y+=int(88*1.34)
    rev=t>=T['rev']
    gk=eo(pr(t,T['rev'],0.4)) if rev else 0
    # label + bar
    ly=max(y+20,820)
    ly=830
    kk=eo(pr(t,0.7,0.5))
    put(fr,CHOOSE,64,ly,kk*(1-gk)); put(fr,CORR,64,ly,gk)
    put(fr,BAR_BG,64,ly+54,kk)
    if t<T['cd0']: w=1.0*kk
    elif t<T['rev']: w=1-pr(t,T['cd0'],T['rev']-T['cd0'])
    else: w=1.0
    if rev:
        put(fr,rr(952,10,5,GREEN),64,ly+54,gk)
    else:
        put(fr,bar(w),64,ly+54,kk)
    # cards
    base=ly+100
    for i in range(4):
        ts=T['opt_t'][i]-0.25
        k=pr(t,ts,0.55); e=eb(k)
        x=64+(1-e)*420; a=eo(clamp(k*1.6))
        yy=base+i*176
        sc=1.0
        hi=0
        if T['opt_t'][i]<=t<=T['opt_e'][i]+0.35 and not rev:
            hi=math.sin(pr(t,T['opt_t'][i],T['opt_e'][i]-T['opt_t'][i]+0.35)*math.pi); sc=1+0.012*hi
        cor=(i==Qo.correct)
        wob=0
        if rev and cor:
            p=pr(t,T['rev'],0.6); sc=1+0.045*math.sin(p*math.pi)
        if rev and not cor: sc=1-0.015*eo(pr(t,T['rev'],0.4))
        cx=x+476; cy=yy+70
        put(fr,CARDS['n'],cx,cy,a,sc,True)
        if hi>0: put(fr,CARDS['h'],cx,cy,a*hi,sc,True)
        if rev and cor: put(fr,CARDS['g'],cx,cy,gk,sc,True)
        txt,dim,bt,_=Qo.opts[i]
        bx=x+25+43; by=yy+70
        put(fr,BADGE['y'],bx*1+0,by,a,sc,True)
        if rev and cor: put(fr,BADGE['g'],bx,by,gk,sc,True)
        put(fr,bt,bx,by-4,a,sc,True)
        tx=x+151; ty=yy+34
        if rev and not cor:
            put(fr,txt,tx,ty,a*(1-gk)); put(fr,dim,tx,ty,a*gk)
        else: put(fr,txt,tx,ty,a)
        if rev and cor:
            p=eo(pr(t,T['rev']+0.15,0.45))
            put(fr,check(p),x+952-130,yy+30)
    # countdown / reveal icon
    cy=1745
    if T['cd0']-0.3<=t<T['rev']:
        a=eo(pr(t,T['cd0']-0.3,0.3))
        el=t-T['cd0']; 
        if el<0: el=0
        n=5-int(el); n=max(1,min(5,n)); fr_=1-clamp(el/5)
        sub=el-int(el)
        sc=1+0.4*(1-eo(clamp(sub/0.28)))
        put(fr,cd_ring(fr_),W//2,cy,a,1,True)
        put(fr,CDTXT[n],W//2,cy-6,a,sc,True)
    elif rev:
        p=eb(pr(t,T['rev'],0.5))
        put(fr,circ(96,GREENBG),W//2,cy,gk,p,True)
        put(fr,check(eo(pr(t,T['rev']+0.1,0.45))).resize((84,70)),W//2,cy,gk,1,True)
        # sparkles
        el=t-T['rev']
        if 0<el<1.1:
            d=ImageDraw.Draw(fr)
            rnd=random.Random(9)
            for j in range(22):
                ang=rnd.uniform(0,6.283); sp=rnd.uniform(200,520); col=rnd.choice([YEL,CYAN,GREEN,WHITE])
                r_=8*(1-el/1.1)+2
                cx0=W//2; cy0=base+Qo.correct*176+70
                px=cx0+math.cos(ang)*sp*eo(el/1.1)*0.9; py=cy0+math.sin(ang)*sp*eo(el/1.1)*0.5+ 80*el*el
                d.ellipse((px-r_,py-r_,px+r_,py+r_),fill=col)
# intro / cta
def pop(t,t0,d=0.5): return eb(pr(t,t0,d))
def draw_intro(fr,t,H0):
    k=pop(t,0.15,0.7)
    put(fr,L_BIG.rotate((1-k)*-120,resample=Image.BICUBIC),W//2,620,clamp(k*2),k*(1+0.025*math.sin(t*3)),True)
    wm=text('Quibloom',112,WHITE); k2=eo(pr(t,0.55,0.5)); put(fr,wm,W//2-wm.width//2+(1-k2)*-120,800,k2)
    t1=H0+HT['w'][0]; a=pop(t,t1,0.55)
    s1=text('%d QUESTIONS'%NQ[0],124 if NQ[0]<10 else 112,WHITE); put(fr,s1,W//2,1110,clamp(a*2),a,True)
    w=int(s1.width*eo(pr(t,t1+0.3,0.5))); 
    if w>4: put(fr,rr(w,12,6,YEL),W//2-s1.width//2,1185)
    t2=H0+HT['w'][1]; a=pop(t,t2,0.5); s2=text('NO SECOND CHANCES',66,CYAN)
    put(fr,s2,W//2-s2.width//2+(1-eo(pr(t,t2,0.45)))*300,1235,eo(pr(t,t2,0.3)))
    t3=H0+HT['w'][2]
    s3=text('CAN YOU SCORE %d / %d ?'%(NQ[0],NQ[0]),60,WHITE); a=pop(t,t3,0.5); put(fr,s3,W//2,1390,clamp(a*2),a,True)
    for i in range(3):
        ti=t3+0.3+0.45*i; kk=pop(t,ti,0.5)
        c=circ(48,YEL if t>ti+0.1 else CARD); put(fr,c,W//2-150+i*150,1520,clamp(kk*2),kk*(1+0.08*math.sin((t-ti)*8)*(1 if t-ti<1 else 0)),True)
        if t>ti+0.1: 
            put(fr,text('?',64,NAVY),W//2-150+i*150,1516,clamp(kk*2),kk,True)
    t4=H0+HT['w'][3]; kk=pop(t,t4,0.5)
    s4=text("LET'S FIND OUT",58,NAVY); pw=s4.width+110
    put(fr,rr(pw,110,55,YEL),W//2,1720,clamp(kk*2),kk*(1+0.03*math.sin(t*6)),True)
    put(fr,s4,W//2,1717,clamp(kk*2),kk*(1+0.03*math.sin(t*6)),True)
def thumb(sz,col):
    def fn(d,S):
        k=sz*S/100
        P=lambda pts:[(x*k,y*k) for x,y in pts]
        d.rounded_rectangle((8*k,46*k,28*k,92*k),4*k,fill=col)
        d.polygon(P([(34,48),(50,10),(60,10),(66,20),(60,42),(88,42),(96,52),(92,62),(95,70),(89,80),(90,88),(82,93),(34,93)]),fill=col)
    return spr(sz,sz,fn)
def sharei(sz,col):
    def fn(d,S):
        k=sz*S/100
        pts=[(22,50),(74,20),(74,80)]
        d.line([(pts[0][0]*k,pts[0][1]*k),(pts[1][0]*k,pts[1][1]*k)],fill=col,width=int(6*k))
        d.line([(pts[0][0]*k,pts[0][1]*k),(pts[2][0]*k,pts[2][1]*k)],fill=col,width=int(6*k))
        for x,y in pts: d.ellipse(((x-13)*k,(y-13)*k,(x+13)*k,(y+13)*k),fill=col)
    return spr(sz,sz,fn)
def bell(sz,col):
    def fn(d,S):
        k=sz*S/100
        d.ellipse((30*k,12*k,70*k,52*k),fill=col)
        d.polygon([(30*k,32*k),(70*k,32*k),(84*k,72*k),(16*k,72*k)],fill=col)
        d.rounded_rectangle((10*k,68*k,90*k,78*k),5*k,fill=col)
        d.ellipse((40*k,76*k,60*k,92*k),fill=col)
        d.ellipse((44*k,4*k,56*k,16*k),fill=col)
    return spr(sz,sz,fn)
def draw_cta(fr,t,C0):
    k=pop(t,0.1,0.6); put(fr,L_BIG.resize((200,200),Image.LANCZOS),W//2,300,clamp(k*2),k*(1+0.03*math.sin(t*3)),True)
    wm=text('Quibloom',70,WHITE); put(fr,wm,W//2-wm.width//2,430,eo(pr(t,0.3,0.5)))
    t0=C0+0.24; a=pop(t,t0,0.55); s=text('WHAT IS YOUR SCORE?',72,WHITE)
    put(fr,s,W//2,640,clamp(a*2),a,True)
    sc=text('?  /  %d'%NQ[0],150,YEL); put(fr,sc,W//2,820,clamp(a*2),a*(1+0.04*math.sin(t*4)),True)
    items=[(C0+1.6,'LIKE',thumb(90,NAVY),1130,CYAN),(C0+2.55,'SHARE',sharei(90,NAVY),1130,CYAN)]
    for (ti,lab,ic,yy,col),xx in zip(items,[290,790]):
        kk=pop(t,ti,0.55); tt=text(lab,54,NAVY)
        bw=360
        # press bounce
        press=1-0.08*max(0,math.sin(clamp((t-ti-0.5)/0.35)*math.pi)) if t>ti+0.5 else 1
        put(fr,rr(bw,170,40,col),xx,yy,clamp(kk*2),kk*press,True)
        put(fr,ic,xx-100,yy-4,clamp(kk*2),kk*press,True)
        put(fr,tt,xx+40,yy-6,clamp(kk*2),kk*press,True)
        # ripple
        el=t-ti-0.5
        if 0<el<0.8:
            r=int(60+200*eo(el/0.8)); rg=ring(r,6,col,0,360); put(fr,rg,xx,yy,1-el/0.8,1,True)
    ts=C0+4.1; kk=pop(t,ts,0.6); done=t>C0+6.0
    lab='SUBSCRIBED' if done else 'SUBSCRIBE'
    col=GREEN if done else YEL
    tt=text(lab,64,NAVY); bw=tt.width+210
    pulse=1+0.04*math.sin(t*7) if not done else 1+0.06*max(0,math.sin(clamp((t-C0-6.0)/0.5)*math.pi))
    put(fr,rr(bw,170,85,col),W//2,1450,clamp(kk*2),kk*pulse,True)
    put(fr,bell(100,NAVY).rotate(18*math.sin(t*12)*(1 if (not done) else 0),resample=Image.BICUBIC),W//2-bw//2+95,1446,clamp(kk*2),kk*pulse,True)
    put(fr,tt,W//2+60,1440,clamp(kk*2),kk*pulse,True)
    if done:
        kk=pop(t,C0+6.0,0.5); n=text('See you in the next quiz!',50,CYAN); put(fr,n,W//2,1680,clamp(kk*2),kk,True)
