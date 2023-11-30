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

choice_str = 0
while choice_str == 0:
    choice_str = input("Votre choix : ")
    try:
        choice_int = int(choice_str)
        if choice_int < 1 or choice_int > 3:
            print("Vous devez choisir entre 1 et 3.")
            choice_str = 0
    except ValueError:
        print("ERREUR ! Vous devez entrer un nombre.")
        choice_str = 0

if choice_int == 1:
    # duration est en seconde
    duration = 180
    minutes = duration // 60
    secondes = duration - (minutes * 60)
    print(f"Cuisson de {minutes:02d}:{secondes:02d} en cours", end="")
    # print(f"{secondes:02d}")

    # print("Cuisson de 3 minutes en cours", end="")
    for i in range(2):
        time.sleep(1)
        print(".", end="", flush=True)

minutes = minutes - 1
secondes = secondes + 50

print()
print(f"Duree restante : {minutes:02d}:{secondes:02d}")
for i in range(2):
    time.sleep(1)
    print(".", end="", flush=True)


# Duree restant : 02:50
"""
for i in range(5):
    time.sleep(1)
    print(".", end="", flush=True)

print()
print("Fin de la cuisson")
beepy.beep(sound="ping")

# duration est en seconde
duration = 100
minutes = duration // 60
secondes = duration - (minutes*60)
print(f"{minutes:02d}")
print(secondes) """
