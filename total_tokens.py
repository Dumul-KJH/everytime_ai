#jsonl 전체 토큰 개수 출력
import json
from transformers import GPT2Tokenizer

def print_total_token_counts(jsonl_file):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    total_tokens = 0
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            item = json.loads(line)

            # convert 'nan' or empty inputs to ""
            item['prompt'] = item['prompt'] if item['prompt'] and str(item['prompt']).lower() != 'nan' else ""
            item['completion'] = item['completion'] if item['completion'] and str(item['completion']).lower() != 'nan' else ""

            tokenized_prompt = tokenizer.encode(item['prompt'], truncation=False)
            tokenized_completion = tokenizer.encode(item['completion'], truncation=False)

            item_tokens = len(tokenized_prompt) + len(tokenized_completion)
            total_tokens += item_tokens

            # print(f"Item {idx}: total tokens={item_tokens}")

    print(f"\nTotal tokens in file: {total_tokens}")

print_total_token_counts('dataset_2_prepared.jsonl')
