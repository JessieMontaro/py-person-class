class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    if people == []:
        return []
    people_class_list = []
    for person in people:
        people_class_list.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        if people[i].get("husband") is not None:
            people_class_list[i].husband = Person.people.get(people[i].get("husband"))
        if people[i].get("wife") is not None:
            people_class_list[i].wife = Person.people.get(people[i].get("wife"))        
    return people_class_list
