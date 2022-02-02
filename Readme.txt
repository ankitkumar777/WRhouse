Warehouse Management System
username: admin
password: root@123

username: customer1
password: warehouse@123

username: supplier1
password: warehouse@123

About code:
Language used: Python (3.9.1), JavaScript and HTML5, CSS
Framework used: Django (3.2.7)
Database used: SQLite3 (Type: RDBMS)
Frontend Tech. used: HTML, CSS, JavaScript
Backend Tech. used: Django and Python
Database used: SQLite (Type: Relational DBMS)

How to run the code:
Download and Install Python from https://www.python.org/downloads/
(During installation make sure to check the checkbox add python to path to include PATH)
Download and Install VS Code IDE from https://code.visualstudio.com/download

Open project folder (WMS) using VS Code IDE.

In Terminal Open New Terminal>open Command Prompt in New terminal.
Run command: pip install -r requiremnts.txt                 (one time)
Run command: python manage.py makemigrations    (one time)
Run command: python manage.py migrate                   (one time)
Run command: python manage.py createsuperuser    (one time)
Run command: python manage.py runserver               (every time)

Commands:
python manage.py runserver	Command to run the code in localhost://127.0.0.1/8000
127.0.0.1 is the local URL and 8000 is the port number.
python manage.py makemigrations	Makes SQL script for the database (prepare database for creating tables)
python manage.py migrate	Migrate SQL scripts to database (create all tables)
pip install -r requirements.txt	Install all the required libraries and modules for the project. Including any dependencies.
python manage.py createsuperuser	To create admin

Important Files (DO NOT MODIFY)
Settings.py: contains all the settings of the project
Manage.py: used to run the project code
urls.py: contains all the URLs of the project
views.py: contains the business logic of the project
models.py: contains the tables of the project
db.sqlite3: database file where all the data is stored
requirements.txt: contains all the required libraries and dependencies

How Projects Works:
 Three users are there in the warehouse application: Admin, Suppliers and Customers
 Users can register themselves as 
1. Customer or 
2. Supplier

 Suppliers can 
1. view its profile details 
2. add new products to warehouse (admin update status as "Approved")
4. view total number of products in warehouse
3. view all the products in the warehouse.

The products created by the suppliers are unapproved and needs admin approval.
The unapproved products need to be approved by admin.
Once approved by admin, these products can be viewed and ordered by the customers.
Admin can perform all the CRUD functionalities on customers suppliers, products, orders and deliveries.
Admin needs to
1. Update the status of products(Approved)
2. Update the status of orders
3. Create Deliveries of orders with status “Approved"
4. Create Stock Requests for supplier

Customers can 
1. view profile information
2. create new orders based upon existing products in warehouse
3. view existing orders
4. Update orders
5. Delete orders
6. View Delivery Orders (to be added/done by admin)

How everything is working:
1.  Admin create Stock requests for any suppliers.
2.	User register and login as Supplier. Supplier creates new product that is yet to be approved by admin.  Supplier can search and view any existing product in products.
3.	Admin approves the warehouse products. (Admin approval=” Approved”).
4.	User register and login as Customer. Customer can place a new order based on the products in the warehouse. Customer can update and delete their orders. Customer can search and view any products.
5.	Based on the status of order of the customer, admin needs to create delivery of the order.
6.	The delivery of each customer can be viewed by the customer once admin creates delivery of order.


Changes in the code:
Deliveries are working now. (Need to be added by admin based on order status).
Product Name choices has been removed.
Product Search feature added in site and admin panel both.
Stock Request quantity column added.
Stock Request separately added in Navbar of supplier.
Product available quantity added. (In product table).
Product Quantity is now reducing once Order is placed.
Product Quantity is restoring to its original quantity if order is deleted.
Admin Unapproved products are now cannot be ordered by customer.(Only approved products can be ordered.)
UI is website improved.
UI of admin is also improved.
