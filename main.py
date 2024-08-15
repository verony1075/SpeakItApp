from gtts import gTTS
import sounddevice as sd
import numpy as np
import os
import time
from pydub import AudioSegment
from io import BytesIO
from scipy.io import wavfile


def fetch_pronunciation(word):
    tts = gTTS(text=word, lang='en')
    mp3_file = 'pronunciation.mp3'
    wav_file = 'pronunciation.wav'

    # Save as MP3 first
    tts.save(mp3_file)

    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')

    # Remove the original MP3 file
    os.remove(mp3_file)

    return wav_file


def play_audio(filename):
    try:
        samplerate, data = wavfile.read(filename)
        sd.play(data, samplerate)
        sd.wait()  # Wait until the sound has finished playing
    except Exception as e:
        print(f"Error playing audio: {e}")


def main():
    print("Welcome to the Word Pronunciation Checker!")
    word = input("Enter a word to check its pronunciation: ")
    print("Fetching pronunciation...")

    audio_file = fetch_pronunciation(word)
    print("Playing pronunciation...")
    play_audio(audio_file)

    # Ensure the file is not in use before deleting
    try:
        os.remove(audio_file)
        print("File removed successfully.")
    except PermissionError as e:
        print(f"Error removing file: {e}")


if __name__ == "__main__":
    main()
