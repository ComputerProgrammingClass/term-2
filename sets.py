# create set of customers
customers = {
    "Kevin Poon",
    "Kevin Zhu",
    "Kevin Wong",
    "Kevin Li",
}

# add customer
customers.add("Danny Li")

# remove customer
customers.discard("Danny Li")

# check if key in set
print("Kevin Poon" in customers)
print("Danny Li" in customers)
