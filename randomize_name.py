import pandas as pd

#Ici on prend des noms qui représentent nos clients.
names = ['Michel Tremblay', 'Francis Ménard', 'Michelle Tremblay', 'Alex Legault']
new_list = names

#On génére un nom aléatoire de la liste.csv
def get_random_name():   
    list_of_names = pd.read_csv('List.csv')
    selected_name = list_of_names.sample(n=1)
    return selected_name.iat[0,0].title()

#Trouver les indexes de tout occurences
def get_index_positions(list_of_elems, element):
    ''' retourne les indexes des occurences '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # cherche tout les indexes dans une liste
            index_pos = list_of_elems.index(element, index_pos)
            # créer une liste d'index
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError:
            break
    return index_pos_list

#remplacer chaque nom de la liste par un nom aléatoire 
for name in names:
    indices = get_index_positions(names,name)
    value = get_random_name()
    for i in indices:
        new_list[i] = value
        
print(new_list)
