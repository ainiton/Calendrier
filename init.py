#!/usr/bin/python3

import sqlite3
import calendar
import sys

# Initialisation de la connexion
conn = sqlite3.connect('calendrier.db')
c = conn.cursor()

# Creation et initialisation de la table des droits au congés (droits totaux et droits restants)
c.execute("CREATE TABLE droits (annee integer, type text, max numeric, reste numeric)")
listeConges = [(sys.argv[1],'normaux',25,25),(sys.argv[1],'ARTT',12,12),(2012,'normaux',12,12),(sys.argv[1],'hiver',2,2),(sys.argv[1],'CHA',2,2),(sys.argv[1],'PF',48,48),(sys.argv[1],'exeptionnel',10,10)]
c.executemany("INSERT INTO droits VALUES (?,?,?,?)",listeConges)

# Creation de la table calendrier
# Outil de creation du calendrier
cal = calendar.Calendar()
c.execute("CREATE TABLE calendrier (annee integer, mois integer, jour integer, placeSemaine integer, congesAM integer, congesPM integer)")
# Creation du calendrier mois par mois
listejours=[]
for m in range(12):
    # Initialisation du mois dans un tableau
    month = [d for d in cal.itermonthdays2(int(sys.argv[1]),m+1) if d[0]!=0]
    # On rajoute chaque jour du mois à la liste des jours (formatté comme il faut (année, mois, jour, placeSemaine))
    for jour in month :
        listejours.append((sys.argv[1], m+1, jour[0], jour[1],0,0))

c.executemany("INSERT INTO calendrier VALUES (?,?,?,?,?,?)",listejours)

# Fermeture de la base
conn.commit()
conn.close()
