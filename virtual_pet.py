#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:37:53 2018


"""
# =============================================================================
# Algorithm
#     -create class pet 
#         -initialize variables
#         -create method to feed pet 
#         -create method to give pet drink
#         -create method to shower
#         -create method to play with pet
#     -create class cat 
#         - use class pet to create class cat through inheritance 
#         -add cat specific edible items 
#     -create class dog
#         -use class pet to create class dog through inheritance 
#         -add dog specific edible items 
#     -create main 
#         -prompt users to input species, name, gender, and fur color of pet.keep\
#         prompting until valid input 
#         -ask users if they want to feed, drink, shower, sleep, or play until they\
#         input q which ends the game. 
# =============================================================================
       

from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
        '''method initializes the variables that were input, or if none were input,\
        initializes the default variables'''

        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items = []

        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)

        self._reply_to_master('newborn')

    def _time_pass_by(self, t=1):
        ''' this method takes an instance of a pet and adjusts its metrics based\
        on the amount of time has passed by. '''
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
        ''' this method takes the instance of the pet and returns the hunger \
        level of the pet'''
        return self._hunger

    def get_thirst_level(self):
        ''' this method takes the instance of the pet and returns the thirst \
        level of the pet'''
        return self._thirst

    def get_energy_level(self):
        ''' this method takes the instance of the pet and returns the energy \
        level of the pet'''
        self._energy
    
    def drink(self, liquid):
        ''' this method takes an instance of a pet and a  liquid and quantity\
        (such as Water(1)) and feeds the pet if the liquid and quantity are \
        both valid. Nothing is returned but the thirst level of the pet is \
        changed within the instance. The thirst level changes depending on how\
        much drink the user gives. '''
        #if following is true, the liquid is valid 
        if isinstance(liquid, tuple(self._drinkable_items)): 
            self._time_pass_by()
            #finds the liquid quantity
            liquid_quantity=liquid.get_quantity()
            thirst_level=self._thirst
            #following functions compare the liquid quantity to the thirst level\
            #to see what action needs to be taken 
            if thirst_level-liquid_quantity>0 and thirst_level>=2:
                self._thirst=self._thirst-liquid_quantity
                self._reply_to_master("drink")
            if thirst_level-liquid_quantity<0 and thirst_level>=2:
                self._thirst=0
                self._reply_to_master("drink")
#            if thirst_level<=2:
#                print("Your pet is satisfied, no desire for sustenance now.")
        else:
            print("Not drinkable")
        #updates the status
        self._update_status()
        
          
    def feed(self, food):
        ''' this method takes an instance of a pet and  food and quantity(such \
        as DogFood(1)) and feeds the pet if the food and quantity are both valid.\
        Nothing is returned but the hunger level of the pet is changed within\
        the instance. The change in hunger level is dependent on the amount of \
        food the user gives. '''
        #if following is true, the user input is valid 
        if isinstance(food, tuple(self._edible_items)):
            self._time_pass_by()
            #gets the quanity of the food from the user input
            food_quantity=food.get_quantity()
            #gets the hunger level
            hunger_level=self._hunger
            #compares the quantity of the food with the hunger level to take\
            #the appropriate action. 
            if hunger_level-food_quantity>2 and hunger_level>=2:
                self._hunger=self._hunger-food_quantity
                self._reply_to_master("feed")
            if hunger_level-food_quantity<2 and hunger_level>=2:
                self._hunger=0
                self._reply_to_master("feed")
            if hunger_level<2:
                print("Your pet is satisfied, no desire for sustenance now.")
        else:
            print("Not edible")
        #updates the status 
        self._update_status()


    def shower(self):
        ''' this method takes an instance of a pet and gives it a shower. Nothing\
        is returned, but the smell of the pet is reduced to 0 and the loneliness\
        decreases by 4.'''
        
        self._time_pass_by(t=4)
        #reduces smell to 0
        self._smell=0
        #reduces loneliness by 4
        self._loneliness-=4
        #if loneliness is below 4, it sets it to 0
        if self._loneliness<0:
            self._loneliness=0
        self._reply_to_master( "shower")
        self._update_status()


    def sleep(self):
        ''' this method takes an instance of a pet and puts the pet to sleep. Nothing\
        is returned, but the pet's energy increases by 7.'''
        self._time_pass_by(7)
        #increases pets energy by 7
        self._energy+=7
        #if the pets energy is above 10, it brings it back to 10 because 10 is the mac
        if self._energy>10:
            self._energy=10
        self._reply_to_master("sleep")
        #updates the status 
        self._update_status()
        
        

    def play_with(self):
        ''' this method takes an instance of a pet and playes with the pet.\
        Nothing is returned but the loneliness decreases by 4, the smell increases\
        by 4 and the energy decreases by 4. '''
        self._time_pass_by(t=4)
        #decreases the loneliness by 4
        self._loneliness-=4
        if self._loneliness<0:
            self._loneliness=0
        #increases the smell by 4
        self._smell+=4
        if self._smell>10:
            self._smell=10
        #decreases energy by 4    
        self._energy-=4
        if self._energy<0:
            self._energy=0
    
        self._reply_to_master("play")    
        #updates the status 
        self._update_status()
        

    def _reply_to_master(self, event='newborn'):
        ''' prints the actions and reactions that are caused by the user's inputs.'''
        # this function is complete #
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = " (๑´ڡ`๑)"
        faces['drink'] = " (๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
        ''' takes an instance of a pet and prints the metrics of the pet. The more\
        full the bars that are printed are, the higher the metric is.'''
        # partially formatted string for your guidance
        #the amount of pound signs is calculated by rounding energy level. Then\
        # you multiple energy level by two. 
        print( "{:<12s}: [{:<20s}]".format("Energy",(round(self._energy)*2*"#"))\
              + "{:5.2f}/{:2d}"\
              .format(self._energy,10 ))
        print( "{:<12s}: [{:<20s}]".format("Hunger",(round(self._hunger)*2*"#"))\
              + "{:5.2f}/{:2d}".format(self._hunger,10 ))
        print( "{:<12s}: [{:<20s}]".format("Loneliness",(round(self._loneliness)\
              *2*"#")) + "{:5.2f}/{:2d}".format(self._loneliness,10 ))
        print( "{:<12s}: [{:<20s}]".format("Smell",(round(self._smell)*2*"#")) + \
              "{:5.2f}/{:2d}".format(self._smell,10 ))
        print( "{:<12s}: [{:<20s}]".format("Thirst",(round(self._thirst)*2*"#")) + \
              "{:5.2f}/{:2d}".format(self._thirst,10 ))
        pass  # replace with your code
        
    def _update_status(self):
        '''  prints the expressions of the pet after you do something with them.'''
        # this function is complete #
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'


class Cat(Pet):
	# insert docstring
    def __init__(self, name='fluffy',gender='male',color='white',species="Cat"):
        Pet.__init__(self,name,species,gender,color)
        ''' Initializes the values that class Cat uses from pet and values that \
        are specific to class Cat'''
        #alters class pet to be cat specific 
        self._species=species
        self._edible_items=[CatFood]#did I set this up correctly?
        self._drinkable_items=[Water]
            
        
class Dog(Pet):
	# insert docstring
    def __init__(self, name='fluffy',gender='male',color='white',species="Dog"):
        Pet.__init__(self,name,species,gender,color)
        ''' Initializes the values that class Dog uses from pet and values that \
        are specific to class dog'''
        #alters class pet to be dog specific 
        self._species=species
        self._edible_items=[DogFood]#did I set this up correctly?
        self._drinkable_items=[Water]

def main(): 
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female),\
    fur color of your pet, seperated by space ---Example input:  [dog] [fluffy] \
    [male] [white] (Hit Enter to use default settings): "

    # error checking for user input
    #I need to see if user inputs are valid. 
    prompt_state=False
    while prompt_state==False and prompt!='':
        input_lst=prompt.split(" ")
        
        #first check if species if valid 
        if input_lst[0].lower() in ["cat","dog"]:
            prompt_state=True
            
        #check if gender is valide:
        if input_lst[2].lower() in ["male","female"] and prompt_state==True:
            prompt_state=True
        
        #deals with if input is not valid 
        if prompt_state==False:
            prompt = input( "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
    if prompt=='':
        input_lst=["dog","fluffy","male","white"]
    

#    print(input_lst)    
        
        
#     create a pet object
    if input_lst[0].lower()=="cat":
#        (self, name='fluffy',gender='male',color='white',species="Cat")
        pet=Cat(input_lst[1],input_lst[2],input_lst[3],input_lst[0])
    if input_lst[0].lower()=="dog":
        pet=Dog(input_lst[1],input_lst[2],input_lst[3],input_lst[0])
    # your code goes here #


#handle user commands    
    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or\
    play with him or her by entering each of the following commands:\n --- [feed] \
    [drink] [shower] [sleep] [play]\n You can also check the health status of \
    your pet by entering:\n --- [status]."
    print(intro)
    while prompt.lower()!="q":
        prompt_input=False
        prompt =input( "\n[feed] or [drink] or [shower] or [sleep] or [play] or \
                      [status] ? (q to quit): ")
       
        #if the user wants to feed pet
        if prompt.lower()=="feed":
            food_amt=(input("How much food ? 1 - 10 scale: "))
            int_state=False
            while_state=True
            #this guarantees that it is an integer that is being passed
            while while_state==True:
                #check to see if value is a string 
                food_state=True
                try:
                    food_amt=int(food_amt)
                except:
                    food_state=False
                #check to see if value is between 1-10
                if food_state==True:
                    if food_amt>10:
                        food_state=False
                    if food_amt<=0:
                        food_state=False
                if food_state==False:
                    print(" Invalid input.")
                    food_amt=(input("How much food ? 1 - 10 scale:"))
                    while_state=True
                if food_state==True:
                    while_state=False
                    food_amt=int(food_amt)
            
            #if dog feed dog food
            if input_lst[0].lower()=="dog":
                pet.feed(DogFood(food_amt))
            #if cat feed cad food 
            if input_lst[0].lower()=="cat":
                pet.feed(CatFood(food_amt))
            prompt_input=True
            
            
        #if the user wants to give pet drink
        if prompt.lower()=="drink":
            drink_amt=(input("How much drink ? 1 - 10 scale:"))
            int_state=False
            while_state=True
            #this guarantees that it is an integer that is being passed
            while while_state==True:
                #check to see if value is a string 
                drink_state=True
                try:
                    drink_amt=int(drink_amt)
                except:
                    drink_state=False
                #check to see if value is between 1-10
                if drink_state==True:
                    if drink_amt>10:
                        drink_state=False
                    if drink_amt<=0:
                        drink_state=False
                if drink_state==False:
                    print(" Invalid input.")
                    drink_amt=(input("How much drink ? 1 - 10 scale:"))
                    while_state=True
                if drink_state==True:
                    while_state=False

            pet.drink(Water(drink_amt))
            prompt_input=True
        
        #if the user wants to shower thier pet 
        if prompt.lower()=="shower":
            pet.shower()
            prompt_input=True

            
        #if the user wants to play with their pet
        if prompt.lower()=="play":
            pet.play_with()
            prompt_input=True

        if prompt.lower()=="status":
            pet.show_status()
            prompt_input=True
            
        if prompt.lower()=="sleep":
            pet.sleep()
            prompt_input=True
        
        if prompt_input!=True and prompt.lower()!="q":
            print("Invalid command.")
            

    print("Bye ~")

if __name__ == "__main__":
    main()