# technotesplus

Tech Notes Plus , that lets user to take notes. User can take notes, add them, edit them delete them, search them and even can share them with other users for view only.

## Features

---

- Create user with username, email and password.

- Used JWT for register and login (Couldn't implement properly).

- Update user's name and email. Password reset no available.

- Add, edit, delete and share note. Note sharing from frontend is not available.

- Search notes from frontend is not available.

- Notify user with whom note is shared via email.

- If the note shared is not viewed by the user, then a periodic task will notify user via email daily at 12PM (UTC).

## Project Setup

---

- Python version supported: 3.8+

- Django version: 3.2.6

- DRF version: 3.12.4

- Database: PostgreSQL

- Frontend: Vue2

---

- Clone the project

  ```bash
  git clone git@github.com:adnan-alam/technotesplus.git
  ```

### Backend

- Install **virtualenv** if not installed on system

  ```bash
  # package to create virtual environment
  pip install virtualenv
  ```

- Go to dir **technotesplus**, create a virtual environment **env**

  ```bash
  virtualenv -p /usr/bin/python3.8 env
  ```

- Create a **.env** file, copy the environment variables from **env_vars_example** into **.env** and set the required values.

- Activate the virtual environment

  ```bash
  source env/bin/activate
  ```

- Install all Python the dependencies

  ```bash
  pip install -r requirements.txt
  ```

- Run database migrations:

  ```bash
  ./manage.py migrate
  ```

- Create Superuser:

  ```bash
  ./manage.py createsuperuser
  ```

  need to provide the username, email and password.

- Run the development server

  ```bash
  ./manage.py runserver
  ```

  and the Django server will be available on `http://127.0.0.1:8000/`.

- For task scheduling, **huey** is being user. It has dependency of **Redis**, so it must be installed on the system. Run the consumer:

  ```bash
  ./manage.py run_huey
  ```

### Frontend

- Go to **frontend** directory, install packages:

  ```
  npm install
  ```

- Run the development server:
  ```
  npm run dev
  ```
  frontend will be available on `http://127.0.0.1:8080/`.
