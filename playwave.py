import pyaudio
import wave

CHUNK = 1024
filename="constwave.wav"

wf = wave.open(filename, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

print("begin")
data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
print("end")
stream.close()

p.terminate()

