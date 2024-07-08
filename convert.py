import codecs

def convert_to_utf8(input_file, output_file):
    with codecs.open(input_file, 'r', encoding='ANSI') as file:
        content = file.read()

    with codecs.open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

# 使用示例
convert_to_utf8('D://PyCharm/FS1/UP-MPF-main/datasets/twitterdp/test.tsv', 'D://PyCharm/FS1/UP-MPF-main/datasets/twitterdp/test01.tsv')
