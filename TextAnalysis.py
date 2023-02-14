# Assignment 5: Read a text file and generate the following information:
#   1) Total word count (number of words in the file)
#   2) Total stopword count (number of stopwords in the file)
#   3) List of words, and their frequencies, that occur >= 20 times

# this import is needed to reference the String constant, string.punctuation
import string


# Main logic that calls the functions for this program. Do NOT modify.
def main():
    # Call create_stopwords_list() which will return a list of stopwords
    stopwords_list = create_stopwords_list()

    # Call calculate_word_frequencies(stopwords_list) which will return a dictionary of word_frequencies (key=word, value=frequency)
    word_frequencies = calculate_word_frequencies(stopwords_list)

    # Display the results as shown in the assignment description
    display_results(word_frequencies)


# Open and read the stopwords.txt file.
# Each line in the file contains a stopword to be added to the stopwords list.
# Open the file with the encoding argument, like this: open(filename, 'r', encoding='utf8')
# feels like it should work but does not
def create_stopwords_list():
    filename = 'stopwords.txt'
    stop_words = [] # initializes list of stopwords to an empty list
    try:
        stop_words_file = open(filename, 'r', encoding='utf-8')
        for stop_word in stop_words_file:
            stop_word = stop_word.strip().lower()
            stop_words.append(stop_word)
        print(stop_words)
        return stop_words
    except FileNotFoundError as err:
        print('Error: cannot find file,', filename)
        print('Error:', err)
    except OSError as err:
        print('Error: cannot access file,', filename)
        print('Error:', err)
    except Exception as err:  # catch all error handler, if the above handlers do not apply
        print('An unknown error occurred')
        print('Error:', err)


# This function creates a word_frequencies dictionary where
#   key = word from the file
#   value = frequency, i.e., the number of times the word appears in the file
#   Open and read the Alice-in-Wonderland.txt file. Use the encoding argument, like this: open(filename, 'r', encoding='utf8')
# Call tokenize_text(line_of_text) for each line in the file to obtain a list of the tokenized words in the line.
# For each word, either increment its frequency in the dictionary,
#  or increment the stopword counter if the word is in the stopwords list.
# After reading the file, display the total number of words, and total number of stopwords.
def calculate_word_frequencies(stopwords):
    filename = 'Alice-in-Wonderland.txt'
    total_count = 0
    stopwords_count = 0
    freq = {}
    # goes through each word in the alice and wonderland text and tokenizes them
    alice_in_wonderland = open(filename, 'r', encoding='utf-8')
    file_contents = alice_in_wonderland.read()
    alice_in_wonderland.close()
    tokens = tokenize_text(file_contents)
    # counts the total number of words and stop words
    for token in tokens:
        total_count = total_count + 1
        for stopword in stopwords:
            if token == stopword:
                stopwords_count = stopwords_count + 1

    # prints the total number of words and stopwords to check if it's working so far
    print(stopwords_count)
    print(total_count)
    # creates a dictionary
    # checks the frequency of tokens and adds them to the dictionary
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    # prints the frequency dictionary to see if it is working
    print(freq)
    # returns the dictionary
    return freq


# Creates a list of words found in line_of_text using the split function.
# Removes leading/trailing punctuation from each word in the list.
# Converts each word to lower case, and returns the list of normalized words
# Refer to Text Analysis slides for examples
# This function returns a list of tokenized (and lower case) words
def tokenize_text(line_of_text):
    final_tokens = []
    tokenized_words = line_of_text.split()
    for tokenized_word in tokenized_words:
        tokenized_word = tokenized_word.strip(string.punctuation).lower()
        final_tokens.append(tokenized_word)
    return final_tokens


# Sorts the dictionary of word_frequencies in descending order and
# displays those that have frequencies >= 20.
# You do NOT need to change this function -- it should work as is.
def display_results(word_frequencies):
    # print(word_frequencies)
    if word_frequencies:
        sorted_by_frequency = ((k, word_frequencies[k]) for k in
                               sorted(word_frequencies, key=word_frequencies.get, reverse=True))
        print("\nWords with frequencies >= 20")
        print(format('WORD', '<15'), format('FREQUENCY', '>12'))
        for k, v in sorted_by_frequency:
            if v >= 20:
                print(format(k, '<12'), format(v, '>10'))
    else:
        print('No word frequencies found')


main()
