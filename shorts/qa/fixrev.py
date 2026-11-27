import json,sys
v=int(sys.argv[1]); fixes=json.loads(sys.argv[2])
d=json.load(open(f'/tmp/t/video{v}.json'))
for q,t in fixes.items(): d['questions'][int(q)-1]['reveal']=t
json.dump(d,open(f'/tmp/t/video{v}.json','w'),ensure_ascii=False,indent=1)
