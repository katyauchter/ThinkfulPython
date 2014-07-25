# For this project, we'll imagine that you've been hired
#  by a business analyst to build a system that models 
#  the bicycle industry. You need to be able to model bicycles, 
#  which are comprised of different combinations of wheels and 
#  frames, bicylce manufactuers, which sell different bike models 
#  at different prices, bikeshops, which sell different bike 
#  models with an added margin on top, and customers, who have 
#  names and different budgets for bicycles.



    # Wheels
    #     Have a weight
    #     Have a cost for manufacturer to produce
    #     Have a model name
    #     You'll need to create a total of three wheel types
    #     Even though you'll create two bicycle manufacturers, 
    #     assume that all manufacturers use the same three wheel types.

    # Frames
    #     Can be made of aluminunum, carbon, or steel
    #     Have a weight
    #     Have a cost for manufacturer to produce
    #     Even though you'll create two bicycle manufacturers, 
    #     assume that all manufacturers use the same three frame types.

    # Bicycle Models
    #     Comprised (in our simplified world) of two wheels of the same type and a frame.
    #     Have a total weight equal to the sum of the weight of the frame and two wheels.
    #     Have a total cost to produce (for our purposes, that cost is the sum of 
    #     the two wheels' and frame's cost to produce)
    #     Have a name
    #     Have a manufactuer

    # Bicycle Manufacturers
    #     Have a name
    #     Produce three models of bikes each
    #     Have a percentage over cost they sell bikes to bike shops at
    #     You'll need to create two bicycle manufacturers

    # Bike Shops
    #     Get their inventory of bikes from manufacturers
    #     Sell bicycle models with a margin over price they pay to manufacturer
    #     Have a name
    #     Have an inventory
    #     Can see how much profit they have made on margin from selling bikes.

    # Customers
    #     Have a name
    #     Have a fund of money to buy a bike
    #     Can buy and own a new bicycle


class Bike(object):
    wheels=True
    frame=True


# class Wheels:
#     def __init__(self, weight, cost, model_name):
class Wheels(self, weight, cost, model_name):
        self.weight = weight
        self.cost = cost
        self.model_name = model_name

        # I don't think there should be __init__ like this?

#        maybe more like this


    # Wheels
    #     Have a weight
    #     Have a cost for manufacturer to produce
    #     Have a model name
    #     You'll need to create a total of three wheel types
    #     Even though you'll create two bicycle manufacturers, 
    #     assume that all manufacturers use the same three wheel types.

class Frames(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

    # Frames
    #     Can be made of aluminunum, carbon, or steel <--material
    #     Have a weight
    #     Have a cost for manufacturer to produce
    #     Even though you'll create two bicycle manufacturers, 
    #     assume that all manufacturers use the same three frame types.

class Models(self, wheels=2, frame, weight=wheels.weight + frame.weight, cost=wheels.cost + frame.cost, name, manufacturer):
        self.wheels = wheels# * 2
        self.frame = frame
        self.weight = weight # wheels.weight + frame.weight
        self.cost = cost # wheels.cost + frame.cost
        self.name = name
        self.manufacturer = manufacturer
    #     Comprised (in our simplified world) of two wheels of the same type and a frame.
    #     Have a total weight equal to the sum of the weight of the frame and two wheels.
    #     Have a total cost to produce (for our purposes, that cost is the sum of 
    #     the two wheels' and frame's cost to produce)
    #     Have a name
    #     Have a manufactuer

class Manufacturers(self, name, model1, model2, model3, profit):
        self.name = name
        self.model1 = model1
        self.model2 = model2
        self.model3 = model3
        self.profit = profit

    # Bicycle Manufacturers
    #     Have a name
    #     Produce three models of bikes each
    #     Have a percentage over cost they sell bikes to bike shops at
    #     You'll need to create two bicycle manufacturers
class BikeShops(self, inventory_man, payment, name, inventory_store, profit):
    self.inventory_man = inventory_man
    self.payment = payment
    self.name = name
    self.inventory_store = inventory_store
    self.profit = profit
   # Bike Shops
    #     Get their inventory of bikes from manufacturers
    #     Sell bicycle models with a margin over price they pay to manufacturer
    #     Have a name
    #     Have an inventory
    #     Can see how much profit they have made on margin from selling bikes.

class Customers:(self, name, funds, can_own_bike)
    self.name = name
    self.funds = funds
    self.can_own_bike = can_own_bike

    # Customers
    #     Have a name
    #     Have a fund of money to buy a bike
    #     Can buy and own a new bicycle



