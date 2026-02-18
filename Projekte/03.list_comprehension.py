def listComprehension(einwohner):
    verdoppelte_einwohner = [i * 2 for i in einwohner]
    return verdoppelte_einwohner


def setComprehension(einwohner):
    einwohner = [1000, 2000, 3000, 4000, 5000]
    einwohner_gross = {i for i in einwohner if i > 2000}
    return einwohner_gross


def dicComprehension(einwohner):
    status = {i : ("groß" if i > 2000 else "klein") for i in einwohner}
    return status

if __name__ == "__main__":
    einwohner = [1000, 2000, 3000, 4000, 5000]
    ### Liste welche nichts hat bei der list comprehension
    print(listComprehension(einwohner))

    ### Set List, welche ein if haben, welche nur die speichern, welche Werte größer als 2000 haben
    print(setComprehension(einwohner))

    ### Dic List, wo ein if und ein else gibt, was entscheidet wie groß eine Stadt ist
    print(dicComprehension(einwohner))

