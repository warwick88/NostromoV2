import pickle

# Below we create a user library file which contains logins for our application
# Two accounts are created, and dumped into a pickle file. They still need to be reloaded

user_library = {"Dom":"Dominatus", "Boo": "Abra"}

filename = 'NostromoUserLibrary.txt'
outfile = open('NostromoUserLibrary.txt', 'wb')

pickle.dump(user_library, outfile)
outfile.close()


infile = open("NostromoUserLibrary.txt", 'rb')
user_library2 = pickle.load(infile)

#print(user_library2)


first_value = list(user_library2.values())[0]

first_pair = next(iter((user_library2.items())))

# Printing the first item, and first pair.
#print(first_pair)
#print(first_value)

#print('First Key:', first_pair[0])
#print('First Value: ', first_pair[1])


#print(new_dict[0])



