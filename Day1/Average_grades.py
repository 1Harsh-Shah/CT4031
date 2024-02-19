def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)


def main():
    try:
        with open('students.txt', 'r') as file:
            lines = file.readlines()

        all_grades = []
        for line in lines:
            data = line.strip().split(',')
            student_grades = list(map(float, data[2:]))
            all_grades.extend(student_grades)

        average_grade = calculate_average(all_grades)
        print(f"The average grade of all students is: {average_grade:.2f}")

    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
