# Josephus Problem Simulation

def josephus(n, k):
    people = list(range(1, n + 1))  # Create list of people
    index = 0  # Starting index

    while len(people) > 1:
        # Find index of person to eliminate
        index = (index + k - 1) % len(people)
        
        print(f"Eliminated: {people[index]}")
        
        # Remove that person
        people.pop(index)

    return people[0]


# Input
n = int(input("Enter number of people: "))
k = int(input("Enter step count (k): "))

# Solve
survivor = josephus(n, k)

# Output
print("Survivor is:", survivor)