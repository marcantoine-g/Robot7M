#import
import random

#code

class Cube():
    """Classe definissant un cube caractérisé par :
    - ses coordonnées, x, y, z
    - sa largueur
    - sa longueur
    - sa hauteur"""

    def __init__(self, x, y, z, larg, long, haut):
        """constructeur de la classe cube

        exemple de creation d'un cube : c1 = Cube(0,0,0,10,10,10)
        (création d'un cube de coordonnées x = y = z = 0 et de taille 10
        """
        self.x = x
        self.y = y
        self.z = z
        self.larg = larg
        self.long = long
        self.haut = haut

        
    def safficher(self):
        """Methode d'affichage d'un cube au format :
        cube[x= , y= , z= , larg= , long= , haut= ]
        """
        print("Cube(x=",self.x,",y=",self.y,",z=",self.z,", larg=",self.larg,",long=",self.long,",haut=",self.haut,")")


    def getPos(self):
        """return la position du cube sous forme d'un triplet -> (x, y, z)"""
        return self.x, self.y, self.z



def Creation_Cube():
    """Creation d'un cube de taille et coordonnees aleatoires"""
    x = random.randint(0,500)
    y = random.randint(0,500)
    z = random.randint(0,500)
    
    larg = random.randint(50,70)
    long = random.randint(50,70)
    haut = random.randint(50,70)
    
    return Cube(x, y, z, larg, long, haut)
