
if __name__ == "__main__":
    
    pokemon = ('pikachu', 'charmander', 'bulbasaur')
    print(pokemon[1])

    starter1 = pokemon[0]
    starter2 = pokemon[1]
    starter3 = pokemon[2]

    name = (tuple('daniel'))
    print(['i'] in name)

    for i in range(2, 11):
        print(i)

    i = 0
    while i < len(range(2, 11)):
        print(i)
        i += 1

    quote = ('This is a simple string')
    for letter in quote:
        print(letter)
 
    set_list = ('this', 'is', 'a', 'simple', 'set')
    for i in set_list:
        for j in set_list * 2:
            print (j )
            