entrees_visibles = [
        (1,10,7,20),
        (1,7,10,20)
]
entrees_invisibles = [
        (7,20,1,10),
        (10,20,1,7),
        (1,10,10,20),
		(1,10,1,10)
]

@solution
def rendezVous(debut1,fin1,debut2,fin2):
   if fin1<debut2 or fin2<debut1:
	   res=False
   else:
	   res=True
   return res
