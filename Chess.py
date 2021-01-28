class echec():
    def __init__(self):
        self.board = [
            [T1N, C1N, F1N, DameN, RoiN, F2N, C2N, T2N],
            [P1N, P2N, P3N, P4N, P5N, P6N, P7N, P8N],
            [Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" ")],
            [Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" ")],
            [Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" ")],
            [Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" "), Case(" ")],
            [P1B, P2B, P3B, P4B, P5B, P6B, P7B, P8B],
            [T1B, C1B, F1B, DameB, RoiB, F2B, C2B, T2B]]
        self.posHori = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.posVert = {1 : 7, 2 : 6, 3 : 5, 4 : 4, 5 : 3, 6 : 2, 7 : 1, 8 : 0}
        self.poslettre = {1 : "A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}
        self.Danger_RoiN = False
        self.Danger_RoiB = False

    def print_board(self):
        print("   A B C D E F G H")
        num_ligne = 8
        for row in self.board:
            tmp = str(num_ligne) + ' |'
            for case in row:
                tmp = tmp + case.display() + " "
            print(tmp)
            num_ligne = num_ligne - 1
    
    def get_X(self, coord):
        colonne = coord
        colonne = colonne.upper()
        abscisse = self.posHori[colonne]
        return abscisse
    
    def get_Y(self, coord):
        ligne = coord
        ordonnee = int(ligne.upper())
        ordonnee = self.posVert[ordonnee]
        return ordonnee
    
    def jouer(self):
        try:
            self.Jeu = True
            while self.Jeu is True :
                self.Check()
                if self.joueur == 1 :
                    while self.joueur == 1:
                        self.jeuB()
                        self.fin_tour()
                elif self.joueur == 2 :
                    while self.joueur == 2:
                        self.jeuN()
                        self.fin_tour()
        except ValueError:
            print("\nEntrez des coordonnées valides (Exemple : B6)\n")
        except IndexError:
            print("\nEntrez des coordonnées valides (Exemple : B6)\n")
        except KeyError:
            print("\nEntrez des coordonnées valides (Exemple : B6)\n")
    
    def jeuB(self):
        RoiB.roque_B()
        RoiB.play_roqueB()
        if RoiB.playroqueB is False :
            choi = input("\nJoueur" + str(self.joueur) + ", quelle Pièce voulez vous bouger ? (Exemple : B2)\n")
            choi = list(choi)
            self.x = self.get_X(choi[0])
            self.y = self.get_Y(choi[1])
            if self.board[self.y][self.x].couleur == "blanc" :
                self.board[self.y][self.x].nouvpossible()
                self.board[self.y][self.x].move()
                self.print_board()
            else :
                print("\nJouez une piece valide (Pièce blanche)\n")
        else:
            self.print_board()
            self.joueur = 2
    
    def jeuN(self):
        RoiN.roque_N()
        RoiN.play_roqueN()
        if RoiN.playroqueN is False :
            choi = input("\nJoueur" + str(self.joueur) + ", quelle Pièce voulez vous bouger ? (Exemple : B7)\n")
            choi = list(choi)
            self.x = self.get_X(choi[0])
            self.y = self.get_Y(choi[1])
            if self.board[self.y][self.x].couleur == "noir" :
                self.board[self.y][self.x].nouvpossible()
                self.board[self.y][self.x].move()
                self.print_board()
            else:
                print("\nJouez une pièce valide (Pièce noire)\n")
        else : 
            self.print_board()
            self.joueur = 1

#___________________________________________________________________________________________________________________________
#
#
#                                                    Victoire
#
#___________________________________________________________________________________________________________________________


    def Check(self): 
        toutes_possB = T1B.possible + T2B.possible + C1B.possible + C2B.possible + F1B.possible + F2B.possible
        toutes_possN = T1N.possible + T2N.possible + C1N.possible + C2N.possible + F1N.possible + F2N.possible
        if self.joueur == 1:
            if self.Danger_RoiB == False :
                if RoiB.pos in T1N.possible:              
                    print("\nVotre Roi Noir et dans l'axe d'une Pièce ennemie\n")
                    self.Danger_RoiB = True
                    self.kill_KB()
        elif self.joueur == 2:
            if game.Danger_RoiN == False :
                if RoiN.pos in F2B.possible :
                    print("\nVotre Roi Blanc et dans l'axe d'une Pièce ennemie\n")
                    self.Danger_RoiN = True
                    self.kill_KB()
        else : 
            pass
    
    def kill_KB(self):
        F2B.tester(RoiN.x, RoiN.y)
        if F2B.destination is True :
           print("Votre roi va être mangé par la tour blanche")

    def gagne(self):
        roi = 0
        for ligne in range(8):
            for case in range(8):
                if isinstance(self.board[ligne][case], roiB) or isinstance(self.board[ligne][case], roiN):
                    roi = roi + 1
        if roi == 1:
            for ligne in range(8):
                for case in range(8):
                    if isinstance(self.board[ligne][case], roiB):
                        print("\nLes Blancs ont gagné\n")
                        exit()
                        
                
                    elif isinstance(self.board[ligne][case], roiN):
                        print ("\nLes Noirs ont gagné\n")
                        exit()
    
    def fin_tour(self):
        self.Check()
        self.gagne()

class Piece():
    def __init__(self, equipe, lettre, y1, x1, couleur):
        self.equipe = equipe
        self.lettre = str(lettre)
        self.couleur = str(couleur)
        self.coup = 0
        self.x = x1
        self.y = y1
        self.pos = [self.x, self.y]

    def display(self):
        if self.equipe:
            return self.lettre
        else:
            return self.lettre.upper()

#___________________________________________________________________________________________________________________________
#
#
#                                            Mouvements d'une pièce choisie
#
#___________________________________________________________________________________________________________________________
    
    def move(self):
        self.coord = input("\nOù voulez vous bouger ?\n Si vous passsez à travers une Piece, cela ne fonctionnera pas\n")
        self.coord = list(self.coord)
        self.abscisse = game.get_X(self.coord[0])
        self.ordonnee = game.get_Y(self.coord[1])
        self.tester(self.abscisse, self.ordonnee)
        if self.destination == True :
            self.absc = self.abscisse + 1
            self.pos = [int(self.absc), int(self.coord[1])]
            if self.pos in self.possible or self.pos == self.possible:
                if game.board[self.ordonnee][self.abscisse].couleur == game.board[game.y][game.x].couleur:
                    print("\nVous ne pouvez pas jouer sur vos pions\n")
                else:
                    self.pos[0] = game.poslettre[self.pos[0]]
                    print(f"\nVous jouez en " + str(self.pos) + "\n")
                    game.board[self.ordonnee][self.abscisse] = game.board[game.y][game.x]
                    game.board[game.y][game.x] = Case(" ")
                    self.x = int(self.absc)
                    self.y = int(self.coord[1])
                    self.coup = 1
                    self.Promo()
                    self.GetKP()
                    if game.joueur == 1:
                        game.joueur = 2
                    elif game.joueur == 2:
                        game.joueur = 1
            else : 
                print("\nVous ne pouvez pas jouer ici\n")
        else:
            print("\nVous ne pouvez pas sauter des pièces\n")
        
    def GetKP(self):
        if game.board[self.ordonnee][self.abscisse] == RoiN:
            self.pos = [self.x, self.y]
            
        elif game.board[self.ordonnee][self.abscisse] == RoiB:
            self.pos = [self.x, self.y]
        else:
            pass

#___________________________________________________________________________________________________________________________
#
#
#                                       Tester si la pièce ne traverse pas d'objet
#
#___________________________________________________________________________________________________________________________
    
    def tester(self, x, y) :
        self.ordonnee = y
        self.abscisse = x
        self.destination = True
        if isinstance(game.board[game.y][game.x], Cavalier) :
            pass
        elif game.y > self.ordonnee :                                              #Si on veut aller vers le haut
            espace = game.y - self.ordonnee
            if game.x > self.abscisse:                                           #en haut à gauche
                for i in range (1, espace):
                    if isinstance(game.board[game.y - i][game.x - i], Piece):
                        self.destination = False
            elif game.x < self.abscisse :                                        #en haut a droite
                for i in range (1, espace):
                        if isinstance(game.board[game.y - i][game.x + i], Piece):
                            self.destination = False
            else :                                                               #en haut
                for i in range (1, espace) :
                    if isinstance(game.board[game.y-i][game.x], Piece) :
                        self.destination = False
                    else :
                        pass
        elif game.y < self.ordonnee :                                            #Si on veut aller vers le bas
            espace = self.ordonnee - game.y
            if game.x > self.abscisse:                                           #en bas à gauche
                for i in range (1, espace):
                    if isinstance(game.board[game.y + i][game.x - i], Piece):
                        self.destination = False
            elif game.x < self.abscisse :                                        #en haut a droite
                for i in range (1, espace):
                        if isinstance(game.board[game.y + i][game.x + i], Piece):
                            self.destination = False
            else :                                                               #en haut
                for i in range (1, espace) :
                    if isinstance(game.board[game.y+i][game.x], Piece) :
                        self.destination = False
                    else :
                        pass
        elif game.y == self.ordonnee :
            if game.x > self.abscisse:
                espace = game.x - self.abscisse
                for i in range (1, espace) :
                    if isinstance(game.board[game.y][game.x-i], Piece) :
                        self.destination = False
            elif self.abscisse > game.x:
                espace = self.abscisse - game.x
                for i in range(1, espace):
                    if isinstance(game.board[game.y][game.x+i], Piece) :
                        self.destination = False
        return self.destination

#___________________________________________________________________________________________________________________________
#
#
#                                                Promotion du pion
#
#___________________________________________________________________________________________________________________________
    
    def Promo(self):
        for i in range(0, 7):
            if isinstance(game.board[0][i], Pion) and game.board[0][i].couleur == "blanc" :
                promo = input("Votre Pion blanc en " + str(self.pos)+ " a droit à une promotion\n 1 - Tour\n 2 - Fou\n 3 - Cavalier\n 4 - Dame\n")
                if promo == "1" :
                    game.board[0][i] = Tour(False, "t", 8, i+1, "blanc")
                    print("Promotion en Tour")
                elif promo == "2":
                    game.board[0][i] = Fou(False, "f", 8, i+1, "blanc")
                    print("Promotion en Fou")
                elif promo == "3":
                    game.board[0][i] = Cavalier(False, "c", 8, i+1, "blanc")
                    print("Promotion en Cavalier")
                elif promo == "4":    
                    game.board[0][i] = Dame(False, "d", 8, i+1, "blanc")
                    print("Promotion en Dame")

            elif isinstance(game.board[7][i], Pion) and game.board[0][i].couleur == "noir" :
                promo = input("Votre Pion blanc en " + str(self.pos)+ " a droit à une promotion\n 1 - Tour\n 2 - Fou\n 3 - Cavalier\n 4 - Dame\n")
                if promo == "1" :
                    game.board[7][i] = Tour(True, "t", 1, i+1, "noir")
                    print("Promotion en Tour")
                elif promo == "2":
                    game.board[7][i] = Fou(True, "f", 1, i+1, "noir")
                    print("Promotion en Fou")
                elif promo == "3":
                    game.board[7][i] = Cavalier(True, "c", 1, i+1, "noir")
                    print("Promotion en Cavalier")
                elif promo == "4":    
                    game.board[7][i] = Dame(True, "d", 1, i+1, "noir")
                    print("Promotion en Dame")

#___________________________________________________________________________________________________________________________
#
#
#                                                Grand et Petit Roque
#
#___________________________________________________________________________________________________________________________
    
    def roque_B(self):
        RoiB.petit_roqueB = None
        RoiB.grand_roqueB = None
        if RoiB.coup == 0 and T2B.coup == 0 and T1B.coup == 0:
            if isinstance(game.board[7][5], Case) and isinstance(game.board[7][6], Case) and isinstance(game.board[7][1], Case) and isinstance(game.board[7][2], Case) and isinstance(game.board[7][3], Case):
                print("\nVous pouvez faire le Grand et le Petit roque\n")
                RoiB.petit_roqueB = True
                RoiB.grand_roqueB = True
                return RoiB.petit_roqueB
            elif isinstance(game.board[7][5], Case) and isinstance(game.board[7][6], Case):
                print("\nVous pouvez faire le petit roque\n")
                RoiB.petit_roqueB = True
                return RoiB.petit_roqueB
            elif isinstance(game.board[7][1], Case) and isinstance(game.board[7][2], Case) and isinstance(game.board[7][3], Case):
                print("\nVous pouvez faire le grand roque\n")
                RoiB.grand_roqueB = True
                return RoiB.grand_roqueB
        elif RoiB.coup == 0 and T2B.coup == 0 :
            if isinstance(game.board[7][5], Case) and isinstance(game.board[7][6], Case):
                print("\nVous pouvez faire le petit roque\n")
                RoiB.petit_roqueB = True
                return RoiB.petit_roqueB
        elif RoiB.coup == 0 and T1B.coup == 0 :
            if isinstance(game.board[7][1], Case) and isinstance(game.board[7][2], Case) and isinstance(game.board[7][3], Case):
                print("\nVous pouvez faire le grand roque\n")
                RoiB.grand_roqueB = True
                return RoiB.grand_roqueB
    
    def roque_N(self):
        RoiN.petit_roqueN = None
        RoiN.grand_roqueN = None
        if RoiN.coup == 0 and T2N.coup == 0 and T1N.coup == 0:
            if isinstance(game.board[0][5], Case) and isinstance(game.board[0][6], Case) and isinstance(game.board[0][1], Case) and isinstance(game.board[0][2], Case) and isinstance(game.board[0][3], Case):
                print("\nVous pouvez faire le Grand et le Petit roque\n")
                RoiN.petit_roqueN = True
                RoiN.grand_roqueN = True
                return RoiN.petit_roqueN
            elif isinstance(game.board[0][5], Case) and isinstance(game.board[0][6], Case):
                print("\nVous pouvez faire le petit roque\n")
                RoiN.petit_roqueN = True
                return RoiN.petit_roqueN
            elif isinstance(game.board[0][1], Case) and isinstance(game.board[0][2], Case) and isinstance(game.board[0][3], Case):
                print("\nVous pouvez faire le grand roque\n")
                RoiN.grand_roqueN = True
                return RoiN.grand_roqueN
        elif RoiN.coup == 0 and T2N.coup == 0 :
            if isinstance(game.board[0][5], Case) and isinstance(game.board[0][6], Case):
                print("\nVous pouvez faire le petit roque\n")
                RoiN.petit_roqueN = True
                return RoiN.petit_roqueN
        elif RoiN.coup == 0 and T1N.coup == 0 :
            if isinstance(game.board[0][1], Case) and isinstance(game.board[0][2], Case) and isinstance(game.board[0][3], Case):
                print("\nVous pouvez faire le grand roque\n")
                RoiN.grand_roqueN = True
                return RoiN.grand_roqueN
    
    def play_roqueB(self):
        if RoiB.petit_roqueB is True and RoiB.grand_roqueB is True : 
            rep = input("\nTapez 'p' pour jouer le Petit Roque\nTapez 'g' pour jouer le Grand Roque\nAutre pour jouer une pièce")
            if rep == "p" or rep == "P" :
                self.Play_Petit_RoqueB()
            elif rep == "g" or rep == "G" :
                self.Play_Grand_RoqueB()
            else : 
                self.playroqueB = False
                return self.playroqueB
        elif RoiB.petit_roqueB is True : 
            rep = input("\nTapez 'p' pour jouer le Petit Roque / Autre pour jouer une pièce\n")
            if rep == "p" or rep == "P":
                self.Play_Petit_RoqueB()
            else : 
                self.playroqueB = False
                return self.playroqueB
        elif RoiB.grand_roqueB is True :
            rep = input("\nTapez 'g' pour jouer le Grand Roque / Autre pour jouer une pièce\n")
            if rep == "g" or rep == "G":
                self.Play_Grand_RoqueB()
            else :
                self.playroqueB = False
                return self.playroqueB
        else:
            self.playroqueB = False
            return self.playroqueB
    
    def play_roqueN(self):
        if RoiN.petit_roqueN is True and RoiN.grand_roqueN is True : 
            rep = input("\nTapez 'p' pour jouer le Petit Roque\nTapez 'g' pour jouer le Grand Roque\n Autre pour jouer une pièce\n")
            if rep == "p" or rep == "P" :
                self.Play_Petit_RoqueN()
            elif rep == "g" or rep == "G" :
                self.Play_Grand_RoqueN()
            else : 
                self.playroqueN = False
                return self.playroqueN
        elif RoiN.petit_roqueN is True : 
            rep = input("\nTapez 'p' pour jouer le Petit Roque\n Autre pour jouer une pièce\n")
            if rep == "p" or rep == "P":
                self.Play_Petit_RoqueN()
            else : 
                self.playroqueN = False
                return self.playroqueN
        elif RoiN.grand_roqueN is True :
            rep = input("\nTapez 'g' pour jouer le Grand Roque\n Autre pour jouer une pièce\n")
            if rep == "g" or rep == "G":
                self.Play_Grand_RoqueN()
            else :
                self.playroqueN = False
                return self.playroqueN
        else:
            self.playroqueN = False
            return self.playroqueN

    def Play_Petit_RoqueB(self):
        game.board[7][6] = roiB(False, "r", 1, 7, "blanc")
        RoiB.x = 7
        RoiB.y = 1
        game.board[7][4] = Case(" ")
        game.board[7][5] = Tour(False, "t", 1, 6, "blanc")
        T2B.x = 6
        T2B.y = 1
        game.board[7][7] = Case(" ")
        RoiB.coup = 1
        T2B.coup = 1
        self.playroqueB = True

    def Play_Petit_RoqueN(self):
        game.board[0][6] = roiN(True, "r", 8, 7, "noir")
        RoiN.x = 7
        RoiN.y = 8
        game.board[0][4] = Case(" ")
        game.board[0][5] = Tour(True, "t", 8, 6, "noir")
        T2N.x = 6
        T2N.y = 8
        game.board[0][7] = Case(" ")
        RoiN.coup = 1
        T2N.coup = 1
        self.playroqueN = True
    
    def Play_Grand_RoqueB(self):
        game.board[7][2] = roiB(False, "r", 1, 3, "blanc")
        RoiB.x = 3
        RoiB.y = 1
        game.board[7][4] = Case(" ")
        game.board[7][3] = Tour(False, "t", 1, 4, "blanc")
        T1B.x = 4
        T1B.y = 1
        game.board[7][0] = Case(" ")
        RoiB.coup = 1
        T1B.coup = 1
        self.playroqueB = True
    
    def Play_Grand_RoqueN(self):
        game.board[0][2] = roiB(True, "r", 8, 3, "noir")
        RoiN.x = 3
        RoiN.y = 8
        game.board[0][4] = Case(" ")
        game.board[0][3] = Tour(True, "t", 8, 4, "noir")
        T1N.x = 4
        T1N.y = 8
        game.board[0][0] = Case(" ")
        RoiN.coup = 1
        T1N.coup = 1
        self.playroqueN = True

class Pion(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x, self.y+1]

#___________________________________________________________________________________________________________________________
#
#
#                                              Mouvements des pions
#
#___________________________________________________________________________________________________________________________
    
    def nouvpossible(self):
        if self.couleur == "blanc" :
            if self.coup == 0 :
                if game.x == 7 :
                    if isinstance(game.board[game.y-1][game.x-1], Case) is False:
                        if isinstance(game.board[game.y-1][game.x], Case) is False:
                            self.possible = [self.x-1, self.y+1]
                        else:
                            self.possible =  [self.x, self.y+1], [self.x-1, self.y+1]
                    elif isinstance(game.board[game.y-1][game.x], Case) is False:
                        self.possible = []
                    else:
                        self.possible = [self.x, self.y+1], [self.x, self.y+2]
                
                elif isinstance(game.board[game.y-1][game.x+1], Case) is False :
                    if isinstance(game.board[game.y-1][game.x-1], Case) is False:
                        if isinstance(game.board[game.y-1][game.x], Case) is False:
                            self.possible = [self.x+1, self.y+1], [self.x-1, self.y+1]
                        else:
                            self.possible = [self.x+1, self.y+1], [self.x, self.y+1], [self.x-1, self.y+1], [self.x, self.y+2]

                    elif isinstance(game.board[game.y-1][game.x], Case) is False:
                        self.possible = [self.x+1, self.y+1]
                    else : 
                        self.possible = [self.x+1, self.y+1], [self.x, self.y+1], [self.x, self.y+2]

                elif isinstance(game.board[game.y-1][game.x-1], Case) is False:
                    if isinstance(game.board[game.y-1][game.x], Case) is False:
                        self.possible = [self.x-1, self.y+1]
                    else:
                        self.possible = [self.x-1, self.y+1], [self.x, self.y+1], [self.x, self.y+2]

                elif isinstance(game.board[game.y-1][game.x], Case) is False:
                    self.possible = []
                else : 
                    self.possible = [self.x, self.y+1], [self.x, self.y+2]
            
            elif game.x == 7 :
                if isinstance(game.board[game.y-1][game.x-1], Case) is False:
                    if isinstance(game.board[game.y-1][game.x], Case) is False:
                        self.possible = [self.x-1, self.y+1]
                    else:
                        self.possible =  [self.x, self.y+1], [self.x-1, self.y+1]
                elif isinstance(game.board[game.y-1][game.x], Case) is False:
                    self.possible = []
                else:
                    self.possible = [self.x, self.y+1]
            
            elif isinstance(game.board[game.y-1][game.x+1], Case) is False :
                if isinstance(game.board[game.y-1][game.x-1], Case) is False:
                    if isinstance(game.board[game.y-1][game.x], Case) is False:
                        self.possible = [self.x+1, self.y+1], [self.x-1, self.y+1]
                    else:
                        self.possible = [self.x+1, self.y+1], [self.x, self.y+1], [self.x-1, self.y+1]

                elif isinstance(game.board[game.y-1][game.x], Case) is False:
                    self.possible = [self.x+1, self.y+1]
                else : 
                    self.possible = [self.x+1, self.y+1], [self.x, self.y+1]

            elif isinstance(game.board[game.y-1][game.x-1], Case) is False:
                if isinstance(game.board[game.y-1][game.x], Case) is False:
                    self.possible = [self.x-1, self.y+1]
                else:
                    self.possible = [self.x-1, self.y+1], [self.x, self.y+1]

            elif isinstance(game.board[game.y-1][game.x], Case) is False:
                self.possible = []
            else : 
                self.possible = [self.x, self.y+1]

        elif self.couleur == "noir":
            if self.coup == 0 :
                if game.x == 7 :
                    if isinstance(game.board[game.y+1][game.x-1], Case) is False:
                        if isinstance(game.board[game.y+1][game.x], Case) is False:
                            self.possible = [self.x-1, self.y-1]
                        else:
                            self.possible =  [self.x, self.y-1], [self.x-1, self.y-1], [self.x, self.y-2]
                    elif isinstance(game.board[game.y+1][game.x], Case) is False:
                        self.possible = []
                    else:
                        self.possible = [self.x, self.y-1], [self.x, self.y-2]

                elif isinstance(game.board[game.y+1][game.x+1], Case) is False :
                    if isinstance(game.board[game.y+1][game.x-1], Case) is False:
                        if isinstance(game.board[game.y+1][game.x], Case) is False:
                            self.possible = [self.x+1, self.y-1], [self.x-1, self.y-1]
                        else:
                            self.possible = [self.x+1, self.y-1], [self.x, self.y-1], [self.x-1, self.y-1], [self.x, self.y-2]

                    elif isinstance(game.board[game.y+1][game.x], Case) is False:
                        self.possible = [self.x-1, self.y-1]
                    else : 
                        self.possible = [self.x+1, self.y-1], [self.x, self.y-1], [self.x, self.y-2]

                elif isinstance(game.board[game.y+1][game.x-1], Case) is False:
                    if isinstance(game.board[game.y+1][game.x], Case) is False:
                        self.possible = [self.x-1, self.y-1]
                    else:
                        self.possible = [self.x-1, self.y-1], [self.x, self.y-1], [self.x, self.y-2]

                elif isinstance(game.board[game.y+1][game.x], Case) is False:
                    self.possible = []
                else : 
                    self.possible = [self.x, self.y-1], [self.x, self.y-2]
            
            elif game.x == 7 :
                if isinstance(game.board[game.y+1][game.x-1], Case) is False:
                    if isinstance(game.board[game.y+1][game.x], Case) is False:
                        self.possible = [self.x-1, self.y-1]
                    else:
                        self.possible =  [self.x, self.y-1], [self.x-1, self.y-1]
                elif isinstance(game.board[game.y+1][game.x], Case) is False:
                    self.possible = []
                else:
                    self.possible = [self.x, self.y-1]

            elif isinstance(game.board[game.y+1][game.x+1], Case) is False :
                if isinstance(game.board[game.y+1][game.x-1], Case) is False:
                    if isinstance(game.board[game.y+1][game.x], Case) is False:
                        self.possible = [self.x+1, self.y-1], [self.x-1, self.y-1]
                    else:
                        self.possible = [self.x+1, self.y-1], [self.x, self.y-1], [self.x-1, self.y-1]

                elif isinstance(game.board[game.y+1][game.x], Case) is False:
                    self.possible = [self.x-1, self.y-1]
                else : 
                    self.possible = [self.x+1, self.y-1], [self.x, self.y-1]

            elif isinstance(game.board[game.y+1][game.x-1], Case) is False:
                if isinstance(game.board[game.y+1][game.x], Case) is False:
                    self.possible = [self.x-1, self.y-1]
                else:
                    self.possible = [self.x-1, self.y-1], [self.x, self.y-1]

            elif isinstance(game.board[game.y+1][game.x], Case) is False:
                self.possible = []
            else : 
                self.possible = [self.x, self.y-1]
    
#___________________________________________________________________________________________________________________________
#
#
#                                             Initialisation des pièces
#
#___________________________________________________________________________________________________________________________

class Tour(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x+1, self.y], [self.x+2, self.y], [self.x+3, self.y], [self.x+4, self.y], [self.x+5, self.y], [self.x+6, self.y], [self.x+7, self.y], [self.x-1, self.y], [self.x-2, self.y], [self.x-3, self.y], [self.x-4, self.y], [self.x-5, self.y], [self.x-6, self.y], [self.x-7, self.y], [self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3], [self.x, self.y+4], [self.x, self.y+5], [self.x, self.y+6], [self.x, self.y+7], [self.x, self.y-1], [self.x, self.y-2], [self.x, self.y-3], [self.x, self.y-4], [self.x, self.y-5], [self.x, self.y-6], [self.x, self.y-7]

    def nouvpossible(self):
        self.possible = [self.x+1, self.y], [self.x+2, self.y], [self.x+3, self.y], [self.x+4, self.y], [self.x+5, self.y], [self.x+6, self.y], [self.x+7, self.y], [self.x-1, self.y], [self.x-2, self.y], [self.x-3, self.y], [self.x-4, self.y], [self.x-5, self.y], [self.x-6, self.y], [self.x-7, self.y], [self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3], [self.x, self.y+4], [self.x, self.y+5], [self.x, self.y+6], [self.x, self.y+7], [self.x, self.y-1], [self.x, self.y-2], [self.x, self.y-3], [self.x, self.y-4], [self.x, self.y-5], [self.x, self.y-6], [self.x, self.y-7]

class Cavalier(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x+1, self.y-2], [self.x-1, self.y-2], [self.x+2, self.y-1], [self.x+2, self.y+1], [self.x-2, self.y-1], [self.x-2, self.y+1], [self.x+1, self.y+2], [self.x-1, self.y+2]

    def nouvpossible(self):
        self.possible = [self.x+1, self.y-2], [self.x-1, self.y-2], [self.x+2, self.y-1], [self.x+2, self.y+1], [self.x-2, self.y-1], [self.x-2, self.y+1], [self.x+1, self.y+2], [self.x-1, self.y+2]
        
class Fou(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x+1, self.y-1], [self.x+2, self.y-2], [self.x+3, self.y-3], [self.x+4, self.y-4], [self.x+5, self.y-5], [self.x+6, self.y-6], [self.x+7, self.y-7], [self.x-1, self.y-1], [self.x-2, self.y-2], [self.x-3, self.y-3], [self.x-4, self.y-4], [self.x-5, self.y-5], [self.x-6, self.y-6], [self.x-7, self.y-7], [self.x+1, self.y+1], [self.x+2, self.y+2], [self.x+3, self.y+3], [self.x+4, self.y+4], [self.x+5, self.y+5], [self.x+6, self.y+6], [self.x+7, self.y+7], [self.x-1, self.y+1], [self.x-2, self.y+2], [self.x-3, self.y+3], [self.x-4, self.y+4], [self.x-5, self.y+5], [self.x-6, self.y+6], [self.x-7, self.y+7]

    def nouvpossible(self):
        self.possible = [self.x+1, self.y-1], [self.x+2, self.y-2], [self.x+3, self.y-3], [self.x+4, self.y-4], [self.x+5, self.y-5], [self.x+6, self.y-6], [self.x+7, self.y-7], [self.x-1, self.y-1], [self.x-2, self.y-2], [self.x-3, self.y-3], [self.x-4, self.y-4], [self.x-5, self.y-5], [self.x-6, self.y-6], [self.x-7, self.y-7], [self.x+1, self.y+1], [self.x+2, self.y+2], [self.x+3, self.y+3], [self.x+4, self.y+4], [self.x+5, self.y+5], [self.x+6, self.y+6], [self.x+7, self.y+7], [self.x-1, self.y+1], [self.x-2, self.y+2], [self.x-3, self.y+3], [self.x-4, self.y+4], [self.x-5, self.y+5], [self.x-6, self.y+6], [self.x-7, self.y+7]


class roiB(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x, self.y-1], [self.x-1, self.y-1], [self.x-1, self.y], [self.x-1, self.y+1], [self.x, self.y+1], [self.x+1, self.y+1], [self.x+1, self.y], [self.x+1, self.y-1]

    def nouvpossible(self) :
        if isinstance(game.board[0][game.x], roiB) :
            RoiN.possible = [self.x, self.y-1], [self.x-1, self.y-1], [self.x-1, self.y], [self.x+1, self.y], [self.x+1, self.y-1]
        elif isinstance(game.board[7][game.x], roiB) :
            RoiB.possible = [self.x, self.y+1], [self.x-1, self.y+1], [self.x-1, self.y], [self.x+1, self.y], [self.x+1, self.y+1]
        else:
            self.possible = [self.x, self.y-1], [self.x-1, self.y-1], [self.x-1, self.y], [self.x-1, self.y+1], [self.x, self.y+1], [self.x+1, self.y+1], [self.x+1, self.y], [self.x+1, self.y-1]

class roiN(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x, self.y-1], [self.x-1, self.y-1], [self.x-1, self.y], [self.x-1, self.y+1], [self.x, self.y+1], [self.x+1, self.y+1], [self.x+1, self.y], [self.x+1, self.y-1]

    def nouvpossible(self) :
        if isinstance(game.board[0][game.x], roiN) :
            RoiN.possible = [self.x, self.y-1], [self.x-1, self.y-1], [self.x-1, self.y], [self.x+1, self.y], [self.x+1, self.y-1]
        elif isinstance(game.board[7][game.x], roiN) :
            RoiB.possible = [self.x, self.y+1], [self.x-1, self.y+1], [self.x-1, self.y], [self.x+1, self.y], [self.x+1, self.y+1]
        else:
            self.possible = [self.x, self.y-1], [self.x-1, self.y-1], [self.x-1, self.y], [self.x-1, self.y+1], [self.x, self.y+1], [self.x+1, self.y+1], [self.x+1, self.y], [self.x+1, self.y-1]

class Dame(Piece):
    def __init__(self, equipe, lettre, y, x, couleur):
        Piece.__init__(self, equipe, lettre, y, x, couleur)
        self.possible = [self.x+1, self.y], [self.x+2, self.y], [self.x+3, self.y], [self.x+4, self.y], [self.x+5, self.y], [self.x+6, self.y], [self.x+7, self.y], [self.x-1, self.y], [self.x-2, self.y], [self.x-3, self.y], [self.x-4, self.y], [self.x-5, self.y], [self.x-6, self.y], [self.x-7, self.y], [self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3], [self.x, self.y+4], [self.x, self.y+5], [self.x, self.y+6], [self.x, self.y+7], [self.x, self.y-1], [self.x, self.y-2], [self.x, self.y-3], [self.x, self.y-4], [self.x, self.y-5], [self.x, self.y-6], [self.x, self.y-7], [self.x+1, self.y-1], [self.x+2, self.y-2], [self.x+3, self.y-3], [self.x+4, self.y-4], [self.x+5, self.y-5], [self.x+6, self.y-6], [self.x+7, self.y-7], [self.x-1, self.y-1], [self.x-2, self.y-2], [self.x-3, self.y-3], [self.x-4, self.y-4], [self.x-5, self.y-5], [self.x-6, self.y-6], [self.x-7, self.y-7], [self.x+1, self.y+1], [self.x+2, self.y+2], [self.x+3, self.y+3], [self.x+4, self.y+4], [self.x+5, self.y+5], [self.x+6, self.y+6], [self.x+7, self.y+7], [self.x-1, self.y+1], [self.x-2, self.y+2], [self.x-3, self.y+3], [self.x-4, self.y+4], [self.x-5, self.y+5], [self.x-6, self.y+6], [self.x-7, self.y+7]

    def nouvpossible(self):
        self.possible = [self.x+1, self.y], [self.x+2, self.y], [self.x+3, self.y], [self.x+4, self.y], [self.x+5, self.y], [self.x+6, self.y], [self.x+7, self.y], [self.x-1, self.y], [self.x-2, self.y], [self.x-3, self.y], [self.x-4, self.y], [self.x-5, self.y], [self.x-6, self.y], [self.x-7, self.y], [self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3], [self.x, self.y+4], [self.x, self.y+5], [self.x, self.y+6], [self.x, self.y+7], [self.x, self.y-1], [self.x, self.y-2], [self.x, self.y-3], [self.x, self.y-4], [self.x, self.y-5], [self.x, self.y-6], [self.x, self.y-7], [self.x+1, self.y-1], [self.x+2, self.y-2], [self.x+3, self.y-3], [self.x+4, self.y-4], [self.x+5, self.y-5], [self.x+6, self.y-6], [self.x+7, self.y-7], [self.x-1, self.y-1], [self.x-2, self.y-2], [self.x-3, self.y-3], [self.x-4, self.y-4], [self.x-5, self.y-5], [self.x-6, self.y-6], [self.x-7, self.y-7], [self.x+1, self.y+1], [self.x+2, self.y+2], [self.x+3, self.y+3], [self.x+4, self.y+4], [self.x+5, self.y+5], [self.x+6, self.y+6], [self.x+7, self.y+7], [self.x-1, self.y+1], [self.x-2, self.y+2], [self.x-3, self.y+3], [self.x-4, self.y+4], [self.x-5, self.y+5], [self.x-6, self.y+6], [self.x-7, self.y+7]

class Case():
    def __init__(self, couleur, piece = None):
        self.piece = piece
        self.couleur = couleur
    
    def display(self):
        if self.piece is not None:
            return self.piece.display()
        return '-'

RoiN = roiN(True, "r", 8, 5, "noir")
RoiB = roiB(False, "r", 1, 5, "blanc")
DameB = Dame(False, "d", 1, 4, "blanc")
DameN = Dame(True, "d", 8, 4, "noir")
T1B = Tour(False, "t", 1, 1, "blanc")
T2B = Tour(False, "t", 1, 8, "blanc")
T1N = Tour(True, "t", 8, 1, "noir")
T2N = Tour(True, "t", 8, 8, "noir")
C1B = Cavalier(False, "c", 1, 2, "blanc")
C2B = Cavalier(False, "c", 1 , 7, "blanc")
C1N = Cavalier(True, "c", 8, 2, "noir")
C2N = Cavalier(True, "c", 8, 7, "noir")
F1B = Fou(False, "f", 1, 3, "blanc")
F2B = Fou(False, "f", 1, 6, "blanc")
F1N = Fou(True, "f", 8, 3, "noir")
F2N = Fou(True, "f", 8, 6, "noir")

P1B = Pion(False, "p", 2, 1, "blanc")
P2B = Pion(False, "p", 2, 2, "blanc")
P3B = Pion(False, "p", 2, 3, "blanc")
P4B = Pion(False, "p", 2, 4, "blanc")
P5B = Pion(False, "p", 2, 5, "blanc")
P6B = Pion(False, "p", 2, 6, "blanc")
P7B = Pion(False, "p", 2, 7, "blanc")
P8B = Pion(False, "p", 2, 8, "blanc")

P1N = Pion(True, "p", 7, 1, "noir")
P2N = Pion(True, "p", 7, 2, "noir")
P3N = Pion(True, "p", 7, 3, "noir")
P4N = Pion(True, "p", 7, 4, "noir")
P5N = Pion(True, "p", 7, 5, "noir")
P6N = Pion(True, "p", 7, 6, "noir")
P7N = Pion(True, "p", 7, 7, "noir")
P8N = Pion(True, "p", 7, 8, "noir")



game = echec()
game.print_board()
game.joueur = 1
game.Jeu = True
game.jouer()