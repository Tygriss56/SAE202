import PySimpleGUI as sg
import time

# Définir la mise en page de la fenêtre
layout = [
    [sg.Image(filename='images/case_blanche.png', key='-IMAGE-')]
]

# Créer la fenêtre
window = sg.Window('Alterner l\'affichage des images', layout)

# Liste des noms de fichiers d'images
image_files = ['images/case_blanche.png', 'images/case_noire.png']
current_image = 0

# Boucle pour alterner l'affichage des images
while True:
    event, values = window.read(timeout=1000)  # Mettre à jour toutes les 1 seconde
    if event == sg.WIN_CLOSED:
        break
    window['-IMAGE-'].update(filename=image_files[current_image])
    window.refresh()  # Rafraîchir l'affichage de la fenêtre
    time.sleep(1)  # Attendre 1 seconde
    current_image = (current_image + 1) % len(image_files)  # Passer à l'image suivante

# Fermer la fenêtre
window.close()