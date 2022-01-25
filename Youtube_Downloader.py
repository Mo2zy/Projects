import pytube
from pytube.__main__ import YouTube
from pytube.cli import on_progress

def main():

    url = input("Beta Youtube Downloader Made by Mo2zy... \n Enter The Youtube Video URL Here : ")
    if url.startswith('http') :
        Convert = YouTube(url)
        video_title = input(u"{}\n Do you want to continue ? (yes/no) : ".format(Convert.title)).lower()
        if video_title == 'yes':
            vidoraud = input("Video or Audio .. ? (v/a) : ").lower()

            if vidoraud == 'v':
                    res = input('High Resultion or Low ? (high/low) : ').lower()
                    
                    if res == 'low':
                        print("Your Video With Low Resultion Will Be Installed in seconds...")
                        myvideo = YouTube(url,on_progress_callback=on_progress)
                        myvideo = myvideo.streams.get_lowest_resolution()
                        myvideo.download()
                        print("Done!")

                    else:
                        print("The Video With High Resultion  Will Be Installed in seconds...")
                        myvideo = YouTube(url,on_progress_callback=on_progress)
                        myvideo = myvideo.streams.get_highest_resolution()
                        myvideo.download()
                        print("Done!")

            elif vidoraud == 'a':
                    print("Ok Your Audio Will Be Installed in seconds ...")
                    myAudio = YouTube(url,on_progress_callback=on_progress)
                    myAudio = myAudio.streams.get_audio_only()
                    myAudio.download()
                    print("Done!")

    else:
        print("Please Enter Full Youtube Link .. !")
    restart=input("Do You Want To Download Another Video/Audio ? (yes/no) : ").lower()
    if restart == 'yes':
        main()
    else:
        quit()
main()



