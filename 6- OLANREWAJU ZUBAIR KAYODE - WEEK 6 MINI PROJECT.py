#!/usr/bin/env python
# coding: utf-8

# ### Project 1: Air traffic control simulation

# In[ ]:


"""Problem: Imagine you're an air traffic controller during a busy day at the airport. Due to an emergency, some 
flights need to make an emergency landing. Design a system that prioritizes these emergency landings over 
regular scheduled flights. Develop a program that takes flight details, including emergency status, and 
manages the landing queue efficiently.
- Display the sequence of servicing emergency landing flights and scheduled flights
- Design classes to manage flights and prioritize emergency situations.
- Practice working with queues to manage the order of operations.
- Understand the importance of prioritization in real-time systems
- Gain experience in managing and servicing tasks based on urgency.
""""


# ### SOLUTION

# In[6]:


# create a class for a flight
class flight:
    def __init__(self, flight_number, emergency = False):
        self.flight_number = flight_number
        self.emergency = emergency


# In[7]:


# create an empty list for the landing sequence
landing_sequence = []


# In[8]:


# create a function to add the flight to the landing squence
def add_flight_to_sequence(flight):
    if flight.emergency:
        landing_sequence.insert(0, flight) # this will help insert the emergency flight
    else:
        landing_sequence.append(flight)


# In[9]:


# create a fuuction for service flight
def service_flights():
    while landing_sequence:
        flight = landing_sequence.pop(0)
        print(f'servicing flight {flight.flight_number}')


# In[12]:


# the air control system

if __name__ == '__main__':
    # create sample flight, the flight with emergency that is true will come first in the squence  
    flight1 = flight("KAYODE AIRLINE", emergency = False)
    flight2 = flight("OGA DAMS AIRLINE", emergency = False)
    flight3 = flight("ZUBAIR AIRLINR", emergency = True)
     
    # add flight to the sequence    
    add_flight_to_sequence(flight1)
    add_flight_to_sequence(flight2)
    add_flight_to_sequence(flight3)
    
    # calling service flight
    print("air traffic control")
    service_flights()


# ### Project 2: File handling – word counter

# In[ ]:


'''

Project 2: File handling – word counter
Problem: You are tasked with developing a plagiarism detection system for a school. Given a text file containing a 
student's essay and a set of reference files, you need to determine if any part of the essay is copied from the 
reference materials.
Design a program that reads and compares the essay with the reference files to identify potential plagiarism instances.
- Display the frequency of each word in the provided text file.
- Learn how to read and process data from text files using file handling.
- Practice tokenization of text into words for analysis.
- Understand the basics of counting and analyzing data frequencies.
- Gain experience in creating a simple text data analysis tool.

'''


# ### SOLUTION

# In[ ]:


# Function to read a text file and return its content as a string
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Function to tokenize text into words
def tokenize_text(text):
    words = text.split()
    return words

# Function to count word frequencies in a list of words
def count_word_frequencies(word_list):
    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

# Function to compare two lists of words and find common words
def find_common_words(list1, list2):
    return list(set(list1) & set(list2))

# Function to check for potential plagiarism
def check_plagiarism(student_words, reference_words_list):
    plagiarism_found = False
    for index, reference_words in enumerate(reference_words_list):
        common_words = find_common_words(student_words, reference_words)
        if common_words:
            plagiarism_found = True
            print(f"Potential Plagiarism in Reference File {index + 1}:")
            print("Common Words:", common_words)
    return plagiarism_found

# Read the student's essay
student_essay = read_file('student_essay.txt')  # replace with actual file name

# Read the reference files (you can have multiple reference files)
reference_files = ['reference1.txt', 'reference2.txt']

reference_texts = []
for reference_file in reference_files:
    reference_text = read_file(reference_file)
    reference_texts.append(reference_text)

# Tokenize the student's essay
student_words = tokenize_text(student_essay)

# Tokenize the reference texts
reference_words_list = []
for reference_text in reference_texts:
    reference_words = tokenize_text(reference_text)
    reference_words_list.append(reference_words)

# Calculate word frequencies in the student's essay
student_word_freq = count_word_frequencies(student_words)

# Display the word frequencies
print("Word Frequencies in Student's Essay:")
for word, freq in student_word_freq.items():
    print(f"{word}: {freq}")

# Check for potential plagiarism
plagiarism_detected = check_plagiarism(student_words, reference_words_list)

if not plagiarism_detected:
    print("No potential plagiarism detected in the essay.")

