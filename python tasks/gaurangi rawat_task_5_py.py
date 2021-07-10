#Task5
#Prefix a list of strings using List Comprehensions
#Given a list of strings, return a list of strings
#prefixed with 'PREFIX_'
#Input: ['mix', 'xyz', 'apple']
#Output: ['PREFIX_mix', 'PREFIX_xyz', 'PREFIX_apple']
#Note: Only use list comprehensions


#CodeBegins
kritika : list = ['mix', 'xyz', 'apple']

      
k = ["Prefix_" + i  for i in kritika]


print("Output list is : ")
print(k)

print("\n\n\n\n\n\n")



#Filter a dictionary using dictionary comprehensions
#Using dict comprehension create a dictionary from the current
#dictionary where only the key:value pairs with value above 2000
#are taken to the new dictionary.
#Input: {"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
#Ouput: {"NFLX":4950,"TREX":2400}

kriti : dict = {"NFLX" : 4950,"TREX" : 2400,"FIZZ" : 1800, "XPO" : 1700 }


c = {a: s for (a, s) in kriti.items() if s > 2000}


print("Output dictionary is : ")
print(c)
print("\n\n\n\n")




