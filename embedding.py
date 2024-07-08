from transformers import BertForMaskedLM, BertTokenizer

# 加载预训练的BERT模型和分词器
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 获取输入嵌入矩阵
input_embeddings = model.bert.get_input_embeddings()

# 获取分词器的词汇表
vocab = tokenizer.get_vocab()

# 打印词汇表中的前几个词语及其对应的嵌入表示
for word, idx in vocab.items():
    if idx < 10:
        embedding = input_embeddings.weight[idx].detach().numpy()
        print(f"{word}: {embedding}")