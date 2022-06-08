import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "YOUR_SPOTIFY_CLIENT_ID"
client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
songs = soup.find_all(name="h3", class_="c-title")

songs_list = [song.getText() for song in songs]

songs_list = songs_list[4:]
songs_list = songs_list[:100]

updated_list = []

for song in songs_list:
    song = song.strip('\n')
    updated_list.append(song)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="YOUR_REDIRECT_URL",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in updated_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, public=False, name=f"{date} Billboard 100")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
