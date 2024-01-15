import os
import csv

def find_sprite(file_path, legendary_keywords):
    if "shiny" in file_path.lower():
        return "Shiny" + (" Legendary" if any(keyword in file_path.lower() for keyword in legendary_keywords) else "")
    elif any(keyword in file_path.lower() for keyword in legendary_keywords):
        return "Legendary"
    else:
        return ""

def search_directory(root_directory, sprite_filename, csv_filename):
    
    print("hi!")
    # Read keywords from CSV
    legendary_keywords = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            legendary_keywords.extend(row)

    print(' '.join(legendary_keywords))
    
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename == sprite_filename:
                file_path = os.path.join(foldername, filename)
                result = find_sprite(file_path, legendary_keywords)
                if result:
                    print(f"{file_path}: {result}")

# Example usage:
# search_directory("Pixelmon_Pack_Revisions_1.20.2_9.2.6/Pixelmon-1.20.2-9.2.6-universal/assets/pixelmon/textures/pokemon", "sprite.png", "Pixelmon_Pack_Revisions_1.20.2_9.2.6/legendaries.csv")

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
alphabetize_lines("existing_subdirectories_with_path.txt", "existing_subdirectories_with_path_alphabetized.txt")