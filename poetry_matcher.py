import random
import sys
import re

def main():
    input_file = sys.argv[1] #sys and sys.argv found on stack overflow
    with open(input_file) as f: #opens the file
        poem_lines = [line for line in f]
    num_lines = get_lines()
    hits = 0
    misses = 0
    while num_lines > 0:
        if line_checker(poem_lines):
            hits += 1
        else:
            misses += 1
        num_lines -= 1
    print("There were {} matches and {} misses for a for a final percent of {}%".format(hits, misses, round((hits/(hits+misses))*100, 2)))

def get_lines():
    while True:
        num_lines = input("Select how many line-pairs you would like to attempt to match.\n==> ")
        try:
            num_lines = int(num_lines)
            if num_lines > 0:
                return num_lines
            else:
                print("Please enter a positive integer.")
        except:
            print("That's not an integer!")

def line_checker(poem_lines):
    poem_lines = [re.sub(r'[^\s\w]', '', line) for line in poem_lines]
    random.shuffle(poem_lines)
    selected_line = poem_lines[0].lower()
    matched_line = poem_lines[1].lower()
    for word in matched_line.split():
        if len(word) > 3 and re.match(word, selected_line):
            print("Two lines share the word {}, They are: \n{}\n{}\n{}\n{}".format(word, "-"*80, selected_line, matched_line, "-"*80))
            return True
        else:
            pass
    return False


if __name__ == '__main__':
    main()
