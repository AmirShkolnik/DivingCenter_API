<p align="center">
  <img src="doc/images/logo.jpg" alt="Diving Center Logo" style="width: 250px; height: auto;">
</p>
<h1 align="center">Diving Center API - Django Rest Framework</h1>

[Diving Center Django Rest Framework API Backend Live Link](https://pp5api-divingspace-f0baea7c564e.herokuapp.com/)

[Diving Center React Frontend Live Link](https://divingspace-900b5a3db777.herokuapp.com/)

[Diving Center React Frontend Github Repo](https://github.com/AmirShkolnik/DivingCenter)

[Diving Center DRF API Testing](TESTING.md)

## Project Goals

### Diving Center - A Community for Scuba Enthusiasts

* **Build a thriving online community:** Build a welcoming space for scuba divers of all levels to connect, share experiences, and learn from each other. [Click to watch the diving center home page](https://divingspace-900b5a3db777.herokuapp.com/courses)

* **Simplify course booking and management:** Allow divers to easily browse and book diving courses directly through the platform. [Courses page](https://divingspace-900b5a3db777.herokuapp.com/courses) ; [Course review and rating](https://divingspace-900b5a3db777.herokuapp.com/courses/advanced-open-water-diver) ; [Contact form](https://divingspace-900b5a3db777.herokuapp.com/contactus)

* **Enhance learning and discovery:** Provide a platform for logged in members to share their diving experiences, reviews, and photos, enriching the knowledge base for the community.

* **Empower user interaction:**  Enable logged in members to follow each other, like and comment on posts, creating a dynamic and engaging social experience. [Click to watch users feed](https://divingspace-900b5a3db777.herokuapp.com/feed)

**Technology Stack:**

* **Django REST Framework (Backend):** A powerful Python web framework that provides a robust foundation for building APIs (Application Programming Interfaces). These APIs will handle data management and communication between the application's frontend and backend. [Diving Center Django Rest Framework API Backend Live Link](https://pp5api-divingspace-f0baea7c564e.herokuapp.com/)

* **React (Frontend):** A popular JavaScript library for building user interfaces. React allows for the creation of interactive and responsive web pages that adapt to different devices. [Diving Center React Frontend Live Link](https://divingspace-900b5a3db777.herokuapp.com/)

**Key functionalities:**

* **User Management:**  Support for both regular users and admin accounts.

* **Course Management:**  Divers can view course information, book courses, and leave reviews. 

* **Content Sharing:**  Divers can create posts, share images, and interact with each other's content through likes, comments, and follows.

* **Admin Panel:**  Admins can manage user accounts, courses, and website content.

This combination of technologies empowers a feature-rich and interactive online platform catering to the needs of scuba diving enthusiasts.

[Visit Our Diving Center Website](https://divingspace-900b5a3db777.herokuapp.com/)

## Table of contents
- [Project Goals](#project-goals)
- [Table of contents](#table-of-contents)
- [Planning](#planning)
- [Data Models](#data-models)
- [API Endpoints](#api-endpoints)
- [Frameworks, Libraries, and Dependencies](#frameworks-libraries-and-dependencies)
- [Testing and Validation](#testing-and-validation)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Cloning and Forking](#cloning-and-forking)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

Based on the information provided and the structure you've requested, here's a robust project planning for your diving center project, covering both backend and frontend development over an 8-week period:

## Planning

### Project Overview

This project is a comprehensive web application for a diving center. It allows users to view diving courses, book courses, leave reviews, and interact with a community of divers. The application will have a Django backend with a REST API, and a React frontend. Key features include user authentication, course management, booking system, review system, and a community feed.

### Objectives

1. Develop a secure and scalable backend API using Django and Django REST Framework.
2. Create an intuitive and responsive frontend using React.
3. Implement user authentication and authorization.
4. Develop a course management system with detailed course pages.
5. Create a booking system for users to reserve courses.
6. Implement a review and rating system for courses.
7. Develop a community feed for user interactions.
8. Ensure the application is responsive and works well on various devices.

### Timeline

#### Week 1: Project Setup and Backend Foundations
- Day 1-2: Project initialization, environment setup
- Day 3-4: Database design, create Django models (User, Course, Booking, Review)
- Day 5: Set up Django REST Framework, create basic API views

#### Week 2: Backend Development - Core Features
- Day 1-2: Implement user authentication (registration, login, logout)
- Day 3-4: Develop course API endpoints (list, detail, create, update, delete)
- Day 5: Create booking system API endpoints

#### Week 3: Backend Development - Advanced Features
- Day 1-2: Implement review system API endpoints
- Day 3-4: Develop community feed API endpoints
- Day 5: Add filtering, pagination, and search functionality to API

#### Week 4: Backend Finalization and Frontend Setup
- Day 1-2: Backend testing and bug fixes
- Day 3: API documentation
- Day 4-5: Set up React project, implement routing, create basic components

#### Week 5: Frontend Development - Core Features
- Day 1-2: Implement user authentication on frontend
- Day 3-4: Develop course listing and detail pages
- Day 5: Create booking form and integration with API

#### Week 6: Frontend Development - Advanced Features
- Day 1-2: Implement review system on frontend
- Day 3-4: Develop community feed components
- Day 5: Add search and filtering functionality on frontend

#### Week 7: Frontend Styling and Responsiveness
- Day 1-2: Implement responsive design
- Day 3-4: Style components and pages
- Day 5: Implement loading states and error handling

#### Week 8: Testing, Optimization, and Deployment
- Day 1-2: Comprehensive testing (unit tests, integration tests)
- Day 3: Performance optimization (backend and frontend)
- Day 4: Prepare for deployment (configuration, environment variables)
- Day 5: Deploy application, final testing in production environment

This timeline provides a structured approach to develop the diving center application over 8 weeks. It covers all major aspects of both backend and frontend development, from initial setup to final deployment. This schedule might change during development as some tasks may take more or less time than anticipated.

[Back to top](#table-of-contents)

## Data Models

The data models for this diving center application represent a comprehensive and interconnected system designed to manage users, courses, bookings, reviews, social interactions, and customer inquiries. These models form the backbone of a feature-rich platform that caters to both the operational needs of a diving center and the social aspects of a diver community.

**Database Schema**

The database schema is carefully crafted to ensure efficient data storage, retrieval, and relationships between various entities. It utilizes Django's ORM (Object-Relational Mapping) to create a robust and scalable database structure. The schema incorporates both built-in Django models and custom-designed models to meet the specific requirements of the diving center application.

**Entity Relationship Diagram (ERD)**

The ERD visually represents the complex relationships between different entities in the system. It illustrates how users interact with courses, bookings, and reviews, as well as how social features like posts, comments, likes, and followers are interconnected. This diagram serves as a crucial tool for understanding the data flow and dependencies within the application. We used [dbdiagram.io](https://dbdiagram.io) to design the ERD.

![Diving Center ERD](doc/images/erd/erd.png)

**Technical Architecture**

**Technical Design:** The application follows a modular design approach, separating concerns into distinct models. This design facilitates easier maintenance, scalability, and future enhancements. The use of Django's built-in User model as a foundation ensures robust authentication and authorization mechanisms.

**Model-Based Design:** Each model is designed to encapsulate specific functionalities and data related to a particular aspect of the application. This approach allows for clear separation of concerns and promotes code reusability.

**Relational Data Modeling:** The database design leverages relational modeling techniques to establish connections between different entities. Foreign key relationships are used extensively to maintain data integrity and enable efficient querying across related data sets.

**Tables Overview**

This table provides a clear overview of the database structure, showing the different tables and their respective purposes within the application. Each table is designed to handle specific aspects of the system, from user management to course bookings and social interactions.

| Table Name | Purpose |
|------------|---------|
| User | Manages user authentication and basic information |
| Profile | Extends user information with additional details and preferences |
| DivingCourse | Stores information about available diving courses, including details like title, description, type, and price |
| Booking | Handles course reservations made by users, including date, time, and additional information |
| Review | Allows users to rate and review courses, with content and rating |
| Post | Manages user-generated content for the community feed, including images and filters |
| Comment | Enables users to comment on posts, with creation and update timestamps |
| Like | Tracks user likes on posts, with creation timestamps |
| Follower | Manages user follow relationships, tracking who follows whom |
| Contact | Stores customer inquiries and messages, including a deletion token for privacy |

[Back to top](#table-of-contents)

**Relationships**

The relationships between these models create a cohesive system:

- Users are linked to Profiles, Bookings, Reviews, Posts, Comments, Likes, and Followers.
- DivingCourses are connected to Bookings and Reviews.
- Posts are associated with Comments and Likes.
- Followers establish connections between users.

The following tables illustrates the relationships between different models in the system. It shows how users are connected to various other entities like profiles, bookings, reviews, posts, comments, likes, and followers. It also demonstrates the connections between diving courses and their bookings and reviews, as well as the relationship between posts and their comments and likes. Lastly, it represents the follower relationship between users.

| Model 1 | Relationship | Model 2 |
|---------|--------------|---------|
| User | has one | Profile |
| User | has many | Bookings |
| User | has many | Reviews/Ratings (through Courses) |
| User | has many | Posts |
| User | has many | Comments |
| User | has many | Likes |
| User | has many | Followers |
| User | has many | Contacts |
| User | follows many | User |
| Courses | has many | Bookings |
| Courses | has many | Reviews/Ratings |
| Post | has many | Comments |
| Post | has many | Likes |
| Post | belongs to | User |
| Comment | belongs to | User |
| Like | belongs to | User |
| Follower | belongs to | User |

[Back to top](#table-of-contents)

This table outlines the key relationships between the models in the diving center application, showing how different entities are connected and interact within the system.

| Relationship Type | Primary Model | Related Model | Description |
|-------------------|---------------|---------------|-------------|
| One-to-One | User | Profile | Each user has one profile |
| One-to-Many | User | Booking | One user can make many bookings |
| One-to-Many | DivingCourse | Booking | One diving course can have many bookings |
| One-to-Many | DivingCourse | Review | One diving course can have many reviews |
| One-to-Many | User | Review | One user can write many reviews |
| One-to-Many | User | Post | One user can create many posts |
| One-to-Many | User | Comment | One user can write many comments |
| One-to-Many | Post | Comment | One post can have many comments |
| One-to-Many | User | Like | One user can like many posts |
| One-to-Many | Post | Like | One post can have many likes |
| Many-to-Many | User | User | Users can follow many users (through Follower model) |
| One-to-Many | User | Contact | One user can submit many contact messages |
| Many-to-One | Post | User | Many posts belong to one user (owner) |
| Many-to-One | Comment | User | Many comments belong to one user (owner) |
| Many-to-One | Like | User | Many likes belong to one user (owner) |
| Many-to-One | Follower | User | Many follower relationships involve one user (as follower or followed) |

[Back to top](#table-of-contents)

### User Model

The User model is a fundamental component of the diving center application, serving as the cornerstone for user authentication, authorization, and management. This model leverages Django's built-in User model, which provides a robust and secure foundation for handling user-related functionalities.

**Key Features**:
1. **Authentication**: Manages user login credentials and authentication processes.
2. **Identity Management**: Provides a unique identifier for each user in the system.
3. **Security**: Ensures secure storage of user passwords through hashing.
4. **Communication**: Stores email addresses for user communication and account-related notifications.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each user, automatically generated |
| username | CharField | Unique username used for login and identification |
| password | CharField | Securely hashed password, never stored in plain text |
| email | EmailField | User's email address for account communication and notifications |

**Implementation Notes**:
- The User model is part of Django's authentication system, located in `django.contrib.auth.models`.
- By utilizing Django's built-in User model, the application inherits a range of security features and best practices for user management.
- The `username` field is unique across all users, ensuring each user has a distinct identifier.
- Passwords are automatically hashed before storage, enhancing security by not storing plain-text passwords.
- The model supports additional fields like `first_name`, `last_name`, `is_staff`, `is_active`, etc., which can be utilized as needed.
- This model serves as a foreign key reference for many other models in the application, establishing relationships between users and various entities like bookings, reviews, and profiles.

**Advantages of Using Django's User Model**:
1. **Security**: Implements best practices for password hashing and user authentication out of the box.
2. **Scalability**: Designed to handle a large number of users efficiently.
3. **Integration**: Seamlessly integrates with Django's admin interface and authentication views.
4. **Extensibility**: Can be easily extended with a custom user model or through one-to-one relationships with other models (like a Profile model) if additional fields are needed.

The User model plays a crucial role in the application by:
- Enabling secure user registration and login processes.
- Providing a basis for user-specific data and permissions throughout the application.
- Facilitating features like user profiles, personalized bookings, and user-generated content (reviews, comments).

By leveraging Django's User model, the diving center application ensures a solid, secure, and scalable foundation for user management, allowing the development team to focus on building domain-specific features while relying on Django's battle-tested user authentication system.

[Back to top](#table-of-contents)

### Profile Model

The Profile model is an extension of the User model, designed to store additional, detailed information about each user. This model creates a more comprehensive and personalized user profile, enhancing the user experience and providing richer user data for the diving center application.

**Key Features**:
1. **User Extension**: Directly linked to the User model, allowing for seamless integration of additional user information.
2. **Personalization**: Stores personal details like full name and biography, enabling a more personalized user experience.
3. **Visual Identification**: Includes an image field for profile pictures, adding a visual element to user profiles.
4. **Timestamp Tracking**: Records creation and update times, providing a history of profile changes.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each profile, automatically generated |
| owner | OneToOneField | Establishes a one-to-one relationship with the User model, ensuring each user has exactly one profile |
| created_at | DateTimeField | Timestamp recording when the profile was first created |
| updated_at | DateTimeField | Timestamp that updates whenever the profile information is modified |
| name | CharField | User's full name, providing a more personal identifier than the username |
| content | TextField | Biographical information or user description, allowing users to share more about themselves |
| image | ImageField | Field for storing the user's profile picture |

**Implementation Notes**:
- The Profile model is typically defined in a separate app (e.g., `profiles/models.py`), emphasizing its role in extending user information.
- The `OneToOneField` to the User model ensures a direct, one-to-one correlation between User and Profile instances.
- Profile creation can be automated using Django signals, creating a profile automatically when a new user is registered.
- The `image` field often uses Django's ImageField, which requires additional setup for file storage (e.g., using Django's FileSystemStorage or cloud storage solutions).

**Advantages of Using a Separate Profile Model**:
1. **Flexibility**: Allows for easy addition of user-related fields without modifying the core User model.
2. **Separation of Concerns**: Keeps authentication-related fields (in the User model) separate from additional profile information.
3. **Customization**: Enables easy customization of user profiles without affecting the authentication system.
4. **Performance**: Can improve database performance by separating frequently accessed authentication data from less frequently accessed profile data.

The Profile model enhances the application by:
- Providing a richer user experience with more detailed user information.
- Enabling features like user galleries, personalized dashboards, and social aspects of the platform.
- Allowing for easy expansion of user-related data as the application grows and evolves.

In the context of the diving center application, the Profile model could be further customized to include diving-specific information such as certification levels, diving experience, or preferred diving locations. This model plays a crucial role in creating a community feel within the application and can be leveraged for features like personalized course recommendations or social networking among divers.

[Back to top](#table-of-contents)

### Courses Model

The Courses model is a central component of the diving center application, designed to represent and manage the various diving courses offered by the center. This model encapsulates all relevant information about each course, providing a comprehensive and structured approach to course management.

**Key Features**:
1. **Detailed Course Information**: The model captures a wide range of details about each course, from basic information like title and price to more comprehensive descriptions.
2. **SEO-Friendly URLs**: Utilizes a slug field for creating user-friendly and search engine optimized URLs.
3. **Rich Content Support**: Incorporates HTML-enabled descriptions, allowing for formatted and visually appealing course details.
4. **Image Management**: Integrates with Cloudinary for efficient storage and retrieval of course images.
5. **Categorization**: Includes a course type field for easy categorization and filtering of courses.
6. **Timestamp Tracking**: Records both creation and update times, providing a history of course modifications.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each course, automatically generated |
| title | CharField | The name or title of the diving course |
| slug | SlugField | A URL-friendly version of the title, used for creating clean, readable URLs |
| excerpt | TextField | A brief summary or introduction to the course, useful for quick overviews |
| description | HTMLField | A detailed description of the course, supporting HTML for rich formatting |
| course_type | CharField | Categorization of the course (e.g., beginner, advanced, specialty) |
| image | CloudinaryField | An image representing the course, stored and managed via Cloudinary |
| price | IntegerField | The cost of the course |
| created_at | DateTimeField | Timestamp recording when the course was first added to the system |
| updated_at | DateTimeField | Timestamp that updates whenever the course information is modified |

**Implementation Notes**:
- The Courses model is defined in the `courses/models.py` file, serving as the foundation for course-related functionality.
- The `slug` field is typically auto-generated from the title, ensuring unique and SEO-friendly URLs for each course.
- The use of `HTMLField` for the description allows for rich text formatting, enhancing the presentation of course details.
- The `CloudinaryField` for the image integrates with the Cloudinary service, providing efficient image management and delivery.
- The `course_type` field can be implemented with choices to ensure consistency in course categorization.
- Timestamp fields (`created_at` and `updated_at`) are automatically managed, providing a clear history of when courses are added or modified.

This model structure allows for efficient management of course offerings, providing all necessary information for both administrative purposes and user display. It supports various features like course listings, detailed course pages, and integration with booking and review systems, forming a cornerstone of the diving center's digital infrastructure.

[Back to top](#table-of-contents)

You can explain the Bookings model as follows:

### Bookings Model

The Bookings model is a crucial component of the diving center application, responsible for managing course reservations made by users. This model ensures that all booking-related information is systematically stored and easily retrievable, facilitating efficient course management and user experience.

**Key Features**:
1. **User-Course Relationship**: Each booking is linked to both a specific user and a specific course, ensuring clear and organized reservation records.
2. **Time and Date Management**: The model captures both the date and time of the booking, allowing for precise scheduling of courses.
3. **Additional Information**: Users can provide extra details related to their booking, which can be useful for instructors and administrative staff.
4. **Timestamp Tracking**: The creation time of each booking is recorded, providing a chronological order of reservations.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each booking |
| user | ForeignKey | Foreign key to User model, linking the booking to the user who made it |
| date | DateField | Date of the booked course, specifying when the course will take place |
| time | TimeField | Time of the booked course, specifying the start time of the course |
| course | ForeignKey | Foreign key to Course model, linking the booking to a specific course |
| additional_info | TextField | Any extra information provided by the user, such as special requests or requirements |
| created_at | DateTimeField | Timestamp of booking creation, automatically set when the booking is first made |

**Implementation Notes**:
- The Bookings model is defined within the `bookings/models.py` file, emphasizing its role in managing reservations.
- The `user` field ensures that each booking is associated with a specific user, providing accountability and traceability.
- The `course` field links each booking to a specific course, ensuring that the reservation is correctly assigned.
- The `date` and `time` fields allow for precise scheduling, which is crucial for managing course timings and availability.
- The `additional_info` field provides flexibility for users to communicate any special needs or preferences, enhancing the overall user experience.
- The `created_at` field is automatically populated when a booking is created, providing a record of when the reservation was made.

By structuring the Bookings model this way, the application can efficiently handle course reservations, ensuring that all necessary information is captured and easily accessible. This enhances the operational efficiency of the diving center and provides a seamless booking experience for users.

[Back to top](#table-of-contents)

### Reviews Model

The Reviews model is an integral part of the Courses app, designed to capture user feedback and ratings for diving courses. Although it's not a standalone app, it's a crucial component that enhances the functionality of the Course model.

This model allows users to rate and review courses they've taken, providing valuable feedback for both the diving center and potential students. It's structured to maintain a clear relationship between users, courses, and their associated reviews.

**Key Features**:
1. **Course-User Relationship**: Each review is linked to both a specific course and the user who wrote it, ensuring accountability and context for each review.
2. **Detailed Feedback**: The model captures both textual feedback (content) and a numerical rating, allowing for comprehensive course evaluations.
3. **Timestamp Tracking**: Creation and update times are recorded, providing a chronological context for each review.
4. **Unique Constraint**: The combination of course and user is set as unique, preventing multiple reviews by the same user for a single course.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each review |
| course | ForeignKey | Foreign key to Course model, linking the review to a specific course |
| user | ForeignKey | Foreign key to User model, identifying the author of the review |
| content | TextField | Text content of the review, allowing users to express their detailed opinions |
| rating | IntegerField | Numerical rating given by the user, typically on a predefined scale (e.g., 1-5) |
| created_at | DateTimeField | Timestamp of review creation, automatically set when the review is first submitted |
| updated_at | DateTimeField | Timestamp of last review update, automatically updated when the review is modified |

**Implementation Notes**:
- The Reviews model is defined within the `courses/models.py` file, emphasizing its close relationship with the Course model.
- The `unique_together` constraint in the model's Meta class ensures that a user can only submit one review per course, maintaining data integrity.
- This model plays a crucial role in gathering user feedback, which can be used to improve course offerings and help potential students make informed decisions.

By structuring the Reviews model this way, the application can efficiently manage and display course reviews, enhancing the overall user experience and providing valuable insights for both the diving center management and prospective students.

[Back to top](#table-of-contents)

### Posts Model

The Posts model is a critical component of the diving center application, designed to manage user-generated content for the community feed. This model allows users to share their experiences, thoughts, and media, fostering a sense of community and engagement among users.

**Key Features**:
1. **User-Generated Content**: Enables users to create and share posts, contributing to the community feed.
2. **Ownership**: Each post is linked to a specific user, ensuring accountability and personalization.
3. **Rich Media Support**: Supports images and image filters, allowing for visually appealing posts.
4. **Timestamp Tracking**: Records both creation and update times, providing a chronological context for posts.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each post, automatically generated |
| owner | ForeignKey | Foreign key to User model, linking the post to its creator |
| created_at | DateTimeField | Timestamp recording when the post was first created |
| updated_at | DateTimeField | Timestamp that updates whenever the post is modified |
| title | CharField | The title of the post, providing a brief summary of its content |
| content | TextField | The main content of the post, allowing users to express their thoughts and experiences |
| image | ImageField | Field for storing an image associated with the post, enhancing its visual appeal |
| image_filter | CharField | Field for applying an image filter, if any, to the associated image |

**Implementation Notes**:
- The Posts model is typically defined in the `posts/models.py` file, emphasizing its role in managing community content.
- The `ForeignKey` to the User model ensures that each post is associated with a specific user, providing a clear link between users and their content.
- The `image` field uses Django's ImageField, which requires additional setup for file storage (e.g., using Django's FileSystemStorage or cloud storage solutions).
- The `image_filter` field can be implemented with choices to allow users to select from predefined image filters.

**Advantages of the Posts Model**:
1. **Engagement**: Encourages user interaction and engagement by allowing users to share their experiences and thoughts.
2. **Community Building**: Fosters a sense of community by providing a platform for users to connect and share content.
3. **Customization**: Supports rich media content and customization options like image filters, enhancing the user experience.
4. **Accountability**: Links posts to their creators, ensuring accountability and enabling features like user-specific feeds and content management.

The Posts model enhances the application by:
- Providing a platform for user-generated content, which can drive engagement and retention.
- Enabling features like user profiles, personalized feeds, and social interactions (e.g., comments and likes).
- Supporting rich media content, which can make the community feed more visually appealing and engaging.

In the context of the diving center application, the Posts model can be used to share diving experiences, photos from dives, tips and advice, and other content that can enrich the community and provide value to users. This model plays a crucial role in building a vibrant and interactive community within the application.

[Back to top](#table-of-contents)

### Comments Model

The Comments model is designed to facilitate community interaction by allowing users to comment on posts. This model plays a crucial role in building engagement and discussions within the diving center application, enabling users to share their thoughts and feedback on user-generated content.

**Key Features**:
1. **User Interaction**: Enables users to engage with posts by leaving comments, fostering a sense of community.
2. **Ownership**: Each comment is linked to a specific user, ensuring accountability and personalization.
3. **Post Association**: Each comment is associated with a specific post, maintaining context and relevance.
4. **Timestamp Tracking**: Records both creation and update times, providing a chronological context for comments.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each comment, automatically generated |
| owner | ForeignKey | Foreign key to User model, linking the comment to its creator |
| post | ForeignKey | Foreign key to Post model, linking the comment to the post it belongs to |
| created_at | DateTimeField | Timestamp recording when the comment was first created |
| updated_at | DateTimeField | Timestamp that updates whenever the comment is modified |
| content | TextField | The main content of the comment, allowing users to express their thoughts and feedback |

**Implementation Notes**:
- The Comments model is typically defined in the `comments/models.py` file, emphasizing its role in managing user interactions with posts.
- The `ForeignKey` to the User model ensures that each comment is associated with a specific user, providing a clear link between users and their comments.
- The `ForeignKey` to the Post model ensures that each comment is associated with a specific post, maintaining the context of the discussion.
- The `created_at` and `updated_at` fields are automatically managed by Django, providing a history of when comments are added or modified.

**Advantages of the Comments Model**:
1. **Engagement**: Encourages user interaction and engagement by allowing users to comment on posts.
2. **Community Building**: Fosters a sense of community by enabling discussions and feedback on user-generated content.
3. **Accountability**: Links comments to their creators, ensuring accountability and enabling features like user-specific comment management.
4. **Contextual Relevance**: Links comments to specific posts, maintaining the context and relevance of discussions.

The Comments model enhances the application by:
- Providing a platform for user interactions and discussions, which can drive engagement and retention.
- Enabling features like threaded discussions, notifications, and comment moderation.
- Supporting rich text content, which can make comments more informative and engaging.

In the context of the diving center application, the Comments model can be used to share feedback on diving experiences, ask questions, and provide tips and advice. This model plays a crucial role in building a vibrant and interactive community within the application, allowing users to connect and engage with each other.

[Back to top](#table-of-contents)

### Likes Model

The Likes model is a key component of the diving center application's social engagement features. It's designed to track and manage user likes on posts, providing a simple yet effective way for users to show appreciation or agreement with content shared by others.

**Key Features**:
1. **Social Engagement**: Enables users to interact with posts through a simple, one-click action.
2. **User Association**: Each like is linked to a specific user, ensuring accurate tracking of user preferences and interactions.
3. **Post Association**: Each like is connected to a specific post, allowing for easy quantification of a post's popularity.
4. **Timestamp Tracking**: Records the creation time of each like, providing chronological context for user interactions.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each like, automatically generated |
| owner | ForeignKey | Foreign key to User model, linking the like to the user who performed the action |
| post | ForeignKey | Foreign key to Post model, connecting the like to the specific post it's associated with |
| created_at | DateTimeField | Timestamp recording when the like was created |

**Implementation Notes**:
- The Likes model is typically defined in the `likes/models.py` file, emphasizing its role in managing user interactions with posts.
- The `ForeignKey` to the User model ensures that each like is associated with a specific user, allowing for accurate tracking of user engagement.
- The `ForeignKey` to the Post model links each like to a specific post, enabling features like like counts and popularity metrics.
- The model often includes a `unique_together` constraint on `owner` and `post` to prevent duplicate likes from the same user on a single post.

**Advantages of the Likes Model**:
1. **Simplified Engagement**: Provides a quick and easy way for users to engage with content.
2. **Content Popularity Metrics**: Enables the application to track and display the popularity of posts based on like counts.
3. **User Preference Tracking**: Helps in understanding user preferences and interests, which can be used for content recommendations.
4. **Enhanced User Experience**: Contributes to a more interactive and engaging platform.

The Likes model enhances the application by:
- Offering a simple mechanism for users to show appreciation for content.
- Enabling features like "most liked" post rankings or trending content identification.
- Providing data for user engagement analytics and content performance metrics.
- Supporting personalized content recommendations based on user likes.

In the context of the diving center application, the Likes model can be particularly useful for:
- Highlighting popular diving spots or experiences shared by users.
- Identifying well-received tips or advice in the community.
- Enhancing user profiles by showing posts a user has liked.
- Generating notifications to post owners when their content is liked, encouraging further engagement.

By implementing the Likes model, the application build a more interactive community, encourages content creation, and provides valuable data on user preferences and content popularity. This simple yet effective feature plays a significant role in enhancing overall user engagement and satisfaction within the diving center's digital community.

[Back to top](#table-of-contents)

### Follower Model

This model manages user follow relationships, enabling social connections.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each follower relationship |
| owner | ForeignKey | Foreign key to User model (follower) |
| followed | ForeignKey | Foreign key to User model (followed user) |
| created_at | DateTimeField | Timestamp of follow relationship creation |

[Back to top](#table-of-contents)

### Contacts Model

The Contact model stores customer inquiries and messages.

**Fields**:

| Field | Attribute | Description |
|-------|-----------|-------------|
| id | BigAutoField | Unique identifier for each contact message |
| name | CharField | Name of the person making the inquiry |
| email | EmailField | Email address for correspondence |
| subject | CharField | Subject of the inquiry |
| message | TextField | Detailed message content |
| created_at | DateTimeField | Timestamp of message creation |

[Back to top](#table-of-contents)

## API Endpoints

This table provides a comprehensive overview of all the API endpoints in the diving center project, including their HTTP methods, CRUD operations, view types, and descriptions. It covers all the major functionalities such as user authentication, profiles, posts, comments, likes, followers, bookings, contact messages, courses, and reviews.

| Model | Endpoint | HTTP Method | CRUD Operation | View Type | Description |
|-------|----------|-------------|----------------|-----------|-------------|
| **Root** |
| | `/` | GET | Read | Function-based view | Root route, welcomes to the Diving Center API |
| **Authentication** |
| | `/admin/` | GET | Read | Django Admin | Django admin interface |
| | `/dj-rest-auth/logout/` | POST | Delete | Function-based view | Custom logout route |
| | `/dj-rest-auth/login/` | POST | Create | DRF built-in view | User login |
| | `/dj-rest-auth/user/` | GET | Read | DRF built-in view | Get current user details |
| | `/dj-rest-auth/registration/` | POST | Create | DRF built-in view | User registration |
| **Profiles** |
| | `/profiles/` | GET | Read | ListAPIView | List all profiles |
| | `/profiles/{id}/` | GET | Read | RetrieveUpdateAPIView | Retrieve a specific profile |
| | `/profiles/{id}/` | PUT/PATCH | Update | RetrieveUpdateAPIView | Update a specific profile (owner only) |
| **Posts** |
| | `/posts/` | GET | Read | ListCreateAPIView | List all posts |
| | `/posts/` | POST | Create | ListCreateAPIView | Create a new post (authenticated users only) |
| | `/posts/{id}/` | GET | Read | RetrieveUpdateDestroyAPIView | Retrieve a specific post |
| | `/posts/{id}/` | PUT/PATCH | Update | RetrieveUpdateDestroyAPIView | Update a specific post (owner only) |
| | `/posts/{id}/` | DELETE | Delete | RetrieveUpdateDestroyAPIView | Delete a specific post (owner only) |
| **Comments** |
| | `/comments/` | GET | Read | ListCreateAPIView | List all comments |
| | `/comments/` | POST | Create | ListCreateAPIView | Create a new comment (authenticated users only) |
| | `/comments/{id}/` | GET | Read | RetrieveUpdateDestroyAPIView | Retrieve a specific comment |
| | `/comments/{id}/` | PUT/PATCH | Update | RetrieveUpdateDestroyAPIView | Update a specific comment (owner only) |
| | `/comments/{id}/` | DELETE | Delete | RetrieveUpdateDestroyAPIView | Delete a specific comment (owner only) |
| **Likes** |
| | `/likes/` | GET | Read | ListCreateAPIView | List all likes |
| | `/likes/` | POST | Create | ListCreateAPIView | Create a new like (authenticated users only) |
| | `/likes/{id}/` | GET | Read | RetrieveDestroyAPIView | Retrieve a specific like |
| | `/likes/{id}/` | DELETE | Delete | RetrieveDestroyAPIView | Delete a specific like (owner only) |
| **Followers** |
| | `/followers/` | GET | Read | ListCreateAPIView | List all follower relationships |
| | `/followers/` | POST | Create | ListCreateAPIView | Create a new follower relationship (authenticated users only) |
| | `/followers/{id}/` | GET | Read | RetrieveDestroyAPIView | Retrieve a specific follower relationship |
| | `/followers/{id}/` | DELETE | Delete | RetrieveDestroyAPIView | Delete a specific follower relationship (owner only) |
| **Bookings** |
| | `/bookings/` | GET | Read | ModelViewSet | List all bookings for the authenticated user |
| | `/bookings/` | POST | Create | ModelViewSet | Create a new booking (authenticated users only) |
| | `/bookings/{id}/` | GET | Read | ModelViewSet | Retrieve a specific booking |
| | `/bookings/{id}/` | PUT/PATCH | Update | ModelViewSet | Update a specific booking (owner only) |
| | `/bookings/{id}/` | DELETE | Delete | ModelViewSet | Delete a specific booking (owner only) |
| **Contact Us** |
| | `/contactus/` | POST | Create | APIView | Create a new contact message |
| | `/contactus/{id}/` | PUT | Update | APIView | Update an existing contact message |
| | `/contactus/{id}` | DELETE | Delete | Function-based view | Delete a specific contact message |
| **Courses** |
| | `/courses/` | GET | Read | ModelViewSet | List all courses |
| | `/courses/` | POST | Create | ModelViewSet | Create a new course (admin only) |
| | `/courses/{slug}/` | GET | Read | ModelViewSet | Retrieve a specific course |
| | `/courses/{slug}/` | PUT/PATCH | Update | ModelViewSet | Update a specific course (admin only) |
| | `/courses/{slug}/` | DELETE | Delete | ModelViewSet | Delete a specific course (admin only) |
| **Reviews** |
| | `/reviews/` | GET | Read | ModelViewSet | List all reviews |
| | `/reviews/` | POST | Create | ModelViewSet | Create a new review (authenticated users only) |
| | `/reviews/{id}/` | GET | Read | ModelViewSet | Retrieve a specific review |
| | `/reviews/{id}/` | PUT/PATCH | Update | ModelViewSet | Update a specific review (owner only) |
| | `/reviews/{id}/` | DELETE | Delete | ModelViewSet | Delete a specific review (owner only) |

[Back to top](#table-of-contents)

## Frameworks, Libraries, and Dependencies

The Diving Center project leverages a variety of frameworks, libraries, and dependencies to ensure robust functionality and performance. Below is a detailed list of the key components used:

### Django Framework and Extensions

1. **Django** (`Django==5.0.6`):
   - A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django handles much of the complexity of web development, allowing developers to focus on writing their app without needing to reinvent the wheel.

2. **Django REST Framework** (`djangorestframework==3.15.1`):
   - A powerful and flexible toolkit for building Web APIs in Django. It provides various features such as serialization, authentication, and view sets that simplify API development.

3. **Django Allauth** (`django-allauth==0.54.0`):
   - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

4. **Django REST Auth** (`dj-rest-auth==2.1.9`):
   - Provides a set of REST API endpoints for handling user registration and authentication tasks. It’s built on top of Django Allauth and Django REST Framework.

5. **Django Filter** (`django-filter==24.2`):
   - Simplifies the process of filtering querysets in Django REST Framework.

6. **Django CORS Headers** (`django-cors-headers==4.3.1`):
   - A Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

### Database Management

7. **dj-database-url** (`dj-database-url==0.5.0`):
   - Allows you to utilize the DATABASE_URL environment variable to configure your Django application.

8. **psycopg2** (`psycopg2==2.9.9`):
   - PostgreSQL database adapter for Python.

### Authentication and Security

9. **djangorestframework-simplejwt** (`djangorestframework-simplejwt==5.3.1`):
   - Provides JSON Web Token (JWT) authentication for Django REST Framework.

10. **oauthlib** (`oauthlib==3.2.2`):
    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python.

11. **requests-oauthlib** (`requests-oauthlib==2.0.0`):
    - OAuthlib support for Python-Requests, the ubiquitous HTTP library for Python.

12. **PyJWT** (`PyJWT==2.8.0`):
    - A Python library which allows you to encode and decode JSON Web Tokens (JWT).

### Storage and Image Handling

13. **Pillow** (`Pillow==10.3.0`):
    - Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats.

14. **Cloudinary** (`cloudinary==1.40.0`):
    - A library that integrates your application with the Cloudinary service for managing media assets such as images and videos.

15. **django-cloudinary-storage** (`django-cloudinary-storage==0.3.0`):
    - Facilitates the integration of Django with Cloudinary for storing media files.

### Miscellaneous

16. **asgiref** (`asgiref==3.8.1`):
    - ASGI specification and utilities, used by Django for asynchronous support.

17. **django-js-asset** (`django-js-asset==2.2.0`):
    - A Django app that provides a template tag for loading JavaScript assets.

18. **django-tinymce** (`django-tinymce==4.1.0`):
    - A Django application that provides a fully integrated TinyMCE WYSIWYG editor.

19. **pytz** (`pytz==2024.1`):
    - World timezone definitions for Python, allowing accurate and cross-platform timezone calculations.

20. **sqlparse** (`sqlparse==0.5.0`):
    - A non-validating SQL parser for Python. It provides support for parsing, splitting, and formatting SQL statements.

21. **gunicorn** (`gunicorn==22.0.0`):
    - A Python WSGI HTTP Server for UNIX, used to serve Django applications in production.

[Back to top](#table-of-contents)

## Testing and Validation

For all testing and validation, please refer to the [TESTING.md](TESTING.md) file.

## Bugs

**ContactUs Bugs**

| Model | Bug Description | Solution | Resource | Solved |
|-------|-----------------|----------|----------|--------|
| ContactUs | DELETE request failing due to missing primary key (pk) in URL | Updated the URL pattern in urls.py to include <int:pk> for detail views. Modified the delete method in views.py to handle the pk parameter correctly. | [Django documentation: URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/) | ✅ |
| ContactUs | PUT request returning 405 (Method Not Allowed) error | Fixed indentation of the put method in the ContactView class. Ensured the put method was properly part of the class definition. | [Stack Overflow: Django REST framework PUT method not allowed](https://stackoverflow.com/questions/23639113/django-rest-framework-put-method-not-allowed) | ✅ |
| ContactUs | Deletion token not updating after editing a message | Modified the put method to generate a new deletion token when updating a message. Updated the frontend to store the new token in localStorage after successful edits. | [Django REST framework documentation: Generic views](https://www.django-rest-framework.org/api-guide/generic-views/) | ✅ |
| ContactUs | Form submission not clearing previous errors | Added error state reset in the handleSubmit function. Cleared the errors object before making new requests. | [React Bootstrap documentation: Forms](https://react-bootstrap.github.io/forms/overview/) | ✅ |
| ContactUs | Non-logged-in users couldn't delete their messages due to permission issues | Implemented a deletion token system to allow secure message deletion without authentication. | [Django REST Framework documentation: Permissions](https://www.django-rest-framework.org/api-guide/permissions/) | ✅ |
| ContactUs | After editing a message, the deletion token became invalid, preventing message deletion | Updated the backend to generate a new deletion token when updating a message and modified the frontend to store this new token. | [UUID documentation in Python](https://docs.python.org/3/library/uuid.html) | ✅ |
| ContactUs | Admin users couldn't delete or update messages without deletion token | Modified the delete and put methods to allow admin users to perform these actions without requiring the deletion token. | [Django REST Framework documentation: Permissions](https://www.django-rest-framework.org/api-guide/permissions/) | ✅ |
| ContactUs | Authenticated non-admin users could see all contact messages | Updated the get method to filter messages based on user authentication status and role. Admin users can see all messages, while regular users can only see their own. | [Django documentation: Queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/) | ✅ |
| ContactUs | Inconsistent permissions for different user types (admin, authenticated, non-authenticated) | Implemented a comprehensive permission system in the `get_object` method to handle all three cases: admin, authenticated users, and non-authenticated users with deletion tokens. | [Django REST Framework: Custom permissions](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions) | ✅ |
| ContactUs | Authenticated users couldn't manage messages created while logged out | Modified the `get_object` method to allow authenticated users to manage messages associated with their email, regardless of whether they were logged in when creating the message. | [Django REST Framework: Generic views](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview) | ✅ |
| ContactUs | Admin users needed deletion token for some operations | Updated the `get_object` method to always return the object for admin users, bypassing the deletion token check. | [Django REST Framework: Authentication](https://www.django-rest-framework.org/api-guide/authentication/) | ✅ |

[Back to top](#table-of-contents)

**Bookings Bugs**

| Model | Bug Description | Solution | Resource | Solved |
|-------|-----------------|----------|----------|--------|
| Booking | Time validation error when submitting booking | Update time validation in serializer to accept 'HH:MM' format | [Django REST Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/) | ✅ |
| Booking | 'NoneType' object has no attribute 'id' when course is not selected | Add validation for course field in serializer | [DRF Serializer Validation](https://www.django-rest-framework.org/api-guide/serializers/#validation) | ✅ |
| Booking | Bookings allowed on dates other than 10th of the month | Implement date validation in serializer and view | [Django Date Validation](https://docs.djangoproject.com/en/3.2/ref/forms/validation/) | ✅ |
| Booking | Users can book past dates | Add validation to prevent booking past dates | [Django Date Validation](https://docs.djangoproject.com/en/3.2/ref/forms/validation/) | ✅ |
| Booking | Multiple bookings for same course, date and time | Implement uniqueness constraint in model | [Django Model Constraints](https://docs.djangoproject.com/en/3.2/ref/models/constraints/) | ✅ |
| Booking | Booking creation fails silently on the frontend | Improve error handling and display in React component.| [React Error Boundaries](https://reactjs.org/docs/error-boundaries.html) | ✅ |
| Booking | Error persists for future dates after fixing past date issue | Update frontend to clear previous errors and backend to handle all validations | [React State Management](https://reactjs.org/docs/hooks-state.html) | ✅ |
| Booking | Duplicate booking validation not working correctly | Updated `validate` method in `BookingSerializer` to properly check for existing bookings | [Django REST Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/) | ✅ |
| Booking | Unable to update existing bookings | Modified `update` method in `BookingViewSet` to handle IntegrityError | [Django REST Framework ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/) | ✅ |

[Back to top](#table-of-contents)

**Courses Bugs**

| Model | Bug Description | Solution | Resource | Solved |
|-------|-----------------|----------|----------|--------|
| Courses | Course dropdown not populating in frontend | Updated `CourseViewSet` to ensure proper serialization of course data | [Django REST Framework ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/) | ✅ |
| Courses | Course type not displaying correctly | Modified `CourseSerializer` to include `get_course_type_display` method | [Django Model Fields](https://docs.djangoproject.com/en/3.2/ref/models/fields/) | ✅ |
| Courses | Any user could perform CRUD operations on courses | Implemented `IsAdminUser` permission in `CourseViewSet` for create, update, and delete actions | [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/) | ✅ |

[Back to top](#table-of-contents)

**Reviews Bugs**

| Model | Bug Description | Solution | Resource | Solved |
|-------|-----------------|----------|----------|--------|
| Reviews | Admin unable to update and delete user reviews | Modified `update` and `destroy` methods in `ReviewViewSet` to allow staff users to edit/delete any review | [DRF ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions) | ✅ |
| Reviews | Authenticated users could see all reviews | Updated `get_queryset` method in `ReviewViewSet` to filter reviews based on user authentication and staff status | [Filtering Querysets](https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-current-user) | ✅ |

[Back to top](#table-of-contents)

**General Bugs**

| Model | Bug Description | Solution | Resource | Solved |
|-------|-----------------|----------|----------|--------|
| General | CORS (Cross-Origin Resource Sharing) issues when making requests from frontend | Added django-cors-headers to the project and configured CORS_ALLOWED_ORIGINS in settings.py. Ensured the frontend domain was included in the allowed origins. | [Django CORS headers documentation](https://github.com/adamchainz/django-cors-headers) | ✅ |
| General | Inconsistent state updates in React components | Implemented the useEffect hook to handle side effects and state updates. Ensured state updates were done using the functional form of setState. | [React documentation: Hooks API Reference](https://reactjs.org/docs/hooks-reference.html) | ✅ |
| General | Unauthorized access to admin-only views | Implemented proper permission classes in Django REST framework views. Used IsAdminUser for admin-only actions and AllowAny for public endpoints. | [Django REST framework: Permissions](https://www.django-rest-framework.org/api-guide/permissions/) | ✅ |
| General | Unhandled promise rejections in async functions | Added try-catch blocks to all async functions. Implemented proper error handling and user feedback using toast notifications. | [MDN Web Docs: Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) | ✅ |

[Back to top](#table-of-contents)

**Unknown Bugs**
There may be other bugs that have not yet been identified.

# Deployment

The "Diving Center" project leverages a combination of platforms and services to facilitate its deployment and management.

For hosting and running the application, Heroku, a cloud platform as a service (PaaS), is utilized. It enables seamless deployment, automatic scaling, and management tools for monitoring and maintaining the application. The Code Institute (CI) database systems are employed to store and manage the application's data during development and deployment phases.

Additionally, Cloudinary, a cloud-based service, is integrated to handle image and video management, providing an end-to-end solution for storing, optimizing, and delivering media assets for the "Diving Center" platform.

The respective URLs for these platforms and services are as follows:

## GitHub
- **Repository Setup:** GitHub serves as the version control system, hosting the project's codebase and enabling collaboration among developers.
[GitHub](https://github.com)

## Gitpod
- **Development Environment:** Gitpod, a cloud-based integrated development environment (IDE), provides a streamlined coding experience by offering a preconfigured workspace with all the necessary tools and dependencies. [Gitpod](https://www.gitpod.io/)

## Heroku
- **Application Hosting:** For hosting and running the application, Heroku, a cloud platform as a service (PaaS), is utilized. It enables seamless deployment, automatic scaling, and management tools for monitoring and maintaining the application.
[Heroku](https://www.heroku.com)
  - **Setting up on Heroku:**
Here's a simplified 10-step explanation on how to use Heroku's cloud server to deploy your "Diving Center" project, written in easy-to-understand language for non-coders:

1. **Sign up for Heroku**: Go to heroku.com and create an account.

2. **Create a new app**: After logging in, click on the "New" button in the top right corner and select "Create New App". Give your app a unique name and choose your preferred region.

3. **Connect to GitHub**: In the "Deploy" section, select "GitHub" as the deployment method. Search for your "Diving Center" repository and connect it to Heroku.

4. **Set up environment variables**: In the "Settings" section, click on "Reveal Config Vars". Here, you'll need to add some important variables:
   - `SECRET_KEY`: A secret key for your Django project (you can generate one online).
   - `DATABASE_URL`: The URL for your database (e.g., Heroku Postgres).
   - `CLOUDINARY_URL`: The URL for your Cloudinary account (for storing images and media).

5. **Enable automatic deploys**: In the "Deploy" section, you can choose to enable automatic deploys from your GitHub repository. This means Heroku will automatically update your app whenever you push new changes to GitHub.

6. **Deploy your app**: If you didn't enable automatic deploys, you can manually deploy your app by scrolling down to the "Manual Deploy" section and clicking "Deploy Branch".

7. **Open your app**: After a successful deployment, Heroku will provide you with a unique URL where your "Diving Center" app is now live! You can click the "View" button to open it.

8. **Set up a database**: If your app requires a database, you'll need to provision one. Heroku recommends using Heroku Postgres, which you can set up through the "Resources" section of your app's dashboard.

9. **Update your code**: If you need to make changes to your app, simply commit and push the updates to your GitHub repository. If you enabled automatic deploys, Heroku will automatically update your live app. Otherwise, you'll need to manually re-deploy.

10. **Monitor your app**: Heroku provides tools to monitor your app's performance, logs, and other metrics. You can access these through the "More" menu in your app's dashboard.

By following these steps, you'll be able to deploy your "Diving Center" project to Heroku's cloud server, making it accessible to anyone with the app's URL. Remember to consult Heroku's documentation or seek help if you encounter any issues during the deployment process.

**For deployment Heroku needs two additional files in order to deploy properly.**
- requirements.txt
- Procfile
  
You can install this project's requirements (where applicable) using:

- **pip3 install -r requirements.txt**

If you have your own packages that have been installed, then the requirements file needs updated using:

- **pip3 freeze --local > requirements.txt**

**The Procfile can be created with the following command:**

echo web: gunicorn app_name.wsgi > Procfile
replace app_name with the name of your primary Django app name; the folder where settings.py is located

[Back to top](#table-of-contents)

## CI database
- **Database Hosting:** The Code Institute (CI) provides PostgreSQL-based database systems specifically for students to use during the development and deployment phases of their projects. PostgreSQL, known for its robustness and reliability, is an advanced, open-source relational database system. It is well-suited for handling complex queries and large volumes of data, making it an excellent choice for web applications.

- **Development Phase:** During development, the CI database allows students to efficiently store, retrieve, and manipulate data required for their applications. It supports various data types and advanced features such as indexing, transactions, and concurrency control, ensuring smooth and effective development processes.

- **Deployment Phase:** When it comes to deployment, the CI database continues to serve as a reliable backend for the application. Students can leverage the database’s capabilities to manage user data, application state, and other critical information with high availability and performance.

- **Accessibility:** The CI database systems are accessible to Code Institute students, providing a consistent and stable environment for learning and project development. This ensures that students have a standardized platform to practice and implement database management techniques, which are crucial skills in the field of web development.

- **Integration:** The PostgreSQL databases provided by CI can be seamlessly integrated with various web frameworks and technologies taught in the course, such as Django. This integration enables students to implement real-world applications with database-driven functionality.

[Back to top](#table-of-contents)

## Cloudinary

To enhance performance and scalability, the project utilizes a third-party service for hosting and serving static media files like images. This approach alleviates the burden on the primary hosting platform, ensuring efficient delivery of content to users. 

- **Media Storage:** Cloudinary is used for hosting media files like images. It removes the load of serving static files from Heroku, ensuring better performance and scalability. [Cloudinary](https://cloudinary.com/)
  - **Integration:**
    1. Set up a Cloudinary account.
    2. Configure the Cloudinary settings in the Django settings file with the API keys provided by Cloudinary.
    3. Use Django’s storage backend for Cloudinary to handle media uploads.

By adopting this approach, the project benefits from a dedicated and optimized infrastructure for managing and delivering static media content. This not only improves the overall user experience but also facilitates future growth and expansion by providing a scalable solution for handling an increasing volume of media assets.

[Back to top](#table-of-contents)

# Cloning and Forking

## Cloning the Repository
- **Local Setup:**
  1. Clone the repository: [GitHub repository](https://github.com/AmirShkolnik/DivingCenter_API). 
 `git clone https://github.com/AmirShkolnik/DivingCenter_API`.
  2. Navigate into the project directory: `cd software-stacks-p4`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Set up local environment variables in a `.env` file.
  5. Run migrations: `python manage.py migrate`
  6. Start the development server: `python manage.py runserver`

1. **Open Your Preferred Code Editor**: Launch the code editor or integrated development environment (IDE) you typically use for your coding projects.

2. **Navigate to the Repository URL**: Visit the following URL in your web browser: https://github.com/AmirShkolnik/DivingCenter_API

3. **Locate the Clone Button**: On the repository page, you'll find a green-colored button labeled "Code". Click on this button to reveal the cloning options.

4. **Copy the Repository URL**: Depending on your preferred cloning method, copy the repository URL provided. You can choose either the HTTPS, SSH URL or GitHub CLI based on your setup and preferences.

5. **Open a Terminal or Command Prompt**: In your code editor or operating system, open a terminal or command prompt window. This will allow you to execute Git commands.

6. **Navigate to Your Desired Directory**: Using the terminal or command prompt, navigate to the directory or folder where you want to clone the "Diving Center" repository. You can use the `cd` command followed by the path to change directories.

7. **Execute the Clone Command**: Once you're in the desired directory, execute the following Git command, replacing `<repository_url>` with the URL you copied earlier:

   ```
   git clone <repository_url>
   ```

   Press Enter, and Git will start cloning the repository to your local machine.

8. **Install requirements**: Install requirements from requirements.txt using the command "pip install -r requirements.txt". If working in a virtual environment, activate the virtual environment before running the command.

9. **Create env.py**: Create a env.py to store database url, secret key and cloudinary url. directory:

[Back to top](#table-of-contents)

## Forking the Repository

Here's a step-by-step guide for forking the "Diving Center" project from the GitHub repository located at https://github.com/AmirShkolnik/DivingCenter_API:

1. **Navigate to the Repository**: Open your web browser and visit the "Diving Center" repository at https://github.com/AmirShkolnik/DivingCenter_API.

2. **Locate the Fork Button**: On the top-right corner of the repository page, you'll find a button labeled "Fork". This button allows you to create a copy of the repository under your own GitHub account.

3. **Create Your Fork**: Click on the "Fork" button. GitHub will prompt you to select the destination account for your forked repository. Choose your personal GitHub account or an organization you have access to. click the green button "Create fork". 

4. **Wait for the Forking Process**: GitHub will initiate the forking process, creating a complete copy of the "Diving Center" repository under your chosen account or organization. This process may take a few moments, depending on the size of the repository.

5. **Navigate to Your Forked Repository**: Once the forking process is complete, you'll be automatically redirected to the forked repository's page within your account or organization. The URL will reflect the new location of your forked repository.

6. **Customize Your Fork (Optional)**: You now have full control over your forked repository. You can rename it, modify the description, or make any other desired changes to distinguish it from the original repository.

[Back to top](#table-of-contents)

## Credits

### Code

The development of the Diving Center application was supported by various resources and contributions from the CI community. Here are the key references and sources of inspiration for the Diving Center project:

- The technique to limit the size of image uploads to Cloudinary is adapted from this [Cloudinary Support Article](https://support.cloudinary.com/hc/en-us/community/posts/360009752479-How-to-resize-before-uploading-pictures-in-Django).
- A replacement for the deprecated `django.conf.urls.url()` was implemented as per this [StackOverflow Article](https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to).
- How to access URL arguments as kwargs in generic APIViews is from this [StackOverflow Article](https://stackoverflow.com/questions/51042871/how-to-access-url-kwargs-in-generic-api-views-listcreateapiview-to-be-more-spec).
- The fix for the Django Rest Framework bug that prevents user's cookies from being cleared on logout is from the Code Institute Django Rest Framework walkthrough project.
- The technique for overriding the `to_representation` method of a serializer to make a change to the outgoing JSON data used in `profiles/serializers.py` is from this [testdriven.io Tip](https://testdriven.io/tips/ed79fa08-6834-4827-b00d-2609205129e0/).
- The method to set up user authentication with JWT in Django Rest Framework is adapted from this [StackOverflow Article](https://stackoverflow.com/questions/44697872/django-rest-framework-jwt-user-login).
- The technique to handle file uploads in Django Rest Framework is from this [StackOverflow Article](https://stackoverflow.com/questions/45232352/file-upload-with-django-rest-framework).
- The method to test Django Rest Framework endpoints using the APIClient is adapted from this [Django Rest Framework Documentation](https://www.django-rest-framework.org/api-guide/testing/).

- Deployment section description is based on the following guides:
[Preparing a Codebase for Heroku Deployment](https://devcenter.heroku.com/articles/preparing-a-codebase-for-heroku-deployment)
[Heroku Deployment Guide](https://coding-boot-camp.github.io/full-stack/heroku/heroku-deployment-guide/)

In addition, the following documentation was extensively referenced throughout development:

- [Django Documentation](https://www.djangoproject.com)
- [Django Rest Framework Documentation](https://www.django-rest-framework.org)
- [django-filter Documentation](https://django-filter.readthedocs.io/en/stable/)
- [django-recurrence Documentation](https://django-recurrence.readthedocs.io/en/latest/)
- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
- [dateutil Documentation](https://dateutil.readthedocs.io/en/stable/index.html)
- [Django Rest Framework JWT Documentation](https://jpadilla.github.io/django-rest-framework-jwt/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

These resources provided invaluable insights and guidance, significantly contributing to the successful development of the Diving Center DRF API application.

[Back to top](#table-of-contents)

### Media

The following sites were used to gather the photographic media used:
- [Freepik](https://www.freepik.com/)

## Acknowledgements

The development of Diving Center has been an exciting journey, and I am grateful for the inspiration, guidance, and resources that have contributed to the project. 

### Inspiration
- **Strava**: The idea for Diving Center was inspired by [Strava](https://www.strava.com/), a leading platform for fitness enthusiasts to track their activities, compete with others, and share their fitness journeys. Strava's robust features and community-centric approach motivated me to create a similar platform focused on comprehensive fitness tracking and community engagement.

[Back to top](#table-of-contents)

### Project Guidance
**Moments DJANGO REST DRF API and Moments REACT Walkthrough Project** I utilized the Moments Walkthrough Project as a foundational guide. This project provided valuable insights into structuring the application, implementing various features, and ensuring a seamless user experience.
The Moments project had several ideas and functionalities similar to what I envisioned for Diving Center, which helped streamline my development process.


### Personal Thanks
- Many thanks to **my husband** for his incredible support and encouragement throughout this journey.
- My heartfelt gratitude to **my son**, who is 18 months old, for bringing joy and motivation into my life.
- Thanks to **Kristyna, Cohort facilitator** at Code Institute, for always being there to provide all the information needed and for keeping the positive energy up.
- Thanks to  my Code Institute **mentor** and my **fellow students** for constantly inspiring me on Slack and being there for each other to help in times of trouble.

[Back to top](#table-of-contents)