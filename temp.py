import pvporcupine
import pyaudio
import struct
import playsound

print(pvporcupine.KEYWORDS)

# porcupine = pvporcupine.create(keywords=pvporcupine.KEYWORDS,access_key="gltlepsfo/R5vPk3AH/JQQXYSD0urATF/ILqfeQDpjdCWq6/ZTR8RA==")
porcupine = pvporcupine.create(keyword_paths=["C:\\Users\\meet2\\Desktop\\zara\\Hey-Zara_en_windows_v2_1_0.ppn"],access_key="gltlepsfo/R5vPk3AH/JQQXYSD0urATF/ILqfeQDpjdCWq6/ZTR8RA==")

# "{'grasshopper', 'bumblebee', 'picovoice', 'jarvis', 'porcupine', 'computer', 'hey google', 'grapefruit', 'hey siri', 'americano', 'pico clock', 'blueberry', 'ok google', 'hey barista', 'terminator', 'alexa'}"

pa = pyaudio.PyAudio()

audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

try:
    while(1):
        keyword = audio_stream.read(porcupine.frame_length)
        keyword = struct.unpack("h"*porcupine.frame_length,keyword)
        keyword_index = porcupine.process(keyword)
        if keyword_index>=0:
            print('done')
            # song = pydub.AudioSegment.from_mp3('C:\\Users\\meet2\\Desktop\\zara\\wake.mp3')
            # pydub.playback.play(song)
            playsound.playsound('C:\\Users\\meet2\\Desktop\\zara\\wake.mp3', True)


finally:
    porcupine.delete()
    audio_stream.close()