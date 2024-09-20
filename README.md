# Django Joke Application

This is a simple Django web application that displays jokes fetched from both a database and the `pyjokes` library. Users can select joke categories and view jokes dynamically.

## Features

- Display jokes from a database
- Fetch jokes from the `pyjokes` library
- Allow users to select joke categories

## Prerequisites

- Python 
- Django
- pyjokes
- pip (python installer package)

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/harizonelopez/django-joke-app.git
    cd django-joke-app
    ```

2. **Create and Activate a Virtual Environment**

    ```sh
    python -m venv venv
    source venv\Scripts\activate   # On mac use `venv/bin/activate` 
    ```

3. **Install Dependencies**

    ```sh
    pip install django pyjokes
    ```

4. **Run the Development Server**

    ```sh
    python manage.py runserver
    ```

5. **Access the Application**

    Open your web browser and go to `http://127.0.0.1:8000` to view the list of jokes and interact with the application.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.