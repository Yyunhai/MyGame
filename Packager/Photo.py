import random
import os
def n():
    Path = "./Image"
    ImageList = os.listdir(Path)
    Num = len(ImageList)
    # ImageList = ["1.jpg","2.jpg",
    #             "3.jpg","4.jpg"]
    Number = random.randint(0,Num-1)
    return ImageList[Number]
    #print(ImageList[Number])
