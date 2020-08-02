import speech_recognition as sr


def extract_text(audio):
    try:
        text = r.recognize_google(audio)
        print("Extracted Text ::\n" + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google; Speech; Recognition; service;; {0} ".format(e))
    finally:
        print("Processing completed...")


if __name__ == '__main__':
    r = sr.Recognizer()
    sample_audio = sr.AudioFile('audio_files/sample_male_wav.wav')
    with sample_audio as source:
        audio = r.record(source)
        extract_text(audio)
