import random
import os

def find_valid_images(folder_path):
    valid_images = []

    for user_folder in os.listdir(folder_path):
        user_folder_path = os.path.join(folder_path, user_folder)

        if os.path.isdir(user_folder_path):
            for image_file in os.listdir(user_folder_path):
                image_path = os.path.join(user_folder_path, image_file)

                if os.path.isfile(image_path) and image_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    if os.path.getsize(image_path) > 0:
                        image_number = os.path.splitext(image_file)[0]
                        valid_images.append((user_folder, image_number))

    return valid_images


def write_to_txt(selected_images, output_file):
    with open(output_file, 'w') as file:
        for user_folder, image_number in selected_images:
            file.write(f"{user_folder} {image_number}\n")

folder_path = "D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/positive"
output_file = "D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/positiveSampleAll.txt"

valid_images = find_valid_images(folder_path)
selected_images = random.sample(valid_images, 1500)

write_to_txt(selected_images, output_file)

print("有效图片序号已保存到", output_file)
