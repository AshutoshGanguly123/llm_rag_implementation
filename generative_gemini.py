import google.generativeai as genai
import os

#genai.configure(api_key=os.environ['API_KEY'])
genai.configure(api_key='AIzaSyA90Jp6T4qGE_x0Y3vhV2Qh9bAgr5P94hc')

def get_summary_gemini(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


