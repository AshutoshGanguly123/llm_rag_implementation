import openai
import os
import numpy as np
openai.api_key = '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'

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return openai.embeddings.create(input=[text], model=model).data[0].embedding

chunked_dir = '/Users/ashutoshganguly/Desktop/pixii_ai/data/chunked'
embeddings_dir = '/Users/ashutoshganguly/Desktop/pixii_ai/data/embeddings'

embeddings_all =[]
title_all = []
for i, file_name in enumerate(os.listdir(chunked_dir)):
    filename = os.path.join(chunked_dir, file_name)
    print(f"Processing the file: {file_name}...")

    with open(filename, 'r') as file:
        recipe_text = file.read()

    title = filename.split('/')[-1]
    print(title)
    embedding_title = get_embedding(title)
    #embedding_text = get_embedding(recipe_text)
    #embedding = embedding_title + embedding_text
    embedding = embedding_title
    embeddings_all.append(embedding)
    title_all.append(title)

np.save(os.path.join(embeddings_dir, 'embeddings_title.npy'), embeddings_all)

#save title
with open('/Users/ashutoshganguly/Desktop/pixii_ai/data/embeddings/titles.txt', 'w') as file:
    for t in title_all:
        file.write(t + '\n')