# Importer le fichier et afficher les premières lignes :
import pandas as pd
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
population = pd.read_excel('populationFR.xlsx')
#données de population recceuillies sur le site de l'INED, seule source trouvée disponible
df.head()

#Création des dictionnaires
import pandas as pd
dictionnaire_2018= {"Bretagne": ["3335414"], 'Nouvelle-Aquitaine':[5979778], 'Île-de-France':[12213447],
       'Bourgogne-Franche-Comté':[2807807], 'Auvergne-Rhône-Alpes':[7994459], 'Normandie':[3327477],
       'Occitanie':[5885496], 'Centre-Val de Loire':[2572853], 'Hauts-de-France':[6044108], 'Grand Est':[5550389],
       "Provence-Alpes-Côte d'Azur":[5052832], 'Pays de la Loire':[3781423]}
dictionnaire_2019= {"Bretagne": [3347004], 'Nouvelle-Aquitaine':[5999253], 'Île-de-France':[12252917],
       'Bourgogne-Franche-Comté':[2801577], 'Auvergne-Rhône-Alpes':[8030533], 'Normandie':[3320832],
       'Occitanie':[5918981], 'Centre-Val de Loire':[2569510], 'Hauts-de-France':[5995908], 'Grand Est':[5543407],
       "Provence-Alpes-Côte d'Azur":[5065696], 'Pays de la Loire':[3800348]}
dictionnaire_2020= {"Bretagne": [3358524], 'Nouvelle-Aquitaine':[6018424], 'Île-de-France':[12291557],
       'Bourgogne-Franche-Comté':[2794517], 'Auvergne-Rhône-Alpes':[8064146], 'Normandie':[3313432],
       'Occitanie':[5951850], 'Centre-Val de Loire':[2565726], 'Hauts-de-France':[5987795], 'Grand Est':[5536002],
       "Provence-Alpes-Côte d'Azur":[5077582], 'Pays de la Loire':[3818421]}

#Création du df population entre 2013 et 2020
import numpy as np
df_Population=pd.DataFrame()

df_Population=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2018","Population_2019","Population_2020"])

df_Population["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population["Population_2013"]=[3258707,5844177,11959807,2819783,7757595,3328364,5683878,2570548,5987883,5552388,4953675,3660852]
df_Population["Population_2014"]=[3276543,5879144,12027565,2820623,7820966,3335645,5730753,2577435,6006156,5554645,4983438,3690833]
df_Population["Population_2015"]=[3293850,5911482,12082144,2820940,7877698,3339131,5774185,2578592,6009976,5559051,5007977,3718512]
df_Population["Population_2016"]=[3306529,5935603,12117132,2818338,7916889,3335929,5808435,2577866,6006870,5555186,5021928,3737632]
df_Population["Population_2017"]=[3318904,5956978,12174880,2811423,7948287,3330478,5845102,2576252,6003815,5549586,5030890,3757600]

df_Population["Population_2018"]=[3335414,5979778,12213447,2807807,7994459,3327477,5885496,2572853,6044108,5550389,5052832,3781423]
df_Population["Population_2019"]=[3347004,5999253,12252917,2801577,8030533,3320832,5918981,2569510,5995908,5543407,5065696,3800348]
df_Population["Population_2020"]=[3358524,6018424,12291557,2794517,8064146,3313432,5951850,2565726,5987795,5536002,5077582,3818421]
#df_Population["ANNEE_2018"]=[2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
#df_Population["ANNEE_2019"]=[2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
#df_Population["ANNEE_2020"]=[2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
df_Population




