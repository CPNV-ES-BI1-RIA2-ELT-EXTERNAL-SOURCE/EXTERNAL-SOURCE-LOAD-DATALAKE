import requests

def api_call(method, url, headers=None, data=None, params=None):

    # TODO Remove french content
    """
    Appelle une API en GET ou POST et retourne la réponse.

    :param method: 'GET' ou 'POST'
    :param url: URL de l'API
    :param headers: Dictionnaire des en-têtes HTTP (optionnel)
    :param data: Données pour le corps de la requête (POST uniquement, optionnel)
    :param params: Paramètres de requête (GET uniquement, optionnel)
    :return: Réponse de l'API sous forme d'objet JSON ou texte brut
    """
    if method.upper() == 'GET':
        response = requests.get(url, headers=headers, params=params)
    elif method.upper() == 'POST':
        response = requests.post(url, headers=headers, json=data)
    else:
        raise ValueError("La méthode doit être 'GET' ou 'POST'")

    response.raise_for_status()

    return response.text


