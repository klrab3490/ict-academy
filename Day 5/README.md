# Day 5

## Topics
- **Button**
    - **Check**
    - **Click / Button**
    - **Dropdown**
    - **Radio Button**
    - **Scale**
- **Django**
---

In Python programming, you can create buttons in graphical user interface (GUI) applications using various libraries like `Tkinter`, `PyQt`, or `Kivy`. Here, I'll show you how to create a simple **button** using **Tkinter**, which is the standard Python library for building GUI applications.

### **1. Tkinter Button Example**

Here’s how you can create a basic Python application with a button using `Tkinter`.


#### **Code Example: Button in Tkinter**

```python
from tkinter import *

# Create the main window
root = Tk()
root.title("Button Example")

# Define a function to be called when the button is clicked
def on_button_click():
    print("Button was clicked!")

# Create a button widget
button = Button(root, text="Click Me", command=on_button_click)

# Place the button in the window
button.pack(pady=20)

# Run the application
root.mainloop()
```

### **2. More Button Variations:**
You can customize the appearance and behavior of buttons. Here are a few variations:

#### **a) Button with a different color and size:**
```python
button = Button(root, text="Click Me", command=on_button_click, bg="blue", fg="white", font=("Arial", 14))
button.pack(pady=20)
```

- `bg="blue"` sets the background color of the button to blue.
- `fg="white"` sets the text color to white.
- `font=("Arial", 14)` sets the font and size of the text.

#### **b) Button with an image:**
```python
from tkinter import PhotoImage

# Assuming you have an image file named "button_image.png"
img = PhotoImage(file="button_image.png")
button = Button(root, image=img, command=on_button_click)
button.pack(pady=20)
```
Here, the `PhotoImage` class loads an image, and you can assign it to the button using the `image` parameter.

#### **c) Disabling a button:**
You can disable a button so it cannot be clicked.
```python
button.config(state="disabled")
```

#### **d) Enabling a button again:**
To enable the button again:
```python
button.config(state="normal")
```

### **3. Radio Button Example in Tkinter**

A **radio button** allows the user to select only one option from a set. Here's an example of how to create a radio button in Tkinter.

```python
import tkinter as tk

# Create the main window
root = Tk()
root.title("Radio Button Example")

# Define a function to handle the radio button selection
def on_radio_button_select():
    print(f"Selected option: {selected_option.get()}")

# Create a Tkinter variable to hold the selected value
selected_option = StringVar()

# Create radio buttons
radio1 = Radiobutton(root, text="Option 1", value="Option 1", variable=selected_option, command=on_radio_button_select)
radio2 = Radiobutton(root, text="Option 2", value="Option 2", variable=selected_option, command=on_radio_button_select)

# Pack radio buttons
radio1.pack()
radio2.pack()

# Run the application
root.mainloop()
```

In this case:
- `selected_option = StringVar()` is used to store the value of the selected radio button.
- `variable=selected_option` binds the radio buttons to the variable.
- `command=on_radio_button_select` is used to call a function when a radio button is selected.

---

### **Introduction to Django:**

Django is a high-level Python web framework that enables fast development of secure and maintainable websites. It follows the "DRY" (Don't Repeat Yourself) principle, ensuring that developers can create robust applications with minimal code duplication. In this guide, we'll walk through how to install Django, initialize a basic project, set up templates, and run the development server.

---

### **1. Installing Django:**

Before you can begin working with Django, you need to install it. The easiest way to install Django is through **pip**, the Python package manager.

#### **Step 1: Install Django**

To install Django globally, run the following command in your terminal or command prompt:

```bash
pip install django
```

This will download and install the latest version of Django and its dependencies.

#### **Step 2: Verify the Installation**

To ensure Django has been installed correctly, you can check the version by running:

```bash
django-admin --version
```

You should see the installed version of Django.

---

### **2. Creating a Django Project:**

Once Django is installed, you can create a new project. A Django project consists of settings, configurations, and the overall structure of your web application.

#### **Step 1: Create a New Project**

To create a new project, use the following command:

```bash
django-admin startproject myproject
```

This command will create a directory named `myproject` containing the basic setup of a Django project, including the following files:

- `manage.py`: A command-line tool for interacting with the project.
- A subdirectory `myproject/` containing:
  - `settings.py`: Configurations for the project.
  - `urls.py`: URL routing.
  - `wsgi.py`: Interface for running the app in production.
  - `asgi.py`: Interface for asynchronous servers.

#### **Step 2: Navigate to Your Project Directory**

```bash
cd myproject
```

---

### **3. Initializing Templates in Django:**

Templates in Django allow you to dynamically generate HTML pages with context from views. Django uses its own templating engine for rendering these pages.

#### **Step 1: Create a Django App**

Before creating templates, you'll need a Django app within the project. An app is a component that handles specific functionality (e.g., a blog, user authentication, etc.).

Run the following command to create a new app:

```bash
python manage.py startapp myapp
```

This will create a folder called `myapp` with the following structure:

- `views.py`: The logic for handling HTTP requests.
- `models.py`: The models for your database schema.
- `tests.py`: A file for writing unit tests.
- `urls.py`: URL configuration for this app (you may need to create it).

#### **Step 2: Set Up Templates Directory**

1. Inside your app's directory (`myapp`), create a folder called `templates`.
2. Inside the `templates` folder, create another folder named after your app (e.g., `myapp`), so that the path is `myapp/templates/myapp/`.
   
   The directory structure should look like this:
   ```
   myapp/
   ├── templates/
   │   └── myapp/
   │       └── home.html
   ```

3. In `home.html`, write a basic template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Django</title>
</head>
<body>
    <h1>Hello, {{ name }}! Welcome to Django.</h1>
</body>
</html>
```

This template will render the `name` context variable passed from the view.

#### **Step 3: Update the Django Settings**

You need to tell Django where to look for templates. Open `settings.py` and find the `TEMPLATES` setting. It should already include `'DIRS': []` where you can add paths to your template directories.

Ensure it includes the `DIRS` setting to point to your templates:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

### **4. Writing Views and Rendering Templates:**

Now, let's create a view that will render the `home.html` template.

#### **Step 1: Define a View in `views.py`**

In `myapp/views.py`, create a view to render the template:

```python
from django.shortcuts import render

def home(request):
    context = {
        'name': 'John Doe'
    }
    return render(request, 'myapp/home.html', context)
```

This view will pass a context variable `name` to the template, which will be rendered in the HTML page.

#### **Step 2: Configure URLs**

You need to map a URL to this view. Open the `urls.py` file in your project directory (`myproject/urls.py`) and include the app's URL configuration:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

Then, create a `urls.py` file in your `myapp` directory (if it doesn’t already exist), and add the path for your view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

### **5. Running the Django Development Server:**

Once you’ve set up your project and app, you can run the development server to see your changes live.

#### **Step 1: Run the Server**

In the terminal, navigate to your project directory (where `manage.py` is located) and run:

```bash
python manage.py runserver
```

Django will start a local development server. You should see something like this in the terminal:

```
Starting development server at http://127.0.0.1:8000/
```

#### **Step 2: Access the Application**

Open your browser and navigate to `http://127.0.0.1:8000/`. You should see the `home.html` template rendered with the message: "Hello, John Doe! Welcome to Django."

---
