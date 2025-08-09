Tweet App
This is a simple social media-style web application built with Django. Users can post tweets with optional images, and all posts are saved to a database and can be viewed on a dedicated page. The application includes word filtering to prohibit certain words and a custom Django admin panel for managing posts.

Prerequisites
To run this project, you need to have the following installed on your system:

Python 3.10 or higher

pip (Python package installer)

Getting Started
Follow these steps to get a copy of the project up and running on your local machine.

1. Clone the repository
Open your terminal or command prompt and clone the project to your local machine using this command:

git clone [Your Repository URL Here]
cd [Your Project Folder Name]

2. Create a virtual environment
It's a good practice to use a virtual environment to manage project dependencies.

python -m venv .venv

3. Activate the virtual environment
On Windows:

.venv\Scripts\activate

On macOS and Linux:

source .venv/bin/activate

4. Install dependencies
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

Running the Application
After installation, you can run the development server to see the application in action.

1. Apply database migrations
Run the migrations to create the database tables for your models.

python manage.py makemigrations
python manage.py migrate

2. Create an admin user
To access the Django admin panel, you need to create a superuser.

python manage.py createsuperuser

For the sake of this example, use the following credentials:

Username: admin

Password: 123

3. Run the server
Start the development server with this command:

python manage.py runserver

You can now access the application in your web browser:

Public Tweet Page: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

How to Create a Tweet
Navigate to the public tweet page at http://127.0.0.1:8000/.

Fill in the tweet text and optionally upload an image.

Click "Post Tweet."

You will be redirected to the "Recent Tweets" page, where your new post will appear.

To see all the posts and manage them, you can log in to the admin panel at http://127.0.0.1:8000/admin/ using the admin credentials you created.
