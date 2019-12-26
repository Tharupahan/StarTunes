#!/home/tharupahan/dev/py_projects/environments/env_StarTunes/bin/python3

from PyQt5.QtWidgets import QFileDialog
from miniaudio import stream_file, PlaybackDevice

class Functions:

    def play(self):
        track_info = QFileDialog.getOpenFileName()
        track = track_info[0]

        stream = stream_file(track)

        self.device = PlaybackDevice()
        self.device.start(stream)

    def stop(self):
        self.device.close()