import os
import re
import shutil
import sys
from time import sleep

import moviepy.editor as mp
from yt_dlp import YoutubeDL


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_faulty_video(link):
    with open("faulty_videos.txt", "a+") as file:
        file.write(link + "\n")

def verify_command(command):
    columns = shutil.get_terminal_size().columns
    answer = input(f"Are you sure you want to {command}?\n[y/n] = ".center(columns))
    return True if answer.lower() == "y" else False

def check_link(link, playlist=False):
    if playlist:
        return bool(re.search(r'(?:https?://)?(?:www\.)?youtube\.com/playlist\?list=', link))
    else:
        return bool(re.search(r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=', link))


def calculate_size():
    dir_name = "./Songs"
    test = os.listdir(dir_name)
    size = sum(os.path.getsize(os.path.join(dir_name, item)) for item in test)
    return size

def convert_bytes_into_mb(num):
    for i in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, i)
        num /= 1024.0

def convert_seconds_to_minutes(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds}"

def download_playlist():
    print(f"{BColors.OKCYAN}Please make sure the playlist is public! And do not open the songs folder until the download is finished! {BColors.ENDC}")
    print("Insert the playlist link:")
    link = input(">> ")
    if check_link(link, True):
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
            'outtmpl': './Songs/%(title)s.%(ext)s',
            'noplaylist': False
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print(f"{BColors.OKGREEN}Playlist downloaded successfully!{BColors.ENDC}")
        except Exception as e:
            print(f"{BColors.WARNING}Error downloading playlist: {str(e)}{BColors.ENDC}")
    else:
        print("Invalid or private playlist link!")
        sleep(2)
        menu()

def download_song():
    print("Insert the song link:")
    link = input(">> ")
    if check_link(link):
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
            'outtmpl': './Songs/%(title)s.%(ext)s',
            'noplaylist': True
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print(f"{BColors.OKGREEN}Song downloaded successfully!{BColors.ENDC}")
        except Exception as e:
            print(f"{BColors.WARNING}Error downloading song: {str(e)}{BColors.ENDC}")
    else:
        print(f"{BColors.WARNING}Invalid or private song link!{BColors.ENDC}")
        sleep(2)
        menu()

def convert_to_mp3():
    folder = "./Songs"
    for file in os.listdir(folder):
        if re.search('webm', file):
            webm_path = os.path.join(folder, file)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(webm_path)
            new_file.write_audiofile(mp3_path)
            os.remove(webm_path)

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
        if file.endswith('.webm'):
            shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))

def remove_3gpp():
    dir_name = "./Songs"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".3gpp"):
            os.remove(os.path.join(dir_name, item))
    menu()

def delete_songs():
    dir_name = "./Songs"
    test = os.listdir(dir_name)

    for item in test:
        os.remove(os.path.join(dir_name, item))
    os.rmdir(dir_name)
    menu()

def menu():
    os.system('cls')
    print(f"{BColors.HEADER}-YouTube Download Manager-\n{BColors.ENDC}")
    folder_name = "Songs"
    check_folder = os.path.isdir(f"./{folder_name}")
    if check_folder:
        print(f"Songs: {convert_bytes_into_mb(calculate_size())}\nDisk Space: {convert_bytes_into_mb(shutil.disk_usage('.')[0])}\n")
    choice = input(f"""A: YouTube PlayList Download;\nB: YouTube Song Download;\n{BColors.OKCYAN}C: Convert the remaining MP4{BColors.ENDC}\nO: Open 'Songs' Folder;\nD: Delete all downloaded songs\nQ: Quit;\n\nPlease enter your choice: """)

    if choice.upper() == "A":
        os.system('cls')
        download_playlist()

    elif choice.upper() == "B":
        os.system('cls')
        download_song()

    elif choice.upper() == "C":
        os.system('cls')
        convert_to_mp3()

    elif choice.upper() == "O":
        os.system('cls')
        if check_folder:
            print("Opening songs folder...")
            os.startfile("Songs")
            sleep(2)
        else:
            print(f"{BColors.WARNING}No songs folder found! Please download some songs first!{BColors.ENDC}")
            sleep(3)
        menu()

    elif choice.upper() == "D":
        os.system('cls')
        if check_folder and verify_command("delete \"Songs\" folder"):
            delete_songs()
        else:
            print(f"{BColors.WARNING}No songs folder found! Please download some songs first!{BColors.ENDC}")
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
