def age_assignment(*args, **kwargs):
    age = {}
    for name in args:
        first_letter = name[0]
        age[name] = kwargs[first_letter]

    return age


print(age_assignment("Peter", "George", G=26, P=19)) #  {'Peter': 19, 'George': 26}
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61)) #  {'Amy': 22, 'Bill': 61, 'Willy': 36}