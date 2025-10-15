import string


def buchstabenZuteilen():
    # Dictionary Comprehension: Buchstabe als Schlüssel, laufende Nummer als Wert
    dic = {buchstabe: nummer for nummer, buchstabe in enumerate(string.ascii_lowercase, start=1)}
    return dic


if __name__ == "__main__":
    dictionary = buchstabenZuteilen()
    print(dictionary)