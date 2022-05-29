import numpy as np


planets = np.array([
    ["Mercury", 0.055],
    ["Venus", 0.815],
    ["Earth", 1.0],
    ["Mars", 0.107],
    ["Jupiter", 318.2],
    ["Saturn", 95.2],
    ["Uranus", 14.5],
    ["Neptune", 17.1],
])  # array of planets and their gravity
print(planets)
print("There are", len(planets), "planets in our solar system.")
other_planet = ["Pluto", 0.063]
np.vstack((planets, other_planet))  # add a row to the array 
print(planets)
print("Actually, there are", len(planets), "planets in our solar system.")
planets.pop()  # Removes the last item in the list
print("No, there are definitly", len(planets), "planets in our solar system.")

print("The first planet in the solar system is", planets[0])
print("The last planet in the solar system is",
      planets[-1])  # -1 is the last item in the list

jupiter_index = planets.index(["Jupiter", 318.2])  # Finds the index of Jupiter
print("Jupiter is the", jupiter_index + 1, "th planet in the solar system.")
earth_i1, earth_i2 = np.where(planets == "Earth")  # Finds the indices of Earth
print("Earth is the", earth_i1, earth_i2, "th planet in the solar system.")
