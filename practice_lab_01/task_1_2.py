"""
Suppose we are making ice cream sundaes. We have four flavors of ice cream: vanilla, chocolate,
strawberry, and pistacchio. And we have three sauces: caramel, butterscotch, and chocolate. How many
different ice cream sundaes can we make? Define a function sundaes() to systematically print out
every possible combination, one per line. For example, the first line should say "vanilla ice cream sundae
with caramel sauce". You should create a list to hold each class of ingredient, and use nested for loops to
iterate over these lists to generate the combinations. At the end, your function should return an integer
giving the total number of combinations.
To get you started here a few things you will need:
flavors = ["vanilla", "chocolate", "strawberry", "pistacchio"]
sauces = ["caramel", "butterscotch", "chocolate"]

print(flavor + " ice cream sundae with " + sauce + " sauce")

"""

flavors = ["vanilla", "chocolate", "strawberry", "pistacchio"]
sauces = ["caramel", "butterscotch", "chocolate"]

for flavor in flavors:
    for sauce in sauces:
        print(f"{flavor} ice cream sundae with {sauce} sauce")
        