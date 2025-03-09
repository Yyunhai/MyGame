import random

def m():
    MusicList = ["Happy brithday to you.oga","……すごく嬉しい。ありがとう.oga",
                "おかえり、先生.oga","この花、もしかして….oga","ブルーアーカイブ.oga"]
    Num = random.randint(0,4)
    return MusicList[Num]
    #print(MusicList[Num])
