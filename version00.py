# distances = [6.82e-10]
distances = [4.1e-10, 2e-10, 3.41e-10]

sigma = 3.41e-10
epsilon = 1.65e-21

bind_energy = 0

for r in distances:
    bind_energy += 4 * epsilon * ((sigma/r)**12 - (sigma/r)**6)

print(bind_energy)
