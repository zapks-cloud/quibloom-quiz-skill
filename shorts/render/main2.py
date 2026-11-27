import sys,wave,subprocess,json,os
import numpy as np
from multiprocessing import Pool
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import r
from r import *
PROJ=sys.argv[1]; CLIPS=sys.argv[2]; OUT=sys.argv[3]; MODE=sys.argv[4] if len(sys.argv)>4 else 'render'
D=json.load(open(PROJ)); NQ[0]=len(D['questions']); HOOKTXT[0]=D['hook']; INTRO2[0]=D.get('intro_line','NO SECOND CHANCES')
CTAT=D.get('cta_times')
if CTAT: CT[:]=CTAT
def wavp(n): return os.path.join(CLIPS,n+'.wav')
def dur(n):
    w=wave.open(wavp(n));return w.getnframes()/w.getframerate()
def segs(n,gap=0.12):
    w=wave.open(wavp(n));sr=w.getframerate();x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)
    h=int(sr*0.02);e=np.array([np.sqrt((x[i:i+h]**2).mean()) for i in range(0,len(x)-h,h)])
    sp=e>max(e.max()*0.06,60);out=[];s=None
    for i,v in enumerate(sp):
        if v and s is None:s=i
        if not v and s is not None:out.append([s*.02,i*.02]);s=None
    if s is not None:out.append([s*.02,len(sp)*.02])
    m=[]
    for a in out:
        if m and a[0]-m[-1][1]<gap:m[-1][1]=a[1]
        else:m.append(a)
    return m
def opt_times(qd,clip):
    import itertools
    sg=segs(clip,0.12); end=sg[-1][1]
    for g_ in (0.12,0.2):
        sg8=segs(clip,g_)
        if len(sg8)<8: continue
        L=[sg8[-8],sg8[-6],sg8[-4],sg8[-2]]
        st=[a for a,b in L]
        if all(b-a<0.6 for a,b in L) and all(1.2<st[k+1]-st[k]<3.4 for k in range(3)):
            return st,[st[k+1]-0.15 for k in range(3)]+[sg8[-1][1]]
    ai=None
    for k in range(len(sg)-1):
        if sg[k][1]>=2.0 and sg[k+1][0]-sg[k][1]>=0.7: ai=k+1;break
    if ai is None: ai=len(sg)-8
    A=sg[ai][0]
    lens=[len(o) for o in qd['options']]
    cand=[s_[0] for s_ in sg[ai+1:] if s_[1]-s_[0]<0.55]
    best=None
    for c in itertools.combinations(cand,3):
        st=[A]+list(c)
        cost=0
        for k in range(3): cost+=(st[k+1]-st[k]-(1.7+0.04*lens[k]))**2
        cost+=(end-st[3]-(0.7+0.04*lens[3]))**2
        if best is None or cost<best[0]: best=(cost,st)
    st=best[1]
    ends=[st[k+1]-0.15 for k in range(3)]+[end]
    return st,ends
scenes=[];audio=[];sfx=[]
t0=0;H0=0.1
hs=segs('hook',0.2)
gaps=sorted(range(len(hs)-1),key=lambda i:-(hs[i+1][0]-hs[i][1]))[:2]; gaps=sorted(gaps)
cuts=[hs[0][0]]+[hs[g+1][0] for g in gaps]
if len(cuts)==3: HT['w']=[cuts[0],cuts[0]+ (cuts[1]-cuts[0])*0.5 if False else cuts[0]+0.0,cuts[1],cuts[2]]
# "Fifteen questions" at start; "no second chances" is mid first segment: estimate at 50% of first segment
fs=hs[0] if len(hs)>=1 else [0.24,2.5]
if len(cuts)==3:
    seg_a_end=hs[gaps[0]][1]; HT['w']=[cuts[0],cuts[0]+(seg_a_end-cuts[0])*0.45,cuts[1],cuts[2]]
if D.get('skip_intro'):
    pass
else:
    end=H0+dur('hook')+0.9
    scenes.append(dict(kind='intro',s=t0,e=t0+end,H0=H0)); audio.append(('hook',t0+H0))
    sfx.append(('whoosh',t0+0.15))
    HT['w']=[0.24,1.4,2.6,3.6]
    for off in HT['w'][:3]: sfx.append(('pop',t0+H0+off))
    t0+=end
for i,qd in enumerate(D['questions']):
    qa='%s_q%02d'%('v%02d'%D['video'],qd['n']); aa='%s_a%02d'%('v%02d'%D['video'],qd['n'])
    qdur=dur(qa);ad=dur(aa)
    ot,oe=opt_times(qd,qa)
    if 'option_start_times' in qd:  # manual override: 4 start times in seconds, relative to the question clip
        ot=[float(x) for x in qd['option_start_times']]
        oe=[float(x) for x in qd.get('option_end_times',[ot[k+1]-0.15 for k in range(3)]+[qdur])]
    lead=0.1 if (D.get('skip_intro') and i==0) else 0.4; cd0=lead+qdur+0.4; rev=cd0+5; a0=rev+0.25; e=a0+ad+2.4
    T=dict(opt_t=[lead+x for x in ot],opt_e=[lead+x for x in oe],cd0=cd0,rev=rev,shift=(1.3 if (D.get('skip_intro') and i==0) else 0))
    if D.get('fmt')==3:
        HK=2.0 if (i==0 and D.get('hook_text')) else 0.0
        lead=0.1+HK; cd0=lead+qdur+0.4; rev=cd0+5; a0=rev+0.25; e=a0+ad+2.4
        q0=HK if HK else 0.0
        T=dict(opt_t=[lead+x for x in ot],opt_e=[lead+x for x in oe],cd0=cd0,rev=rev,shift=-q0,bar0=lead,vis_t=[q0+1.5]*4)
        if HK: T.update(hook_end=HK,hook_text=D['hook_text'])
    scenes.append(dict(kind='q',s=t0,e=t0+e,Q=build_q(D['category'],qd['question'],qd['options'],qd['correct_index'],qd.get('reveal')),idx=qd['n'],T=T))
    audio.append((qa,t0+lead)); audio.append((aa,t0+a0))
    sfx.append(('whoosh',t0+0.1))
    for x in (T['vis_t'][:1] if D.get('fmt')==3 else T['opt_t']): sfx.append(('pop',t0+x-0.1))
    for k in range(5): sfx.append(('tick',t0+cd0+k))
    sfx.append(('ding',t0+rev))
    t0+=e
