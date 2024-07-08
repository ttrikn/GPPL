import json
import os.path
import re


def clean_text(raw_text):
    cleaned_text = re.sub(r'[^a-zA-Z.,?!]', ' ', raw_text)
    return cleaned_text


def find_text(file_path, target_id):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                tweet_data = json.loads(line.strip())
                tweet_id = str(tweet_data.get('id', None))
                tweet_text = tweet_data.get('text', None)

                if tweet_id == target_id and tweet_text is not None:
                    tweet_text = re.sub(r'\s*http\S*$', '', tweet_text)
                    tweet_text = re.sub(r'\s*https\S*$', '', tweet_text)
                    tweet_text = re.sub(r'[@#]\S+|:[a-zA-Z]+:', '', tweet_text)
                    tweet_text = re.sub(r'RT', '', tweet_text)
                    tweet_text = re.sub(r'[@#]\S+|:[a-zA-Z_]+:|\s+', ' ', tweet_text).strip()
                    cleaned_text = clean_text(tweet_text)

                    # print(f"ID: {tweet_id}, Text: {cleaned_text}")
                    return cleaned_text
            else:
                print(f"找不到ID为 {target_id} 的记录")
                return ""
    else:
        print(f"找不到 {file_path} ")
        return ""


file_path = "D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/positiveSampleAll.txt"
output_file_path = "D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/positiveData2.txt"

fin = open(file_path, 'r', encoding='utf-8')
lines = fin.readlines()
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    fin = open(file_path, 'r', encoding='utf-8')
    lines = fin.readlines()
    for line in lines:
        line = line.strip()
        user_folder, image_number = line.split(maxsplit=1)
        text = find_text(f'D://PyCharm/FS1/UP-MPF-main/datasets/MultiModalDataset/positive/{user_folder}/timeline.txt',
                         image_number)
        if len(text) > 1:
            output_file.write(f"{user_folder} {image_number} {text} \n")
print(f"Output written to {output_file_path}")
