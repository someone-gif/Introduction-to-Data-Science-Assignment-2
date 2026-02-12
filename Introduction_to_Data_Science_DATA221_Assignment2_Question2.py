#open file in trhe reading mode
lowercase_tokens_without_punctuation = []  # Global list for ALL tokens

with open(file='C:/Users/zaint/Downloads/sample-file.txt', mode='r') as sample_file_for_text_operations:
    # Process each line
    for current_line in sample_file_for_text_operations:
        lowercase_line = current_line.lower()
        separated_tokens_in_the_current_line = lowercase_line.split()
        
        # Process tokens in this line
        for token in separated_tokens_in_the_current_line:
            # Strip punctuation FIRST
            tokens_without_punctuation = token.strip('.,!?;:')
            
            # Check alphabetic characters in CLEANED token
            count_of_alphabetic_characters = 0
            for letter in tokens_without_punctuation:  # Fixed: use cleaned token
                if letter.isalpha():
                    count_of_alphabetic_characters += 1
            
            # Add to GLOBAL list if valid
            if count_of_alphabetic_characters >= 2:
                lowercase_tokens_without_punctuation.append(tokens_without_punctuation)

#Construct bigrams
bigram_of_tokens = []

#add consequtive tokens to the biogram
for token_count in range(len(lowercase_tokens_without_punctuation) - 1):
    first_word_of_the_current_biogram = lowercase_tokens_without_punctuation[token_count]
    second_word_of_the_current_biogram = lowercase_tokens_without_punctuation[token_count + 1]
    current_bigram = (first_word_of_the_current_biogram, second_word_of_the_current_biogram)       
    bigram_of_tokens.append(current_bigram)

print(bigram_of_tokens)

#future biogram frequancy
frequency_of_each_bigram = {} 

#count the biograms
for current_biogram in bigram_of_tokens:
    if current_biogram in frequency_of_each_bigram:
        frequency_of_each_bigram[current_biogram] += 1
    else:
        frequency_of_each_bigram[current_biogram] = 1


bigram_items = list(frequency_of_each_bigram.items())

for first_biogram in range(len(bigram_items)):
    for second_biogram in range(first_biogram + 1, len(bigram_items)):
        # compare counts
        if (bigram_items[second_biogram][1] > bigram_items[first_biogram][1]) or (bigram_items[second_biogram][1] == bigram_items[first_biogram][1] and bigram_items[second_biogram][0] < bigram_items[first_biogram][0]):
            bigram_items[first_biogram], bigram_items[second_biogram] = bigram_items[second_biogram], bigram_items[first_biogram]

#top 5 biograms
number_of_top_bigrams = 5

for biograms in range(min(number_of_top_bigrams, len(bigram_items))):
    (first_biogram, second_biogram), count = bigram_items[biograms]
    print(first_biogram, second_biogram, "->", count)