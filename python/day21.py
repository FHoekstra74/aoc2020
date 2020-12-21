lines,allallergens,allingredients,ingredientswithallergen,answera=[line.strip() for line in open('../input/day21.txt','r')],{},set(),set(),0
for line in lines:
    ingredients=set(line.split(' (')[0].split(' '))
    allingredients=allingredients.union(ingredients)
    allergens=line.split('contains ')[1][:-1]
    for allergen in [allergen.strip() for allergen in allergens.split(',')]:
        if allergen in allallergens: allallergens[allergen] = allallergens[allergen].intersection(ingredients)
        else: allallergens[allergen]=ingredients

for ingredients in allallergens.values(): ingredientswithallergen=ingredientswithallergen.union(ingredients)
for ingredient in allingredients.difference(ingredientswithallergen):
    for line in lines:
        if ingredient in set(line.split(' (')[0].split(' ')): answera+=1
print(answera)

ingredient_allergen,answerb={},''
while any([ingredients for ingredients in allallergens.values() if len(ingredients)>0]):
    for allergen,ingredients in allallergens.items():
        if len(ingredients) == 1: ingredient_allergen[ingredients.pop()]=allergen
    for ingredients in allallergens.values():
        toremove=[]
        for ingredient in ingredients:
            if ingredient in ingredient_allergen: toremove.append(ingredient)
        for ingredient in toremove: ingredients.remove(ingredient)
for allergen in sorted(allallergens):
    for ingredient,theallergen in ingredient_allergen.items():
        if theallergen==allergen: answerb+=','+ingredient
print(answerb[1:])
