#!/usr/bin/env python3
from operator import itemgetter
import sys
current_word = None
current_count = 0
for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        
        # CES DEUX LIGNES DOIVENT ÊTRE EXÉCUTÉES DANS TOUS LES CAS DU 'else'
        current_count = count
        current_word = word

# Sortie du dernier mot
if current_word:  # Le 'if current_word == word:' du TP n'est pas correct ici.
    print('%s\t%s' % (current_word, current_count))