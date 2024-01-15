import tkinter as tk
from tkinter import filedialog

class StringSorterApp:
    def __init__(self, root, input_file):
        self.root = root
        self.input_file = input_file
        self.strings = self.read_strings_from_file()
        self.current_index = 0

        self.label = tk.Label(root, text=self.get_current_string())
        self.label.pack(pady=10)

        self.boss_button = tk.Button(root, text="Boss", command=lambda: self.copy_to_file("boss.txt"))
        self.boss_button.pack(side=tk.LEFT, padx=10)

        self.skin_button = tk.Button(root, text="Skin", command=lambda: self.copy_to_file("skin.txt"))
        self.skin_button.pack(side=tk.LEFT, padx=10)

        self.rare_button = tk.Button(root, text="Rare", command=lambda: self.copy_to_file("rare.txt"))
        self.rare_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(root, text="Next", command=self.show_next_string)
        self.next_button.pack(pady=10)

    def read_strings_from_file(self):
        with open(self.input_file, 'r') as file:
            return file.read().splitlines()

    def get_current_string(self):
        if 0 <= self.current_index < len(self.strings):
            return self.strings[self.current_index]
        else:
            return ""

    def copy_to_file(self, output_file):
        current_string = self.get_current_string()
        if current_string:
            with open(output_file, 'a') as file:
                file.write(current_string.rsplit('\\',1)[-1] + ',')
            self.show_next_string()

    def show_next_string(self):
        self.current_index += 1
        if self.current_index < len(self.strings):
            self.label.config(text=self.get_current_string())
        else:
            self.label.config(text="No more strings!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("String Sorter")

    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])

    if input_file:
        app = StringSorterApp(root, input_file)
        root.mainloop()
