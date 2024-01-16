import os
import csv
from PIL import Image, ImageOps

def check_strings_in_csv(strings_array, csv_file):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            csv_strings = set([item for row in reader for item in row])

        for string in strings_array:
            if string in csv_strings:
                return True

        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def extract_path_after_string(file_path, given_string):
    index = file_path.find(given_string)
    return file_path[index + len(given_string):]

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

# sane, true version    
    output_dir = os.path.join(os.getcwd(), os.path.dirname(extract_path_after_string(imagename, "textures/")))
    output_file = os.path.join(os.getcwd(), extract_path_after_string(imagename, "textures/"))

    if not os.path.exists(output_dir):
                os.makedirs(output_dir)
    x.save(output_file)

# check your work version
#    shortfilename = extract_path_after_string(imagename, "textures/")
#    longfilename = shortfilename.replace("\\", "-")
#    output_file = os.path.join(os.getcwd(), "pokemon")
#    output_file = os.path.join(output_file, longfilename)
#    print(output_file)
#
#    x.save(output_file)

    return 1

def outline_sprites(root_directory, sprite_filename):
    
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename == sprite_filename:
                file_path = os.path.join(foldername, filename).lower()
                file_path_array = file_path.split("\\")

                # Shiny takes precedence above all other outlines
                if "shiny" in file_path:
                    if check_strings_in_csv(file_path_array, "csv/boss.csv"):
                        saveOutline(file_path, False, 4) # Shiny Boss Pokemon
                    else:
                        saveOutline(file_path, False, 0) # Shiny

                # Special cases for certain Pokemon
                elif "415_combee" in file_path_array and "female" in file_path_array:
                    saveOutline(file_path, False, 6) # Rare Mon (female combee)
                elif "550_basculin" in file_path_array and "white" in file_path_array:
                    saveOutline(file_path, False, 6) # Rare Mon (white basculin)
                elif "666_vivillon" in file_path_array and "pokeball" in file_path_array:
                    saveOutline(file_path, False, 6) # Rare Mon (pokeball Vivillon), else, will get "skin" outline
                elif "179_mareep" in file_path_array or "831_wooloo" in file_path_array or "832_dubwool" in file_path_array:
                    pass # else, Pink Mareep, Wooloo and Dubwool will get "skin" outline
                    #saveOutline(file_path, False, 7) # Sanity check
                elif "585_deerling" in file_path_array or "586_sawsbuck" in file_path_array:
                    pass # else, Summer Deerling and Sawsbuck will get "skin" outline
                    #saveOutline(file_path, False, 7) # Sanity check
                elif "493_arceus" in file_path_array or "773_silvally" in file_path_array:
                    saveOutline(file_path, False, 1) # Outline as Legendary, else Dark type will get "skin" outline
                elif "422_shellos" in file_path_array or "423_gastrodon" in file_path_array:
                    if check_strings_in_csv(file_path_array, "csv/shellos_gastrodon.csv"):
                        saveOutline(file_path, False, 5) # Special case due to "sun" skin which affects Castform
                    #else:
                        #saveOutline(file_path, False, 7) # Sanity check
                elif "591_amoonguss" in file_path_array:
                    if check_strings_in_csv(file_path_array, "csv/amoonguss.csv"):
                        saveOutline(file_path, False, 5) # Special case due to skins which match Minecraft wool colors
                    #else:
                        #saveOutline(file_path, False, 7) # Sanity check

                # Skin, Boss, Legendary, UB, Paradox, Rare outlines
                elif check_strings_in_csv(file_path_array, "csv/skin.csv"):
                    saveOutline(file_path, False, 5) # Fancy Skin
                elif check_strings_in_csv(file_path_array, "csv/boss.csv"):
                    saveOutline(file_path, False, 3) # Normal Boss
                elif check_strings_in_csv(file_path_array, "csv/legendaries.csv"):
                    saveOutline(file_path, False, 1) # Legendary
                elif check_strings_in_csv(file_path_array, "csv/ultrabeasts_paradoxmons.csv"):
                    saveOutline(file_path, False, 2) # UB, Paradox
                elif check_strings_in_csv(file_path_array, "csv/rare.csv"):
                    saveOutline(file_path, False, 6) # Rare Mon

                #else: # only for sanity checking
                #    saveOutline(file_path, False, 7) # Sanity check


# Example usage:
outline_sprites("assets/pixelmon/textures/pokemon", "sprite.png")

def update_subdirectories_file(root_directory, existing_file, existing_file_with_path):
    existing_subdirectories = set()

    # Read existing subdirectories from the file
    if os.path.exists(existing_file):
        with open(existing_file, 'r') as existing_file_content:
            existing_subdirectories = set(existing_file_content.read().splitlines())

    # Traverse the directory and its subdirectories
    new_subdirectories = set()
    new_subdirectories_with_path = set()
    for foldername, subfolders, filenames in os.walk(root_directory, topdown=True):
        for subfolder in subfolders:
            if not (subfolder in new_subdirectories) and not subfolder[:3].isdigit():
                new_subdirectories.add(subfolder)
                new_subdirectories_with_path.add(os.path.join(foldername, subfolder))

    # Find subdirectories that are not in the existing file
    subdirectories_to_add = new_subdirectories - existing_subdirectories

    # Append new subdirectories to the existing file
    with open(existing_file, 'a') as output:
        for subdirectory in subdirectories_to_add:
            output.write(subdirectory + '\n')

    with open(existing_file_with_path, 'a') as output:
        for subdirectory in new_subdirectories_with_path:
            output.write(subdirectory + '\n')

# Example usage:
#update_subdirectories_file("Pixelmon_Pack_Revisions_1.20.2_9.2.6/Pixelmon-1.20.2-9.2.6-universal/assets/pixelmon/textures/pokemon", "existing_subdirectories.txt", "existing_subdirectories_with_path.txt")

def alphabetize_lines(input_file, output_file):
    with open(input_file, 'r') as input_content:
        lines = input_content.readlines()

    # Alphabetize the lines
    sorted_lines = sorted(lines)

    with open(output_file, 'w') as output:
        for line in sorted_lines:
            output.write(line)

# Example usage:
#alphabetize_lines("existing_subdirectories_with_path.txt", "existing_subdirectories_with_path_alphabetized.txt")