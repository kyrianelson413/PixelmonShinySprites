import os
import csv

rootdir = 'C:/Users/Kyria/Desktop/Pixelmon Pack Revisions/Pixelmon_Pack_Revisions_1.20.2_9.2.6/Pixelmon-1.20.2-9.2.6-universal/assets/pixelmon/textures/pokemon'
filepath = 'C:/Users/Kyria/Desktop/Pixelmon Pack Revisions/toplevelskins.txt'

def ifNotInFileAddToFile(name):
    with open(filepath, 'rt') as f:
        reader = csv.reader(f, delimiter=',') # good point by @paco
        flag = False
        for row in reader:
            for field in row:
                if field == name:
                    flag = True
    if(flag):
        with open(filepath, 'a') as f:
            f.write(name + ",")

    return 1

for subdir in os.listdir(rootdir):
    for ssubdir in os.listdir(os.path.join(rootdir, subdir + "/all")):
        ifNotInFileAddToFile(ssubdir)