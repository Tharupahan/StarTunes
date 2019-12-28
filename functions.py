from PyQt5.QtWidgets import QFileDialog
from pygame import mixer
from pygame.mixer_music import *
from subprocess import call

class Functions:


    def toggle_elements(self, status):

        self.pauseButton.setEnabled(status)
        self.resumeButton.setEnabled(status)
        self.stopButton.setEnabled(status)
        self.label.setEnabled(status)
        self.label2.setEnabled(status)
        self.label3.setEnabled(status)
        self.volumeBox.setEnabled(status)
        self.repeatBox.setEnabled(status)
        self.fadeBox.setEnabled(status)
        self.timeSlider.setEnabled(status)


    def select(self):

        #get track directory
        track_info = QFileDialog.getOpenFileName()
        track = track_info[0]

        self.start_playing(track)


    def start_playing(self, track):
        
        #inititalize mixer
        mixer.init()

        #set default volume
        DEFAULT_VOLUME = 35
        self.volumeBox.setValue(DEFAULT_VOLUME)
        call( ["amixer", "-D", "pulse", "sset", "Master", f"{DEFAULT_VOLUME}%"] )

        #load and play track
        load(track)
        play()

        #enable buttons
        self.toggle_elements(True)

        #hide resume button & show pause button
        #this is important when playing next track
        self.resumeButton.hide()
        self.pauseButton.show()


    def pause(self):
        
        #pause track
        pause()

        #hide pause button & show resume button
        #this is important when playing next track
        self.pauseButton.hide()
        self.resumeButton.show()


    def resume(self):
        
        #resume the track
        unpause()

        #hide resume button & show pause button
        self.resumeButton.hide()
        self.pauseButton.show()


    def stop(self):
        
        #stop the current track
        stop()

        #disable elements
        self.toggle_elements(False)


    def change_volume(self):
        
        #get volume level
        volume = self.volumeBox.value() 

        #set volume level
        call( ["amixer", "-D", "pulse", "sset", "Master", f"{volume}%"] )

    