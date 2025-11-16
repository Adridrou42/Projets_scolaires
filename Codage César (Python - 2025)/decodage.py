from unidecode import unidecode

def decodage(message_code, clef, message_decode = ""):
    message_code = unidecode(message_code) # Convertit les caractères non ASCII en caractères ASCII.

    if abs(clef) > 25:
        clef -= int(26 * (clef / abs(clef)))
    if clef == 0:
        return message_code

    for character in message_code:

        if ord(character) >= 65 and ord(character) <= 90:  # Majuscules
            character = ord(character) + clef
            if character > 90:
                character -= 26
            if character < 65:
                character += 26
            message_decode += chr(character)
        elif ord(character) >= 97 and ord(character) <= 122:  # Minuscules
            character = ord(character) + clef
            if character > 122:
                character -= 26
            if character < 97:
                character += 26
            message_decode += chr(character)
        else:  # Autres caractères
            message_decode += character

    return message_decode


def tout_tester(message_code):
    retour = ""
    for clef in range(26):
        message_decode = decodage(message_code, clef)
        retour += f"Clef {clef} : {message_decode} \n"
    return retour


def try_except_decodage(message_code, clef):
    try:
        clef = int(clef)
        return decodage(message_code, clef)
    except ValueError:
        return "Erreur : La clé doit être un nombre entier."