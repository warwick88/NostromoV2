import pickle

# Tutorial: https://www.datacamp.com/tutorial/pickle-python-tutorial
# Creating a dictionary of dogs to write using pickle to a text file.
dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}

# So we create our filename, which already exists, then open it and WRITE to it.
filename = 'dogs.txt'
outfile = open('dogs.txt', 'wb')

# The info is actually dumped into the pickle file and closed.
pickle.dump(dogs_dict, outfile)
outfile.close()

infile = open('dogs.txt', 'rb')
new_dict = pickle.load(infile)
infile.close()

x = input("so how are you?")
print(new_dict)
print(new_dict == dogs_dict)
print(type(new_dict))


first_value = list(new_dict.values())[0]

first_pair = next(iter((new_dict.items())))

# Printing the first item, and first pair.
print(first_pair)
print(first_value)

print('First Key:', first_pair[0])
print('First Value: ', first_pair[1])


#print(new_dict[0])

