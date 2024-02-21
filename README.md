# Race Tracker

## Project Status

As of February 2024, Race Tracker is no longer in active development. This project was my first experience in full-stack app development, and my goal was to use simple tools to build a polished and intuitive web application featuring user-friendly and responsive design principles.

I am now shifting my focus towards building new applications with more complex tools and logic. I'm excited to explore new technologies and implement more sophisticated solutions in my upcoming projects.

## Description
Race Tracker is a Django-powered full-stack web application designed specifically for runners. It offers a platform for managing and analyzing race data, helping users to track their progress, set goals, and stroll down memory lane.

## Tech Stack

Race Tracker is built with a combination of technologies that ensure a robust, scalable, and user-friendly experience. Here's a breakdown of the main components of the project's technology stack:

- **Frontend**:
  - HTML: For structuring the web content.
  - CSS: For styling the web application.
  - Bootstrap: For interactive elements.

- **Backend**:
  - Django: A high-level Python web framework that enables rapid development and clean, pragmatic design.

- **Database**:
  - SQLite: Used for development due to its simplicity and ease of setup.

- **Deployment**:
  - Heroku: Examples of platforms where Race Tracker can be deployed.

- **Version Control**:
  - Git: For source code management.
  - GitHub: For hosting the project repository and tracking issues.

- **Development Tools**:
  - Visual Studio Code: Recommended editor for code development.

This setup was chosen for its simplicity, efficiency, and the wide support community available for these technologies.

## Features
Race Tracker offers a set of intuitive features designed to help runners manage, analyze, and visualize their race data.

* User Authentication: Securely sign up, log in, and log out using Django's built-in authentication system to manage your personal race data.

* Race Management: Keep a detailed record of your races, including information like race name, distance, location, and terrain. This feature allows you to organize and access your race history easily.

* Results Tracking: For each race, you can store and review results, including your finishing time, calculated pace, and rank. This allows for an analysis of your performance over time.

* CRUD Operations: Easily create, read, update, and delete (CRUD) information about races and results. These operations form the core of Race Tracker, making it a versatile tool for managing your racing history.

* Visualizations: Enhance your tracking experience with visual representations of your data. Each race displays a distinct badge representing its distance.

* Multiple Views: Access information about your races and results in a list view for quick comparison, or access detailed views of your races and results, enabling you to dive deep into the specifics of each event and performance.

## Screenshot
![Race Tracker Screenshot](./docs/race-tracker-screenshot%20copy.png)

## Installation Instructions

Follow these steps to get Race Tracker up and running on your local machine:

### 1. Fork and Clone the Repository

First, fork the repository to your GitHub account, then clone your forked repository to your local machine:

    git clone https://github.com/<your-username>/race-tracker.git
    cd race-tracker

Replace `<your-username>` with your GitHub username.

### 2. Set Up a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for Python projects. This keeps dependencies required by different projects separate by creating isolated environments for them. You can create a virtual environment by running:

    python -m venv venv

Activate the virtual environment:

- On Windows:

      .\venv\Scripts\activate

- On macOS and Linux:

      source venv/bin/activate

### 3. Install Dependencies

Install the project dependencies by running:

    pip install -r requirements.txt

### 4. Initialize the Database

Before running the application, you need to make migrations and migrate the database. This sets up your database schema:

    python manage.py makemigrations
    python manage.py migrate

### 5. Run the Development Server

Finally, start the development server:

    python manage.py runserver

### 6. Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application. You should now be able to use Race Tracker locally.

## Support
For support, please open an issue in the [GitHub issue tracker for Race Tracker](https://github.com/danielbrainich/race-tracker/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
