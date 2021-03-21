# Start camille renaudin

def who_and_old():
    name = input("what is your name? ")
    age = int(input("what is your age? "))
    print("Hello {}, so, you have {} years!" .format(name, age))


def swap(param1, param2):
    print("Before : {}, {}".format(param1,param2))
    tmp = param1
    param1 = param2
    param2 = tmp
    print("After: {}, {}" .format(param1, param2))


def moyenne(param1, param2, param3):
    if type(param1) is int or float and type(param2) is int or float and type(param3) is int or float:
        ret = (param1 + param2 + param3) / 3
        print("La moyenne de {}, {} et {} est : {}".format(param1, param2, param3, ret))
    else:
        print("L'une des valeurs n'est pas un chiffre.")


def my_sqrt():
    nb = int(input("Donnez le chiffre dont vous souhaiter la racine carre : "))
    i = 1
    if nb <= 0:
        print("0.")
        return
    while i <= 14654:
        if (i * i) == nb:
            print("La racine carre de {} est : {}".format(nb, i))
            break
        if (i * i) > nb:
            print("La racine carre la plus proche de {} est : {}".format(nb, i - 1))
            break
        i += 1


if __name__ == '__main__':
    param1 = 2.5
    param2 = "texte au pif"
    param3 = 20
    param4 = 15
    print('\nExo_01')
    who_and_old()
    print('\nExo_02')
    swap(param1, param2)
    print('\nExo_03')
    moyenne(param1, param3, param4)
    print('\nExo_04')
    my_sqrt()
