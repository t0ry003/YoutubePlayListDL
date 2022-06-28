import os
import sys
import re
import shutil
from time import sleep
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp  # moviepy needs ffmpeg


# calculate the size of the songs folder
def calculate_size():
    dir_name = "./Songs"
    test = os.listdir(dir_name)
    size = 0

    for item in test:
        size += os.path.getsize(os.path.join(dir_name, item))

    return size


# convert bytes to MB
def convert_bytes_into_mb(num):
    for i in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, i)
        num /= 1024.0


# convert seconds to minutes and seconds
def convert_seconds_to_minutes(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds}"


# download playlist
def download_playlist():
    print("Insert the playlist link:")
    link = input(">>")
    playlist = Playlist(link)

    for url in playlist:
        print(f"Downloading {YouTube(url).title} - {convert_seconds_to_minutes(YouTube(url).length)};")
        YouTube(url).streams.filter(only_audio=True).first().download()
    print(f"Downloaded {playlist.title} - {convert_seconds_to_minutes(playlist.length)};")


# download song
def download_song():
    print("Insert the song link:")
    link = input(">>")

    song = YouTube(link)
    print(f"Downloading {song.title} - {convert_seconds_to_minutes(song.length)};")
    song.streams.filter(only_audio=True).first().download()
    print(f"Downloaded {song.title} - {convert_seconds_to_minutes(song.length)};")


# convert to mp3
def convert_to_mp3():
    folder = "./songs"

    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder, file)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)


# move files to songs folder
def move():
    source_path = './'
    source_files = os.listdir(source_path)
    download_folder = "Songs"
    check_folder = os.path.isdir(download_folder)

    if not check_folder:
        os.mkdir(download_folder)
        print("Your songs will be in: ", download_folder)

    else:
        print(download_folder, " folder already exists!")

    destination_path = './Songs'

    for file in source_files:
        if file.endswith('.mp4'):
            shutil.move(os.path.join(source_path, file),
                        os.path.join(destination_path, file))


# remove 3gbp
def remove_3gpp():
    dir_name = "./Songs"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".3gpp"):
            os.remove(os.path.join(dir_name, item))

    menu()


# main menu
def menu():
    os.system('cls')
    print("-YouTube Download Manager-\n")
    check_folder = os.path.isdir("./Songs")
    if check_folder:
        print(
            f"Songs: {convert_bytes_into_mb(calculate_size())}\nDisk Space: {convert_bytes_into_mb(shutil.disk_usage('.')[0])}\n")
    choice = input(
        """A: YouTube PlayList Download;\nB: YouTube Song Download;\nO: Open 'Songs' Folder;\nQ: Quit;\n\nPlease enter your choice: """)

    if choice == "A" or choice == "a":
        os.system('cls')
        download_playlist()
        move()
        convert_to_mp3()
        remove_3gpp()

    elif choice == "B" or choice == "b":
        os.system('cls')
        download_song()
        move()
        convert_to_mp3()
        remove_3gpp()

    elif choice == "O" or choice == "o":
        os.system('cls')
        if check_folder:
            print("Opening songs folder...")
            os.startfile("Songs")
            sleep(2)
        else:
            print("No songs folder found! Please download some songs first!")
            sleep(3)
        menu()

    elif choice == "Q" or choice == "q":
        os.system('cls')
        sys.exit()

    else:
        os.system('cls')
        print("You must only select either A, B, O or Q;\nPlease try again!")
        sleep(3)
        menu()


if __name__ == "__main__":
    menu()
