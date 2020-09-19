stats = {
    "name": "Clark Kent",
    "alias": "Superman",
    "super_powers": ["Flight", "Strength", "Speed", "Heat Vision"]
}


class SuperHero():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)


supe = SuperHero(stats)

print(supe.name)
print(supe.super_powers)

for attr in ["name", "origin", "alias", "super_powers"]:
    print(getattr(supe, attr, "Not defined"))

stats_to_delete = ["isHuman", "super_powers"]

for stat in stats_to_delete:
    if hasattr(supe, stat):
        delattr(supe, stat)

for attr in ["name", "origin", "alias", "super_powers"]:
    print(getattr(supe, attr, "Not defined"))


print(supe.name)
print(supe.super_powers)
