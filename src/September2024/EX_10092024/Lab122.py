import os

full_path_file = os.path.join("C:\Users\prach\PycharmProjects\PyATB4xLearning\src\September2024\EX_10092024", "prachi.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)
