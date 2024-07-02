Avoir la liste des fichiers c’est bien joli mais on aimerait connaˆıtre les contextes.
Integrez dans votre code la fontion suivante qui prend en entr ́ee un texte et un mot et
affiche tous les contextes d’apparition de ce mot dans le texte :
def afficher contextes (chaine , terme , taille contexte = 30):
match = re.search(terme , chaine)
contexts = []
while match is not None:
#Les b o r n e s g auc he e t d r o i t e a u t o u r du mot :
gauche = max(match.start()−taille contexte−1, 0)
droite = match.end ()+1+ taille contexte
contexts.append(chaine[gauche:droite ])
chaine = chaine[match.end ():]
match = re.search(terme , chaine)
for c in contexts:
print(c)