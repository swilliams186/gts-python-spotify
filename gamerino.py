from spotify_handler import SongGrabber, Track
from music_box import MusicBox, Photogenic





class Gamerino():
    mb = MusicBox()
    sg = SongGrabber()
    pg = Photogenic()
    track_list = []
    track_index = 0

    def play_track(self):
        self.mb.play_track()

    def next_track(self) -> Track:
        self.track_index += 1
        self.mb.load_track(self.track_list[self.track_index])
        self.pg.download_art(self.track_list[self.track_index])
        return self.track_list[self.track_index]


    def search(self, artist: str) -> None:
        self.track_list = self.sg.get_artist_tracks(artist)
        print(f"ARTIST {artist}")
        if not self.track_list:
            print("NOTHING")
            pass
        self.track_index = -1
        self.next_track()

    def search_genre_year(self, genre: str, year: str) -> None:
        print(f"Genre: {genre}, Year: {year}")
        self.track_list = self.sg.search_year_genre(genre=genre,
                                                    year=year)
        print(self.track_list)
        self.track_index = -1
        self.next_track()

    def get_current_track_info(self) -> Track:
        return self.track_list[self.track_index]

