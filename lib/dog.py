#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
   def __init__(self,name):
      self.name= ''
      self.breed = ''
   def get_name(self):
      print('Getting age....')
      return self.name
   
   def set_name(self,name):
      if(type(name) == ''):
         print(f'Setting name to {name}')
         self.name = name
      else:
         print('Name must be a string')

   name = property(get_name,set_name,)
      
class breed:
   def __init__(self,name):
      self.name = name
      self.breed = ''
   def get_breed(self):
      print('Getting breed....')
      return self.breed
   def set_breed(self,breed):
      if (breed in APPROVED_BREEDS):
         print(f'Setting breed to {breed}')
      else:
         print("Breed not approved")