import hashlib
import json

def generate_unique_name(value):
    """
    Génère un nom unique basé sur le contenu de la valeur fournie.

    :param value: Peut être un texte, JSON, CSV, etc.
    :return: Nom unique sous forme de chaîne de caractères
    """
    try:
        # Si la valeur est un dictionnaire ou une liste, on la convertit en chaîne JSON triée
        if isinstance(value, (dict, list)):
            value = json.dumps(value, sort_keys=True)
        elif not isinstance(value, str):
            # Si la valeur n'est pas une chaîne, on la convertit en chaîne
            value = str(value)

        # Génération du hash unique basé sur le contenu
        unique_hash = hashlib.sha256(value.encode('utf-8')).hexdigest()
        return f"unique_{unique_hash[:10]}"  # On utilise les 10 premiers caractères du hash

    except Exception as e:
        return f"error_generating_name_{str(e)}"