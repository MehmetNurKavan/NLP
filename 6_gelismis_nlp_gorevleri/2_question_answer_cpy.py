from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import warnings
warnings.filterwarnings("ignore")

# GPT-2 model
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_answer(context, question):
    input_text = f"Question: {question}, Context: {context}. Please answer the Question according to the Context" # only one word yazsak tek kelimelik veriri cevabi, bu prompt ile oynayarka fakrlı cevap veridirteibliyoz

    # Tokenize the input text
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    
    # Attention mask ve pad token id'yi belirt
    attention_mask = torch.ones(inputs.shape, device=inputs.device)

    # Generate the answer using the model
    with torch.no_grad():
        outputs = model.generate(
           inputs, 
           max_length=100,  # Yanıtın uzunluğunu kısıtla
           attention_mask=attention_mask,  # Attention mask ayarı
           pad_token_id=tokenizer.eos_token_id  # Pad token id'si ayarı
       )

    # Decode the generated text
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Clean the generated answer
    answer = answer.split("Answer:")[-1].strip()

    return answer


def display_answer(context, question):
    answer = generate_answer(context, question)
    print("***NEW****")
    print(question)
    print(".....")
    print(answer)

# Test the functions
question0 = "Which city is the capital of France?"
context0 = "The capital of France, known officially as the French Republic, is Paris."
display_answer(context0, question0)

question1 = "When did World War II end?"
context1 = "World War II ended on September 2, 1945, with the formal surrender of Japan."
display_answer(context1, question1)
