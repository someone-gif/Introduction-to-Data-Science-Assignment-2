# In this question, you will practice reading a text file and performing basic text preprocessing
# before computing word statistics.
# Using sample-file.txt:
# • Read the file and split it into tokens (words).
# • Convert all tokens to lowercase.
# • Remove punctuation characters from the beginning and end of each token.
# • Keep only tokens that contain at least two alphabetic characters.
# • Count word frequencies and print the 10 most frequent words in descending order in the
# format: word -> count

#open file in trhe reading mode
sample_file_for_text_operations =  open(file = 'C:/Users/zaint/Downloads/sample-file.txt', mode  ='r')

#space holder for the rest of the tokes in the file
all_of_the_separated_tokens_in_the_test_file = []

#for loop that splits each line into tokens and then appends in to the list with every token
for current_line in sample_file_for_text_operations:
    lowercse_line = current_line.lower()
    separated_tokens_in_the_current_line = lowercse_line.split()
    lowercase_tokens_without_punctuation = []

    #remove the punctuation
    for token in separated_tokens_in_the_current_line:
        tokens_without_punctuation = token.strip('.,!?;:') 
        lowercase_tokens_without_punctuation.append(tokens_without_punctuation)

        #check alphabetic characters
        count_of_alphabetic_characters = 0
        for letter in token:
            if letter.isalpha():
                count_of_alphabetic_characters += 1

        if count_of_alphabetic_characters >= 2:
            lowercase_tokens_without_punctuation.append(token)

#Count word frequencies using a dictionary
word_frequencies_in_the_file = {}
for word in lowercase_tokens_without_punctuation:
    if word in word_frequencies_in_the_file:
        #increments the word count by 1 every time the word apears
        word_frequencies_in_the_file[word] += 1
    else:
        word_frequencies_in_the_file[word] = 1

# Sort by frequency, then by word 
tokens_in_the_dictionary = list(word_frequencies_in_the_file.items())

for first_token in range(len(tokens_in_the_dictionary)):
    for second_token in range(first_token + 1, len(tokens_in_the_dictionary)):
        # sort by count descending, then word ascending
        if (tokens_in_the_dictionary[second_token][1] > tokens_in_the_dictionary[first_token][1]) or (tokens_in_the_dictionary[second_token][1] == tokens_in_the_dictionary[first_token][1] and tokens_in_the_dictionary[second_token][0] < tokens_in_the_dictionary[first_token][0]):
            tokens_in_the_dictionary[first_token], tokens_in_the_dictionary[second_token] = tokens_in_the_dictionary[second_token], tokens_in_the_dictionary[first_token]

# Print top 10
top_10_most_frequent_tokens = 10
for i in range(min(top_10_most_frequent_tokens, len(tokens_in_the_dictionary))):
    word, count = tokens_in_the_dictionary[i]
    print(word, "->", count)

    


    
    all_of_the_separated_tokens_in_the_test_file.extend(lowercase_tokens_without_punctuation)


print(all_of_the_separated_tokens_in_the_test_file)