C0=0.5
e=C0+dur('cta')+1.7
scenes.append(dict(kind='cta',s=t0,e=t0+e,C0=C0)); audio.append(('cta',t0+C0)); sfx.append(('whoosh',t0+0.1))
for off in CT[:2]: sfx.append(('pop',t0+C0+off))
sfx.append(('ding',t0+C0+dur('cta')+0.1))
TOTAL=t0+e
SC_S=[s['s'] for s in scenes]
import bisect
def frame(i):
    t=i/FPS
    k=max(0,bisect.bisect_right(SC_S,t)-1); sc=scenes[k]
    lt=t-sc['s']; L=sc['e']-sc['s']
    base=bg(t); fr=base.copy()
    if sc['kind']=='intro': draw_intro(fr,lt,sc['H0'])
    elif sc['kind']=='q': draw_q(fr,lt,sc['Q'],sc['idx'],sc['T'])
    else: draw_cta(fr,lt,sc['C0'])
    a=1-pr(lt,L-0.4,0.4) if k<len(scenes)-1 else 1-pr(lt,L-0.5,0.5)
    if a<1: fr=Image.blend(base,fr,a)
    return fr.tobytes()
SR=48000
def mix(outwav):
    N=int((TOTAL+0.3)*SR); out=np.zeros(N)
    def load(n):
        w=wave.open(wavp(n));x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
        rr_=w.getframerate(); idx=np.arange(0,len(x)*SR/rr_)/(SR/rr_); return np.interp(idx,np.arange(len(x)),x)
    def add(x,t,g=1.0):
        i=int(t*SR); x=x*g; out[i:i+len(x)]+=x[:max(0,N-i)]
    for n,t in audio: add(load(n),t)
    rng=np.random.default_rng(1)
    def tone(f0,f1,d,env=8):
        t=np.arange(int(d*SR))/SR; f=f0+(f1-f0)*t/d; return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-env*t/d)
    def ding():
        t=np.arange(int(0.8*SR))/SR; return (np.sin(2*np.pi*880*t)+0.6*np.sin(2*np.pi*1318*t))*np.exp(-5*t)*0.4
    def whoosh():
        d=0.4;n=rng.normal(size=int(d*SR));y=np.convolve(n,np.ones(60)/60,'same');t=np.arange(len(y))/SR;return y*np.sin(np.pi*t/d)**2*0.6
    fx=dict(pop=lambda:tone(500,900,0.09,5)*0.5,tick=lambda:tone(1100,1100,0.05,6)*0.5,ding=ding,whoosh=whoosh)
    for n,t in sfx: add(fx[n](),t,0.28 if n!='ding' else 0.3)
    pk=np.abs(out).max(); out=out/max(1,pk/0.92)
    w=wave.open(outwav,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
if __name__=='__main__':
    print('total',TOTAL,'HT',HT)
    json.dump(dict(total=TOTAL,scenes=[(s['kind'],s['s'],s['e']) for s in scenes],opt=[(s['s'],s['T']) for s in scenes if s['kind']=='q']),open(OUT+'.tl.json','w'))
    if MODE=='mix':
        mix(OUT+'.wav'); print('mixed')
    elif MODE=='chunk':
        a,b=int(sys.argv[5]),min(int(sys.argv[6]),int(TOTAL*FPS))
        p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','%dx%d'%(W,H),'-r','30','-i','-','-c:v','libx264','-crf','15','-preset','medium','-pix_fmt','yuv420p','-g','30','-bf','2','%s.c%05d.mp4'%(OUT,a)],stdin=subprocess.PIPE)
        with Pool(2) as pool:
            for bb in pool.imap(frame,range(a,b),chunksize=8): p.stdin.write(bb)
        p.stdin.close();p.wait();print('chunk',a,b)
    elif MODE=='still':
        for tt in map(float,sys.argv[5:]):
            Image.frombytes('RGB',(W,H),frame(int(tt*FPS))).save(OUT+'.s_%05.1f.png'%tt)
    else:
        mix(OUT+'.wav')
        n=int(TOTAL*FPS)
        p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','%dx%d'%(W,H),'-r','30','-i','-','-i',OUT+'.wav','-c:v','libx264','-crf','15','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',OUT],stdin=subprocess.PIPE)
        with Pool(2) as pool:
            for b in pool.imap(frame,range(n),chunksize=8): p.stdin.write(b)
        p.stdin.close();p.wait();print('done')
