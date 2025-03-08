import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv(r"C:\Users\Ken\Videos\R2DS\Matplotlib\gas_prices.csv")

gas.columns = gas.columns.str.strip()

gas["Year"] = pd.to_numeric(gas["Year"], errors="coerce")

plt.figure(figsize=(8,5))

plt.plot(gas["Year"], gas["USA"], 'r.-', label='USA')
plt.plot(gas["Year"], gas["Canada"], 'b.-', label='Canada')


plt.title("USA vs Canada Gas Prices")
plt.ylabel("Dollar/Gallon")
plt.xlabel("Year")
plt.legend()


plt.xticks(sorted(gas["Year"].unique())[::3])

plt.show()
