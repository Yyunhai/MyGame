import random
import os

def m():
    
    Path = "./Music"
    MusicList = os.listdir(Path)
    Num = len(MusicList)
    # MusicList = ["Happy brithday to you.oga","……すごく嬉しい。ありがとう.oga",
    #             "おかえり、先生.oga","この花、もしかして….oga","ブルーアーカイブ.oga"]
    Number = random.randint(0,Num-1)
    return MusicList[Number]
    #print(MusicList[Number])