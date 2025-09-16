# Online Store Database Project

##  Project Context

This project was created as part of a university course on databases. The goal was to demonstrate an understanding of database theory, modeling, implementation, and security. It consists of three main parts:

1. **Essay** on a database-related topic  
2. **Entity-Relationship Diagram (ERD)** for an online store  
3. **PostgreSQL database implementation** with example queries

---

##  Part 1: Essay — *SQL Injection: A Persistent Threat to Database Security*

This essay explores the topic of **SQL Injection (SQLi)** — a critical and widespread security vulnerability in web applications. It explains how SQLi attacks work, their different types, real-world incidents, and how to prevent them through best practices such as prepared statements, input validation, and security testing.

 You can read the full essay in the `essay.odt` file.

---

##  Part 2: Database Model Diagram

The Entity-Relationship Diagram (ERD) was created using the **Graphviz** Python library and models an online store with the following entities:

- Customers
- Products
- Orders
- Order_Items (join table for many-to-many)
- Payments

 Relationships include:
- A customer can place multiple orders (1:N)
- An order can contain multiple products (N:M via Order_Items)
- Each order can have one or more payments

The final diagram is available in the file: `online_store_erd.png`.

---

##  Part 3: PostgreSQL Implementation

The database schema was implemented in **PostgreSQL**, following the ERD design. The project includes:

- **SQL scripts** to create tables
- **Sample data** for customers, products, orders, and payments
- **SQL queries** to demonstrate key functionality such as:
  - Viewing all customer orders
  - Checking available product stock
  - Retrieving payments per order

All SQL scripts are available in the `sql/` folder.

---

##  Technologies Used

- PostgreSQL
- SQL
- Python (Graphviz for ERD generation)
- Git & GitHub

---

##  Project Structure

