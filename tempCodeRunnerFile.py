def get_pirate_gold_array(num_pirates):
    # Step 1: Calculate total gold
    total_gold = num_pirates * 20
    bribes = []
    
    # Step 2 & 3: Loop and alternate 0s and 1s for the crew
    # (We use num_pirates - 1 because we are leaving Amaro out for now)
    for i in range(num_pirates - 1):
        if i % 2 == 0:
            bribes.append(0)  # Even positions get 0
        else:
            bribes.append(1)  # Odd positions get 1
            
    # Step 4: Calculate Amaro's share and stick him at the front
    total_bribes_given = sum(bribes)
    amaro_share = total_gold - total_bribes_given
    
    # Return the final array with Amaro at index 0
    return [amaro_share] + bribes

# Test it with 5 pirates
print(get_pirate_gold_array(5)) 
# Output: [98, 0, 1, 0, 1]