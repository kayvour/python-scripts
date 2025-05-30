from pytubefix import YouTube
from sys import argv
import os
from pathlib import Path

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print(f"Downloading... {percent:.2f}%", end="\r")

def main():
    if len(argv) < 2:
        print("Usage: python YTdownloader.py <YouTube-URL> [quality] [audio-only]")
        return
    
    link = argv[1]
    
    requested_quality = None
    audio_only = False
    
    if len(argv) >= 3:
        if argv[2].isdigit():
            requested_quality = int(argv[2])
        elif argv[2].lower() == 'audio':
            audio_only = True
    
    if len(argv) >= 4 and argv[3].lower() == 'audio':
        audio_only = True

    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        
        downloads_folder = os.path.join(Path.home(), "Downloads")
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)

        print(f"Downloading to folder: {downloads_folder}")

        if audio_only:
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            if not stream:
                print("No audio-only stream available.")
                return
        else:
            if requested_quality:
                stream = yt.streams.filter(res=f"{requested_quality}p", progressive=True).first()
                if not stream:
                    print(f"No video stream available at {requested_quality}p, downloading highest resolution instead.")
                    stream = yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.get_highest_resolution()
        
        stream.download(output_path=downloads_folder)
        print("\nDownload completed successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()