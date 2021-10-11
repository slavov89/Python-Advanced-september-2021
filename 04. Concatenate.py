# def concatenate(*args):
#     text = [el for el in args]
#     return "".join(text)

def concatenate(*args):
    text = ""
    for el in args:
        text += el
    return text

print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
