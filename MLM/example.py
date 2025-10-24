from transformers import BertTokenizer, BertForMaskedLM
import torch

# Load pretrained BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

# Input sentence with mask
text = "The cat sat on the [MASK]."
input_ids = tokenizer(text, return_tensors="pt")["input_ids"]

# Predict masked token
with torch.no_grad():
    outputs = model(input_ids)
    predictions = torch.argmax(outputs.logits, dim=-1)

predicted_token = tokenizer.decode(predictions[0])
print(predicted_token)
