import random

movieList = ["Title 1", "Title 2", "Title 3", "Title 4"]

event = ["death", "win", "lose", "loss of gold", "loss of life", "random thing"]

prizeFromTheBox = ["green", "orange", "purple", "legendary"]

from collections import Counter

print(random.choice(movieList))
print(Counter(random.choices (prizeFromTheBox, [0.8, 0.15, 0.04, 0.01], k = 100)))
