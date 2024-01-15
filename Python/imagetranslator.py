from PIL import Image, ImageOps
from os import listdir, path
from shutil import copy2

#used to add an outline to an image, and possibly resize it.
def saveOutline(imagename, is4k, color):

    x = Image.open(imagename)
    size = 32

    x = x.convert('RGBA')
    
    if(is4k):
        x = x.resize((64,64), Image.NEAREST)
        size = 64
    
    pix_val = x.load()

    colorArray = [(0,0,0,255),(0,0,0,255),(0,0,0,255),(0,0,0,255)]
    
    if(color == 0): # gold, for shinies
        colorArray[0] = (255, 240, 179, 255)
        colorArray[1] = (255, 219, 77, 255)
        colorArray[2] = (230, 184, 0, 255)
        colorArray[3] = (153, 122, 0, 255)
    elif(color == 1): # purple, for legendaries and mythicals
        colorArray[0] = (230, 204, 255, 255)
        colorArray[1] = (206, 153, 255, 255)
        colorArray[2] = (156, 51, 255, 255)
        colorArray[3] = (79, 0, 153, 255)
    elif(color == 2): # magenta, for ultra beasts
        colorArray[0] = (255, 204, 255, 255)
        colorArray[1] = (255, 128, 255, 255)
        colorArray[2] = (255, 26, 255, 255)
        colorArray[3] = (179, 0, 179, 255)
    elif(color == 3): # orange, for megas and gigantamax (bosses)
        colorArray[0] = (255, 217, 179, 255)
        colorArray[1] = (255, 166, 77, 255)
        colorArray[2] = (230, 115, 0, 255)
        colorArray[3] = (153, 77, 0, 255)
    elif(color == 4): # red, for shiny megas & shiny gigantamax (bosses)
        colorArray[0] = (255, 179, 179, 255)
        colorArray[1] = (255, 77, 77, 255)
        colorArray[2] = (204, 0, 0, 255)
        colorArray[3] = (128, 0, 0, 255)
    elif(color == 5): # green, for special skins
        colorArray[0] = (230, 255, 179, 255)
        colorArray[1] = (196, 255, 77, 255)
        colorArray[2] = (153, 230, 0, 255)
        colorArray[3] = (102, 153, 0, 255)
    elif(color == 6): # slim blue, for rare but otherwise standard Pokemon
        colorArray[0] = (230, 250, 255, 255)
        colorArray[1] = (179, 240, 255, 255)
        colorArray[2] = (128, 229, 255, 255)
        colorArray[3] = (77, 219, 255, 255)
    else: # black, error
        colorArray[0] = (0, 0, 0, 255)
        colorArray[1] = (0, 0, 0, 255)
        colorArray[2] = (0, 0, 0, 255)
        colorArray[3] = (0, 0, 0, 255)


    
    outline_matrix = [[0 for x in range(size)] for x in range(size)]
    outline_matrix2 = [[0 for x in range(size)] for x in range(size)]
    outline_matrix3 = [[0 for x in range(size)] for x in range(size)]
    outline_matrix4 = [[0 for x in range(size)] for x in range(size)]

    if(is4k and color != 6):
        for i in range(1,size - 1):
            for j in range(1,size - 1):
                empty = 254
                if(pix_val[i,j][3] <= empty):
                    if(pix_val[i-1,j-1][3] > empty or pix_val[i+1,j-1][3] > empty or pix_val[i-1,j+1][3] > empty or pix_val[i+1,j+1][3] > empty or pix_val[i,j-1][3] > empty or pix_val[i,j+1][3] > empty or pix_val[i-1,j][3] > empty or pix_val[i+1,j][3] > empty):
                        outline_matrix[i][j] = 1

        for i in range(size):
            for j in range(size):
                if(outline_matrix[i][j] == 1):
                    pix_val[i,j] = colorArray[0]

    for i in range(1,size - 1):
        for j in range(1,size - 1):
            empty = 254
            #print(pix_val[i,j])
            if(pix_val[i,j][3] <= empty):
                if(pix_val[i-1,j-1][3] > empty or pix_val[i+1,j-1][3] > empty or pix_val[i-1,j+1][3] > empty or pix_val[i+1,j+1][3] > empty or pix_val[i,j-1][3] > empty or pix_val[i,j+1][3] > empty or pix_val[i-1,j][3] > empty or pix_val[i+1,j][3] > empty):
                    outline_matrix2[i][j] = 1

    for i in range(size):
        for j in range(size):
            if(outline_matrix2[i][j] == 1):
                pix_val[i,j] = colorArray[1]

    if(is4k and color != 6):
        for i in range(1,size - 1):
            for j in range(1,size - 1):
                empty = 254
                if(pix_val[i,j][3] <= empty):
                    if(pix_val[i-1,j-1][3] > empty or pix_val[i+1,j-1][3] > empty or pix_val[i-1,j+1][3] > empty or pix_val[i+1,j+1][3] > empty or pix_val[i,j-1][3] > empty or pix_val[i,j+1][3] > empty or pix_val[i-1,j][3] > empty or pix_val[i+1,j][3] > empty):
                        outline_matrix3[i][j] = 1

        for i in range(size):
            for j in range(size):
                if(outline_matrix3[i][j] == 1):
                    pix_val[i,j] = colorArray[2]

    for i in range(1,size - 1):
        for j in range(1,size - 1):
            empty = 254
            if(pix_val[i,j][3] <= empty):
                if(pix_val[i-1,j-1][3] > empty or pix_val[i+1,j-1][3] > empty or pix_val[i-1,j+1][3] > empty or pix_val[i+1,j+1][3] > empty or pix_val[i,j-1][3] > empty or pix_val[i,j+1][3] > empty or pix_val[i-1,j][3] > empty or pix_val[i+1,j][3] > empty):
                    outline_matrix4[i][j] = 1

    for i in range(size):
        for j in range(size):
            if(outline_matrix4[i][j] == 1):
                pix_val[i,j] = colorArray[3]
    
    x.save(imagename)

    return 1

