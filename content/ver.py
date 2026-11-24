import sys,urllib.request,re,json,concurrent.futures as cf
sys.path.insert(0,'.')
from data import T,W
items=[(v,i,q) for v,_,_,qs in T for i,q in enumerate(qs)]
cache={}
def get(p):
    if p in cache: return cache[p]
    try:
        r=urllib.request.Request(W+p,headers={'User-Agent':'Mozilla/5.0 quiz-verify'})
        t=urllib.request.urlopen(r,timeout=20).read().decode('utf8','ignore')
        t=re.sub(r'<[^>]+>',' ',t); cache[p]=t
    except Exception as e: cache[p]=None
    return cache[p]
pages={q[3] for _,_,q in items}
with cf.ThreadPoolExecutor(8) as ex: list(ex.map(get,pages))
bad=[]
for v,i,q in items:
    t=get(q[3])
    if t is None: bad.append((v,i+1,'FETCHFAIL',q[3]))
    elif q[4].lower() not in t.lower(): bad.append((v,i+1,'NOSTR',q[4],q[3]))
print(len(items),len(bad));[print(b) for b in bad]
