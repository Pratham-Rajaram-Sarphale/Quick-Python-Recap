people=[
{'name':'harry','house':'gryffindor'},
{'name':'cho','house':'ravenclaw'},
{'name':'draco','house':'slytherin'}
]


people.sort(key=lambda person: person['name'])
print(people)