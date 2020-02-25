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
def rendezVous(d1,f1,d2,f2):
   if f1<d2 or f2<d1:
	   res=False
   else:
	   res=True
   return res
