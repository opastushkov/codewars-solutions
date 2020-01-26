def cakes(recipe, available):    
    return min([available.setdefault(x, 0)//recipe[x] for x in recipe])