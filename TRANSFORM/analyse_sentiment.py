import nltk
nltk.download('vader_lexicon')
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd

# Charger les données dans un DataFrame
#df = pd.read_csv("votre_fichier.csv")

# Instancier le module d'analyse des sentiments
sia = SentimentIntensityAnalyzer()

# Créer une fonction pour attribuer le sentiment à chaque texte
def get_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'positif'
    elif sentiment['compound'] <= -0.05:
        return 'négatif'
    else:
        return 'neutre'

data1 = pd.read_csv('/media/prempeh/Nouveau nom/MASTER2/DATA ENGINEERING/airflow/biden/2023/2/28.csv')
data1.head(5)         

# Appliquer la fonction à chaque texte dans le DataFrame
data1['sentiment'] = data1['abstract'].apply(get_sentiment)


data1.to_csv('/media/prempeh/Nouveau nom/MASTER2/DATA ENGINEERING/airflow/LOAD/data_final.csv', index = False)