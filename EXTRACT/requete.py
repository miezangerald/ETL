import global_variable
from datetime import date, datetime
from pynytimes import NYTAPI


def requettage_api(request_element):

    # Initialisation d'une instance de requettage
    nyt = NYTAPI( key = global_variable.cle_api, parse_dates=True)
    try:
        article = nyt.article_search(
            # recherche d'un article sur element_requete
            query = str(request_element),
            # retourne 30 articles
            results = 30, 
            # recherche des articles de janvier 2022 à decembre 2022
            # dates = {
            #     "begin": datetime.datetime(2022, 1, 1),
            #     "end": datetime.datetime(2022, 12, 31)
            # },
        )
    except:
        article = "erreur de requettage"

    return article




































































































# def requeteApi(sujet,source):
#     # Nous utilisons la dependance de Api integré a python
#     # Initialisation d'une instance de requettage
#     nyt = NYTAPI( key= globalParamettre.keyApi,parse_dates=True)
#     # essayons d'acceder à la ressource en utilisant article_seach qui effectue une requette get sur le endpoint
#     try :
#         outputRequete = nyt.article_search(query=str(sujet),
#                                            # prendre les informations du jour
#                                            dates={"begin": datetime.now().date(), "end":datetime.now().date()},
#                                            options = {"sort": "oldest", # Trier en fonction des plus anciens
#                                            # Definir les différntes sources
#                                             "sources": source })
#     except:
#         outputRequete={"message":"erreur sur la requette"}
    
#     return outputRequete