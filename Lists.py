from pickletools import pylist


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist[1:2] = ["blackcurrant", "watermelon"]
thislist.append("orange")
thislist.insert(1, "orange")

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

thislist.remove("banana")
thislist.pop(1)
thislist.pop()
del thislist[0]
del thislist
thislist.clear()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
mylist = thislist.copy()

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)