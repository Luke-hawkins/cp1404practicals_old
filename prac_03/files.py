def main():
    OUTPUT_FILE = "name.txt"
    question_1(OUTPUT_FILE)


def question_1(OUTPUT_FILE):
    name = input("Name: ")
    out_file = open(OUTPUT_FILE, 'w')
    print(name, file=out_file)
    out_file.close()


main()
