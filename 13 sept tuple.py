# this is a tuple
'''
numbers_tuple=(1,2,3,4)
print(numbers_tuple)
print(len(numbers_tuple))

numbers_list=[1,2,3,4]
print(numbers_list)
numbers_list[0]=3
print(numbers_list)
'''

# create an empty set
'''
shopping_list=set()
shopping_list={'milk','coconut','pasta','watermelon'}
print(shopping_list)
shopping_list.add('cookies')
print(shopping_list)
# shopping_list.remove('beef')
# print(shopping_list)
shopping_list.discard('beef')
print(shopping_list)
'''
# dictionary
'''
my_dictionary = {}
my_dictionary['nimi'] = 'name'
my_dictionary['osoite']='phone number'
my_dictionary['puh']='address'
print(len(my_dictionary))
print(my_dictionary['osoite'])
print(my_dictionary)
my_dictionary['osoite']='address'
print(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())
my_dictionary.pop('puh') #to remove an item in dictionary(key+value)
print(my_dictionary)
'''
# Exercise classwork
'''
def add_movie(database: list, name:str, director: str, year: int, runtime: int):
    movie={'name':name,'director':director,'year':year,'runtime':runtime }
    database.append(movie)

database=[]
add_movie(database,'my friend', 'yogi',1985, 90)
add_movie(database,'the great gatsby','hugh grunt', 1890, 85)
print(database)
'''

# create a search database

def search_movies(database:list,search_word:str):
    found_movies=[]
    for movie in database:
        if search_word.lower() in movie['name'].lower():
            found_movies.append(movie)

    return found_movies
def add_movie(database: list, name:str, director: str, year: int, runtime: int):
    movie={'name':name,'director':director,'year':year,'runtime':runtime }
    database.append(movie)

database=[]
add_movie(database,'my friend', 'yogi',1985, 90)
add_movie(database,'the great gatsby','hugh grunt', 1890, 85)
# print(database)

my_search_movies=search_movies(database,'man')
print(my_search_movies)