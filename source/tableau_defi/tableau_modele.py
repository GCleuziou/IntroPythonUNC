# imagier_modele_1_facile.py
# Version 1 du modèle

nomFic='/Users/cleuziou/donnees/enseignement/UNC/IntroPython/easySphinx/source/tableau_defi/tentatives_csv.csv'
exercices=["ProduitScalaire","MotPalindrome","CompteChiffre","PhrasePalindrome","SousChaine","ElemSuiteArithmetique","ElemSuiteGeometrique","VerifSuiteAriGeo","SuiteArithmetique","SuiteGeometrique","SuiteAriGeo","Conway"]

def chargerResultats(nomFic,listeExercices):
	"""Parcour du fichier des resultats synthetiques de l'exerciseur"""
	fic=open(nomFic,'r')
	resultats=dict()
	for ligne in fic:
		decomp=ligne.split(';')
		for i in range(len(decomp)):
			decomp[i]=decomp[i][1:-1]
		if decomp[6] in listeExercices:
			name=decomp[0].split('.')
			decomp[0]=name[0][0].upper()+name[0][1:]+' '+name[1][0].upper()+name[1][1:]
			if decomp[0] not in resultats.keys():
				resultats[decomp[0]]=dict()
			resultats[decomp[0]][decomp[6]]=decomp[3]
	fic.close()
	return resultats

resultats=chargerResultats(nomFic,exercices)


# ===========
# Traitements sur les données
# ===========
