from music21 import *

cancion = stream.Score()
p0 = stream.Part()
p1 = stream.Part()

p0.append(note.Note('C', type="whole"))
p1.append(note.Note('G', type="whole"))

cancion.insert(0, p0)
cancion.insert(0, p1)

print("Reproduciendo ...")
sp = midi.realtime.StreamPlayer(p0)
sp.play()
sp = midi.realtime.StreamPlayer(cancion)
sp.play()
print("Hol vale")

parte1 = stream.Score()
p = stream.Part()
p.append(note.Note('C'))
p.append(note.Note('G', type="whole"))
p.append(note.Note('F'))
p.append(note.Note('G'))

parte1.insert(0,p)
print("Reproduciendo ...")

sp = midi.realtime.StreamPlayer(parte1)
sp.play()
print("Hol vale")

print("Reproduciendo ...")
s = converter.parse('cancion2.tinynotation')
sp = midi.realtime.StreamPlayer(s)
sp.play()



