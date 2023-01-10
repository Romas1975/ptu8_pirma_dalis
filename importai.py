# from zaislai import testinis

tekstas = "Labas rytas!"
# print(testinis.atbulai(tekstas))
# print(testinis.atbulai(testinis.kintamasis))

from zaislai.testinis import atbulai, kintamasis
# from zaislai.testinis import *

print(atbulai(tekstas))
print(atbulai(kintamasis))

from zaislai import testinis as t
# from zaislai.testinis import kintamasis as tk

# print(t.atbulai(tekstas))
# print(t.atbulai(tk))

# from zaislai.testinis import atbulai, kintamasis as k
# print(atbulai(k))

# print(__name__)
# print(t.__name__)

# from zaislai import geris
# print(geris.geras)
