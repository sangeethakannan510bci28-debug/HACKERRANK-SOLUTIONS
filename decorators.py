def sort_people(people):
  people.sort(key=lambda person: int(person[2]))
  for person in people:
    yield person

def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

people = [
    ["Mike", "Thomson", "20", "M"],
    ["Robert", "Bustle", "32", "M"],
    ["Andria", "Bustle", "30", "F"]
]

sorted_people = sort_people(people)
print(*map(name_format, sorted_people), sep='\n')
