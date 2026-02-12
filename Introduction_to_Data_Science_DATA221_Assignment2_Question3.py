# dentify sets of near-duplicate lines.
# • Print the number of such sets.
# • Print the first two sets you find, including line numbers and original lines

lowercase_tokens_without_punctuation = []

with open(file='C:/Users/zaint/Downloads/sample-file.txt', mode='r') as sample_file_for_text_operations:
    for current_line in sample_file_for_text_operations:
        # Remove spaces, lowercase, make single "word"
        single_word = current_line.lower().replace(" ", "")

        #  remove common punctuation
        for punct in '.,!?;:':
            single_word = single_word.replace(punct, "")
        
        lowercase_tokens_without_punctuation.append(single_word.strip())

print(lowercase_tokens_without_punctuation)


