# testwritewave.py
# encoding: utf-8
# http://nalab.mind.meiji.ac.jp/~mk/lecture/fourier-2017/testwavemodule3.py
# これは Python 3.x 用のプログラム
import numpy as np
import wave
import struct
fname ='constwave.wav'
wf = wave.open(fname, 'w')
ch = 1
width = 2
samplerate = 44100
wf.setnchannels(ch)
wf.setsampwidth(width)
wf.setframerate(samplerate)
time = 10
numsamples = time * samplerate
print( u"チャンネル数 = ", ch)
print( u"サンプル幅 (バイト数) = ", width)
print( u"サンプリングレート (Hz) =", samplerate)
print( u"サンプル数 =", numsamples)
print( u"録音時間 =", time)
# 信号データを作る (numpy の ndarray で)
freq = 440 # 周波数 freq を 440 Hz にする
x=np.linspace(0, time, numsamples+1) # 0 ≦ t ≦ time を numsamples 等分
y=np.ones(x.shape[0]) # 周波数 freq (Hz) の正弦波
y=np.rint(32767*y/max(abs(y))) # [-32767,32767] の範囲に収める
y=y.astype(np.int16)
# 16 ビット整数に型変換する
y=y[0:numsamples] # numsamples 個のデータに打ち切る
# ndarray から bytes オブジェクトに変換
data=struct.pack("h" * numsamples , *y)
# データを書き出す
wf.writeframes(data)
wf.close()
