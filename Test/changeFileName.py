import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
all_file_name = os.listdir(dir_path)

# print(all_file_name)
print(dir_path)

n = 1842
for i in all_file_name:
    if i == 'changeFileName.py':
        continue
    print(dir_path +'\\'+ f'{n:04d}.jpg')
    os.rename(dir_path + '\\' +i, dir_path + '\\' +f'{n:04d}.jpg')
    n = n + 1

# for i in all_file_name:
#     abs_file = os.path.join(dir_path, i)
#     if i == "changeFileName.py":
#         break
#     print(i)
#     with open(abs_file, 'r', encoding='utf-8') as load_f:
#         load_dict = json.load(load_f)
        
#     load_dict['imagePath'] = '../JPEGImages/' + i
    
#     with open(abs_file, 'w', encoding='utf-8') as f:
#         json.dump(load_dict, f, indent=4)
# for i in range(1, 503):
#     fileName = str(i).zfill(3) + ".json"
#     print(fileName)
    
#     with open(fileName,'r',encoding='utf-8') as load_f:
#         load_dict = json.load(load_f)
        
    # load_dict['imagePath'] = "../JPEGImages/" + fileName

    # with open(fileName, 'w') as f:
    #     json.dump(load_dict, f, indent=4)
