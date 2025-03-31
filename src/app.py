import os
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

try:
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    result = spotify.artist_top_tracks("3o2dn2O0FCVsWDFSh8qxgG")
    top10 = result['tracks']

    data = {'name':[],'duration':[],'popularity':[]}
    for track in top10:
        data['name'].append(track['name'])
        data['duration'].append(track['duration_ms'])
        data['popularity'].append(track['popularity'])   
except Exception as e:
    print("Ocurrió un error:", e)

df = pd.DataFrame(data)
df_sorted = df.sort_values(['popularity'])
df_sorted.head(3)

serie = pd.Series(data['duration'])
duracion_s = serie / 1000

plt.figure(figsize=(10,5))
plt.title('relacion duracion/popularidad')
plt.scatter(duracion_s,data['popularity'])
plt.show()