import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *

def download_audio():
    try:
        # Get the YouTube video URL from the input field
        url = url_input.get()

        # Download the YouTube video
        youtube = YouTube(url)
        video = youtube.streams.filter(only_audio=True).first()
        video.download()

        # Convert the video to MP3
        video_path = video.default_filename
        audio_path = video_path.replace('.mp4', '.mp3')
        video_clip = AudioFileClip(video_path)
        video_clip.write_audiofile(audio_path)
        video_clip.close()
        os.remove(video_path)

        # Get the save path from the user
        save_path = filedialog.asksaveasfilename(defaultextension='.mp3')

        # Save the audio file
        shutil.move(audio_path, save_path)
        tk.messagebox.showinfo(title='Download complete', message='Audio saved successfully!')
    except Exception as e:
        tk.messagebox.showerror(title='Error', message=str(e))

# Create the TKinter GUI
root = tk.Tk()
root.title('YouTube Audio Downloader')

url_label = tk.Label(root, text='Enter YouTube video URL:')
url_label.pack()

url_input = tk.Entry(root, width=50)
url_input.pack()

download_button = tk.Button(root, text='Download', command=download_audio)
download_button.pack()

root.mainloop()
