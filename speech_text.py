import os

import speech_recognition as sr
from pydub import AudioSegment


def extract_text(audio):
    try:
        text = r.recognize_google(audio)
        write_to_file(text)
        print("Extracted Text ::\n" + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google; Speech; Recognition; service;; {0} ".format(e))
    finally:
        print("Processing completed...")


def write_to_file(text):
    try:
        os.mkdir(text_folder)
    except FileExistsError:
        pass
    os.chdir(text_folder)
    name = file_name[0] + '.txt'
    file_text = open(name, 'a+')
    file_text.write(text + '\n')
    file_text.close()
    os.chdir('..')
    print(f'{name} file generated with text...')


def long_files_transcript(song):
    print(f'duration -> {song.duration_seconds}, splits -> {song.duration_seconds // 50}')
    chunk_size = 50 * 1000

    # split sound in 50-second slices and export
    try:
        os.mkdir('audio_files')
        os.mkdir('audio_files/obama_chunks')
    except FileExistsError:
        try:
            os.mkdir('audio_files/obama_chunks')
        except FileExistsError:
            pass
    os.chdir('audio_files/obama_chunks')
    for i, chunk in enumerate(song[::chunk_size]):
        file_name_chunk = "obama-%s.wav" % i
        with open(file_name_chunk, "wb") as f:
            single_chunk = AudioSegment.silent(10) + chunk + AudioSegment.silent(10)
            single_chunk.export(f, bitrate='192k', format="wav")
        with sr.AudioFile(file_name_chunk) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            write_to_file(text)


if __name__ == '__main__':
    r = sr.Recognizer()
    audio_folder = 'audio_files'
    text_folder = 'text_files'
    file_name = ('sample_male_wav', 'obama')
    extension = ('wav', 'mp3')

    # file 1
    song_file = audio_folder + '/' + file_name[0] + '.' + extension[0]
    sample_audio = sr.AudioFile(song_file)
    with sample_audio as source:
        audio = r.record(source)
        extract_text(audio)

    # file 2
    # song_file = audio_folder + '/' + file_name[1] + '.' + extension[1]
    # try:
    #     song_file_wav = AudioSegment.from_mp3(song_file)
    #     song_file_wav.export(audio_folder + '/obama.wav', bitrate='192k', format="wav")
    #     song = AudioSegment.from_wav(audio_folder + '/obama.wav')
    #     long_files_transcript(song)
    # except FileNotFoundError as e:
    #     print(f'Custom ==> {e}')
