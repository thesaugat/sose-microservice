# Microservices Documentation

Welcome to the documentation for our Microservices project! This project is divided into three microservices, each
encapsulated within its own container. Below, you'll find detailed information about each microservice, including
endpoints, functionalities, and instructions on building and running the project.

## Table of Contents

- [1. Student Online Identity Creation](#1-student-online-identity-creation)
- [2. Library Service](#2-library-service)
- [3. Course Enrollment Service](#3-course-enrollment-service)
- [Building and Running the Microservices](#building-and-running-the-microservices)

## 1. Student Online Identity Creation

### Endpoints:

1. **Login**
    - **URL:** `/login`
    - **Method:** POST
    - **Parameters:**
        - `email` (string): Email of the student
        - `password` (string): Password for authentication
    - **Description:** Initiates a login process, authenticating the student's account.

2. **Signup**
    - **URL:** `/signup`
    - **Method:** POST
    - **Parameters:**
        - `email` (string): Email of the student
        - `password` (string): Password for account creation
        - `name` (string): Full name of the student
        - `phone_number` (string): Phone number of the student
        - `year` (integer): Year of enrollment
    - **Description:** Creates a new student account with the provided details.

3. **Student List**
    - **URL:** `/studentlist`
    - **Method:** GET
    - **Description:** Retrieves and displays the list of all students.

### Admin Login:

- **Email:** admin@uow.com
- **Password:** Test123

### Student Test Account:

- **Email:** student@uow.com
- **Password:** Stud123

## 2. Library Service

### Endpoints:

1. **Book List**
    - **URL:** `/book`
    - **Method:** GET
    - **Description:** Fetches and presents a list of available books in the library.

2. **Upload Book**
    - **URL:** `/book`
    - **Method:** POST
    - **Parameters:**
        - `title` (string): Title of the book
        - `author` (string): Author of the book
    - **Description:** Adds a new book to the library collection with the provided details.

3. **Books Borrow**
    - **URL:** `/books-borrow`
    - **Method:** POST
    - **Parameters:**
        - `student_id` (string): ID of the student borrowing the book
        - `book_id` (string): ID of the book being borrowed
    - **Description:** Records the borrowing of a book by a student.

## 3. Course Enrollment Service

### Endpoints:

1. **Course List**
    - **URL:** `/course`
    - **Method:** GET
    - **Description:** Retrieves and presents a list of available courses.

2. **Upload Course**
    - **URL:** `/course`
    - **Method:** POST
    - **Parameters:**
        - `title` (string): Title of the course
        - `code` (string): Code of the course
        - `credit` (integer): Credit hours for the course
    - **Description:** Adds a new course to the list of available courses.

3. **Course Enroll**
    - **URL:** `/course-enroll`
    - **Method:** POST
    - **Parameters:**
        - `student_id` (string): ID of the student enrolling in the course
        - `course_id` (string): ID of the course being enrolled
    - **Description:** Records the enrollment of a student in a course.

## Building and Running the Microservices

### Prerequisites:

- Docker installed on your machine

### Installation Steps:

1. Clone this repository: `git clone https://github.com/thesaugat/sose-microservice.git`
2. Navigate to the project directory: `cd sose-microservice`
3. Build and run the microservices containers: `docker-compose up --build`

This command will build the Docker images for each microservice and start the containers.

**Note:** The necessary data has already been seeded, including an admin account and a test student account.

Feel free to explore each microservice's documentation for detailed information about the available endpoints and
functionalities.
