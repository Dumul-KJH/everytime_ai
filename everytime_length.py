#길이제한 해주는 프로그램 GPT3 최대 2048개의 토큰 처리 가능
import pandas as pd
from transformers import GPT2Tokenizer

def trim_to_combined_token_limit(csv_file, max_tokens=2048):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    df = pd.read_csv(csv_file)

    for idx, row in df.iterrows():
        # convert 'nan' or empty inputs to ""
        row['Title'] = row['Title'] if row['Title'] and str(row['Title']).lower() != 'nan' else ""
        row['Content'] = row['Content'] if row['Content'] and str(row['Content']).lower() != 'nan' else ""
        row['Comments'] = row['Comments'] if row['Comments'] and str(row['Comments']).lower() != 'nan' else ""

        tokenized_title = tokenizer.encode(row['Title'], truncation=False)
        tokenized_content = tokenizer.encode(row['Content'], truncation=False)
        tokenized_comments = tokenizer.encode(row['Comments'], truncation=False)

        # If the combined tokens exceed the limit, trim the 'content' from the end
        # and the 'comments' from the beginning until they fit
        while len(tokenized_title) + len(tokenized_content) + len(tokenized_comments) > max_tokens:
            if len(tokenized_content) > len(tokenized_comments):
                tokenized_content = tokenized_content[:-1]
            else:
                tokenized_comments = tokenized_comments[1:]

        df.loc[idx, 'Title'] = tokenizer.decode(tokenized_title)
        df.loc[idx, 'Content'] = tokenizer.decode(tokenized_content)
        df.loc[idx, 'Comments'] = tokenizer.decode(tokenized_comments)

    df.to_csv('trimmed_dataset.csv', index=False)

trim_to_combined_token_limit('everytime_hotarticle_merged.csv')
