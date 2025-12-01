#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    try:
        # Lire la paire (word, count) séparée par une tabulation
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue
    
    # Agrégation des comptes pour la même catégorie
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Écrire le résultat de la catégorie précédente
            print('%s\t%s' % (current_word, current_count))
        
        # Démarrer le nouveau mot/groupe
        current_count = count
        current_word = word

# Sortie du dernier mot/groupe
if current_word:
    print('%s\t%s' % (current_word, current_count))