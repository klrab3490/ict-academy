# Day 6: Django Basics

This README covers the following topics:
- Using Django URLs
- Linking two HTML files
- Including scripts and CSS files
- Uploading images
- Passing and Displaying Data

---

## 1. Using Django URLs

Django URLs map views to specific routes. Here's a quick guide:

1. **Define a URL pattern in `urls.py`:**
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),  # Homepage
       path('about/', views.about, name='about'),  # About page
   ]
   ```

2. **Create corresponding views in `views.py`:**
   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html')

   def about(request):
       return render(request, 'about.html')
   ```

3. **Create the templates:**
   Place `home.html` and `about.html` in the `templates` folder.

---

## 2. Linking Two HTML Files

To navigate between pages, use Django's `{% url %}` template tag:

- In `home.html`:
  ```html
  <a href="{% url 'about' %}">Go to About Page</a>
  ```

- In `about.html`:
  ```html
  <a href="{% url 'home' %}">Go to Home Page</a>
  ```

The `name` parameter in the `path` function of `urls.py` is used here.

---

## 3. Including Scripts and CSS Files

To include static files like JavaScript and CSS:

1. **Add the static files directory:** Ensure `settings.py` has:
    ```python
    import os

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
   ```

2. **Create a `static` folder in your app directory.** Inside, create subfolders for CSS, JS, and images as needed.

3. **Load static files in your template:**
   - In the HTML file:
    ```html
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <script src="{% static 'js/script.js' %}"></script>
    ```

4. **File Structure Example:**
   ```
   myapp/
       static/
           css/
               style.css
           js/
               script.js
   ```

---

## 4. Uploading Images

### Setting Up Image Uploads

1. **Update `settings.py`:**
    ```python
    import os 

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    ```

2. **Add media URL patterns in `urls.py`:**
   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

3. **Create a view for uploading images:**
    ```python
    from django.core.files.storage import FileSystemStorage

    def uploadImage(request):
        # Initialize the variable to store the path of the uploaded image
        path = ""

        # Check if the request method is POST
        if request.POST:
            # Check if any files have been uploaded in the request
            if len(request.FILES) != 0:
                # Get the uploaded file from the request with the key "image"
                image = request.FILES["image"]

                # Create a FileSystemStorage instance for saving files
                fs = FileSystemStorage()

                # Save the uploaded image to the file system and get the file name
                fileName = fs.save(image.name, image)  # Saves the image

                # Get the URL path of the saved image
                path = fs.url(fileName)  # Contains Path

        # Return or process the `path` as needed (this part depends on your implementation)

    ``` 

5. **Create the template (`upload_image.html`):**
   ```html
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}

        <div class="form-group d-flex justify-content-start align-items-center">
            <label for="image-upload" class="btn btn-outline-primary">Upload Image</label>
            <input type="file" id="image-upload" name="image" accept="image/*" style="display: none;" onchange="displayFileName()">
            <span id="file-name"></span> 
        </div>

        <button type="submit" class="btn btn-primary btn-block mt-4">Add Data</button>
    </form>
   ```

---

## 5. Passing and Displaying Data

### Passing Data to Templates
Django views can pass data to templates using the context dictionary:

1. **Update the view:**
    ```python
    def home(request):
        context = {
            'greeting': 'Welcome to the Homepage!',
            'items': ['Item 1', 'Item 2', 'Item 3']
        }
        return render(request, 'home.html', context)
    ```

2. **Display the data in the template:**
   ```html
    <h1>{{ greeting }}</h1>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
            {% empty %}
            <div> Empty </div>
        {% endfor %}
    </ul>
   ```

### Getting Data from Forms

1. **Handle form data in the view:**
    ```python
    def submit_data(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            message = request.POST.get("message")
            print(f"Name: {name}, Message: {message}")
        return render(request, 'form.html')
    ```

2. **Create the form template (`form.html`):**
    ```html
    <form method="POST">
        {% csrf_token %}
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Submit</button>
    </form>
    ```

### Displaying Data from the Database

1. **Fetch data in the view:**
    ```python
    from .models import ImageUpload

    def gallery(request):
        images = [
            data....
        ]
        return render(request, 'gallery.html', {'images': images})
    ```

2. **Display data in the template (`gallery.html`):**
    ```html
    <h1>Image Gallery</h1>
    <ul>
        {% for image in images %}
            <li>
                <h2>{{ image.title }}</h2>
                <img src="{{ image.image.url }}" alt="{{ image.title }}">
            </li>
        {% endfor %}
    </ul>
    ```

---

## Final Notes
- Always use `{% csrf_token %}` in forms to protect against CSRF attacks.
- Use `DEBUG = False` in production and configure proper media file handling for security.
- Static files and media uploads must be handled separately in production environments (e.g., using services like AWS S3 or Django's `collectstatic` command).
