import google.generativeai as genai
import os

#genai.configure(api_key=os.environ['API_KEY'])
genai.configure(api_key='')

def get_summary_gemini(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


