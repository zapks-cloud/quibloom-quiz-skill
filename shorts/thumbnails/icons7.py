from icons6 import *
import icons6, math
def lotus():
    im,d=new()
    cols=((235,120,165),(244,150,185),(250,175,205))
    for ang,L,col in ((-70,330,cols[0]),(70,330,cols[0]),(-42,400,cols[1]),(42,400,cols[1]),(0,450,cols[2])):
        a=math.radians(ang);bx,by=500,760
        tx,ty=bx+math.sin(a)*L,by-math.cos(a)*L
        px,py=math.cos(a)*85,math.sin(a)*85
        mx,my=(bx+tx)/2,(by+ty)/2
        d.polygon([(bx,by),(mx-px,my-py),(tx,ty),(mx+px,my+py)],fill=col)
    d.ellipse((260,740,740,830),fill=(40,150,100))
    return im
icons6.ICONS.update(lotus=lotus);ICONS=icons6.ICONS
