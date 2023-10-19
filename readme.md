# Microservices Documentation

This project encompasses three distinct microservices, each residing in its own container. The orchestration and deployment of these containers can be achieved using Docker Compose with the command `docker-compose up --build` in the main project directory.

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

---

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

---

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

---

## Building and Running the Microservices

To build and run all three microservices containers, execute the following command in the main project directory:

```bash
docker-compose up --build
