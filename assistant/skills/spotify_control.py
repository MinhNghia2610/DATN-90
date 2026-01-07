import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="http://localhost:8888/callback",
        scope="user-modify-playback-state user-read-playback-state"
    )
)

def play():
    sp.start_playback()
    print("🎵 Đã bật Spotify")

def pause():
    sp.pause_playback()
    print("⏸️ Đã tạm dừng Spotify")
