#!/usr/bin/env python3
import sys

# Lire les données ligne par ligne depuis STDIN
for line in sys.stdin:
    try:
        # Supprimer les espaces et diviser la ligne en champs
        fields = line.strip().split()
        
        # Le format typique du fichier d'achats est :
        # Date Time Ville Catégorie Prix MéthodePaiement
        # L'indice 3 correspond donc à la catégorie (le 4e élément)
        category = fields[3]
        
        # Émettre la paire (Catégorie \t 1)
        print('%s\t%s' % (category, 1))
        
    except IndexError:
        # Ignorer les lignes vides ou mal formatées
        continue