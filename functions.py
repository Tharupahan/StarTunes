#!/usr/bin/env python3

from PyQt5.QtWidgets import QFileDialog

class Functions:
    
    def play(self):
        track_path = QFileDialog.getOpenFileName()

    def stop(self):
        pass