#just do a simple resize
def saveResize(imagename):
    x = Image.open(imagename)
    x = x.resize((64,64), Image.NEAREST)
    x.save(imagename)
    return 1

#used to write an entire folder of images.
def outlineFiles(directoryName=None, is4k=None, color=None, justResize=False):

    if(justResize):
        a_directory = directoryName
        for filename in listdir(a_directory):
            filepath = path.join(a_directory, filename)
            saveResize(filepath)
        return 1

    if(directoryName == None or (isinstance(directoryName, str)) == False):
        print("Please enter a directory (filepath) in the form of a string as the first argument.")
    if(is4k == None or (isinstance(is4k, bool)) == False):
        print("Please answer whether you would like the files to be upsized to 64 pixels as the second argument (True or False).")
    if(color == None or (isinstance(color, int)) == False or (0 <= color <= 6) == False):
        print("Please enter a number, 0 thru 6. 0 is gold, 1 is purple, 2 is magenta, 3 is orange, 4 is red, 5 is green, and 6 is slim blue.")

    a_directory = directoryName
    for filename in listdir(a_directory):
        filepath = path.join(a_directory, filename)
        saveOutline(filepath, is4k, color)

    return 1

def getNewFiles(newFilesList=None, newFilesFolder=None, destFolder=None):

    if(newFilesList == None or newFilesFolder == None or destFolder == None):
        print("Please enter all arguments.")
        return 0

    with open(newFilesList, 'r') as file:
        lines = file.read().splitlines()

    a_directory = newFilesFolder
    for line in lines:
        for filename in listdir(a_directory):
            if(line == filename):
                copy2(path.join(newFilesFolder, filename), destFolder)

    return 1
    

