# Importer le fichier et afficher les premières lignes :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\projet_energie.csv', sep=';', low_memory=False)
df.head()

#Création “Date_datetime” au format date :
from datetime import datetime as dt

df["Date_datetime"]=pd.to_datetime(df.Date)
df.head()

#“Heure” au format heure
from datetime import datetime as dt

df["Heure"]=df.Heure.astype("datetime64")
df["Heure"]=df.Heure.dt.hour
df.head()

#Affichage des colonnes du dataset
print(df.columns)