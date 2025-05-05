from transformers import BertTokenizer, BertForQuestionAnswering
import torch
import warnings
warnings.filterwarnings("ignore")

# squad veri seti üzerinde fine-tuning yapılmış bert dil modeli
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

def predict_answer(context, question):
    # token
    encoding = tokenizer.encode_plus(question, context, return_tensors="pt", max_length=512, truncation=True)
    
    # giriş tensorları
    input_ids = encoding["input_ids"]
    attention_mask = encoding["attention_mask"]
    
    # model çalıştır ve skor al
    with torch.no_grad():  # herhangi öğrenme yapmadan skor tahmini et
        start_scores, end_scores = model(input_ids, attention_mask=attention_mask, return_dict=False)
        
    # en yüksek olasılıklı başlangıç ve bitiş indekslerini bul
    start_index = torch.argmax(start_scores, dim=1).item()
    end_index = torch.argmax(end_scores, dim=1).item()
    
    # tokenları al ve cevabı çöz
    answer_tokens = tokenizer.convert_ids_to_tokens(input_ids[0][start_index:end_index + 1])
    answer = tokenizer.convert_tokens_to_string(answer_tokens)
    
    return answer


def display_answer(context, question):
    answer = predict_answer(context, question)

    print("Question: ",question)
    print("Answer: ",answer)


question0 = "Which city is the capital of France?"
context0 = "The capital of France, known officially as the French Republic, is Paris."
display_answer(context0, question0)



question1 = "When did World War II end?"
context1 = "World War II ended on September 2, 1945, with the formal surrender of Japan."

display_answer(context1, question1)


'''
display answer :
    
Question:  Which city is the capital of France?
Answer:  paris

Question:  When did World War II end?
Answer:  september 2 , 1945
'''