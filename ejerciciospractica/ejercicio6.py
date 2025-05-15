courses = {
    "titles": [],
    "durations": [],
    "enrollments": []
}

def main():
    menu()

def menu():
    while True:
        print("1. Register a new course")
        print("2. Update number of enrolled students")
        print("3. Filter courses by minimum duration")
        print("4. Exit")

        option = int(input("Choose an option: "))
        
        if option == 1:
            add_course()
        elif option == 2:
            update_enrollment()
        elif option == 3:
            filter_by_hours()
        elif option == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def add_course():
    title = input("Enter course title: ")
    duration = int(input("Enter course duration (in hours): "))
    enrolled = int(input("Enter number of enrolled students: "))

    courses["titles"].append(title)
    courses["durations"].append(duration)
    courses["enrollments"].append(enrolled)
    print(f"Course '{title}' has been registered.")

def update_enrollment():
    title = input("Enter the course title to update enrollment: ")
    index = courses["titles"].index(title)
    new_enrollment = int(input("Enter new number of enrolled students: "))
    courses["enrollments"][index] = new_enrollment
    print("Enrollment updated.")

def filter_by_hours():
    min_duration = int(input("Enter minimum course duration (in hours): "))
    print(f"\nCourses with at least {min_duration} hours:")
    for i in range(len(courses["titles"])):
        if courses["durations"][i] >= min_duration:
            print(f"- {courses['titles'][i]} | {courses['durations'][i]}h | {courses['enrollments'][i]} students")