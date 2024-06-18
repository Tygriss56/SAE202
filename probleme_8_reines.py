import PySimpleGUI as sg
import math
import time



sg.theme('darkBrown6')


class Echiquier():
    """
    Constructeur de la classe Echiquier
    self.n : nombre de cases de côté de l'échiquier
    self.nbCases : nombre de cases de l'échiquier
    self.layout : un tableau d'images de cases noires ou blanches qui permettent l'affichage d'un échiquier
    """
    def __init__(self, n) -> None:
        self.n = n
        self.nbCases = n*n
        self.grille = []
        for i in range(n):
            self.grille.append([1]*n) #une grille de n*n 1. Le 1 signifie que la case n'est pas bloquée par une reine (0 indique le contraire)

        
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
    
    
    def afficher_grille(self):
        for i in range(self.n):
            print(self.grille[i])
    
    def retirerLigneColonne(self,l,c):
        """remplace les valeurs de la ligne et de la colonne de la case (l,c) par des 0"""
        
        for i in range(self.n):
            self.grille[i][c] = 0
            self.grille[l][i] = 0
            
    def retirer_diags(self, l, c):
        """remplace les valeurs des diagonales de la case (l,c) par des 0"""
        for i in range(self.n):
            for j in range(self.n):
                if (i - j == l - c or i+j == l+c):
                    self.grille[i][j] = 0
                    
    def ajouterLigneColonne(self,l,c):
        """remplace les valeurs de la ligne et de la colonne de la case (l,c) par des 0"""
        
        for i in range(self.n):
            self.grille[i][c] = 1
            self.grille[l][i] = 1
            
    def ajouter_diags(self, l, c):
        """remplace les valeurs des diagonales de la case (l,c) par des 0"""
        for i in range(self.n):
            for j in range(self.n):
                if (i - j == l - c or i+j == l+c):
                    self.grille[i][j] = 1
    
    
    
    def ajouteReine(self, window, ligne, colonne):
        """place une reine sur la case de coordonnées (ligne, colonne), et retire toutes les cases qu'elle couvre des cases possibles pour
        les autres reines"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n):
            # ------------------partie affichage------------------
            if((ligne+colonne)%2 == 0):
                window[(ligne, colonne)].update(filename='images/reine_case_blanche.png')
            else:
                window[(ligne, colonne)].update(filename='images/reine_case_noire.png')
            #-----------------------------------------------------
            self.retirer_diags(ligne, colonne)
            self.retirerLigneColonne(ligne, colonne)
        

    def supprimeReine(self, window, ligne, colonne):
        """supprime une reine sur la case de coordonnées (ligne, colonne),  et remet toutes les cases qu'elle couvre 
        des cases possibles pour les autres reines"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n):
            # ------------------partie affichage------------------
            if((ligne+colonne)%2 == 0):
                window[(ligne, colonne)].update(filename='images/case_blanche.png')
            else:
                window[(ligne, colonne)].update(filename='images/case_noire.png')
            #-----------------------------------------------------
            self.ajouter_diags(ligne, colonne)
            self.ajouterLigneColonne(ligne, colonne)

    def deplacerReine(self, window,  l_depart, c_depart, l_arrivee, c_arrivee):
        self.supprimeReine(window, l_depart, c_depart)
        self.ajouteReine(window, l_arrivee, c_arrivee)


def main(n):
    """programme principal"""
    e = Echiquier(n)
    window = sg.Window("reines", e.layout)
    i = -1 #sert pour l'exemple ci dessous
    
    #--------------pas touche--------------
    while True:
        event, value = window.read(timeout=500)
        if event == sg.WIN_CLOSED:
            break
    #--------------------------------------

        #exemple d'utilisation pour déplacer une reine
        if(i < e.n-1):
            #if(i > 0):
            #    e.supprimeReine(window, 4, i-1)
            #e.ajouteReine(window, 4, i)
            e.deplacerReine(window, i, 0, i+1, 0)
            i += 1
  


def test():
    e = Echiquier(8)
    e.afficher_grille() 
    e.retirer_diags(2, 2)
    print("\n")
    e.afficher_grille()



main(8)
