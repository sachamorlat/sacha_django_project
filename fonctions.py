import re

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def compter_mots(phrase):
    mots = re.findall(r'\b\w+\b', phrase)  # Utilisation d'une expression régulière pour trouver les mots
    return len(mots)

def somme_liste(liste):
 somme = 0
 for element in liste:
    somme += element
 return somme

def est_palindrome(chaine):
 chaine = chaine.lower() #Pour gérer la casse
 chaine_inverse = chaine[::-1]
 return chaine == chaine_inverse

def calculer_moyenne(liste):
    if not liste:
        return 0
    else:
        return sum(liste) / len(liste)

class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
    def obtenir_solde(self):
        return self.solde


class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)
    def calculer_surface(self):
        return self.longueur * self.largeur
