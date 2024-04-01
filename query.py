import numpy as np
import faiss
import openai
import os

query = "How to make a lamb?"

openai.api_key = ''
# Load DB vectors
db_vectors = np.load('/Users/ashutoshganguly/Desktop/pixii_ai/data/embeddings/embeddings_title.npy')
#print("Loaded DB vectors:", db_vectors.shape)

# Initialize the index
index = faiss.IndexFlatL2(1536)
index.add(db_vectors)
#print("Indexed vectors:", index.ntotal)

# Save and load the index
index_path = '/Users/ashutoshganguly/Desktop/pixii_ai/data/embeddings/recipe_index.faiss'
faiss.write_index(index, index_path)
index = faiss.read_index(index_path)

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return openai.embeddings.create(input=[text], model=model).data[0].embedding

# # Get query embedding
query_embedding = np.array(get_embedding(query))
#print("Query embedding shape:", query_embedding.shape)
query_embedding = query_embedding.reshape(1, -1)  # Ensure it's 2D: 1 sample, 256 features
#print("Reshaped query embedding:", query_embedding.shape)

# Perform the search
D, I = index.search(query_embedding, 1)  # Top 1 similar recipe
#print("Distances:", D)
#print("Indices:", I)

# Get the titles of the top 5 similar recipes
with open('/Users/ashutoshganguly/Desktop/pixii_ai/data/embeddings/titles.txt', 'r') as file:
    titles = file.readlines()

for i in range(1):
    #print(f"Title: {titles[I[0][i]]}")

    # Fetch the corresponding file from the chunked folder
    filename = titles[I[0][0]]
    chunked_folder = '/Users/ashutoshganguly/Desktop/pixii_ai/data/chunked/'
    file_path = os.path.join(chunked_folder, filename).split('\n')[0]
    #print("File path:", file_path)

    # Read the contents of the file
    with open(file_path, 'r') as file:
        contents = file.read()

    #print("Contents of the file:")
    #print(contents)


#generate answer using gpt-3
from generative_gemini import get_summary_gemini
from generative_gpt import get_summary_gpt

def generate_text_gemeini(prompt):
    instructions = "Understand and strictly maintain the style of the text and generate a wikihow article as a response to the question."
    prompt = instructions + "\n" + prompt
    answer = get_summary_gemini(prompt)
    return answer

def generate_text_gpt(prompt):
    answer = get_summary_gpt(prompt)
    return answer

prompt = 'question: ' + query + "\n" + 'answer: ' + contents
#print(generate_text_gemeini(prompt))
print(generate_text_gpt(prompt))
