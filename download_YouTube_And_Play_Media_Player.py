from pytube import YouTube
import os
import PySimpleGUI as sg
import vlc
import pytube

def download_youtube_video_as_mp3():
    try:
        yt = YouTube(str(input("Enter URL of YouTube Video link: \n>> ")))
        # yt = YouTube(https://www.youtube.com/watch?v=GXkYC8zn2Ss)

        video = yt.streams.filter(only_audio=True).first()

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        destination = os.path.join(base_dir + "/song")

        out_file = video.download(output_path=destination)
        filename = out_file.split("/")

        print(yt.title + "has been successfully downloaded in .mp3 format")
    except Exception as err:
        print(err)
        return 0




def download_youtube_video_as_mp4():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        destination = os.path.join(base_dir + "/song")

        yt = input("Enter YouTube Video Link: ")
        video_instance = pytube.YouTube(yt)
        stream = video_instance.streams.get_highest_resolution()
        video_download = stream.download(destination)
        print("Video download has been completed successfully")
    except Exception as err:
        print(err)
        return 0


def play_songs_via_mediaplayer():
    try:
        controls = [sg.Button("Play"),sg.Button("Pause"),sg.Button("Stop")]
        layout = [[sg.FileBrowse(key="-MP3-",enable_events=True)], controls]
        player = None

        window = sg.Window("MP3 Player", layout)

        while True:
            event, values =  window.read()

            if event == "OK" or event == sg.WIN_CLOSED:
                break
            if event == "-MP3-":
                player = vlc.MediaPlayer(values['-MP3-'])
            # if event == "-MP4-":
            #     player = vlc.MediaPlayer(values['-MP4-'])
            if event == "Play" and player is not None:
                player.play()
            if event == "Pause" and player is not None:
                player.pause()
            if event == "Stop" and player is not None:
                player.stop()


        window.close()
    except Exception as err:
        print(err)
        return 0






if __name__ == '__main__':
    user_input = input("Please choose your option:  1. Download YouTube Song and Play Songs in MP3 Player, 2. Download YouTube Video Song and Play. 3. Play Songs \n>> ")
    print(user_input)
    if user_input == "1":
        download_youtube_video_as_mp3()
        play_songs_via_mediaplayer()
    if user_input == "2":
        download_youtube_video_as_mp4()
        play_songs_via_mediaplayer()
    if user_input == "3":
        play_songs_via_mediaplayer() 
    
