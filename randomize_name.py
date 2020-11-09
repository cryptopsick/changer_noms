import pandas as pd

names = ['Michel Tremblay', 'Francis Ménard', 'Michelle Tremblay', 'Alex Legault']
new_list = names

def get_random_name():   
    list_of_names = pd.read_csv('List.csv')
    selected_name = list_of_names.sample(n=1)
    return selected_name.iat[0,0].title()

print(get_random_name())


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

for name in names:
    indices = get_index_positions(names,name)
    value = get_random_name()
    for i in indices:
        new_list[i] = value
        
print(new_list)