import random
import os

def m():
    
    Path = "./Music"
    MusicList = os.listdir(Path)
    Num = len(MusicList)
    Number = random.randint(0,Num-1)
    return MusicList[Number]
    #print(MusicList[Number])
#m()