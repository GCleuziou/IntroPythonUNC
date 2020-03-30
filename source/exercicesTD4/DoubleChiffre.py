entrees_visibles = [
        (2009),
        (2020),
]

entrees_invisibles = [
		(2),
		(22),
		(12),
		(122),
		(123),
		(123456789987654321),
]


@solution
def doubleChiffre(nombre):
    res=False
    prec=nombre%10
    reste=nombre/10
    while not res and reste!=0:
        if prec==reste%10:
            res=True
        else:
            prec=reste%10
            reste=reste//10
    return res
