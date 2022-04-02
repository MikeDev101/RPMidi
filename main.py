from rpmidi import RPMidi
from songs import SongData

if __name__ == "__main__":
    midi = RPMidi() # Instanciate RPMidi
    songs = SongData() # Load songs. See songs.py
    midi.play_song(songs.morning_music()) # Konami Bubble System "Morning Music" :)