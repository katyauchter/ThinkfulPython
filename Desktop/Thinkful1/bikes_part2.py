# Write a script that:

#     Lives in a file separate from your models and imports them.

#     Creates two bicycle manufacturers, which both produce three different 
#     bicycle models (note that this implicitly requires you to create the 
#     wheels and frames that both manufacturers will need to produce their bicycles)
   
#     Creates one bicycle shop that has 6 different bicycle models in stock, 
#     3 from each manufacturer. The bicycle shop should charge its customers 20% over 
#     its cost for buying the bikes from the manufacturers.
    

    #------ >  Are we creating this bike shop as a class?


#     Creates three customers. One customer has a budget of $200, the second $500, 
#     and the third $1000.

    # Customers as a class?
    
#     Prints the name and total weight of each bicycle model carried by the bike shop
    
#     Prints the name of each customer, and a list of the bikes offered by the bike shop 
#     that they can afford given their budget. Make sure you price the bikes in such a way 
#     that each customer can afford at least one.
    
#     Prints the initial inventory of the bike shop for each bike it carries.
#     Has each of the three customers purchase a bike then prints the name of the bike 
#     the customer purchased, the cost, and how much money they have left over in 
#     their bicycle fund.
    
#     After each customer has purchased their bike, the script should print out the bicycle 
#     shop's remaining inventory for each bike, and how much profit they have made 
#     selling the three bikes.
 
import Wheels  #<--- I feel like I'm making specific wheel types here.

shimano = Wheels(1, 60, 'tubular')
cobalt = Wheels(1.2, 90, 'wheelset')
armadillo = Wheels(1.5, 120, 'disk')

import Frames   #<--- specific frame types here?

carbon = Frames('carbon', 4, 700)
aluminunum = Frames('aluminunum', 2, 800)
steel = Frames('steel', 10, 150)

import Models    # are we suppose to get more specific here?  should weights and costs be done in functions ?
                # <--- specific combinations of wheels and frames here?
model1 = Models(shimano, carbon, totalweight = shimano.weight + carbon.weight, totalcost = shimano.cost + carbon.cost, 'Model1', 'BikeMaker1')
model2 = Models(shimano, aluminunum, totalweight = shimano.weight + aluminunum.weight, shimano.cost + aluminunum.cost, 'Model2', 'BikeMaker1')
model3 = Models(cobalt, steel, totalweight =  cobalt.weight + steel.weight, totalcost = shimano.cost + aluminunum.cost, 'Model3', 'BikeMaker1')
model4= Models(armadillo, aluminunum, totalweight =  armadillo.weight + aluminunum.weight, totalcost =armadillo.cost + aluminunum.cost, 'Model4', 'BikeMaker2')
model5= Models(armadillo, carbon, totalweight = armadillo.weight + carbon.weight, totalcost =armadillo.cost + carbon.cost, 'Model5', 'BikeMaker2')
model6 = Modles(cobalt, steel, totalweight = cobalt.weight + steel.weight, totalcost = cobalt.cost + steel.cost, 'Model6', 'BikeMaker2')

import Manufacturers

BikeMaker1 = Manufacturers('BikeMaker1', model1, model2, model3, profit)
BikeMaker2 = Manufacturers('BikeMaker2', model4, model5, model6, profit)


###....
import BikeShops 

BikeShop = 
bike1Cost = model1.totalcost + model1.totalcost(.2)
bike2Cost = model2.totalcost + model2.totalcost(.2)

import Customers

customer1 = Customers('James', 200, True)
customer2 = Customers('Clhoe', 500, True)
customer3 = Customers('Jed', 1000, True)




