#vid --> .mp4
import os
from yt_dlp import YoutubeDL

def download_playlist(playlist_url, output_path='videos'):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f"An error occurred: {e}")

playlist_url = 'https://www.youtube.com/playlist?list=PL_PgxS3FkP7ATPveBQ1yah7LDqysyzDCG'
download_playlist(playlist_url,'/Users/ashutoshganguly/Desktop/pixii_ai/data/mp4' )



