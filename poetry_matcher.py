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
    print("There were {} matches and {} misses for a for a final percent of {}%".format(hits, misses, round((hits/misses)*100, 2)))

def get_lines():
    while True:
        num_lines = input("Select how many lines you would like to attempt to match.")
        try:
            num_lines = int(num_lines)
            if num_lines > 0:
                return num_lines
            else:
                print("Please enter a positive integer.")
        except:
            print("That's not an integer!")

def line_checker(poem_lines):
    selected_line = random.choice(poem_lines).lower()
    failed_matches = 0
    for line in poem_lines:
        if line.lower() == selected_line:
            pass
        else:
            for word in line.lower().split():
                if len(word) > 3 and re.match(word, selected_line):
                    print("The line \n{}\n and the line \n{}\n share the word \"{}\" and there were {} failed matches".format(selected_line, line, word, failed_matches))
                    return True
                else:
                    pass
            failed_matches += 1
    print("{} failed to match".format(selected_line))
    return False


if __name__ == '__main__':
    main()
