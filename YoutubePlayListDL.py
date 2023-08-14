import os
import re
import shutil
import sys
from time import sleep

import moviepy.editor as mp  # moviepy needs ffmpeg
from pytube import Playlist
from pytube import YouTube


def verify_command(command):
    # command must be a simple operation definition
    # q = verify_command("open the menu")
    # print(q)
    columns = shutil.get_terminal_size().columns
    answear = input(f"Are you sure you want to {command}?\n[y/n] = ".center(columns))
    return True if answear.lower() == "y" else False


# check if a link is a YouTube link
def check_link(link, playlist=False):
    if playlist:
        if re.search('www.youtube.com/playlist', link):
            return True
        else:
            return False
    else:
        if re.search('www.youtube.com/watch', link):
            return True
        else:
            return False


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
    link = input(">> ")
    if check_link(link, True):
        playlist = Playlist(link)
        for url in playlist:
            print(f"Downloading {YouTube(url).title} | {convert_seconds_to_minutes(YouTube(url).length)};")
            YouTube(url).streams.filter(only_audio=True).first().download()
        print(f"Downloaded {playlist.title} | {convert_seconds_to_minutes(playlist.length)};")
    else:
        print("Invalid or private playlist link!")
        sleep(2)
        menu()


# download song
def download_song():
    print("Insert the song link:")
    link = input(">> ")
    if check_link(link):
        song = YouTube(link)
        print(f"Downloading {song.title} | {convert_seconds_to_minutes(song.length)};")
        song.streams.filter(only_audio=True).first().download()
        print(f"Downloaded {song.title} | {convert_seconds_to_minutes(song.length)};")
    else:
        print("Invalid or private song link!")
        sleep(2)
        menu()


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


# delete the "Songs" folder
def delete_songs():
    dir_name = "./Songs"
    test = os.listdir(dir_name)

    for item in test:
        os.remove(os.path.join(dir_name, item))

    os.rmdir(dir_name)
    menu()


# main menu
def menu():
    os.system('cls')
    print("-YouTube Download Manager-\n")
    folder_name = "Songs"
    check_folder = os.path.isdir(f"./{folder_name}")
    if check_folder:
        print(
            f"Songs: {convert_bytes_into_mb(calculate_size())}\nDisk Space: {convert_bytes_into_mb(shutil.disk_usage('.')[0])}\n")
    choice = input(
        """A: YouTube PlayList Download;\nB: YouTube Song Download;\nO: Open 'Songs' Folder;\nD: Delete all downloaded songs\nQ: Quit;\n\nPlease enter your choice: """)

    if choice.upper() == "A":
        os.system('cls')
        download_playlist()
        move()
        convert_to_mp3()
        remove_3gpp()

    elif choice.upper() == "B":
        os.system('cls')
        download_song()
        move()
        convert_to_mp3()
        remove_3gpp()

    elif choice.upper() == "O":
        os.system('cls')
        if check_folder:
            print("Opening songs folder...")
            os.startfile("Songs")
            sleep(2)
        else:
            print("No songs folder found! Please download some songs first!")
            sleep(3)
        menu()

    elif choice.upper() == "D":
        os.system('cls')
        if check_folder and verify_command("delete \"Songs\" folder"):
            delete_songs()
        else:
            print("No songs folder found! Please download some songs first!")
            sleep(3)
        menu()

    elif choice.upper() == "Q":
        os.system('cls')
        sys.exit()

    else:
        os.system('cls')
        print("You must only select either A, B, O, D or Q;\nPlease try again!")
        sleep(3)
        menu()


if __name__ == "__main__":
    menu()
