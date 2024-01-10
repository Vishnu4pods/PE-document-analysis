import os
from collections import Counter
import glob
import sys

if len(sys.argv) != 2:
    print("Usage: python your_script.py <folder_path>")
    sys.exit(1)
#Only to see where the image is mounted and current dir structure.     
print("INFO:Current objects in present directory" + str(os.listdir(os.getcwd())))  
folder_path = sys.argv[1]
def get_most_common_words(files, num_words=4):
    word_counter = Counter()
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            word_counter.update(words)
    most_common_words = word_counter.most_common(num_words)
    return most_common_words
files = glob.glob(os.path.join(folder_path, '*.txt'))
print("Available files:")
for i, file_path in enumerate(files, start=1):
    print(f"{i}. {os.path.basename(file_path)}")
while True:
    try:
        indices_input = input("Enter the indexes of  files separated by space or type 'exit' to quit: ")
        if indices_input.lower() == 'exit':
            print("Exiting the program.")
            exit()
        selected_files_indices = [int(index) for index in indices_input.split()]
        selected_files = [files[index - 1] for index in selected_files_indices]
        break
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
result = get_most_common_words(selected_files, num_words=4)
print("\nMost four common words in the selected files:")
for word, frequency in result:
    print(f"{word}: {frequency} occurrences")
