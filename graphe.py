# grille = [[0]*8]*8
# grilleTest = [[1]*8]*8
N = 8
grille = [[0 for i in range(N)] for j in range(N)]
def retirerLigneColonne(grille,x,y):
    for i in range(len(grille)):
        for j in range(len(grille)):
            if i == x and j == y:
                grille[i][j] = 0#met toutes la ligne colonne à zéro
    return grille

def retirerDiag(grille,x,y):
    for i in range(len(grille)):
        for j in range(len(grille)):
            if (i == x and j == y) and i == j:
                grille[i][j] = 0#met toute la diagonole à 0
    return grille

def placeAletoire(grille):
    estPlace = False
    boucleX = 0
    boucleY  = 0
    while(estPlace == False and (boucleX < N or boucleY < N)):
        if possible(grille,(boucleY,boucleX)) == True:
            grille[boucleY][boucleX] = 1
            estPlace = True
            coordonnees = (boucleX,boucleY)
        else:
            boucleY += 1
            boucleX += 1
    return grille,coordonnees

def possible(grille,case):
    (X,Y) = case
    boucleL = X
    boucleC = Y
    estPossible = True
    while(estPossible == True and boucleC< N):
        while(estPossible == True and boucleL < N):
            if grille[boucleC][boucleL] == 1:
                estPossible = False
            boucleL += 1
        boucleC += 1

    numBlocC = X*N/N
    numBlocL = Y*N/N
    while (estPossible == True and numBlocC < N):
        while (estPossible == True and numBlocL < N):
            if grille[boucleC][boucleL] == 1:
                estPossible = False
            boucleL += 1
        boucleC += 1
    return estPossible

def backTracking(grille,numCase):
    estPossible = False
    if numCase == N*N:
        estPossible = True
    else:
        ligne = numCase/N
        colonne = numCase/N
        if grille[ligne][colonne] == 1:
            resultat = backTracking(grille,numCase+1)
        else:
            for i in range(len(grille)):
                if possible(grille(numCase)) == False:
                    grille[ligne][colonne] = 1
                if backTracking(grille,numCase+1) == True:
                    estPossible = True
                else:
                    grille[ligne][colonne] = 0
    return estPossible

print(grille)
placeAletoire(grille)
placeAletoire(grille)
print(grille)

class caseSommet():
    def __init__(self) -> None:
        self.valeurCase = 0
        self.dispo = True

    def estDispo(self):
        return self.dispo
    
    def valeur(self):
        return self.valeur

    def changeDispo(self,newDispo):
        self.dispo = newDispo

    def changeValeur(self,newValeur):
        self.valeurCase = newValeur

    def afficheCase(self):
        print("La case à pour valeur",self.valeur)
        if self.estDispo == True:
            print("La case est dispo")
        else:
            print("La case est occupée")

class Jeu(caseSommet):
    def __init__(self,tailleJeu) -> None:
        super().__init__()
        self.taille = tailleJeu
        self.nbCases = tailleJeu*tailleJeu
        self.grille = [[caseSommet.changeDispo(self,True) for i in range(tailleJeu)]for j in range(tailleJeu)]
        self.tabReines = []
        

    def afficher_grille(self):
        """affiche la grille dans le terminal"""
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j].afficheCase()
    
    def retirerLigneColonne(self,l,c):
        """remplace les valeurs de la ligne et de la colonne de la case (l,c) par des 0"""
        for i in range(self.n):
            self.grille[i][c].changeValeur(self.grille[l][c],1)
            self.grille[l][i].changeValeur(self.grille[l][c],1)
        self.grille[l][c].changeValeur(self.grille[l][c],2)
     
    def retirer_diags(self, l, c):
        """remplace les valeurs des diagonales de la case (l,c) par des 0"""
        for i in range(self.n):
            for j in range(self.n):
                if (i - j == l - c or i+j == l+c):
                    self.grille[i][j].changeValeur(self.grille[l][c],1)
        self.grille[l][c] = 2
    
    def ajouterLigneColonne(self,l,c):
        """remplace les valeurs de la ligne et de la colonne de la case (l,c) par des 0"""
        for i in range(self.n):
            self.grille[i][c].changeValeur(self.grille[l][c],0)
            self.grille[l][i].changeValeur(self.grille[l][c],0)
            
    def ajouter_diags(self, l, c):
        """remplace les valeurs des diagonales de la case (l,c) par des 0"""
        for i in range(self.n):
            for j in range(self.n):
                if (i - j == l - c or i+j == l+c):
                    self.grille[i][j].changeValeur(self.grille[l][c],0)
    
    def caseLibre(self):
        """renvoie les coordonnées de la 1ere case libre de la grille, (-1,-1) si il n'y a pas de case libre"""
        l = 0
        print(self.n)
        while l < self.n:
            c = 0
            while c < self.n:
                if self.grille[l][c].valeurCase == 0:
                    return (l, c)
                c = c + 1
            l = l + 1
        return (-1, -1)
    
    
    def ajouteReineGrille(self, ligne, colonne):
        """place une reine sur la case de coordonnées (ligne, colonne), et retire toutes les cases qu'elle couvre des cases possibles pour
        les autres reines (sans l'affichage)"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n):
            self.retirer_diags(ligne, colonne)
            self.retirerLigneColonne(ligne, colonne)
        self.grille[ligne][colonne] = 2
        

    def supprimeReineGrille(self, window, ligne, colonne):
        """supprime une reine sur la case de coordonnées (ligne, colonne),  et remet toutes les cases qu'elle couvre 
        des cases possibles pour les autres reines (sans l'affichage)"""
        if (ligne >= 0 and colonne >= 0 and ligne < self.n and colonne < self.n):
            self.ajouter_diags(ligne, colonne)
            self.ajouterLigneColonne(ligne, colonne)

    def deplacerReineGrille(self, window,  l_depart, c_depart, l_arrivee, c_arrivee):
        self.supprimeReineGrille(l_depart, c_depart)
        self.ajouteReineGrille(l_arrivee, c_arrivee)
    
    
    #------------ méthodes reines ------------
    def cosCaseSuivante(self,X,Y):
        """Donne la prochaine case disponible peut importe"""
        boucleC = X
        boucleL = Y
        estTrouvee = False
        #
        while(boucleC < len(self.grille) and estTrouvee == False):
            while (boucleL < len(self.grille) and estTrouvee == False):
                if boucleC == X and boucleL == Y:
                    if(self.grille[boucleC][boucleL]) == 0:
                        coordonnes = (boucleC,boucleL)
                        estTrouvee = True
                boucleL
            boucleC
        if (coordonnes) != (-1,-1):
            coordonnes = (boucleC,boucleL)
        else:
            coordonnes = (-1,1)
        return coordonnes

