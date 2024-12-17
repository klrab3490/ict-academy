# Day 7 - Install MongoDB and Connect to Python

#### 1. **Install MongoDB**
Make sure MongoDB is installed and running on your system. Follow the steps below based on your operating system:

- **Windows/Mac/Linux**: Download MongoDB from the [official MongoDB website](https://www.mongodb.com/try/download/community) and follow the installation guide.

- Ensure the MongoDB service is running:
   - Run `mongod` in your terminal to start the MongoDB server.

---

#### 2. **Install `pymongo`**
`pymongo` is the official Python driver for MongoDB.

```bash
pip install pymongo
```

---

#### 3. **Connect to MongoDB**
Create a Python script to connect to MongoDB:

```python
from pymongo import MongoClient

# Establish a connection to the local MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create or access a database
db = client["mydatabase"]

# Create or access a collection
collection = db["mycollection"]
```

---

#### 4. **Verify Connection**
- Run the Python script.
- Verify that the document is successfully inserted into the MongoDB collection.

To interact with MongoDB further, you can use MongoDB Compass (GUI) or the command-line shell `mongo`.

---
