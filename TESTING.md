# Diving Center DRF API Testing

This is the TESTING file for the [Diving Center Django Rest Framework API Backend Live Link](https://pp5api-divingspace-f0baea7c564e.herokuapp.com/).

[Diving Center React Frontend Live Link](https://divingspace-900b5a3db777.herokuapp.com/)
and 
[Diving Center React Frontend Github Repo](https://github.com/AmirShkolnik/DivingCenter)

Return back to the [README.md](README.md) file.

## Table of contents

- [Fit\&Fine DRF API Testing](#fitfine-drf-api-testing)
  - [Table of contents](#table-of-contents)
  - [Manual Testing](#manual-testing)
    - [Authentication Endpoints](#authentication-endpoints)
    - [Profile Endpoints](#profile-endpoints)
    - [Post Endpoints](#post-endpoints)
    - [Comment Endpoints](#comment-endpoints)
    - [Daily Routine Endpoints](#daily-routine-endpoints)
    - [Challenge Endpoints](#challenge-endpoints)
    - [Collaborate Endpoints](#collaborate-endpoints)
    - [Like Endpoints](#like-endpoints)
    - [Follower Endpoints](#follower-endpoints)
  - [Automated Testing](#automated-testing)
    - [Challenge Model Tests](#challenge-model-tests)
    - [Collaborate Model Tests](#collaborate-model-tests)
    - [Comment Model Tests](#comment-model-tests)
    - [Daily Routine Model Tests](#daily-routine-model-tests)
    - [Followers Model Tests](#followers-model-tests)
    - [Like Model Tests](#like-model-tests)
    - [Post API Tests](#post-api-tests)
    - [Profile Model Tests](#profile-model-tests)
    - [Running the Tests](#running-the-tests)
  - [Python Validation](#python-validation)
    - [FitandFine\_DRF Project Python Validation Results](#fitandfine_drf-project-python-validation-results)
    - [Profile Module Python Validation Results](#profile-module-python-validation-results)
    - [Posts Module Python Validation Results](#posts-module-python-validation-results)
    - [Comments Module Python Validation Results](#comments-module-python-validation-results)
    - [Daily Routine Module Python Validation Results](#daily-routine-module-python-validation-results)
    - [Challenges Module Python Validation Results](#challenges-module-python-validation-results)
    - [Followers Module Python Validation Results](#followers-module-python-validation-results)
    - [Likes Module Python Validation Results](#likes-module-python-validation-results)
    - [Collaborate Module Python Validation Results](#collaborate-module-python-validation-results)

##  Manual Testing

This document outlines the comprehensive testing process for our diving center's backend API, built using Django REST Framework. The main goal of our testing is to ensure that all parts of the API work correctly and securely. We've created a set of careful tests for each endpoint, covering different user roles like regular users and admins. 

These tests check if users can access the right information, create and change their own data, and if admins have the extra abilities they need. We want to make sure that everyone can use the API as intended, whether they're booking a course, writing a review, or managing the center's activities. By running these tests, we aim to catch any problems early and make our API reliable and user-friendly for all divers and staff members.

### Authentication Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|---------|-----------------|---------------|-----------|
| `/admin/` | GET | Read | Django Admin interface | | Admin interface loads successfully | Admin interface loaded successfully | ✅ |
| `/dj-rest-auth/logout/` | POST | Delete | Custom logout route | <details> <summary>Click to view Logout</summary> ![Authentication](doc/images/logout/dj-rest-auth-logout.png)</details> | User is logged out and session is terminated | User logged out successfully | ✅ |
| `/dj-rest-auth/login/` | POST | Create | User login | <details><summary>Click to view Login step 1</summary>![Authentication](doc/images/login/dj-rest-auth-login-post-1.png)</details> <details><summary>Click to view Login step 2</summary>![Authentication](doc/images/login/dj-rest-auth-login-post-2.png)</details> | User is authenticated and receives a token | User authenticated and received token | ✅ |
| `/dj-rest-auth/user/` | GET | Read | Get current user details | <details><summary>Click to view User Get</summary>![Authentication](doc/images/user/dj-rest-auth-user-get-1.png)</details> | Returns current user's profile information | Returned correct user profile information | ✅ |
| `/dj-rest-auth/user/` | PUT | Update | Update current user details | <details><summary>Click to view User Put</summary>![Authentication](doc/images/user/dj-rest-auth-user-put-1.png)</details> | User details are updated successfully | User details updated correctly | ✅ |
| `/dj-rest-auth/registration/` | POST | Create | User registration | <details><summary>Click to view Registration Post step 1</summary>![Authentication](doc/images/registration/dj-rest-auth-registration-post.png)</details> <details><summary>Click to view Registration Post step 2</summary>![Authentication](doc/images/registration/dj-rest-auth-registration-post-2.png)</details> <details><summary>Click to view Registration Post step 3</summary>![Authentication](doc/images/registration/dj-rest-auth-registration-post-3.png)</details>| New user account is created | New user account created successfully | ✅ |

### Profile Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/profiles/` | GET | Read | List all profiles | <details><summary>Click to view Profiles List</summary>![Profiles](doc/images/profiles/profiles.png)</details> | Returns a list of all user profiles | Returned a list of all user profiles successfully | ✅ |
| `/profiles/{id}/` | GET | Read | Retrieve a specific profile | <details><summary>Click to view Profile Detail</summary>![Profiles](doc/images/profiles/profiles-id.png)</details> | Returns details of a specific user profile | Returned correct details for the specified profile | ✅ |
| `/profiles/{id}/` | PUT | Update | Update a specific profile (owner only) | <details><summary>Click to view Profile Update step 1</summary>![Profiles](doc/images/profiles/profiles-put-1.png)</details> <details><summary>Click to view Profile Update step 2</summary>![Profiles](doc/images/profiles/profiles-put-2.png)</details> | Updates the profile details for the authenticated user | Profile details updated successfully for the authenticated user | ✅ |
| `/profiles/{id}/` | PATCH | Update | Partially update a specific profile (owner only) | | Partially updates the profile details for the authenticated user | Profile details partially updated successfully for the authenticated user | ✅ |

### Posts Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/posts/` | GET | Read | Retrieve a list of posts | <details><summary>Click to view Posts List</summary>![Posts](doc/images/posts/posts-list-users-get-1.png)</details> | List of posts returned | List of posts returned | ✅ |
| `/posts/` | POST | Create | Create a new post | <details><summary>Click to view Create Post</summary>![Posts]()</details> | Post created, details returned | Post created, details returned | ✅ |
| `/posts/<id>/` | GET | Read | Retrieve a specific post by ID | <details><summary>Click to view Post Detail</summary>![Posts]()</details> | Post details returned | Post details returned | ✅ |
| `/posts/<id>/` | PUT | Update | Update a specific post by ID | <details><summary>Click to view Update Post - Missing Title Test</summary>![Posts](doc/images/posts/posts-post-title-missing-1.png)</details> | Post updated, updated details returned | Post updated, updated details returned | ✅ |
| `/posts/<id>/` | PATCH | Update | Partially update a specific post by ID | <details><summary>Click to view Partial Update Post</summary>![Posts]()</details> | Post partially updated, updated details returned | Post partially updated, updated details returned | ✅ |
| `/posts/<id>/` | DELETE | Delete | Delete a specific post by ID | <details><summary>Click to view Delete Post</summary>![Posts]()</details> | Post deleted | Post deleted | ✅ |

### Comments Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/comments/` | GET | Read | List all comments | <details><summary>Click to view Comments List 1</summary>![Comments](doc/images/comments/comments-list-all-users-get-1.png)</details> <details><summary>Click to view Comments List 2</summary>![Comments](doc/images/comments/comments-list-all-users-get-2.png)</details> | Returns a list of all comments | Returned a list of all comments successfully | ✅ |
| `/comments/` | POST | Create | Create a new comment (authenticated users only) | <details><summary>Click to view Create Comment step 1</summary>![Comments](doc/images/comments/comments-user-post-1.png)</details> <details><summary>Click to view Create Comment step 2</summary>![Comments](doc/images/comments/comments-user-post-2.png)</details> | New comment is created and returned | New comment created and returned successfully | ✅ |
| `/comments/{id}/` | GET | Read | Retrieve a specific comment | <details><summary>Click to view Comment Detail</summary>![Comments]()</details> | Returns details of a specific comment | Returned correct details for the specified comment | ✅ |
| `/comments/{id}/` | PUT | Update | Update a specific comment (owner only) | <details><summary>Click to view Update Comment step 1</summary>![Comments](doc/images/comments/comments-user-put-1.png)</details> <details><summary>Click to view Update Comment step 2</summary>![Comments](doc/images/comments/comments-user-put-2.png)</details> | Updates the comment details for the authenticated owner | Comment details updated successfully for the authenticated owner | ✅ |
| `/comments/{id}/` | PATCH | Update | Partially update a specific comment (owner only) | <details><summary>Click to view Partial Update Comment</summary>![Comments]()</details> | Partially updates the comment details for the authenticated owner | Comment details partially updated successfully for the authenticated owner | ✅ |
| `/comments/{id}/` | DELETE | Delete | Delete a specific comment (owner only) | <details><summary>Click to view Delete Comment step 1</summary>![Comments](doc/images/comments/comments-user-delete-1.png)</details> <details><summary>Click to view Delete Comment step 2</summary>![Comments](doc/images/comments/comments-user-delete-2.png)</details> | Deletes the specified comment for the authenticated owner | Comment deleted successfully for the authenticated owner | ✅ |

### Likes Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/likes/` | GET | Read | List all likes | <details><summary>Click to view Likes List</summary>![Likes](doc/images/likes/likes-get-all.png)</details> | Returns a list of all likes | Returned a list of all likes successfully | ✅ |
| `/likes/` | POST | Create | Create a new like (authenticated users only) | <details><summary>Click to view Create Like setp 1</summary>![Likes](doc/images/likes/likes-post-user-1.png)</details> <details><summary>Click to view Create Like step 2</summary>![Likes](doc/images/likes/likes-post-user-2.png)</details> | New like is created and returned | New like created and returned successfully | ✅ |
| `/likes/{id}/` | GET | Read | Retrieve a specific like | <details><summary>Click to view Like Detail step 1</summary>![Likes](doc/images/likes/likes-get-user-1.png)</details> <details><summary>Click to view Like Detail step 2</summary>![Likes](doc/images/likes/likes-get-user-2.png)</details> | Returns details of a specific like | Returned correct details for the specified like | ✅ |
| `/likes/{id}/` | DELETE | Delete | Delete a specific like (owner only) | <details><summary>Click to view Delete Like step 1</summary>![Likes](doc/images/likes/likes-delete-user-1.png)</details> <details><summary>Click to view Delete Like step 2</summary>![Likes](doc/images/likes/likes-delete-user-2.png)</details> <details><summary>Click to view Delete Like step 3</summary>![Likes](doc/images/likes/likes-delete-user-3.png)</details>| Deletes the specified like for the authenticated owner | Like deleted successfully for the authenticated owner | ✅ |

### Followers Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/followers/` | GET | Read | List all follower relationships | <details><summary>Click to view Followers List</summary>![Followers](doc/images/followers/followers-get-1.png)</details> | Returns a list of all follower relationships | Returned a list of all follower relationships successfully | ✅ |
| `/followers/` | POST | Create | Create a new follower relationship (authenticated users only) | <details><summary>Click to view Create Follower</summary>![Followers](doc/images/followers/followers-post-2.png)</details> | New follower relationship is created and returned | New follower relationship created and returned successfully | ✅ |
| `/followers/{id}/` | GET | Read | Retrieve a specific follower relationship | <details><summary>Click to view Follower Detail</summary>![Followers]()</details> | Returns details of a specific follower relationship | Returned correct details for the specified follower relationship | ✅ |
| `/followers/{id}/` | DELETE | Delete | Delete a specific follower relationship (owner only) | <details><summary>Click to view Delete Follower step 1</summary>![Followers](doc/images/followers/followers-delete-1.png)</details> <details><summary>Click to view Delete Follower step 2</summary>![Followers](doc/images/followers/followers-delete-2.png)</details> <details><summary>Click to view Delete Follower step 3</summary>![Followers](doc/images/followers/followers-delete-3.png)</details>| Deletes the specified follower relationship for the authenticated owner | Follower relationship deleted successfully for the authenticated owner | ✅ |

### Bookings Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/bookings/` | GET | Read | List all bookings for the authenticated user |   <details><summary>Click to view Bookings List - Authenticated - Empty List</summary>![Bookings](doc/images/bookings/bookings-logged-in-get-1.png)</details> <details><summary>Click to view Bookings List - Authenticated - Not Empty</summary>![Bookings](doc/images/bookings/bookings-get.png)</details> <details><summary>Click to view Bookings List - Not Authenticated User</summary>![Bookings](doc/images/bookings/bookings-not-authenticated.png)</details>| Returns a list of all bookings for the authenticated user | Returned a list of all bookings for the authenticated user successfully | ✅ |
| `/bookings/` | POST | Create | Create a new booking (authenticated users only) | <details><summary>Click to view Create Booking Test - Past Date</summary>![Bookings](doc/images/bookings/bookings-logged-in-post-past-date-1.png)</details> <details><summary>Click to view Create Booking Test - Booking Same Coures</summary>![Bookings](doc/images/bookings/bookings-logged-in-post-same-course-4.png)</details> <details><summary>Click to view Create Booking Test - Booking Wrong Date</summary>![Bookings](doc/images/bookings/bookings-logged-in-post-wrong-date-2.png)</details> <details><summary>Click to view Create Booking Test - Booking Wrong Time</summary>![Bookings](doc/images/bookings/bookings-logged-in-post-wrong-time-3.png)</details>| New booking is created and returned | New booking created and returned successfully | ✅ |
| `/bookings/{id}/` | GET | Read | Retrieve a specific booking | <details><summary>Click to view Booking Detail - Specific Booking</summary>![Bookings](doc/images/bookings/bookings-get-spesific.png)</details> | Returns details of a specific booking | Returned correct details for the specified booking | ✅ |
| `/bookings/{id}/` | PUT | Update | Update a specific booking (owner only) | <details><summary>Click to view Update Booking step 1</summary>![Bookings](doc/images/bookings/bookings-logged-in-get-1.png)</details> <details><summary>Click to view Update Booking step 2 - Success</summary>![Bookings](doc/images/bookings/bookings-id-put-success-6.png)</details> <details><summary>Click to view Update Booking Test 1 - Update Wrong Time</summary>![Bookings](doc/images/bookings/bookings-id-put-wrong-time-2.png)</details> <details><summary>Click to view Update Booking Test 2 - Update Wrong Date</summary>![Bookings](doc/images/bookings/bookings-id-put-wrong-date-3.png)</details> <details><summary>Click to view Update Booking Test 3 - Update Past Date</summary>![Bookings](doc/images/bookings/bookings-id-put-past-date-4.png)</details> <details><summary>Click to view Update Booking Test 4 - Update No Course</summary>![Bookings](doc/images/bookings/bookings-id-put-must-have-course-5.png)</details> | Updates the booking details for the authenticated owner | Booking details updated successfully for the authenticated owner | ✅ |
| `/bookings/{id}/` | PATCH | Update | Partially update a specific booking (owner only) | | Partially updates the booking details for the authenticated owner | Booking details partially updated successfully for the authenticated owner | ✅ |
| `/bookings/{id}/` | DELETE | Delete | Delete a specific booking (owner only) | <details><summary>Click to view Delete Booking step 1</summary>![Bookings](doc/images/bookings/bookings-id-delete-1.png)</details> <details><summary>Click to view Delete Booking step 2 - Delete Success</summary>![Bookings](doc/images/bookings/bookings-id-delete-success-2.png)</details> | Deletes the specified booking for the authenticated owner | Booking deleted successfully for the authenticated owner | ✅ |

### Contact Us Endpoints

For testing purposes with the Django Rest Framework, I used the following code:
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "subject": "Test Subject",
    "message": "This is a test message."
}
In the future, for a better user experience, I will implement the Django Rest Framework HTML function to maintain browser compatibility.

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/contactus/` | POST | Create | Create a new contact message | <details><summary>Click to view Create Contact Message step 1 - Empty</summary>![Contact Us](doc/images/contactus/contactus.png)</details> <details><summary>Click to view Create Contact Message step 2 - Add Message</summary>![Contact Us](doc/images/contactus/contactus-post-2.png)</details> <details><summary>Click to view Create Contact Message step 3 - Success</summary>![Contact Us](doc/images/contactus/contactus-post-success-3.png)</details> <details><summary>Click to view Create Contact Message Test - Missing Fields</summary>![Contact Us](doc/images/contactus/contactus-post-empty-1.png)</details>| New contact message is created and returned | New contact message created and returned successfully | ✅ |
| `/contactus/{id}/` | PUT | Update | Update an existing contact message | <details><summary>Click to view Update Contact Message step 1</summary>![Contact Us](doc/images/contactus/contactup-put-update-3.png)</details> <details><summary>Click to view Update Contact Message step 2</summary>![Contact Us](doc/images/contactus/contactup-put-update-4.png)</details> <details><summary>Click to view Update Contact Message step 3</summary>![Contact Us](doc/images/contactus/contactup-put-update-5.png)</details> <details><summary>Click to view Update Contact Message step 4</summary>![Contact Us](doc/images/contactus/contactup-put-update-6.png)</details>| Updates the existing contact message | Contact message updated successfully | ✅ |
| `/contactus/{id}` | DELETE | Delete | Delete a specific contact message | <details><summary>Click to view Delete Contact Message step 1</summary>![Contact Us](doc/images/contactus/contactus-delete-1.png)</details> <details><summary>Click to view Delete Contact Message step 2 - Delete Success</summary>![Contact Us](doc/images/contactus/contactus-delete-4.png)</details> <details><summary>Click to view Delete Updated Contact Message step 1 </summary>![Contact Us](doc/images/contactus/contactus-delete-after-update-1.png)</details> <details><summary>Click to view Delete Updated Contact Message step 2 </summary>![Contact Us](doc/images/contactus/contactus-delete-after-update-2.png)</details>| Deletes the specified contact message | Contact message deleted successfully | ✅ |

### Courses Endpoints

#### Future Improvements Flexible Course Management System and Dynamic Course Types and Prices

We plan to enhance the flexibility of our Course model by:

1. Removing hardcoded course types and prices.
2. Implementing a system that allows website owners to:
   - Add, edit, or remove course types dynamically.
   - Set custom price points without being restricted to predefined options.

This improvement will provide greater adaptability to changing business needs and course offerings.

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/courses/` | GET | Read | List all courses | <details><summary>Click to view Courses List</summary>![Courses](doc/images/courses/courses-get.png)</details> | Returns a list of all courses | Returned a list of all courses successfully | ✅ |
| `/courses/` | POST | Create | Create a new course (admin only) | <details><summary>Click to view Create Course Test - Missing Fields</summary>![Courses](doc/images/courses/courses-post-1.png)</details> <details><summary>Click to view Create Course step 1</summary>![Courses](doc/images/courses/courses-post-2.png)</details> <details><summary>Click to view Create Course step 2 - Success</summary>![Courses](doc/images/courses/courses-post-3.png)</details> | New course is created and returned (admin only) | New course created and returned successfully (admin only) | ✅ |
| `/courses/{slug}/` | GET | Read | Retrieve a specific course | <details><summary>Click to view Course Detail</summary>![Courses](doc/images/courses/courses-slug-get.png)</details> | Returns details of a specific course | Returned correct details for the specified course | ✅ |
| `/courses/{slug}/` | PUT | Update | Update a specific course (admin only) | <details><summary>Click to view Update Course Test - Missing Fields</summary>![Courses](doc/images/courses/courses-put-1.png)</details> <details><summary>Click to view Update Course step 1</summary>![Courses](doc/images/courses/courses-put-2.png)</details> <details><summary>Click to view Update Course step 2 - Success</summary>![Courses](doc/images/courses/courses-put-3.png)</details>| Updates the course details (admin only) | Course details updated successfully (admin only) | ✅ |
| `/courses/{slug}/` | PATCH | Update | Partially update a specific course (admin only) | | Partially updates the course details (admin only) | Course details partially updated successfully (admin only) | ✅ |
| `/courses/{slug}/` | DELETE | Delete | Delete a specific course (admin only) | <details><summary>Click to view Delete Course step 1</summary>![Courses](doc/images/courses/courses-delete-1.png)</details> <details><summary>Click to view Delete Course step 2 - Success</summary>![Courses](doc/images/courses/courses-delete-2.png)</details> | Deletes the specified course (admin only) | Course deleted successfully (admin only) | ✅ |

### Reviews Endpoints

| Endpoint | Method | CRUD Operation | Description | Images | Expected Result | Actual Result | Pass/Fail |
|----------|--------|----------------|-------------|--------|-----------------|---------------|-----------|
| `/reviews/` | GET | Read | List all reviews | <details><summary>Click to view Reviews List</summary>![Reviews](doc/images/reviews/reviews-get.png)</details> | Returns a list of all reviews | Returned a list of all reviews successfully | ✅ |
| `/reviews/` | POST | Create | Create a new review (authenticated users only) | <details><summary>Click to view Create Review Test - Missing Fields</summary>![Reviews](doc/images/reviews/reviews-post-missing-fields.png)</details> <details><summary>Click to view Create Review step 1</summary>![Reviews](doc/images/reviews/reviews-post-1.png)</details> <details><summary>Click to view Create Review step 2</summary>![Reviews](doc/images/reviews/reviews-post-2.png)</details>| New review is created and returned | New review created and returned successfully | ✅ |
| `/reviews/{id}/` | GET | Read | Retrieve a specific review | <details><summary>Click to view Review Detail</summary>![Reviews]()</details> | Returns details of a specific review | Returned correct details for the specified review | ✅ |
| `/reviews/{id}/` | PUT | Update | Update a specific review (owner only) | <details><summary>Click to view Update Review</summary>![Reviews]()</details> | Updates the review details for the authenticated owner | Review details updated successfully for the authenticated owner | ✅ |
| `/reviews/{id}/` | PATCH | Update | Partially update a specific review (owner only) | <details><summary>Click to view Partial Update Review</summary>![Reviews]()</details> | Partially updates the review details for the authenticated owner | Review details partially updated successfully for the authenticated owner | ✅ |
| `/reviews/{id}/` | DELETE | Delete | Delete a specific review (owner only) | <details><summary>Click to view Delete Review step 1</summary>![Reviews](doc/images/reviews/reviews-owner-delete-1.png)</details> <details><summary>Click to view Delete Review step 2 </summary>![Reviews](doc/images/reviews/reviews-owner-delete-2.png)</details> <details><summary>Click to view Delete Review step 3 - Success</summary>![Reviews](doc/images/reviews/reviews-owner-delete-3.png)</details>| Deletes the specified review for the authenticated owner | Review deleted successfully for the authenticated owner | ✅ |

## Automated Testing 

This provides an overview of the automated tests implemented for the Fit and Fine project. These tests ensure the reliability and correctness of various functionalities, including user authentication, model validations, and API endpoints.

### Challenge Model Tests


**File:** `/workspace/FitandFine-P5/challenges/tests.py`

**Description:** Tests for the Challenge model, ensuring that challenges are created, associated with users, and can be updated correctly.

**Tests:**
- **Challenge Creation:** Verifies that a challenge can be created.
- **User Association:** Ensures a challenge is associated with the correct user.
- **Default Field Values:** Checks the default values for challenge fields.
- **Retrieve by User:** Tests if a challenge can be retrieved by the associated user.
- **Update Fields:** Verifies that challenge fields can be updated correctly.

![alt text](documentation/tests/image.png)

### Collaborate Model Tests

**File:** `/workspace/FitandFine-P5/collaborate/tests.py`

**Description:** Tests for the About and Collaborate models, ensuring they can be created and updated correctly.

**Tests:**
- **About Creation:** Verifies that an About entry can be created.
- **About Update:** Checks that the About entry can be updated.
- **Collaborate Creation:** Ensures a Collaborate entry can be created.
- **Collaborate Field Values:** Validates the fields of the Collaborate model.

![alt text](documentation/tests/image1.png)

### Comment Model Tests

**File:** `/workspace/FitandFine-P5/comments/tests.py`

**Description:** Tests for the Comment model, ensuring that comments are correctly associated with users and posts.

**Tests:**
- **Comment Creation:** Verifies that a comment can be created.
- **User Association:** Ensures a comment is associated with the correct user.
- **Post Association:** Checks that a comment is associated with the correct post.
- **Comment Content:** Validates the content of the comment.
- **Comment Ordering:** Ensures comments are ordered correctly.

![alt text](documentation/tests/image2.png)

### Daily Routine Model Tests

**File:** `/workspace/FitandFine-P5/dailyroutines/tests.py`

**Description:** Tests for the Daily Routine model, ensuring routines are valid and realistic.

**Tests:**
- **Routine Creation:** Verifies that a daily routine can be created.
- **Date Validation:** Ensures the date is not set in the future.
- **Update Mood:** Tests updating the mood of a routine.
- **Profile Link:** Ensures routines link to the user's profile.
- **Water Intake Validation:** Checks for realistic water intake values.
- **Default Junk Food Setting:** Verifies the default setting for junk food consumption.

![alt text](documentation/tests/image7.png)

### Followers Model Tests

**File:** `/workspace/FitandFine-P5/followers/tests.py`

**Description:** Tests for the Follower model, ensuring follower relationships are managed correctly.

**Tests:**
- **Follower Creation:** Verifies that a follower relationship can be created.
- **Owner Association:** Ensures a follower is associated with the correct owner.
- **Followed Association:** Checks that a follower is associated with the correct followed user.
- **Unique Follower:** Validates that duplicate follower relationships are not allowed.

![alt text](documentation/tests/image3.png)

### Like Model Tests

**File:** `/workspace/FitandFine-P5/likes/tests.py`

**Description:** Tests for the Like model, ensuring likes are managed correctly.

**Tests:**
- **Like Creation:** Verifies that a like can be created.
- **User Association:** Ensures a like is associated with the correct user.
- **Post Association:** Checks that a like is associated with the correct post.
- **Unique Like:** Validates that duplicate likes are not allowed.

![alt text](documentation/tests/image4.png)

### Post API Tests

**File:** `/workspace/FitandFine-P5/posts/tests.py`

**Description:** Tests for the Post API, ensuring that users can list, create, and update posts correctly.

**Tests:**
- **List Posts:** Ensures posts can be listed.
- **Create Post (Logged In):** Verifies that a logged-in user can create a post.
- **Create Post (Not Logged In):** Ensures that a non-logged-in user cannot create a post.
- **Retrieve Post by ID:** Checks that a post can be retrieved using a valid ID.
- **Update Post (Own Post):** Verifies that a user can update their own post.
- **Update Post (Others' Post):** Ensures a user cannot update another user's post.

![alt text](documentation/tests/image5.png)

### Profile Model Tests

**File:** `/workspace/FitandFine-P5/profiles/tests.py`

**Description:** Tests for the Profile model, ensuring profiles are created and associated with users correctly.

**Tests:**
- **Profile Creation on User Creation:** Ensures a profile is created when a user is created.
- **User Association:** Checks that a profile is associated with the correct user.
- **Default Field Values:** Verifies the default values for profile fields.
- **Retrieve Profile by User ID:** Ensures a profile can be retrieved by user ID.
- **Update Profile Fields:** Validates that profile fields can be updated correctly.

![alt text](documentation/tests/image6.png)

### Running the Tests

To run the tests, use the following command:
```bash
python manage.py test
```
This command will execute all the tests and provide a summary of the results.

## Python Validation

- **Tool Used:** [CI Python Linter](https://pep8ci.herokuapp.com/#)
- **Purpose:** Analyzes Python source code to identify coding errors, enforce a coding standard, and look for code smells.
- **Process:** Python code within the Diving Center application is analyzed with Pylint to ensure adherence to coding standards and to improve code quality.

### FitandFine_DRF Project Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **settings.py**            | ![screenshot](documentation/validation/fitandfine/settings.JPG) | 0      | 6        |
| **manage.py**              | ![screenshot](documentation/validation/fitandfine/manage.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/fitandfine/urls.JPG)     | 0      | 0        |
| **views.py**               | ![screenshot](documentation/validation/fitandfine/views.JPG)    | 0      | 0        |
| **serializers.py**                | ![screenshot](documentation/validation/fitandfine/serializers.JPG)     | 0      | 0        |
| **permissions.py**               | ![screenshot](documentation/validation/fitandfine/permissions.JPG)    | 0      | 0        |
| **wsgi.py**                | ![screenshot](documentation/validation/fitandfine/wsgi.JPG)     | 0      | 0        |
| **asgi.py**                | ![screenshot](documentation/validation/fitandfine/asgi.JPG)     | 0      | 0        |

### Profile Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/profile/profile_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/profile/profile_models.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/profile/profile_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/profile/profile_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/profile/profile_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/profile/profile_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/profile/profile_tests.JPG)    | 0      | 0        |

### Posts Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/posts/posts_views.JPG)    | 0      | 1        |
| **models.py**              | ![screenshot](documentation/validation/posts/posts_models.JPG)   | 0      | 2        |
| **urls.py**                | ![screenshot](documentation/validation/posts/posts_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/posts/posts_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/posts/posts_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/posts/posts_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/posts/posts_tests.JPG)    | 0      | 0        |

### Comments Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/comments/comments_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/comments/comments_models.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/comments/comments_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/comments/comments_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/comments/comments_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/comments/comments_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/comments/comments_tests.JPG)    | 0      | 0        |

### Daily Routine Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/dailyroutine/routine_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/dailyroutine/routine_models.JPG)   | 0      | 2        |
| **urls.py**                | ![screenshot](documentation/validation/dailyroutine/routine_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/dailyroutine/routine_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/dailyroutine/routine_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/dailyroutine/routine_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/dailyroutine/routine_tests.JPG)    | 0      | 0        |

### Challenges Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/challenges/challenges_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/challenges/challenges_models.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/challenges/challenges_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/challenges/challenges_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/challenges/challenges_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/challenges/challenges_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/challenges/challenges_tests.JPG)    | 0      | 0        |

### Followers Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/followers/followers_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/followers/followers_models.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/followers/followers_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/followers/followers_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/followers/followers_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/followers/followers_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/followers/followers_tests.JPG)    | 0      | 0        |

### Likes Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/likes/likes_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/likes/likes_models.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/likes/likes_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/likes/likes_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/likes/likes_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/likes/likes_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/likes/likes_tests.JPG)    | 0      | 0        |

### Collaborate Module Python Validation Results
| Python File                | Results Screenshots                                | Errors | Warnings |
|----------------------------|----------------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/collaborate/collaborate_views.JPG)    | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/collaborate/collaborate_models.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/collaborate/collaborate_urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/collaborate/collaborate_admin.JPG)    | 0      | 0        |
| **apps.py**                | ![screenshot](documentation/validation/collaborate/collaborate_apps.JPG)     | 0      | 0        |
| **serializers.py**         | ![screenshot](documentation/validation/collaborate/collaborate_serializers.JPG) | 0   | 0        |
| **tests.py**               | ![screenshot](documentation/validation/collaborate/collaborate_tests.JPG)    | 0      | 0        |