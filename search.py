import json

# Load the JSON data from file
with open('tricks.json') as f:
    data = json.load(f)

# List of trigger_id values to search for
trigger_ids = [240, 229]

# Iterate through each object in the JSON data
for obj in data:
    # Extract the trick sequence array from the object
    trick_sequence = obj['trick_sequence']
    # Iterate through each trigger in the trick sequence
    for i in range(len(trick_sequence)):
        # Check if the current trigger has one of the trigger_id values
        if trick_sequence[i]['trigger_id'] in trigger_ids:
            # Check if the next triggers have the consecutive trigger_id values
            j = i + 1
            k = 1
            while j < len(trick_sequence) and trick_sequence[j]['trigger_id'] == trigger_ids[k % len(trigger_ids)] and int(trick_sequence[j]['order']) == int(trick_sequence[j-1]['order']) + 1:
                j += 1
                k += 1
            # If all trigger_id values are found consecutively, print the information
            if k == len(trigger_ids):
                print(f"ID: {obj['id']}, Name: {obj['name']}")
