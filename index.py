#!/usr/bin/python3

import sqlite3

# Constante d'abreviation des jours de la semaine
WEEK = ['L','M','M','J','V','S','D']

# Constante d'abreviation des mois de l'année
MONTH = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet', 'Aout','Septembre','Octobre','Novembre','Decembre']

# Variable qui contiendra le calendrier
year = []

# Outil de creation du calendrier
cal = calendar.Calendar()

# Creation du calendrier mois par mois
for m in range(12):
    # Initialisation du mois dans un tableau
    month = [d for d in cal.itermonthdays2(2013,m+1) if d[0]!=0]
	# On rajoute des 0 pour avoir un tableau de 31 valeurs
    for i in range(len(month),31) :
        month.append((0,0))
    # On ajoute le tableau du mois au calendrier
    year.append(month)

# Creation de l'entete de la page html, plus le debut du corps
print ("""
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Calendrier</title>
  <link rel="stylesheet" href="style.css">
</head>
  <body>
    <table class="year">
	  <tr><th colspan="12">2013</th></tr>
""")
# Ecriture des noms de mois
print ('<tr class="month">')
for m in MONTH :
    print ('<th>'+m+'</th>')
print ('</tr>')

# Ecriture des jours
for d in range(31) :
    # Debut d'une nouvelle ligne
    print('<tr>')
    for m in range(12) :
        # Debut d'une nouvelle cellule
        if year[m][d][0]!=0 :
            cell='<td'
            if year[m][d][1] in [6,7] :
                cell += ' class="weekend"'
            cell+= '>'+WEEK[year[m][d][1]]+' : '+str(year[m][d][0])+'</td>'
            print(cell,end='')
        else :
            print('<td></td>')
    print('<tr>')

# Creation du pied de page html, précédé de la fin du corps
print ("""
    </table>
  </body>
</html>
""")
