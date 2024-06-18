import PySimpleGUI as sg
import math
import time



sg.theme('darkBrown6')


class Echiquier():
    def __init__(self, n) -> None:
        """
        Constructeur de la classe Echiquier
        self.n : nombre de cases de côté de l'échiquier
        self.grille : une grille 2d de n*n elements représentant l'échiquier (0 si la case est libre, 1 sinon)
        self.layout : un tableau d'images de cases noires ou blanches qui permettent l'affichage d'un échiquier        
        """
        
        self.n = n
        self.grille = []
        for i in range(n):
            self.grille.append([0]*n)   # une grille de n*n 1. Le 0 signifie que la case est libre, le 1 que la case est bloquée par une reine,
                                        # le 2 qu'il y a une reine sur la case

        
        # ------------------partie affichage------------------
        tab_images = []
        for l in range(self.n):
            tab_images.append([])
            for c in range(self.n):
                if((l+c)%2 == 0): #permet l'aternance entre une case blanche et une case noire
                    tab_images[l].append(sg.Image(filename="images/case_blanche.png", key=(l, c)))
                else:
                    tab_images[l].append(sg.Image(filename="images/case_noire.png", key=(l, c)))
        self.layout = [tab_images]
        # -----------------------------------------------------
    
    
    #------------ méthodes grille ------------
    
    def afficher_grille(self):
        """affiche la grille dans le terminal"""
        for i in range(self.n):
            print(self.grille[i])
        print(" ")
       
    def casePossible(self, l, c):
        """renvoie true si il est possible de placer une reine sur la case de coordonnées (l,c), false sinon"""
        if (1 in self.grille[l]):
            return False
        for ligne in self.grille:
            if(ligne[c] == 1):
                return False
        
        for i in range(self.n):
            for j in range(self.n):
                if(i+j == l+c or i-j == l-c):
                    if(self.grille[i][j] == 1):
                        return False
        return True
               
    #------------ méthodes affichage ------------
    
    def ajouteReine(self, window, ligne, colonne):
        """place une reine sur la case de coordonnées (ligne, colonne)"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n): #si coordonnées dans les bornes

            if((ligne+colonne)%2 == 0):
                window[(ligne, colonne)].update(filename='images/reine_case_blanche.png')
            else:
                window[(ligne, colonne)].update(filename='images/reine_case_noire.png')

    def supprimeReine(self, window, ligne, colonne):
        """supprime une reine sur la case de coordonnées (ligne, colonne)"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n): #si coordonnées dans les bornes
 
            if((ligne+colonne)%2 == 0):
                window[(ligne, colonne)].update(filename='images/case_blanche.png')
            else:
                window[(ligne, colonne)].update(filename='images/case_noire.png')
    #--------------------------------------------


def backtrackingGrille(e : Echiquier, l, lReine1 = None):
    """algorithme de backtracking """
    if(l == lReine1):
        return backtrackingGrille(e, l+1, lReine1)
    
    if (l >= e.n):
        return True
    else:
        for c in range(e.n):
            if(e.casePossible(l, c)):
                e.grille[l][c] = 1
                
                if(backtrackingGrille(e, l+1, lReine1)):
                    return True
                else:
                    e.grille[l][c] = 0
        return False


def backtrackingVisuel(window : sg.Window, e : Echiquier, l, lReine1 = None):
    event, value = window.read(timeout=10)
    e.afficher_grille
    if(l == lReine1):
        return backtrackingVisuel(window,e, l+1, lReine1)
    if (l >= e.n):
        return True
    else:
        
        for c in range(e.n):
            if(e.casePossible(l, c)):
                e.ajouteReine(window, l, c)
                e.grille[l][c] = 1
                
                if(backtrackingVisuel(window, e, l+1, lReine1)):
                    
                    return True
                else:
                    e.grille[l][c] = 0
                    e.supprimeReine(window, l, c)
        return False

def resolutionAvecVisuel(n, l, c):
    """résoud le problème des n reines avec la première reine placée sur la case (l,c)
    affiche la solution et le temps d'exécution si le booléen correspondant vaut True"""
    e = Echiquier(n)
    window = sg.Window("reines", e.layout)
    e.grille[l][c] = 1
    backtracking_done = False
    #--------------pas touche--------------
    while True:
        event, value = window.read(timeout=0)
        
        if event == sg.WIN_CLOSED:
            break
        #--------------------------------------
        
        if not backtracking_done:
            e.ajouteReine(window, l, c)
            backtrackingVisuel(window, e, 0, l)
            backtracking_done = True

def resolutionTerminal(n, l, c, afficheResultat = True):
    """résoud le problème des n reines avec la première reine placée sur la case (l,c)
    affiche la solution et le temps d'exécution si le booléen correspondant vaut True"""
    e = Echiquier(n)
    e.grille[l][c] = 1
    t1 = time.time()
    backtrackingGrille(e, 0, l)
    if (afficheResultat):
        e.afficher_grille()
        t2 = time.time()
        print("solution trouvée en",round(t2-t1, 10), "secondes")


def main():
    """permet à l'utilisateur de choisir la résolution visuelle étape par étape ou simplement la solution avec le temps d'exécution"""
    choix_valide = False
    while not choix_valide:
        print("veuillez choisir une action à effectuer")
        print("1 : voir la résolution du problème des n reines étape par étape")
        print("2 : voir la solution et connaître le temps d'exécution")
        c = int(input())
        
        if(c == 1 or c == 2):
            choix_valide = True
        else:
            print("choix invalide")
    
    n = int(input("quelle sera la taille de l'échiquier (nombre de cases de côté)\n"))
    
    ligne = int(input(f"entrez la ligne où placer la première reine (entre 1 et {n})\n"))-1
    colonne = int(input(f"entrez la colonne où placer la première reine (entre 1 et {n})\n"))-1
    print()
    
    if (c == 1):
        resolutionAvecVisuel(n, ligne, colonne)
    else:
        resolutionTerminal(n, ligne, colonne)

main()