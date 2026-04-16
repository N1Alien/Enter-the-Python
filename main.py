# Zadanie 1

name_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

name_dictionary = {name: len(name) for name in name_list}

print(name_dictionary)

# Zadanie 2

number_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]

prime_numbers = [number for number in number_list if number > 1 and all(number % i != 0 for i in range(2, number))]

print(prime_numbers)

# Zadanie 3

incomplete_days = ['pon','śro','pią','sob']

missing_days = ['wto', 'czw', 'nie']

def merge_days(incomplete, missing):
    result = incomplete_days.copy()
    for i, day in enumerate(missing[:-1]):
        result.insert(2 * i + 1, day)
        # print(i, day)
    result.append(missing[-1])
    return result

full_days = merge_days(incomplete_days, missing_days)

print(full_days)

# Zadanie 4

def simple_topo_sort(steps, dependencies):
    ordered = []
    remaining = steps.copy()

    while remaining:
        for step in remaining:
            # print(f"Adding step: {step}")
            # Check if all dependencies are satisfied
            if all(dep[0] in ordered for dep in dependencies if dep[1] == step):
                ordered.append(step)
                # print(f"Ordered: {ordered}")
                remaining.remove(step)
                break

    return ordered

steps = [
    "włącz czajnik",
    "włóż herbatę do kubka",
    "wyjmij kubek",
    "zalej herbatę",
    "znajdź opakowanie herbaty",
    "nalej wody do czajnika",
]

dependencies = [
    ("włóż herbatę do kubka", "zalej herbatę"),
    ("wyjmij kubek", "włóż herbatę do kubka"),
    ("znajdź opakowanie herbaty", "włóż herbatę do kubka"),
    ("nalej wody do czajnika", "włącz czajnik"),
    ("włącz czajnik", "zalej herbatę"),
]

print(simple_topo_sort(steps, dependencies))

