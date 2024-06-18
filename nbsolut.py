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
            self.grille.append([0]*n)
        
        # ------------------partie affichage------------------
        tab_images = []
        for l in range(self.n):
            tab_images.append([])
            for c in range(self.n):
                if((l+c)%2 == 0): #permet l'alternance entre une case blanche et une case noire
                    tab_images[l].append(sg.Image(filename="images/case_blanche.png", key=(l, c)))
                else:
                    tab_images[l].append(sg.Image(filename="images/case_noire.png", key=(l, c)))
        self.layout = [tab_images]
        # -----------------------------------------------------
    
    def afficher_grille(self):
        """Affiche la grille dans le terminal"""
        for i in range(self.n):
            print(self.grille[i])
        print(" ")
       
    def casePossible(self, l, c):
        """Renvoie True si il est possible de placer une reine sur la case de coordonnées (l,c), False sinon"""
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
               
    def ajouteReine(self, window, ligne, colonne):
        """Place une reine sur la case de coordonnées (ligne, colonne)"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n): #si coordonnées dans les bornes
            if((ligne+colonne)%2 == 0):
                window[(ligne, colonne)].update(filename='images/reine_case_blanche.png')
            else:
                window[(ligne, colonne)].update(filename='images/reine_case_noire.png')

    def supprimeReine(self, window, ligne, colonne):
        """Supprime une reine sur la case de coordonnées (ligne, colonne)"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n): #si coordonnées dans les bornes
            if((ligne+colonne)%2 == 0):
                window[(ligne, colonne)].update(filename='images/case_blanche.png')
            else:
                window[(ligne, colonne)].update(filename='images/case_noire.png')

def backtrackingGrille(e : Echiquier, l, lReine1 = None, solutions_set=None):
    if(l == lReine1):
        return backtrackingGrille(e, l+1, lReine1, solutions_set)
    
    if (l >= e.n):
        return 1  # Une solution trouvée
    
    count = 0  # Initialiser le compteur de solutions
    
    for c in range(e.n):
        if(e.casePossible(l, c)):
            e.grille[l][c] = 1
            
            # Récursivement chercher les solutions
            count += backtrackingGrille(e, l+1, lReine1, solutions_set)
            
            e.grille[l][c] = 0
    
    # Vérifier si la solution n'a pas déjà été trouvée
    solution_hash = hash(str(e.grille))
    if solutions_set is not None and solution_hash not in solutions_set:
        solutions_set.add(solution_hash)
        return count  # Retourner le nombre total de solutions
    else:
        return 0  # Solution déjà trouvée, ne pas compter

def resolutionTerminal(n, l, c):
    e = Echiquier(n)
    e.grille[l][c] = 1
    t1 = time.time()
    solutions_set = set()  # Ensemble pour stocker les solutions uniques
    solutions = backtrackingGrille(e, 0, l, solutions_set)
    e.afficher_grille()
    t2 = time.time()
    print("solution trouvée en", round(t2-t1, 10), "secondes")
    print("Nombre de solutions possibles avec la première reine donnée:", solutions)

def main():
    choix_valide = False
    while not choix_valide:
        print("veuillez choisir une action à effectuer")
        print("1 : voir la résolution du problème des n reines en temps réel")
        print("2 : voir le nombre de solutions pour un premier emplacement de reine donné")
        c = int(input())
        
        if(c == 1 or c == 2):
            choix_valide = True
        else:
            print("choix invalide")
    
    if c == 1:
        n = int(input("quelle sera la taille de l'échiquier (nombre de cases de côté)\n"))
        ligne = int(input(f"entrez la ligne où placer la première reine (entre 1 et {n})\n"))-1
        colonne = int(input(f"entrez la colonne où placer la première reine (entre 1 et {n})\n"))-1
        print()
        resolutionTerminal(n, ligne, colonne)
    else:
        n = int(input("quelle sera la taille de l'échiquier (nombre de cases de côté)\n"))
        ligne = int(input(f"entrez la ligne où placer la première reine (entre 1 et {n})\n"))-1
        colonne = int(input(f"entrez la colonne où placer la première reine (entre 1 et {n})\n"))-1
        print()
        
        e = Echiquier(n)
        e.grille[ligne][colonne] = 1
        t1 = time.time()
        solutions_set = set()  # Ensemble pour stocker les solutions uniques
        solutions = backtrackingGrille(e, 0, ligne, solutions_set)
        t2 = time.time()
        print("Nombre de solutions possibles avec la première reine donnée:", solutions)
        print("Temps d'exécution:", round(t2-t1, 10), "secondes")

main()

