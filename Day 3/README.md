# Day 3 - Python Classes

## Topics

- **Class**
    - **Create an Object**
    - **Data Encapsulation**
    - **Inheritance**
    - **Polymorphism**
- **Desktop Application**
- **Virtual Environment**
---

### Class

A **class** in Python is a blueprint for creating objects. It defines methods (functions) and attributes (variables) that will be associated with the objects.

#### Define a Class

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        # Initialization code
        self.attribute1 = parameter1
        self.attribute2 = parameter2
```

- **`__init__()`**: The initializer method is called when an object of the class is created. It sets up initial values for the object's attributes.
- **`self`**: Refers to the instance of the class (the object being created).

#### Create an Object

Once a class is defined, you can create an object (an instance of that class) like this:

```python
object_name = ClassName(value1, value2)
```

For example, if we have a class `Car`:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
```

Here, `my_car` is an object of the `Car` class.

---

### Data Encapsulation

**Data Encapsulation** refers to the bundling of data (attributes) and methods (functions) that operate on the data within a class. It also includes restricting direct access to some of the class's attributes and methods.

To access or modify attributes safely, we can use **getter** and **setter** methods.

#### Example:

```python
class Product:
    def __init__(self, name, price):
        self.__name = name   # private attribute
        self.__price = price # private attribute

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive.")

    # Getter method
    def get_price(self):
        return self.__price
```

Here, `__name` and `__price` are private attributes, meaning they can’t be accessed directly from outside the class. Instead, the `get_name()` and `set_price()` methods are used to interact with them.

---

### Inheritance

**Inheritance** allows a class to inherit attributes and methods from another class, promoting code reuse and creating a hierarchy of classes.

#### Example:

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)  # Call the parent class constructor
        self.breed = breed

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

# Create a Dog object
my_dog = Dog("Buddy", "Woof", "Golden Retriever")
my_dog.speak()  # Inherited method from Animal
my_dog.fetch()  # Method specific to Dog
```

In this example:
- The `Dog` class inherits from the `Animal` class.
- `super().__init__(name, sound)` is used to call the parent class's constructor, ensuring the attributes are initialized.
- The `Dog` class adds its own attribute `breed` and method `fetch()`.

---

### Polymorphism

**Polymorphism** allows objects of different classes to be treated as instances of the same class through a common interface. It enables the same method to behave differently based on the object calling it. Polymorphism can be achieved through **method overriding** and **method overloading**.

#### Example: Method Overriding

In method overriding, a subclass provides its own implementation of a method that is already defined in its superclass.

```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects
dog = Dog()
cat = Cat()

# Polymorphism in action
animals = [dog, cat]

for animal in animals:
    animal.make_sound()  # Calls the appropriate method for each object
```

Output:
```
Woof!
Meow!
```

Here:
- The `Dog` and `Cat` classes override the `make_sound()` method of the `Animal` class.
- When the method `make_sound()` is called on `dog` and `cat` objects, each class’s specific implementation is executed, demonstrating polymorphism.

#### Example: Polymorphism with Different Objects

```python
class Shape:
    def area(self):
        pass  # This will be overridden in subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Polymorphism in action
shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
```

Output:
```
Area: 78.5
Area: 16
```

In this example:
- The `Shape` class is a base class with a method `area()`, which is overridden by the `Circle` and `Square` subclasses.
- The same method `area()` is used on different objects, but the result is different based on the specific subclass, demonstrating polymorphism.

#### Duck Typing

**Duck Typing** is a concept in Python where an object's suitability is determined by the presence of certain methods and properties, rather than its actual type. If an object has the required methods and behaviors, it can be treated as if it were of a certain type, regardless of its actual class.

In other words, "If it looks like a duck and quacks like a duck, then it's a duck."

#### Example of Duck Typing:

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Bird:
    def speak(self):
        print("Chirp!")

def animal_sound(animal):
    animal.speak()  # No need to check the type, just call the method

# All these objects can be passed to the function, demonstrating Duck Typing
dog = Dog()
cat = Cat()
bird = Bird()

animals = [dog, cat, bird]

for animal in animals:
    animal_sound(animal)  # Calls the appropriate 'speak' method for each object
```

Output:
```
Woof!
Meow!
Chirp!
```

Here:
- We have three different classes (`Dog`, `Cat`, and `Bird`), but as long as they have a `speak()` method, they can all be passed to the `animal_sound()` function.
- The function doesn't care about the specific type of the object, just whether it has the `speak()` method (this is Duck Typing in action).

---

### Virtual Environment

```cmd
python - venv environment_name
environment_name\scripts\activate.bat
```

```ubuntu terminal
source venv/bin/activate
```

---

### Install

- Package: pip install pyinstaller