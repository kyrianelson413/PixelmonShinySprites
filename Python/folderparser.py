import os
import csv

rootdir = 'assets/pixelmon/textures/pokemon'
filepath = 'csv.skins.csv'

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