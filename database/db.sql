-- Create the "school" table
CREATE TABLE school (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Create the "users" table
CREATE TABLE users (
    id UUID PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    school_id UUID NOT NULL,
    FOREIGN KEY (school_id) REFERENCES school(id)
);

-- Create the "courses" table
CREATE TABLE courses (
    id UUID PRIMARY KEY,
    course_code VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    professor_name VARCHAR(100),
    professor_email VARCHAR(100),
    description TEXT,
    school_id UUID NOT NULL,
    FOREIGN KEY (school_id) REFERENCES school(id)
);

-- Create the "user_courses" table
CREATE TABLE user_courses (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    course_id UUID NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create the "documents" table
CREATE TABLE documents (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100) NOT NULL,
    url VARCHAR(255) NOT NULL,
    class_id UUID,
    assignment_id UUID,
    user_id UUID,
    FOREIGN KEY (class_id) REFERENCES courses(id),
    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the "events" table
CREATE TABLE events (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    description TEXT,
    end_time TIMESTAMP,
    priority INTEGER,
    course_id UUID,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create the "assignments" table
CREATE TABLE assignments (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    due_date TIMESTAMP NOT NULL,
    description TEXT,
    priority INTEGER,
    completed BOOLEAN,
    course_id UUID NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create the "tasks" table
CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date TIMESTAMP NOT NULL,
    description TEXT,
    priority INTEGER,
    completed BOOLEAN,
    assignment_id UUID,
    course_id UUID,
    event_id UUID,
    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (event_id) REFERENCES events(id)
);
