Classes Questions


# I need help with this concept.  Sometimes, the % means take the remainder,
# And sometimes it means substitute one thing for another right?
# I'm confused about this sign.

# Especially about what it means here:

You can also add functions
(a.k.a methods)

class Fish:
    def move(self, speed):
        print "swimming %s!" % speed <-------------------------- 
        # So this is saying that the %s should be essentailly "formatted" with "speed?"


>> myfish = Fish()
>> myfish.move("fast")
swimming fast!



class Aquarium(object):    
    fish = []  
    # food = []  <-----------------------This was first def feed(): attempt

    def __init__(self, fish):        
        self.fish = fish

    # def add_food(amount): <------------This was first def feed(): attempt
    #     self.food =  food

    def feed(self, food):
        for fish in self.fish:
            fish.eat(food)


class Fish(object):    
    color = "Blue"   # <---------- This is saying all the fish will be blue (unless over-ridden)

    def __init__(self, name):      #<------------This is starting an instance? saying, every fish in this  
        self.name = fish_name      # class named "Fish" will be identified distinctly with a name?

        class Goldfish(Fish): # <----- this is saying the more specific class of Goldfish will be    
            color = "Gold"    # over-ridden with the color "Gold"

        def eat(self,food):
            print self.name + "is eating " + food + "!" #<--- Food is a variable here defined in the 
                                                        #argument above (in acquarium)
                                                        # IS this function specific to the class Goldfish,
                                                        # or does it apply to all specific classes in the general
                                                        # class of Fish?
        class Flounder(Fish):    
            pass





>> my_fish = [Goldfish("Spencer"), Goldfish("Vladimir"), Flounder("Susan")]

>> my_aquarium = Aquarium(my_fish)
>> for fish in my_aquarium.fish:...    
print fish.name



class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:         #<---- What would you put to i.d. a fruit as non poisonuos?  Ah, True and False.
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()




