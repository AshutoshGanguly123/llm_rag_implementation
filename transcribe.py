import os
from deepgram import DeepgramClient, PrerecordedOptions, FileSource
# Ensure you import the necessary classes and methods correctly.

API_KEY = ''
DIRECTORY_PATH = '/Users/ashutoshganguly/Desktop/pixii_ai/data/mp4'
TRANSCRIPTS_DIRECTORY = '/Users/ashutoshganguly/Desktop/pixii_ai/data/transcripts'

def transcribe_video(deepgram_client, video_path):
    try:
        with open(video_path, "rb") as file:
            buffer_data = file.read()

        payload = {
            "buffer": buffer_data,
            "mimetype": "video/mp4"
        }

        # Assuming 'prerecorded' might be the correct method name, but double-check with the SDK documentation.
        response = deepgram_client.transcription.prerecorded(payload, {'model': 'general'})
        transcript_text = response['results']['channels'][0]['alternatives'][0]['transcript']

        return transcript_text
    except Exception as e:
        print(f"Exception during transcription of {video_path}: {e}")
        return None

def transcribe_videos_in_directory(directory_path, transcripts_directory):
    # Create a Deepgram client using the API key
    deepgram_client = Deepgram(API_KEY)

    # Ensure the transcripts directory exists
    os.makedirs(transcripts_directory, exist_ok=True)

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.mp4'):
            print(f"Transcribing {file_name}...")
            file_path = os.path.join(directory_path, file_name)
            transcription = transcribe_video(deepgram_client, file_path)

            if transcription:
                transcript_file_name = f"{os.path.splitext(file_name)[0]}.txt"
                transcript_file_path = os.path.join(transcripts_directory, transcript_file_name)
                with open(transcript_file_path, 'w') as transcript_file:
                    transcript_file.write(transcription)
                print(f"Saved transcription for {file_name}.")

# Example usage
transcribe_videos_in_directory(DIRECTORY_PATH, TRANSCRIPTS_DIRECTORY)
