-- Create section_enum type
CREATE TYPE section_enum AS ENUM ('Lecture', 'Discussion', 'Quiz');

-- Create status_enum type
CREATE TYPE status_enum AS ENUM ('TODO', 'IN_PROGRESS', 'COMPLETE');

-- Create the "school" table
CREATE TABLE schools (
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
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

-- Create the "courses" table
CREATE TABLE courses (
    id UUID PRIMARY KEY,
    course_code VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    description TEXT,
    units DOUBLE PRECISION,
    school_id UUID NOT NULL,
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

-- Create the "sections" table
CREATE TABLE sections (
    id UUID PRIMARY KEY,
    section_id VARCHAR(100) NOT NULL,
    section_type section_enum NOT NULL,
    days VARCHAR(100) NOT NULL,
    start_time TIME NOt NULL,
    end_time TIME NOT NULL,
    instructor_first_name VARCHAR(100) NOT NULL,
    instructor_last_name VARCHAR(100) NOT NULL,
    instructor_email VARCHAR(100),
    description TEXT,
    grading_scale TEXT,
    location VARCHAR(100),
    course_id UUID NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create the "user_sections" table
CREATE TABLE user_sections (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    section_id UUID NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (section_id) REFERENCES sections(id)
);



-- Create the "assignments" table
CREATE TABLE assignments (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    due_date TIMESTAMP NOT NULL,
    status status_enum NOT NULL,
    description TEXT,
    priority INTEGER,
    section_id UUID NOT NULL,
    user_id UUID NOT NULL,
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the "documents" table
CREATE TABLE documents (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100) NOT NULL,
    url TEXT NOT NULL,
    section_id UUID,
    assignment_id UUID,
    user_id UUID,
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the "events" table
CREATE TABLE events (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    description TEXT,
    priority INTEGER,
    section_id UUID,
    user_id UUID NOT NULL,
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create the "tasks" table
CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date TIMESTAMP NOT NULL,
    status status_enum NOT NULL,
    description TEXT,
    priority INTEGER,
    assignment_id UUID,
    section_id UUID,
    event_id UUID,
    user_id UUID NOT NULL,
    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (event_id) REFERENCES events(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
