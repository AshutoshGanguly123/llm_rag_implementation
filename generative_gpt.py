import os
import openai

openai.api_key = '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'

def get_summary_gpt(prompt):
    prompt_text = (
        f"{prompt}n"
    )
    # Generate the prompt based on the attributes
    prompt = [
        {"role": "system", "content": "Understand and strictly maintain the style of the text and generate a wikihow article as a response to the question."},
        {"role": "user", "content":prompt_text },
    ]

    summary = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= prompt,)
    #summary = summary['choices'][0]['message']['content']
    return summary.choices[0].message.content




#summary = get_summary_llm(prompt)
#print(summary)