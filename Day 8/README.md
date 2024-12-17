# Day 8: Flask with MySQL Basics

This README covers the following topics:
- Setting up MySQL with XAMPP
- Installing Flask and MySQL dependencies
- Using Routes in Flask
- Displaying Data from MySQL
- Getting Data from MySQL
- User Sessions and Login
- Redirecting with `url_for`

---

## 1. Setting up MySQL with XAMPP

1. **Install XAMPP:**
   Download and install XAMPP from [apachefriends.org](https://www.apachefriends.org/).

2. **Start MySQL:**
   Open the XAMPP control panel and start the MySQL service.

3. **Access phpMyAdmin:**
   Go to [http://localhost/phpmyadmin](http://localhost/phpmyadmin) to manage your databases.

4. **Create a Database:**
   - Click on **"New"** and create a database (e.g., `flask_app`).
   - Add tables as required.

---

## 2. Installing Flask and MySQL Dependencies

Run the following command to install the necessary packages:

```bash
pip install flask flask-mysql flask_sqlalchemy flask-mysql-connector
```

---

## 3. Using Routes in Flask

Routes in Flask define the different endpoints of your application.

1. **Basic Route:**
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Welcome to the Homepage!"

    if __name__ == "__main__":
        app.run(debug=True)
    ```

2. **Dynamic Route:**
    ```python
    @app.route('/user/<name>')
    def user(name):
        return f"Hello, {name}!"
    ```

3. **POST and GET Methods:**
    ```python
    @app.route('/submit', methods=['POST', 'GET'])
    def submit():
        if request.method == 'POST':
            data = request.form['input_data']
            return f"Data Received: {data}"
        return "Submit Page"
    ```

---

## 4. Displaying Data from MySQL

1. **Set up the Database Connection:**
    ```python
    from flask import Flask, render_template
    from flask_mysql_connector import MySQL

    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DATABASE'] = 'flask_app'

    mysql = MySQL(app)
    ```

2. **Fetch Data in a Route:**
    ```python
    @app.route('/users')
    def users():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        cursor.close()
        return render_template('users.html', users=data)
    ```

3. **Display Data in the Template (`users.html`):**
    ```html
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
        {% for user in users %}
        <tr>
            <td>{{ user[0] }}</td>
            <td>{{ user[1] }}</td>
            <td>{{ user[2] }}</td>
        </tr>
        {% endfor %}
    </table>
    ```

---

## 5. Getting Data from MySQL

1. **Insert Data:**
    ```python
    @app.route('/add_user', methods=['POST', 'GET'])
    def add_user():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('users'))
    ```

2. **Form to Submit Data (`add_user.html`):**
    ```html
    <form method="POST" action="/add_user">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <button type="submit">Add User</button>
    </form>
    ```

---

## 6. User Sessions and Login

1. **Set Up Sessions:**
    ```python
    from flask import session

    app.secret_key = 'your_secret_key'

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            cursor.close()

            if user:
                session['user'] = username
                return redirect(url_for('dashboard'))
            else:
                return "Invalid Credentials"
        return render_template('login.html')
    ```

2. **Logout:**
    ```python
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))
    ```

3. **Protect Routes:**
    ```python
    @app.route('/dashboard')
    def dashboard():
        if 'user' in session:
            return f"Welcome {session['user']}!"
        return redirect(url_for('login'))
    ```

---

## 7. Redirecting with `url_for`

Flask’s `url_for` is used for URL generation and redirection.

1. **Redirect to Another Route:**
    ```python
    @app.route('/home')
    def home():
        return redirect(url_for('dashboard'))
    ```

2. **Using `url_for` in Templates:**
    ```html
    <a href="{{ url_for('logout') }}">Logout</a>
    ```

---

## Final Notes
- Always sanitize inputs to avoid SQL injection.
- Use environment variables to store sensitive data like database credentials.
- For production, configure Flask to run with a proper WSGI server like Gunicorn.
