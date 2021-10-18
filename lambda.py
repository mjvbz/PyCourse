people = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "draco", "house": "slytherin"},
    {"name": "cho", "house": "Ravenclaw"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)