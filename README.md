# Library Management System

This project is a Library Management System that allows users to manage books, users, and lending records. The project uses a **MySQL database** managed with **phpMyAdmin** and **XAMPP**, and the main code is written in **Python**.



## Prerequisites
- **XAMPP** (for Apache and MySQL)
- **Python 3.x**
- **MySQL Connector for Python**



## Setup Instructions

### Step 1: Install XAMPP
1. Download and install XAMPP from [Apache Friends](https://www.apachefriends.org/).
2. Start the **Apache** and **MySQL** services from the XAMPP Control Panel.

### Step 2: Setup the Database
1. Open **phpMyAdmin** by navigating to [http://localhost/phpmyadmin](http://localhost/phpmyadmin) in your web browser.
2. Create a new database named `library`.
3. Import the SQL dump file (`library.sql`) into the `library` database:
   - Click on the `library` database.
   - Go to the **Import** tab.
   - Choose the `library.sql` file and click **Go**.

### Step 3: Install MySQL Connector for Python
Install the MySQL Connector for Python using pip:
```bash
pip install mysql-connector-python
```
### Step 4: Configure the Python Script
1. Open the `lbm.py` file.
2. Ensure the database connection details are correct:
```python
host = "localhost"
user = "root"
password = ""
```
### Step 5: Run the Python Script
Run the `lbm.py` script:
```
python lbm.py
```
## Usage
### Admin Menu
1. Register New Student
2. Delete Existing Student
3. Register New Manager
4. Delete Existing Manager
### Logout
1. Manager Menu
2. Add New Book
3. Remove Existing Book
4. Logout
### Student Menu
1. Search Books
2. Lend Book
3. Return Book
4. Logout
## License
This project is licensed under the MIT License.
## Acknowledgements
- [phpMyAdmin](https://www.phpmyadmin.net/)
- [XAMPP](https://www.apachefriends.org/index.html)
- [MySQL Connector for Python](https://dev.mysql.com/doc/connector-python/en/)
