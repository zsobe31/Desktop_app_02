
def hi(name):
    print(f"Hello {name}")

friends = []
while True:
    name = input("Írd ide egy barátod nevét: ")
    if name == "":
        break
    friends.append(name)

for name in friends:
    hi(name)

