import os

FILE_NAME = 'result_file.txt'
FILE_NAME_DIR = 'files'
BASE_PATH = os.getcwd()

files_list = []
files_path = os.path.join(BASE_PATH, FILE_NAME_DIR)
result_file_path = os.path.join(BASE_PATH, FILE_NAME_DIR, FILE_NAME)
files = os.listdir(files_path)
# print(files)
# files_list = [files_list + for ]

for file in files:
    file = "./files/" + file
    files_list.append(file)
files_dict = {}
for item in files_list:
    # print(item)
    with open(item, "r", encoding="UTF-8") as f:
        count_lines = sum(1 for _ in f)
        # print(count_lines)
        # print(f.readline())
    files_dict[item] = count_lines

sorted_keys = sorted(files_dict, key=files_dict.get)
sorted_dict = {}
for element in sorted_keys:
    sorted_dict[element] = files_dict[element]
print(files_dict)
print(sorted_dict)

with open(result_file_path, "a", encoding="UTF-8") as result_f:
    for path_name, count_lines in sorted_dict.items():
        result_f.write(path_name + '\n')
        # result_f.write('\n')
        result_f.write(str(count_lines) + '\n')
        # result_f.write('\n')
        with open(path_name, "r", encoding="UTF-8") as f:
            for line in f:
                result_f.write(line)
        result_f.write('\n')
# with open('./files/1.txt') as f:
#     print(f.readline())