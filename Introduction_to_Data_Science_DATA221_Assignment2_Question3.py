# dentify sets of near-duplicate lines.
# • Print the number of such sets.
# • Print the first two sets you find, including line numbers and original lines

lowercase_tokens_without_punctuation = []
near_duplicates = {}
original_lines = []
line_number = 1

with open(file='C:/Users/zaint/Downloads/sample-file.txt', mode='r') as sample_file_for_text_operations:
    for current_line in sample_file_for_text_operations:
        original_lines.append((line_number, current_line.rstrip('\n')))  # Store original
        # Remove spaces, lowercase, make single "word"
        single_word = current_line.lower().replace(" ", "")

        #  remove common punctuation
        for punctuation in '.,!?;:':
            single_word = single_word.replace(punctuation, "")
        
        lowercase_tokens_without_punctuation.append(single_word.strip())
        line_number += 1

# delete white spaces
current_counter = 0
while current_counter < len(lowercase_tokens_without_punctuation):
    if lowercase_tokens_without_punctuation[current_counter] == "":
        lowercase_tokens_without_punctuation.remove(lowercase_tokens_without_punctuation[current_counter])
        original_lines.remove(original_lines[current_counter])  
    else:
        current_counter += 1

# find near-duplicate sets using your normalized tokens
near_duplicates = {}
for current_count_of_the_element_in_the_list in range(len(lowercase_tokens_without_punctuation)):
    normalized = lowercase_tokens_without_punctuation[current_count_of_the_element_in_the_list]
    if normalized not in near_duplicates:
        near_duplicates[normalized] = []
    near_duplicates[normalized].append(original_lines[current_count_of_the_element_in_the_list])

# Find sets with 2+ lines
duplicate_sets = []
for normalized_lines in near_duplicates.values():
    if len(normalized_lines) >= 2:
        duplicate_sets.append(normalized_lines)

print(f"Number of near-duplicate sets: {len(duplicate_sets)}")

# Print first two sets
set_counter = 1
for line_set in duplicate_sets[:2]:
    print(f"\nSet {set_counter}:")
    for line_num, original_line in line_set:
        print(f"  Line {line_num}: {original_line}")
    set_counter += 1