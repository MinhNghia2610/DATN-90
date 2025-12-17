import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        redirect_uri="http://localhost:8888/callback",
        scope="user-modify-playback-state"
    )
)

def play_music():
    devices = sp.devices()
    if devices["devices"]:
        sp.start_playback()
        return "Tôi đã bật nhạc cho bạn."
    return "Không tìm thấy thiết bị Spotify."
