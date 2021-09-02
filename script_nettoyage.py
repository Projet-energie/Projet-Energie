# Importer le fichier et afficher les premières lignes :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\projet_energie.csv', sep=';', low_memory=False)
print(df.head())
