
def my_global_function(a,b):
    """Global Function. return a+b"""
    return a + b

try:
    None.some_method_none_does_not_know_about()
except Exception as ex:
    ex2 = ex
print(ex2.args[0])
print(ex2.__class__)

count_of_three = (1, 2, 5)
try:
    count_of_three[2] = "three"
except TypeError as ex:
    msg = ex.args[0]

print(msg)

locations = [
    ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
    ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
]

print(locations[0][1][2])

try:
    my_global_function(1, 2, 3)
except Exception as e:
    msg = e.args[0]

print(msg)

def whhile():
    i = 1
    result = 1
    while i <= 10:
        result = result * i
        i += 1
    return result

def whhile2():
    i = 0
    result = []
    while i < 10:
        i += 1
        if (i % 2) == 0: continue
        result.append(i)
    return result

print(whhile())
print(whhile2())

round_table = [
    ("Lancelot", "Blue"),
    ("Galahad", "I don't know!"),
    ("Robin", "Blue! I mean Green!"),
    ("Arthur", "Is that an African Swallow or Amazonian Swallow?")
]
result = []
for knight, answer in round_table:
    result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")
    print(knight + ": " + answer + "\n")
print(result)