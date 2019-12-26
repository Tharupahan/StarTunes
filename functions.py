#!/usr/bin/env python3

from PyQt5.QtWidgets import QFileDialog
from playsound import playsound

class Functions:
    
    def play(self):
        track_info = QFileDialog.getOpenFileName()
        track = track_info[0]
        playsound(track)

    def stop(self):
        playsound(None)