#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)  # Initialize all boxes as locked
    unlocked[0] = True  # The first box is unlocked
    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop()  # Get a key
        for key in boxes[current_key]:  # Check all keys in the current box
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add the key to the list to explore further

    # Return True if all boxes are unlocked
    return all(unlocked)
