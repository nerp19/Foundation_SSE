SIGMA = 3.41e-10
EPSILON = 1.65e-21


def bind_energy(r):
    return 4 * EPSILON * ((SIGMA / r) ** 12 - (SIGMA / r) ** 6)


print("Standard index notation can be entered."
      "\nFor example, for 9.2 * 10^(-5) type '9.2e-5'.")

distances = []
synonyms_done = ["done", "d", "do", "don"]

while True:
    radius = input("Please input a distance in metres"
                   " (or type 'done' if finished): ")
    if radius.lower() in synonyms_done:
        break
    try:
        distances.append(float(radius))
    except ValueError:
        print("It doesn't look like that's a number.")

total_bind_energy = sum(bind_energy(d) for d in distances)

two_s_f = "{0:.1e}".format(total_bind_energy)

print("You entered these {} distances in metres: {}"
      .format(len(distances), distances))
print("The total binding energy is {} J."
      .format(two_s_f))
