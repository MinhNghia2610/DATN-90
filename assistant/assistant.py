from nlp.intent_parser import parse_intent
from skills.spotify_control import play, pause
from skills.weather import get_weather

def handle_command(text):
    intent, _ = parse_intent(text)

    if intent == "spotify_play":
        play()

    elif intent == "spotify_pause":
        pause()

    elif intent == "weather":
        print(get_weather())

    else:
        print("🤖 Tôi chưa hiểu lệnh đó")
