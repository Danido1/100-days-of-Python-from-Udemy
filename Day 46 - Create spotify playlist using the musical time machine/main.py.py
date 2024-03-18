import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_year = input("What year you would like to travel?(Type the date in this format YYYY-MM-DD)")

URL = f"https://www.billboard.com/charts/hot-100/{user_year}/"
client_id = "881d11cc28414e28991aab5e112b3546"
client_secret = "0ad494567f1d4bbc9d472901beeb0580"

r = requests.get(URL)
r.raise_for_status()
webpage = r.text



soup = BeautifulSoup(webpage, "html.parser")

top_songs = soup.select(selector="div ul li ul li h3", id="title-of-a-story")

songs_list = [song.getText().strip() for song in top_songs]
print(songs_list)





sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
results = sp.current_user()
USER_ID = results['id']

uris = [sp.search(song_name)['tracks']['items'][0]['uri'] for song_name in songs_list]
print(uris)
PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{user_year} BillBoard-100")['id']

sp.user_playlist_add_tracks(user=USER_ID, playlist_id=PLAYLIST_ID, tracks=uris)