#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# FileCopyrightText: <text> 2019-2022 Matthew Buchanan Astley ( matthewbuchanan@astley.nl ) </text>
#
# God allemachtig! Jezus! Wat een vrolijk script om grafiekjes te maken van data dat ik in een file 
# verzameld heb, zoals bijvoorbeeld het aantal keer dat journalisten en columnisten backspace 
# gebruiken.
# Een wrapper om de keyboard driver op FreeBSD/Mac OSX  of iets dergelijks die elke backspace
# naar mijn mod_wsgi JSON input script stuurt komt misschien nog wel. Mod_wsgi en JSON werkt al.
#
# In dat boek heeft de auteur even snel en makkelijk in dat voorbeeld wat waardes gedefinieerd zoals
# [ 126, 45, 23, 12, 234 ] en in het wild wil je natuurlijk je eigen verzamelde waardes vanuit een 
# file of op de commandline voeren aan het script.
#
# En dan moet je weten dat je integers moet gebruiken in plaats van strings voor de getallen als invoer 
# en dat gaat met int(). 
# Ook is met lief waardes handmatig in je script vastzetten, statisch, het probleem van het in willekeurige
# volgorde teruggeven van waardes uit een dictionary dict()  dat python doet (net als andere talen),
# omzeild.
# Dit moet een mens daarom ook met key values in lists/arrays doen en dan de indexes van de lists/arrays in de gaten houden.
# Liefdevol worden de waardes in een list in de juiste volgorde weergegeven. 
# OPPASSEN MET SORTEREN!!!!

import os,sys
import matplotlib.pyplot as plt

#
# Open een bestandje op de commandline zoals ./pplot.py "bestandje.txt"
# Bestandje met daarin bijvoorbeeld:
# journalist1 15
# journalist2 59
# 

inputlist = open( sys.argv[1], "r")

#
# Maak een lege dictionary aan en definieer daarna "dit is een dictionary"

#nbdata = {}
#nbdata = dict({}) 

nbdata = []
jnamen = []

#
# Voor elke regel van het bestandje haal de newline character of whitspace eraf
# Split de twee waardes in variabelen name en nbacksp en voeg toe aan list (array) nbdata als
# key name en value nbacksp. EN ZORG DAT HET GETAL EEN GETAL IS MET funtie int() !!!!

for i in inputlist:
    i.strip()
    (name,nbacksp) = i.split()
    nbdata.append([name, int(nbacksp) ])

#debug print('nbdata lijstje:', nbdata)
#debug print(nbdata[0][1])


#
# aangeven dat Wij ggplot gaan gebruiken..

plt.style.use('ggplot')

#
# Maak een leeg array lijstje.
 
aantal_keer_backspace_ingedrukt = []

#
# Voeg de backspace indruk waardes in de nbdata lijst toe aan het lijstje aantal_keer_backspace_ingedrukt
#
# Omdat Wij lijstjes gebruiken moeten wij in de gaten houden op welke positie in het lijstje de waarde staat.
# Daarvoor gebruiken Wij een extra nummer. Nummer 1.
#
# nbdata[ [ journalist1, 243 ],
#         [ journalist2,  53 ] 
#
# De posities zijn
#
# nbdata[ [ 0, 1 ],
#         [ 1, 1 ]  <-- dat is een list slice en die nummers zijn de index nummers.
# 
# met de functie enumerate() word handig even geteld vanaf 0 en dat zijn dan de index nummers van de list slices.
# 
# Overmatig eureka had ik toen ik voor het eerst een loop deed met for en foreach, elke programmeertaal staat er vol mee, 
# en for( $i =0 ; $i < 100; $i++ ) was voor mij echt next level HOERA! Zover ik vrolijk toen elke handeling met arrays deed 
# en indexjes tellen omdat ik hashes (associatieve arrays/key value stores) nog...weetje.. dat was nog te abracadabra .
# Heel liefdevol wordt ik helemaal blij door denken aan dat moment dat ik opeens snapte hee index nummers met een for loopje.
#
# dus g = 1
# 
# Wij voegen het aantal keer backspace ingedrukt getal toe aan het lijstje aantal_keer_backspace_ingedrukt,
# daarna voegen wij de namen (example1, example2..enzovoorts) toe aan het lijstje jnamen. 
# 

f = 0

#debug print('enumerate list:')
for i,j in enumerate(nbdata):
    g = 1
    #debug print(i, j, g, nbdata[i][g])
    #debug print(nbdata[i][g])  
    aantal_keer_backspace_ingedrukt.append(nbdata[i][g]) 
    jnamen.append(nbdata[i][f])


#debug print('namenarray:', jnamen)

#
# Opnieuw maken wij een lijstje met index nummers, dit keer van het lijstje aantal_keer_backspace_ingedrukt.
# Met de functie range() maken Wij een reeks en daarna met len() specificeren wij het eind van de reeks want
# len() geeft een getal terug, het getal van het totaal aantal elementen in het lijstje.

aantal_journalisten = range(len(aantal_keer_backspace_ingedrukt))


#
# Plot het figuur, maak de balken met de namen en het aantal keer backspace ingedrukt

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(jnamen, aantal_keer_backspace_ingedrukt , align='center', color='blue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

#
# Voeg de waardes toe aan de bar plots (oplossing van stackoverflow iets aangepast)
# 

for i,v in enumerate(aantal_keer_backspace_ingedrukt):
    #debug print(i,v)
    ax1.text(i + .10 ,v + 4, str(v), color='blue', va='center', fontweight='bold') 

plt.xticks(aantal_journalisten, jnamen, rotation=0,fontsize='small')
plt.xlabel('journalist columnist')
plt.ylabel('Aantal keer backspace ingedrukt')
plt.title('Aantal keer backspace gebruikt in een alinea')
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()
