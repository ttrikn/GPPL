import os
import shutil
import csv

# 读取.txt文件
txt_file_path = 'D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/negativeData2.txt'
with open(txt_file_path, 'r') as file:
    lines = file.readlines()

# 创建新文件夹用于存放复制后的图片
output_folder = 'D://PyCharm/FS1/UP-MPF-main/datasets/twitter-dp/image-undepressed'
os.makedirs(output_folder, exist_ok=True)

# 初始化新的图片序号
new_index = 1463
data = []
# 循环处理每一行
for i, line in enumerate(lines):
    parts = line.split(' ', 2)  # 只分割一次，将文本部分保留在一起
    #print(len(parts))
    if len(parts) == 3:
        username, index, text_content = parts[0], parts[1], parts[2].strip()
        # 确保列表长度足够长
        # print(username)
        # print(index)
        # print(text_content)
        source_path = f'D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/negative/{username}/{index}.jpg'
        target_name = f'{new_index}.jpg'
        target_path = os.path.join(output_folder, target_name)

        # 复制图片
        shutil.copy(source_path, target_path)

        # 更新.txt文件中的行
        data.append({
            'username': username,
            'id': new_index,
            'text_content': text_content
        })
        lines[i] = f'{username} {new_index} {text_content} \n'
        new_index += 1

csv_file_path = 'D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/negativeData2.csv'
fieldnames = ['username', 'id', 'text_content']

with open(csv_file_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()

    for entry in data:
        writer.writerow(entry)

print(f"CSV文件已生成：{csv_file_path}")
