# Set your OpenAI API key here


import os
import openai

openai.api_key = 

def get_summary_llm(transcript):
    prompt_text = (
        f"{transcript}n"
    )
    # Generate the prompt based on the attributes
    prompt = [
        {"role": "system", "content": "This transcript needs to be chunked without any change in its text. Identify the steps here and just add relevant labels."},
        {"role": "user", "content":prompt_text },
    ]

    summary = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= prompt,)
    #summary = summary['choices'][0]['message']['content']
    return summary.choices[0].message.content

#transcript = "Hi. I'm Jacques Pepin, and I'm cooking at home. I love Brussels sprouts already for Thanksgiving, whatever, but I like it just sauteed like the dairy briefly. And very often, I do that with bacon. And, so you start with a couple of tablespoons of good olive oil. I have sausage here. As you can see, 2 sausage, and those are I like the spicy one, you know, but so you can make little bowl or leave it just in pieces like this. As I'm doing, I'm gonna cook that first. Gonna take a couple of minutes. I have a pan of brussels sprouts here, and I'm gonna put a can of beans at the end. And always the brussels sprouts, I trim the end of it like this. You know, if there is any damaged one, those happen to be beautiful and all that. And I slice them by hand this way as I've done here, but it's pretty hard. So if you happen to have a if you happen to have a a slicer like this, I use that. And this is silya slicer. There is 2 sides. 1 is thicker, and the other one is thinner. I do the thicker part that goes right in there and right on top of it here. And, and that's it. I can put my thing right in there. And this is it. So it's a cinch. So here I have my sausage cooking here. Nice and browned. Let's start rendering some fat. And as you can see here, they are cut very nicely, very equally. Okay. It's basically cooked, and now I can add the rest of this. I have a pound of brussels sprouts here. So that would be for 6 people that I would do that. Salt on top of it. Of course, I can always re season it at the end. I'm gonna cover it. Let it steam a little bit. After 2, 3 minutes, you say it's starting browning, but I think I need some moisture. So as long as I have those beans here. I'm going to use those beans later on, so I might as well add that liquid in there now to cook it. A couple of minutes more. This way, I think a couple of minutes. A bit crunchy but still I like it this way. So the beans, beans are there. And this is about it. Just warm it up until you can do that ahead. Warm it at the last moment. Beautiful frickace or a medley of brussels sprouts, sausage, and beans. Happy cooking."

#summary = get_summary_llm(transcript)
#print(summary)
import json 

transcript_dir = '/Users/ashutoshganguly/Desktop/pixii_ai/data/transcripts'
chunked_dir = '/Users/ashutoshganguly/Desktop/pixii_ai/data/chunked'

for file_name in os.listdir(transcript_dir):
    transcript_path = os.path.join(transcript_dir, file_name)
    print(f"Processing {file_name}...")
    with open(transcript_path, 'r') as file:
        transcript = file.read()
        summary = get_summary_llm(transcript)
        # Ensure to only use the base name without the extension for the summary file
        base_name = os.path.splitext(file_name)[0]
        summary_file_path = os.path.join(chunked_dir, f"{base_name}_summary.txt")
        with open(summary_file_path, 'w') as summary_file:
            summary_file.write(summary)
        print(f"Saved summary for {file_name}.")


