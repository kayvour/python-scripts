A Python script to download YouTube videos or audio streams with custom quality selection, live progress feedback, and automatic saving to your system’s Downloads folder.

Usage:
Run the script with:
python YTdownloader.py <YouTube_URL> [quality] [audio-only]

-<YouTube_URL> (required): The URL of the YouTube video to download.
-[quality] (optional): Desired video resolution as a number (e.g., 720, 1080). If omitted or unavailable, highest resolution will be downloaded.
-[audio-only] (optional): Specify audio to download audio-only stream instead of video.

Download location:
-On Windows, downloads go to C:\Users\<YourUsername>\Downloads
-On macOS/Linux, downloads go to /Users/<YourUsername>/Downloads or /home/<YourUsername>/Downloads

The script automatically creates the folder if it doesn’t exist.

Error Handling:
-Displays usage instructions if no URL is provided.
-Warns if requested quality is unavailable and falls back to highest resolution.
-Handles connection errors and other exceptions with error messages.