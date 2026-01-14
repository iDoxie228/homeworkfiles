with open("recipes.txt") as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ing_count = int(f.readline().strip())
        ing_list = []
        for _ in range(ing_count):
            ing, quant, mes = f.readline().strip().split(' | ')
            ing_list.append({
                'ingredient_name': ing,
                'quantity': int(quant),
                'measure': mes
            })
        cook_book[dish_name] = ing_list
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    dct = {}
    for dish in dishes:
        dish_ing = cook_book[dish]
        for ingredient in dish_ing:
            ing_quant = ingredient['quantity'] * person_count
            ing_name = ingredient['ingredient_name']
            ing_measure = ingredient['measure']
            if ing_name not in dct:
                dct[ing_name] = {'measure': ing_measure, 'quantity': ing_quant}
            else:
                dct[ing_name]['quantity'] += ing_quant      
    return dct



res = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 4)
print(res)




    

            
            

         


    
    
