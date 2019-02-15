from packages.classes import planet

from packages.calc import planet_mass,planet_vol

naboo = planet("naboo",18,122)

naboo_mass=planet_mass(naboo.gravity,naboo.radius)
naboo_vol=planet_vol(naboo.radius)

print(f"{naboo.name} has a mass of {naboo_mass} and a vole {naboo_vol}")
