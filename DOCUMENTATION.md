# YouTube Download Manager

The "YouTube Download Manager" script is a Python program that allows you to download YouTube videos and playlists and convert them to MP3 format. It provides a text-based menu for interacting with various functions. Below is an overview of what each part of the script does.

## Table of Contents
1. [Imports](#imports)
2. [BColors Class](#bcolors-class)
3. [Utility Functions](#utility-functions)
    1. [log_faulty_video](#log_faulty_video)
    2. [verify_command](#verify_command)
    3. [check_link](#check_link)
    4. [calculate_size](#calculate_size)
    5. [convert_bytes_into_mb](#convert_bytes_into_mb)
    6. [convert_seconds_to_minutes](#convert_seconds_to_minutes)
4. [Main Functions](#main-functions)
    1. [download_playlist](#download_playlist)
    2. [download_song](#download_song)
    3. [convert_to_mp3](#convert_to_mp3)
    4. [move](#move)
    5. [remove_3gpp](#remove_3gpp)
    6. [delete_songs](#delete_songs)
    7. [menu](#menu)
5. [Main Execution](#main-execution)

## Imports <a name="imports"></a>
The script imports necessary Python modules and libraries, including `os`, `re`, `shutil`, `sys`, `time`, `moviepy.editor`, and `pytube`. These libraries are used for file operations, regular expressions, user input, and YouTube video processing.

## BColors Class <a name="bcolors-class"></a>
The `BColors` class defines ANSI color codes for console output, making the console output more visually appealing.

## Utility Functions <a name="utility-functions"></a>
### log_faulty_video(link)
This function logs a faulty video link to a file named "faulty_videos.txt". It is used when an error occurs while downloading a video.

### verify_command(command)
This function prompts the user to confirm a command. It displays a message to the user and returns `True` if the user confirms the command by typing "y", or `False` otherwise.

### check_link(link, playlist=False)
This function checks if a given link is a valid YouTube link. It returns `True` if the link is valid (or for a playlist if `playlist` is `True`) and `False` if it's not.

### calculate_size()
Calculates the size of the 'Songs' folder by summing up the file sizes within it. It returns the total size in bytes.

### convert_bytes_into_mb(num)
Converts a number of bytes into a human-readable string with appropriate units, such as KB, MB, GB, or TB.

### convert_seconds_to_minutes(seconds)
Converts a duration in seconds to a human-readable time string in the format "minutes:seconds".

## Main Functions <a name="main-functions"></a>
### download_playlist()
Allows the user to download a YouTube playlist. It prompts the user for a playlist link, downloads all videos in the playlist, and stores them in the 'Songs' folder. It also logs any errors in a "faulty_videos.txt" file.

### download_song()
Allows the user to download a single YouTube video as an MP4 file. It prompts the user for a video link and downloads the video to the 'Songs' folder.

### convert_to_mp3()
Converts all MP4 files in the 'Songs' folder to MP3 format using the `moviepy.editor` library. After conversion, the original MP4 files are removed.

### move()
Moves downloaded MP4 files from the current directory to the 'Songs' folder.

### remove_3gpp()
Removes any ".3gpp" files from the 'Songs' folder.

### delete_songs()
Deletes all files in the 'Songs' folder and then removes the folder itself.

### menu()
The main menu of the program. It provides a text-based user interface for selecting various options, such as downloading playlists, songs, converting to MP3, opening the 'Songs' folder, deleting downloaded songs, and quitting the program.

## Main Execution <a name="main-execution"></a>
The script's execution starts at the `menu()` function when it is run. The main menu allows the user to interact with different functions and perform various tasks related to downloading and managing YouTube videos and playlists.

**Note:** Before using the script, ensure you have the required Python libraries installed. The script also assumes the existence of a folder named "Songs" for storing downloaded content.

Enjoy using the "YouTube Download Manager" to download and manage your favorite YouTube content!
