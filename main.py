import time
import beepy

# print("A")
# time.sleep(1)
# print("B")

print("""
        Bienvenue dans le Minuteur""")

print("""Quelle programme de cuisson desirez-vous effectuer ?
    1) Oeufs à la coque : 3 minutes
    2) Oeufs mollets : 6 minutes
    3) Oeufs durs : 9 minutes""")

# Boucle pour verifier la saisie utilisateur
while True:
    choice_string = input("Votre choix : ")
    if choice_string == "1" or choice_string == "2" or choice_string == "3":
        break
    print("ERREUR: Vous devez choisir 1, 2 ou 3\n")

duration = 0  # Dans les if ici, j'ai laisser le choix en chaine de caractere
if choice_string == "1":
    duration = 3 * 60  # Conversion de 3 minutes en secondes
if choice_string == "2":
    duration = 6 * 60
if choice_string == "3":
    duration = 9 * 60

# Création de la boucle qui affichera les points
while True:
    for i in range(10):
        time.sleep(1)  # Chaque 1 sec, afficher un point "." Le end="" enleve le retour a la ligne
        print(".", end="", flush=True)  # Le flush=True c'est pour forcer l'affichage des points sur la meme ligne
        duration -= 1
        if duration <= 0:
            break  # On sort de la boucle for ...

    if duration <= 0:
        break  # On sort de la boucle pour ne pas afficher temps restant = 00:00 et aussi pour pas avoir de tempsNegatif
    minutes = duration // 60  # Le double '//' c'est pour avoir une division entière et non un nombre a virgule
    secondes = duration - (minutes * 60)  # Pour avoir le nombre de sécondes
    print()
    print(f"Temps restant : {minutes:02d}:{secondes:02d}", end="", flush=True)

print("\nCuisson terminée")
beepy.beep(sound="ping")