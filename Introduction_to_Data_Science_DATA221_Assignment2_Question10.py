def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain keyword
    (case-insensitive). Line numbers start at 1.
    """
    matches = []
    line_number = 1
    
    with open(filename, 'r') as file:
        for current_line in file:
            # Case-insensitive search
            if keyword.lower() in current_line.lower():
                matches.append((line_number, current_line.rstrip('\n')))
            line_number += 1
    
    return matches

# Test the function
filename = 'C:/Users/zaint/Downloads/sample-file (1).txt'
keyword = 'lorem'

matching_lines = find_lines_containing(filename, keyword)

print(f"Found {len(matching_lines)} matching lines")

# Print first 3 matching lines
line_counter = 1
for line_num, line_text in matching_lines[:3]:
    print(f"Line {line_num}: {line_text}")
    line_counter += 1
