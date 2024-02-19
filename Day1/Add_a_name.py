def add_student(filename):
    # Prompt the user for student information
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")

    # Format the student information
    student_info = f"{name},{age},{grade}\n"

    try:
        # Open the file in append mode and write the student information
        with open(filename, 'a') as file:
            file.write(student_info)
        print("Student information added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'students.txt' with the path where you want to store the student information
add_student('students.txt')
