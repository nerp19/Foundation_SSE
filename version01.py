sigma = 3.41e-10
epsilon = 1.65e-21

distances = []
done = ["Done", "done", "D", "d", "Do", "do", "Don", "don"]

while True:
    radius = input("Please input a distance in metres (or type 'done' if finished): ")
    if radius in done:
        break
    distances.append(float(radius))

bind_energy = 0

for r in distances:
    bind_energy += 4 * epsilon * ((sigma/r)**12 - (sigma/r)**6)

two_s_f = "{0:.1e}".format(bind_energy)

print("You entered these {} distances in metres: {}".format(len(distances), distances))
print("The binding energy is {} J.".format(two_s_f))
