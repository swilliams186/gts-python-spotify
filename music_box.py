import requests
from pydub import AudioSegment
from pydub.playback import play, _play_with_pyaudio
from spotify_handler import Track

class MusicBox():




    def play_track(self) -> None:
        song = AudioSegment.from_mp3("temp.mp3")
        song = song[4000:11000]
        awesome = song.fade_in(1000).fade_out(2000)
        play(awesome)
        #pydub.playback.

    def load_track(self, track: Track) -> None:
        mp3 = requests.get(track.url)
        with open('temp.mp3', 'wb') as f:
            f.write(mp3.content)


class Photogenic():

    def download_art(self, track: Track) -> None:
        art = requests.get(track.artwork)
        with open('temp.jpg', 'wb') as f:
            f.write(art.content)


#
# song = AudioSegment.from_mp3("temp.mp3")
# song = song[4000:11000]
# awesome = song.fade_in(1000).fade_out(2000)
# play(awesome)
#