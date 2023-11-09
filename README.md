<h1 align="center">Uni-Cronos</h1>

# General Information
Uni-Cronos is an innovative web application designed specifically to simplify the creation of university schedules. With Uni-Cronos, you can customize your schedules in an efficient and personalized way in just a few seconds. This tool allows you to take full control of your study plan, allowing you to include the subjects you want, choose your favorite teachers and avoid those you don't like, and all this according to your schedule and availability

# Requirements of the application
Before starting to use this program, it is important to verify that you have the following elements installed on your system:

**pip**: pip is a Python tool used to download, install, and manage additional libraries and packages that can be added to your programs. Make it easy to add additional functionality to your projects without having to write everything from scratch.

**Django**: This project uses the Django framework. Django is a high-level web development framework that makes it easy to create robust and scalable web applications. We need Django to build and run the web application for this project. To install Django, we use pip, since pip allows us to install Python libraries from the PyPI (Python Package Index) repository:

 ```bash
 pip install Django
 ```

**OpenAI Python SDK**: The OpenAI SDK for Python is a set of tools that allows developers to use OpenAI AI services, such as GPT-3, in Python projects, simplifying the communication and use of these models for processing-related tasks. of natural language.

 ```bash
pip install openai
 ```
# Technologies
![Python](https://img.shields.io/badge/-Typescript-333333?style=flat&logo=python)
![PostgreSQL](https://img.shields.io/badge/-Typescript-333333?style=flat&logo=postgresql)
![JavaScript](https://img.shields.io/badge/-JavaScript-333333?style=flat&logo=javascript)
![HTML](https://img.shields.io/badge/-HTML5-333333?style=flat&logo=HTML5)
![CSS](https://img.shields.io/badge/-CSS-333333?style=flat&logo=CSS3&logoColor=1572B6)

# Installation instructions

1. Navigate to your project folder:
  ```bash
cd your-project
  ```

2. Clone this repository to your local repository:
  ```bash
    git clone --single-branch --branch main https://github.com/AnaSofiR/Project-Uni-Cronos.git
  ```

3. Perform database migrations:
  ```bash
    python manage.py migrate
  ```

4. Run the server:
  ```bash
    python manage.py runserver
  ```

5. Enter the page [http://localhost:8000/](http://localhost:8000/) to see the application working.


# How our application works?
1. Choose the times that you do not have available during the week.
2. Choose the subjects you want to see in the semester.
3. Choose the teachers you like and then the ones you don't like.
4. Finally, the application will use this information to generate the schedules that best suit your preferences.
  
