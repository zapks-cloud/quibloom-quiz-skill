import sys,json,re,urllib.request
sys.path.insert(0,'.')
from data import T
v=int(sys.argv[1])
d=[t for t in T if t[0]==v][0]
cache={}
for i,(q,c,wr,page,kw) in enumerate(d[3]):
    p='https://en.wikipedia.org/wiki/'+page
    if p not in cache:
        t=urllib.request.urlopen(urllib.request.Request(p,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode('utf8','ignore')
        t=re.sub(r'(?s)<(script|style).*?</\1>','',t);t=re.sub(r'<[^>]+>',' ',t);t=re.sub(r'\s+',' ',t);t=re.sub(r'\{[^}]{0,400}\}','',t);cache[p]=t
    t=cache[p]
    print('\n#%d %s -> %s | wrong: %s'%(i+1,q,c,wr))
    for k in (c.replace('The ','').replace('the ',''),kw):
        ms=[m for m in re.finditer(re.escape(k),t,re.I) if 'Toggle' not in t[m.start()-40:m.start()+40]]
        if ms:
            m=ms[0] if k==kw else ms[min(1,len(ms)-1)]
            print('  [%s] ..%s'%(k,t[max(0,m.start()-110):m.start()+160]));break
