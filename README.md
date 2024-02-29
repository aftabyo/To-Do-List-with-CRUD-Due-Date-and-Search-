![Screenshot 2024-02-29 235935](https://github.com/aftabyo/To-Do-List-with-CRUD-Due-Date-and-Search-/assets/86048783/07c7e47a-9b15-4eaa-83ba-cf2107fabaad)

![Screenshot 2024-02-29 235958](https://github.com/aftabyo/To-Do-List-with-CRUD-Due-Date-and-Search-/assets/86048783/c5c03043-7e43-4543-b1ad-9d066468845d)

![Screenshot 2024-03-01 000011](https://github.com/aftabyo/To-Do-List-with-CRUD-Due-Date-and-Search-/assets/86048783/6c99770d-3197-411a-a8ee-675d8e3bf227)

```markdown
# Django Todo List

Django Todo List is a simple web application built with Django that allows users to manage their tasks in a todo list format.


## Getting Started

These instructions will help you set up the project on your local machine for development or testing purposes.

### Prerequisites

Make sure you have the following software installed on your machine:

- [Python](https://www.python.org/downloads/) (version 3.x)
- [Django](https://www.djangoproject.com/download/) (install using `pip install django`)

### Installing

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/django-todo-list.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-todo-list
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Apply migrations:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser account for administration:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

### Running the Application

Start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the Todo List application.

### Usage

1. Log in with your superuser account at `http://127.0.0.1:8000/admin/` to manage tasks.

2. Navigate to `http://127.0.0.1:8000/` to view and interact with your todo list.


