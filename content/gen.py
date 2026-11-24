import sys,json,random;sys.path.insert(0,'.')
from data import T,W
hook=json.load(open('../video02_animals.json'))['hook']
num=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen']
I='Engaging English quiz host, bright and clear at a natural pace. Give each answer option a distinct beat. No rushed delivery.'
man=[dict(id='hook',text=hook,instructions=I,voice='Sadachbia'),dict(id='cta',text="Enjoyed it? Like, share this video with a friend, and subscribe to Quibloom for more quizzes!",instructions=I,voice='Sadachbia')]
rng=random.Random(2411)
for v,topic,cat,qs in T:
    out=dict(video=v,topic=topic,category=cat,hook=hook,questions=[])
    for i,(q,c,wr,page,_) in enumerate(qs):
        opts=wr[:]; pos=[1,2,3,0,2,1,3,0,1,3,2,0,3,1,2][(i+v)%15]; rng.shuffle(opts); opts.insert(pos,c)
        L='ABCD'[pos]
        qs_='Question %s. %s %s'%(num[i],q,' '.join('%s. %s.'%('ABCD'[k],o) for k,o in enumerate(opts)))
        asp='%s is correct, %s.'%(L,c)
        out['questions'].append(dict(n=i+1,question=q,options=opts,correct_index=pos,answer_letter=L,question_speech=qs_,answer_speech=asp,source=W+page))
        vv='v%02d'%v
        man.append(dict(id='%s_q%02d'%(vv,i+1),text=qs_,instructions=I,voice='Sadachbia'))
        man.append(dict(id='%s_a%02d'%(vv,i+1),text=asp,instructions=I,voice='Sadachbia'))
    json.dump(out,open('video%02d.json'%v,'w'),indent=1)
json.dump(man,open('tts_manifest_all.json','w'),indent=1)
json.dump([m for m in man if m['id'] in('hook','cta') or m['id'].startswith('v11')],open('tts_manifest_v11.json','w'),indent=1)
