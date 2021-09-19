# Codded by tory#003. Waiting for suggestions. Remember to import every library i have here :)

import time
from pytube import YouTube
from pytube import Playlist
import os
import sys
# in case the ffmpeg gives errors just specify the bin path :P
# os.environ["IMAGEIO_FFMPEG_EXE"] = "C:/ffmpeg/bin"
import moviepy.editor as mp
import re
import shutil

def download_playlist():
    print("Insert the link:")
    link = input("")
    playlist = Playlist(link)

    playlist.video_urls

    for url in playlist:
        print(url)

    for vid in playlist.videos:
        print(vid)

    for url in playlist:
        YouTube(url).streams.filter(only_audio=True).first().download()


def convert_to_mp3():
    folder = "./songs"

    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder, file)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)


def move():
    sourcepath = './'
    sourcefiles = os.listdir(sourcepath)
    download_folder = ("Songs")
    CHECK_FOLDER = os.path.isdir(download_folder)

    if not CHECK_FOLDER:
        os.mkdir(download_folder)
        print("Your songs will be in: ", download_folder)

    else:
        print(download_folder, " already exists!")

    destinationpath = './Songs'

    for file in sourcefiles:
        if file.endswith('.mp4'):
            shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))


def remove_3gbp():
    dir_name = "./Songs"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".3gpp"):
            os.remove(os.path.join(dir_name, item))

    menu()


def menu():
    os.system('cls')
    print("************ YouTube Download Manager **************")
    # time.sleep(1)
    print()

    choice = input("""
            A: YouTube PlayList Download
            B: Youtube Song Download
            Q: Quit

        Please enter your choice: """)

    if choice == "A" or choice == "a":
        os.system('cls')
        download_playlist()
        move()
        convert_to_mp3()
        remove_3gbp()

    elif choice == "B" or choice == "b":
        os.system('cls')
        print("Single song download not available at the moment! if you want this feature give the project a star!")
        time.sleep(2)
        menu()

    elif choice == "Q" or choice == "q":
        os.system('cls')
        sys.exit

    else:
        os.system('cls')
        print("You must only select either A, B or Q")
        print("Please try again")
        menu()

menu()