import random
import sys

def main():
    input_file = sys.argv[1] #sys and sys.argv found on stack overflow
    with open(input_file) as f: #opens the file
        poem_lines = [line for line in f]
    num_lines = get_lines()
    while num_lines > 0:
        line_checker(poem_lines)
        num_lines -= 1


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
    selected_line = random.choice(poem_lines)
    print(selected_line)
    print(type(poem_lines))
    print(type(selected_line))
    return True



if __name__ == '__main__':
    main()
