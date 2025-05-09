import pandas as pd

poke = pd.read_csv('pokemon_data.csv')
poke.shape()

print(poke.tail(5))


