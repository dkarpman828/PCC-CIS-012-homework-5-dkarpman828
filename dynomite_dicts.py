
if __name__ == "__Main__":

    pokedex = {
        'Venosaur' : ('Grass', 'Poison'),
        'Charizard' : ('Fire', 'Flying'),
        'Blastoise' : 'Water'
    }
    del pokedex ['Blastoise']
    print(pokedex)