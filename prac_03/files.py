def main():
    OUTPUT_FILE_FOR_NAME = "name.txt"
    OUTPUT_FILE_FOR_NUMBERS = "numbers.txt"
    # question_1(OUTPUT_FILE_FOR_NAME)
    # question_2(OUTPUT_FILE_FOR_NAME)
    question_3(OUTPUT_FILE_FOR_NUMBERS)


def question_1(OUTPUT_FILE_FOR_NAME):
    name = input("Name: ")
    out_file = open(OUTPUT_FILE_FOR_NAME, 'w')
    print(name, file=out_file)
    out_file.close()


def question_2(OUTPUT_FILE_FOR_NAME):
    out_file = open(OUTPUT_FILE_FOR_NAME, 'r')
    for line in out_file:
        print(f"Your name is {line.title()}")
    out_file.close()


def question_3(OUTPUT_FILE_FOR_NUMBERS):
    total = 0
    out_file = open(OUTPUT_FILE_FOR_NUMBERS, 'r')
    total += int(out_file.readline())
    total += int(out_file.readline())
    print(f"The total of the first 2 lines is {total}")


main()
