#a changable unordered collection of unique key:value pair

# capitals = {'usa':'washington dc','india':'new delhi','china':'beigin','russia':'moscow'}
# capitals['nigeria']='abuja' #add new item to dictionary

# default_value=capitals.get('illorin','no state value assigned')
# print(default_value)
#print(capitals['russia'])
#print(capitals.get('Germany'))#it is much safer to use the get keyword to check 
#if a key exists while using a dictionary
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())#print both key and values
#capitals.update({'germany':'berlin'})
#capitals.pop('china')
#capitals.clear()

# for key,values in capitals.items():
#     print(key,values)
# #building an empty dictionary
# alien_0={}
# alien_0['color']='green'
# alien_0['points']=5

# print(alien_0)

# favorite_languages = {
#       'jen': ['python', 'rust'],
#       'sarah': ['c'],
#       'edward': ['rust', 'go'],
#       'phil': ['python', 'haskell'],
#       }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# person={
#       'firstname': 'itohan',
#        'lastname': 'eregie',
#        'age': 37,
#        'city': 'milton keynes'
#        }
       
#get key from dictionary
# for key in person.keys():
#     print(key.title())

# firstnames=person['firstname']
# print(firstnames)

# favourite_num={
#        'june': 4,
#        'ese': 5,
#        'titi': 37,
#        'ana': 78
# }
# for key,value in favourite_num.items():
#     print(f"\nKey: {key}")
#     print(f"\nValue: {value}")

# for key in favourite_num.keys():
#     print(key.title())
favourite_languages={#first loop through the dictionary and then loop through the list
    'jen': ['python','rust'],
    'luke':['c','c++'],
    'james':['python','go'],
    'fen':['rust']
}

for name,languages in favourite_languages.items():
        if len(languages) > 1:
            print(f"{name.title()}")
            for language in languages:
                print(f"\t{language}")

# friends=['luke','james']
# for friend in friends:
#     print(f"{friend.title()}")
#     if friend in friends:
#         language=favourite_languages[friend].title()
#         print(f"\t{friend.title()},i see you love{language}")

# for language in set(favourite_languages.values()):#to print out unique values in a list or dictionary
#     print(language)

#list of dictionaries
# alien_0={'color':'green','points':5}
# alien_1={'color':'red','points':6}
# alien_2={'color':'blue','points':9}

# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

# aliens=[]
# for alien in range(0,30):
#     new_alien={'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print(len(aliens))


