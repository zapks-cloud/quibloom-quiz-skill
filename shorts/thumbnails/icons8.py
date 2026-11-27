from icons7 import *
import icons7, math
def yurt():
    im,d=new()
    d.polygon([(500,300),(220,520),(780,520)],fill=(236,226,200))
    d.rectangle((220,520,780,760),fill=(244,236,214))
    d.polygon([(500,300),(420,520),(580,520)],fill=(224,212,180))
    d.rectangle((440,600,560,760),fill=(150,60,50))
    d.rectangle((220,520,780,545),fill=(200,70,60))
    d.ellipse((470,255,530,315),fill=(244,236,214))
    d.rectangle((150,760,850,790),fill=(120,160,90))
    return im
icons7.ICONS.update(yurt=yurt);ICONS=icons7.ICONS
