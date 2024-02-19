def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found!")

# Replace 'filename.txt' with the path to your .txt file
read_file('students.txt')
