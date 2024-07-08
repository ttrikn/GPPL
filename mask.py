from transformers import BertTokenizer, BertForMaskedLM
import torch

# 加载预训练的BERT模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

# 输入一句话，并选择一个要遮蔽的单词
sentence = ("Sentiment of the sentence 'I feel bad !' is maskede .")
tokenized_sentence = tokenizer(sentence, return_tensors='pt')
tokens = tokenizer.encode(sentence, add_special_tokens=True)
for i, token in enumerate(tokens):
    print(f"Token {i}: {tokenizer.convert_ids_to_tokens([token])[0]}")
masked_index = 12 # 选择要遮蔽的位置（例如，这里选择的是 "brown"）

#将选择的位置遮蔽
tokenized_sentence['input_ids'][0][masked_index] = tokenizer.mask_token_id

# 使用模型进行预测
with torch.no_grad():
    outputs = model(**tokenized_sentence)

# 获取预测的概率分布
predictions = outputs.logits
predicted_index = torch.argmax(predictions[0, masked_index]).item()

# 获取预测的单词
predicted_word = tokenizer.convert_ids_to_tokens([predicted_index])[0]

print(f"原始句子：{sentence}")
print(f"遮蔽位置：{masked_index}")
print(f"预测的单词：{predicted_word}")
