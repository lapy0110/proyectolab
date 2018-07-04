from music21 import *

print("Reproduciendo ...")
s = converter.parse('cancion2.tinynotation')
sp = midi.realtime.StreamPlayer(s)
sp.play()
print("Reproduciendo ...")
s.transpose("m3")
sp = midi.realtime.StreamPlayer(s.transpose("m3"))
sp.play()



