#Dictionaries are defined using key : value pairss. You access values
#using a key instead of an index. This makes sense when you have a lot of data.

person = {"name" : "John", "age" : 30, "country" : "Kenya", "city" : "Nairobi"}
b1 = "ages" in person.keys()
print(b1)
#Create a dictionary replica of IEBC voters with ther personal info

#Anthony


#Letina
voterlist = {
    "123456": {
        "age": 30,
        "name": "Brian",
        "city": "Kisumu"
    },
    "136543": {
        "age": 28,
        "name": "Scovia",
        "city": "Narok"
    },
    "918273": {
        "age": 35,
        "name": "Peter",
        "city": "nairobi"
    }
}
print(voterlist["918273"])
print(voterlist["136543"]["city"])

#Abdi


#Ryan
voters={"1000":{"name":"john","city":"nairobi"}, 
        "2000":{"name":"ken","city":"machakos"},
        "3000":["dave","nakuru"]
        }

