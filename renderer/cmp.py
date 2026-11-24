import sys
V=sys.argv[1]
sys.argv=['x','video%s.json'%V,'c%s'%V,'./out/x.mp4','none']
import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'main2.py')).read().split('scenes=[];audio=[]')[0])
for n in range(1,16):
    c='v%s_q%02d'%(V,n)
    st,en=opt_times(D['questions'][n-1],c)
    a=segs(c,0.12);b=segs(c,0.2)
    print(n,[round(x,2) for x in st],len(a),len(b))
