message = "Hello Python"
print(message)

name = "ada lovelace"

print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

greeting_ada = f"Hello, {full_name.title()}!"
print(greeting_ada)


x, y, z = 0, 0, 0

numbers = f"{x} {y} {z}"
print(numbers)

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles.append('ducati')

print(motorcycles)

del motorcycles[3]

print(motorcycles)

motorcycles.append('ducati')

ducati = motorcycles.pop()

print(ducati)

print(motorcycles)


cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)

# cars.sort()
# cars.sort(reverse=True)
# print(cars)

print(sorted(cars))

print(cars)

print(cars.reverse())

print(len(cars))