from pytube import YouTube
import os
import PySimpleGUI as sg
import vlc

def download_youtube_video_as_mp3():
    yt = YouTube(str(input("Enter URL of Video: \n>> ")))
    # yt = YouTube(https://www.youtube.com/watch?v=GXkYC8zn2Ss)

    video = yt.streams.filter(only_audio=True).first()

    # print("Enter destination file location")
    # destination = str(input(">> ")) or '.'
    # destination = "C:\Users\THIS PC\project_ET\project_ET\git_source\song\"
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    destination = os.path.join(base_dir + "/song")

    out_file = video.download(output_path=destination)
    print(out_file)
    print(os.path)
    filename = out_file.split("/")
    print(filename[-1])



    print(yt.title + "has been successfully downloaded in .mp3 format")

def play_songs_via_mediaplayer():
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
        if event == "Play" and player is not None:
            player.play()
        if event == "Pause" and player is not None:
            player.pause()
        if event == "Stop" and player is not None:
            player.stop()


    window.close()




if __name__ == '__main__':
    user_input = input("Please choose your option:  1. Download YouTube Song and Play Songs in MP3 Player, 2. Play Songs in MP3 Player. \n>> ")
    print(user_input)
    if user_input == "1":
        download_youtube_video_as_mp3()    
    play_songs_via_mediaplayer()
