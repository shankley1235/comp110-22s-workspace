"""Demo some dict abilities"""


# Declaring the type of a dict
school: dict[str, int]

# Initialize to an empty dict
schools = dict()

# Set a key-value pairing in dict
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dict literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dict
# BY ITS KEEEYYY!
schools.pop("Duke")

# Test or the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["NCSU"] += 200

print(schools)

# Demo of dict literals
schools = {}  # Empty dict literal

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 4567876}


for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
