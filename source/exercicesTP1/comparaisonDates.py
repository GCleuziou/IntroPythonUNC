entrees_visibles = [
        (10,1,2020,14,2,2020),
        (14,2,2020,11,2,2020),
        (10,1,2020,10,1,2020)
]
entrees_invisibles = [
        (10,1,2020,10,1,2021),
        (10,1,2021,10,1,2020),
        (10,1,2020,10,2,2020),
		(10,2,2020,10,1,2020),
		(10,1,2020,11,1,2020),
		(11,1,2020,10,1,2020),
		(10,1,2020,10,1,2020)
]

@solution
def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
   if annee1<annee2:
       res=-1
   elif annee2<annee1:
       res=1
   elif mois1<mois2:
	   res=-1
   elif mois2<mois1:
	   res=1
   elif jour1<jour2:
	   res=-1
   elif jour2<jour1:
	   res=1
   else:
       res=0
   return res
