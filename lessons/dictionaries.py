"""Dictionaries demonstaTIONS!"""


# eclaring dictionary
schools: dict[str, int]

# initialize into empty dict
schools = dict()

# Set key value pairing
schools["UNC"] = 19400
schools["Puke"] = 6717
schools["NCSU"] = 26150

# print a dict literal representation
print(schools)

# Access a value by its key -- Look-up
print(f"UNC has {schools['UNC']} students!")

# Remove a value from dict by key
schools.pop("Puke")

# Test of existance of a key
is_puke_present: bool = "Puke" in schools
print(f"Puke is present: {is_puke_present}")

# Reassign key-value
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# demonstration of dict literals

# empty dict literal

schools = {}  # same as dict()

# alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Puke": 6717, "NCSU": 26150}
print(schools)
# print(schools["UNCC"])

# looping over keys
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")