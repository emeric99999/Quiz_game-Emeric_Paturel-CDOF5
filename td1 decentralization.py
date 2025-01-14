error = "La valeur entrée est incorrecte\n"
dicoFacile = {"allo ?" : ["oui ?", "non !", "feur...",1],"hello ?" : ["no","yes ?", "wut", 2 ]} 
dicoMoyen = {"hello ?" : ["no","yes ?", "wut", 2 ]}
dicoDifficile = {"hola ?" : ["nyet", "poyo", "si ?", 3]}

def ChooseDifficulty():
    choix = input("Choisissez la difficulté\n1 : Facile\n2 : Moyen\n3 : Difficile\n")
    SelectDico(choix)

def SelectDico(choix):
    
    if choix == "1":
        ReadQuestion(dicoFacile)
    elif choix == "2":
        ReadQuestion(dicoMoyen)
    elif choix == "3": 
        ReadQuestion(dicoDifficile)
    else : 
       print(error)
       ChooseDifficulty()

def ReadQuestion(dico):
    score = 0
    
    for question,reponse in dico.items():
        print(question +"\n1 : " + reponse[0] +"`\n2 : " + reponse[1] + "\n3 : " + reponse[2]+ "\n")
        answer = input()
        if answer == str(reponse[3]):
            print("Bonne réponse !")
            score += 1
        else :
            print("Mauvaise réponse !")
    print("Votre score est : ", score, "\n")
    retry = input("Voulez-vous réessayer ?\n1 : Oui\n2 : Non")
    if retry == "1":
        ChooseDifficulty
    else : 
        print("Au revoir !")

ChooseDifficulty()