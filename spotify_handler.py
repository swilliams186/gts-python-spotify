import pprint
import random

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


class Track():
    def __init__(self, name, artist, artwork, url):
        self.url = url
        self.artwork = artwork
        self.artist = artist
        self.name = name


class SongGrabber():
    def __init__(self):
        SPOTIFY_CLIENT_ID = "b86c694135d442c8b8e0746ff7a31e23"
        SPOTIFY_CLIENT_SECRET = "3aef3353296b4df68a1fb45adc78b5d4"
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                                                           client_secret=SPOTIFY_CLIENT_SECRET))

    def get_sample_list(self, artist: str) -> list:
        results = self.spotify.search(artist, type="artist", limit=1)
        artist_id = results["artists"]["items"][0]["id"]
        results = self.spotify.artist_top_tracks(artist_id)
        sample_urls = []

        # print(json.dumps(results,indent=2))
        for track in results['tracks'][:10]:
            sample_urls.append(track["preview_url"])
        return sample_urls

    def results_to_track_list(self, results):
        tracks = []

        for track in results['tracks']:
            track_obj = Track(name=track["name"],
                              artist=track["artists"][0]["name"],
                              artwork=track["album"]["images"][1]["url"],
                              url=track["preview_url"])  # Can be NULL - so search for specfic track and likely to
            # get URI
            print(track["preview_url"])
            if track["preview_url"] != "null" and track["preview_url"] is not None:

                #print("Not none")
                #pprint.pprint((track))
                tracks.append(track_obj)
        return tracks

    def search_year_genre(self, genre: str, year: str) -> list:
        results = self.spotify.search(f"{genre} {year}",
                                      type="playlist",
                                      limit=10)
        for item in results["playlists"]["items"]:
            if item["owner"]["display_name"] == "Spotify":
                pl_id = item["uri"]
                results = self.spotify.playlist_items(pl_id,
                                                      fields='items.track.id,total',
                                                      additional_types=['track'])  # Returns list of tracks in playlist
        # print(json.dumps(results, indent=2))
        uris = []
        for track in results["items"]:  # Get the track URI's from JSON
            try:
                uris.append(track["track"]["id"])
            except:
                print("oops")
        uris = random.choices(uris, k=10)  # spotify has a limit to amount of songs you can query at once
        results = self.spotify.tracks(uris)
        # print(json.dumps(results, indent=2))

        tracks = []
        for track in results["tracks"]:
            track_obj = Track(name=track["name"],
                              artist=track["artists"][0]["name"],
                              artwork=track["album"]["images"][0]["url"],
                              url=track["preview_url"])
            tracks.append(track_obj)
        return self.results_to_track_list(results)

    def get_artist_tracks(self, artist: str) -> dict:
        results = self.spotify.search(artist, type="artist", limit=1, market="US")
        artist_id = results["artists"]["items"][0]["id"]
        results = self.spotify.artist_top_tracks(artist_id)
        # print(json.dumps(results,indent=2))
        return self.results_to_track_list(results)
        # print(json.dumps(results,indent=2))
        # results = self.spotify.artist_top_tracks("")

    # results = spotify.artist_top_tracks(lz_uri)
    # #
    # #
    # for track in results['tracks'][:10]:
    #     print('track    : ' + track['name'])
    #     print('audio    : ' + track['preview_url'])
    #     print('cover art: ' + track['album']['images'][0]['url'])
    #     print()

    # from pydub import AudioSegment
    # from pydub.playback import play
    #
    # song = AudioSegment.from_mp3("temp.mp3")
    # song = song[4000:11000]
    # awesome = song.fade_in(1000).fade_out(2000)
    # play(awesome)
    #


if __name__ == "__main__":
    sg = SongGrabber()
    sg.search_year_genre("Rock", "1970")
