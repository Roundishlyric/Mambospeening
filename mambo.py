from tkinter import *
import cv2
import threading
import time
from ffpyplayer.player import MediaPlayer
import cv2

def play_vid():
    video_path = 'C:\\Users\\renzd\\Downloads\\speen.mp4'
    mam = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    start_time = time.time()
    while True:
        ret, frame = mam.read()
        if not ret:
            break

        audio_frame, val = player.get_frame()
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame

        cv2.imshow("MAMBO SPEEEEEEN", frame)

        if time.time() - start_time > 10.5:  # stop after 10.5s
            break

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    mam.release()
    cv2.destroyAllWindows()
    player.close_player()


def start_video():
    threading.Thread(target=play_vid).start()

#tkinter UI

window = Tk()
photo=PhotoImage(file='C:\\Users\\renzd\\OneDrive\\Pictures\\program\\mambos.png')
window.title('Mambo spin')
button = Button(window,
                text="click me to see mambo spin",
                command=play_vid,
                font=("Comic Sans",30),
                fg="#FFFFFF",
                bg="black",
                activeforeground="#9900FF",
                activebackground="white",
                image=photo,
                state=ACTIVE,
                compound='bottom')
button.pack()

window.mainloop()