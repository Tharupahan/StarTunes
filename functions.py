#!/home/tharupahan/dev/py_projects/environments/env_StarTunes/bin/python3

from PyQt5.QtWidgets import QFileDialog
from vlc import MediaPlayer

class Functions:

    def play(self):
        track_info = QFileDialog.getOpenFileName()
        track = track_info[0]
        player = MediaPlayer(track)
        player.play()

    def stop(self):
        pass