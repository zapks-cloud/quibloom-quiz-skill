import sys,json,subprocess,os
from PIL import Image
n=int(sys.argv[1]);name=sys.argv[2];fix=[int(x) for x in sys.argv[3].split(',')]
t=json.load(open('./out/v%d.tl.json'%n));o=t['opt']
times=[3.0,12.0]
for q in fix:
    s,d=o[q-1];times+= [s+d['opt_t'][3]+0.3, s+d['rev']+0.8]
times+=[o[6][0]+o[6][1]['opt_t'][1]+0.3,o[9][0]+o[9][1]['rev']+0.8,o[14][0]+o[14][1]['opt_t'][3]+0.3,t['total']-2.0]
HERE=os.path.dirname(os.path.abspath(__file__))
subprocess.run(['python3',os.path.join(HERE,'main2.py'),'video%d.json'%n,'c%d'%n,'out/v%d'%n,'still']+['%.1f'%x for x in times],cwd='.',capture_output=True)
ims=[Image.open('out/v%d.s_%05.1f.png'%(n,x)).resize((300,533)) for x in times]
os.makedirs('final',exist_ok=True)
s=Image.new('RGB',(300*5,533*((len(ims)+4)//5)))
for i,im in enumerate(ims): s.paste(im,((i%5)*300,(i//5)*533))
s.save('./final/v%d-qa-sheet.png'%n)
f='./final/%s'%name
for q in fix:
    st,d=o[q-1];a=st+d['rev']-0.5
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','%.2f'%a,'-t','5','-i',f,'-vn','/tmp/fin_%d_%d.wav'%(n,q)])
subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','100','-t','8','-i',f,'-c','copy','./final/v%d-motion-proof-8s.mp4'%n])
print(times)
