# AnimalCrossing-Calculator
For given recipe requirements, this calculator will determine how many component items you need in your inventory to make an inventory full of them.

You'll have to input your inventory size (20, 30, or 40), how many spaces of your inventory are taken, at least one recipe component, and how many of that component will stack in your inventory


Below are planning notes for the file
the goal is to create a calculator that will give you the ideal number of ingredients to make
a full inventory of items

inventory capacities are 20, 30, or 40. Need to be able to select for these.
would change the picture of your inventory to 20, 30, or 40.

optional, could also subtract how many items you don't want to take out of your inventory.
would highlight full inventory with 0 selected, then unhighlight spots starting from the topleft

need to have most common ingredients, at least
those would be branches, stone, iron, weeds, softwood, wood, hardwood
could also include clay, gold, seasonal ingredients later
to not include all the resources like shells and stuff would have to include "other 1"
! other1 - other6 will just have a #1-6 as pic, ! have to specify how much item sits in a stack
could actually start the project with just Other1-6 and then do the most common ingredients
!!ingredients required [6 drop down menus, default value is None]

need to have the recipe cost somehow that's not me listing it out for every single recipe because fuck that
would require userinput for cost of recipe
6 is max number of components
!! have a / [#input] for how many required for the recipe next to each ingredient
I think the max possible [#input] should be 90, there aren't any recipes that require more than 90 stone for stone arch iirc, min is 1

so the user has input 1-6 ingredients, and user has input how many ingredient per recipe
the common ingredients will have how much they stack (i.e. iron, stone, wood = 30)
the Other1-6 ingredients will specify how many are in a stack by the user.


calculator functionality

what's the math function for how much space you have
spaces available = max number of items you can hold
inventory size - space used = space available
max number of items = x
total = x * ingredients of recipe should give you an amount of items where if you had the exact number of ingredients you'd end up with the exact number of product
need to return the total, but also return it as a # of stacks of items (i.e. if the ideal is 87 round up to 3 stacks of 30)

what's the best way to display this on a webpage? can that even work with python code or would I have to convert to JS

to test like say if I was creating a shovel, it requires 5 hardwood and 1 iron
a full inventory of 40 would require 200 hardwood and 40 iron
so most efficient would be 7 stacks hardwood, 2 stacks iron, with a remainder of 10 wood and 20 iron left
maybe for full stacks you subtract two for each leftover component and show that you make 38
would only be slightly more complicated, would have to be like if there's a remainder then add to the taken inventory spaces for each component
