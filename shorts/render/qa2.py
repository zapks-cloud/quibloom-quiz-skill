import json,subprocess,sys
from PIL import Image
v=sys.argv[1]; name=sys.argv[2]
t=json.load(open('out/v%s.tl.json'%v));o=t['opt']
times=[3.0,5.5]
for s,d in o: times+=[s+d['opt_t'][3]+0.3, s+d['cd0']+2.5, s+d['rev']+1.2]
times+=[t['total']-3.0]
subprocess.run(['python3','main2.py','/tmp/t/video%s.json'%v,'/tmp/t/c%s'%v,'out/v%s'%v,'still']+['%.1f'%x for x in times],capture_output=True)
ims=[Image.open('out/v%s.s_%05.1f.png'%(v,x)).resize((216,384)) for x in times]
cols=6;rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(216*cols,384*rows))
for i,im in enumerate(ims): S.paste(im,((i%cols)*216,(i//cols)*384))
S.save('/downloads/p%s_qa_sheet.png'%v)
f='final/'+name
subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','%.1f'%(t['total']-14.4),'-t','14.4','-i',f,'-c','copy','/downloads/p%s_tail.mp4'%v])
pts=[0,o[0][0]+o[0][1]['rev']-0.5,o[2][0]+o[2][1]['rev']-0.5,o[4][0]+o[4][1]['rev']-0.5]
for i,a in enumerate(pts): subprocess.run(['ffmpeg','-y','-v','error','-ss','%.1f'%a,'-t','%.1f'%(8 if i==0 else (t['total']-a if i==3 else 12)),'-i',f,'-vn','-ac','1','-ar','24000','/tmp/asr%s_%d.wav'%(v,i)])
print(times[-1],len(ims))
