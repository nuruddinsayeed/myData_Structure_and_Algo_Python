import math
import statistics

arr = [25, 12, 18, 42, 9, 4, 71, 85, 19, 14, 11,
       12, 17, 29, 44, 45, 1, 33, 37, 18, 14, 28]


def area(r):
    return format(math.pi * (r ** 2), ".4f")


areas = list(map(area, arr))

print(areas)

# wit tuples
temps = [("Banglades", 30), ("Uk", 10),
         ("US", 20), ("Germany", 10)]


# c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)
def c_to_f(data): return data[0], format((9 / 5) * data[1] + 32, ".2f")


print(list(map(c_to_f, temps)))


# Filter Funciton
avg = statistics.mean(arr)
print(avg)
bellw_avg_list = list(filter(lambda x: x < avg, arr))
print(bellw_avg_list)

# filter emty sting
countries = ["bd", "uk", "", "0fk", "", "Jb"]
print(list(filter(None, countries)))
#['bd', 'uk', '0fk', 'Jb']

print(list(filter(lambda x: ("0" not in x), countries)))
#['bd', 'uk', '', '', 'Jb']
