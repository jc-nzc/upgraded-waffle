thislist = ["jac", "df", "agv"]

print(thislist[2])
print(thislist[-1])
print(thislist[1:4])
print(thislist[:2])
if "agv" in thislist:
  print("Yes, 'Ale is present' is in the fruits list")

if "jac" in thislist:
    print(True)

print(len(thislist))

print(type(thislist))


thatlist = list(("peanuts", "tofu", "fruit rollup")) # note the double round-brackets

print(thatlist)


# change an item in the list
thislist = ["apple", "banana", "cherry", "watermelon", "lemon", "peach"]
print(thislist)

thislist[2] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blueberry", "dragonfruit"]
print(thislist)

hitlist = ["donut", "ale", "jorge"]
hitlist.insert(2, "lemon")
print(hitlist)
