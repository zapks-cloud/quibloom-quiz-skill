import json,subprocess,io,sys
from PIL import Image
import numpy as np
# usage: chk.py vid masterfile ; fails if any reveal text lower than y=1850 (3-line max ~1841)
v,f=sys.argv[1],sys.argv[2]
d=json.load(open(f'/tmp/t/rp2/out/v{v}.tl.json')); bad=[];res=[]
for i,s in enumerate([s for s in d['scenes'] if s[0]=='q']):
    b=subprocess.run(['ffmpeg','-v','error','-ss',str(s[2]-0.4),'-i',f,'-frames:v','1','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
    a=np.array(Image.open(io.BytesIO(b)).convert('L'))[1500:,40:1040]
    r=np.where((a>200).sum(axis=1)>3)[0]; y=int(1500+r.max()) if len(r) else 0
    res.append(y)
    if y>1850: bad.append(i+1)
print('lowest text rows',res,'OVER_MARGIN' if bad else 'margin_ok',bad)
