from PyQt5.QtWidgets import QFileDialog

from pygame import mixer
from pygame.mixer_music import *

from mutagen.mp3 import MP3

from subprocess import call


class Functions:

    def toggle_elements(self, status):

        self.pauseButton.setEnabled(status)
        self.resumeButton.setEnabled(status)
        self.stopButton.setEnabled(status)
        self.volumeLabel.setEnabled(status)
        self.repeatLabel.setEnabled(status)
        self.fadeLabel.setEnabled(status)
        self.volumeBox.setEnabled(status)
        self.repeatBox.setEnabled(status)
        self.fadeBox.setEnabled(status)
        self.progressBar.setEnabled(status)


    def select(self):

        #get track directory
        track_info = QFileDialog.getOpenFileName()
        self.track = track_info[0]

        self.start_playing(self.track)


    def start_playing(self, track):
        
        #inititalize mixer
        mixer.init()

        #set default volume
        DEFAULT_VOLUME = 35
        self.volumeBox.setValue(DEFAULT_VOLUME)
        call( ["amixer", "-D", "pulse", "sset", "Master", f"{DEFAULT_VOLUME}%"] )

        #enable buttons
        self.toggle_elements(True)

        #hide resume button & show pause button
        #this is important when playing next track
        self.resumeButton.hide()
        self.pauseButton.show()

        self.display_track_info(track)

        load(track)
        play()


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

    
    def display_track_info(self, track):

        #get track name
        

        #display track name
        track_name = f"#{track}"
        self.trackName.setText(track_name)


    def change_volume(self):
        
        #get volume level
        volume = self.volumeBox.value() 

        #set volume level
        call( ["amixer", "-D", "pulse", "sset", "Master", f"{volume}%"] )

    
    def repeat(self):
        
        #last track position
        #calculate in seconds
        last_position = (get_pos() / 1000)

        #repeat infinitely
        play(loops=-1, start=last_position)

        #has a problem. to be solved..
        self.repeatBox.setDisabled(True)
        self.fadeBox.setDisabled(True)


    def fade(self):
        
        #calculate in milliseconds
        track_duration = ( MP3(self.track).info.length ) * 1000

        #played time
        finished_duration = get_pos()

        #remaining time
        #fadeout function requires an integer
        remaining_duration = track_duration - finished_duration
        remaining_duration = round(remaining_duration)

        fadeout(remaining_duration)

        #has a problem. to be solved..
        self.fadeBox.setDisabled(True)
        self.repeatBox.setDisabled(True)


    