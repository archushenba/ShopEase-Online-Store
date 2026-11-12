# 🛍️ ShopEase
### A Modern & Responsive E-Commerce Web Application

<p align="center">
  **Discover. Shop. Experience.**
</p>

---

## 📌 Project Overview

**ShopEase** is a modern, user-friendly e-commerce web application developed using Python and Django as part of the **CodeAlpha Full Stack Development Internship**.

The platform provides a simple and smooth online shopping experience where customers can explore products, search for items, filter products by category, manage their shopping cart, and place orders.

The application also includes a Django Admin Panel for managing products, inventory, and customer orders.

## 🎯 Project Objectives

- Build a functional full-stack e-commerce application.
- Understand Django's Model-View-Template (MVT) architecture.
- Implement product and order management.
- Develop shopping cart functionality.
- Store customer orders in an SQLite database.
- Create a responsive and attractive user interface.
- Gain practical experience in full-stack web development.

## ✨ Key Features

### 🏠 1. Modern Home Page
- Attractive and organized homepage.
- Premium ShopEase branding.
- Product cards with images and prices.
- Easy navigation between sections.

### 🔍 2. Product Search
- Search products by name.
- Search using product descriptions.
- Find products easily.

### 🗂️ 3. Category Filtering
- Filter products based on categories.
- Quickly discover relevant products.
- Reset filters to view all products.

### 📦 4. Product Details
- View individual product information.
- Display product images.
- Read product descriptions.
- Check product price and available stock.

### 🛒 5. Shopping Cart
- Add products to the cart.
- Increase or decrease product quantity.
- Remove products from the cart.
- View the total cart amount.

### 💳 6. Checkout System
- Enter customer information.
- Provide email and phone details.
- Enter delivery address.
- Submit an order.

### 📋 7. Order Management
- Save customer orders in the database.
- Store individual order items.
- Calculate order totals.
- Display order confirmation.

### 📊 8. Inventory Management
- Maintain product stock information.
- Track available product quantities.
- Update stock after successful orders.

### ⚙️ 9. Django Admin Panel
- Manage products.
- View customer orders.
- Review order information.
- Manage inventory through the admin dashboard.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Website structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| SQLite | Database management |
| Django Admin | Product and order administration |

## 🏗️ Project Architecture

The application follows Django's Model-View-Template (MVT) architecture.

- **Model:** Handles product, order, and order-item data.
- **View:** Processes user requests and application logic.
- **Template:** Displays the website interface using HTML and Django Template Language.
- **URL:** Connects website routes to their corresponding views.
- **Database:** Stores product and order information.

## 📁 Project Structure

```text
CodeAlpha-Ecommerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   ├── templates/
│   │   └── products/
│   │       ├── home.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       ├── product_detail.html
│   │       └── order_success.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

*Note: Project structure-ஐ உங்கள் actual files-க்கு ஏற்ப update செய்யவும்.*

## 🚀 Installation & Setup

### Step 1 – Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2 – Open Project Folder

```bash
cd CodeAlpha-Ecommerce
```

### Step 3 – Install Django

```bash
pip install django
```

### Step 4 – Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5 – Create Admin Account

```bash
python manage.py createsuperuser
```

### Step 6 – Start Development Server

```bash
python manage.py runserver
```

### Step 7 – Open Website

Website: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

---

## 🧪 Testing Checklist

- [ ] Homepage loads successfully.
- [ ] Products display correctly.
- [ ] Product search works.
- [ ] Category filtering works.
- [ ] Product details page opens.
- [ ] Add to Cart works.
- [ ] Quantity update works.
- [ ] Remove from Cart works.
- [ ] Checkout form works.
- [ ] Order is saved in the database.
- [ ] Stock is updated correctly.
- [ ] Order confirmation page displays.
- [ ] Django Admin displays products and orders.

## 🔐 Database Models

### Product
Stores product information such as:
- Product name
- Description
- Price
- Image
- Category
- Available stock

### Order
Stores customer order information such as:
- Customer name
- Email
- Phone number
- Delivery address
- Total amount
- Order status

### OrderItem
Stores individual products associated with an order:
- Product
- Product name
- Price
- Quantity
- Related order

## 🌟 Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications using Django.
- Understanding Django MVT architecture.
- Creating and managing database models.
- Implementing CRUD operations.
- Handling forms and user requests.
- Building shopping cart functionality.
- Managing customer orders.
- Integrating frontend and backend.
- Testing and debugging web applications.

## 🔮 Future Enhancements

- User registration and login.
- User profile and order history.
- Secure online payment integration.
- Product reviews and ratings.
- Wishlist functionality.
- Advanced product recommendations.
- Order tracking.
- Improved mobile responsiveness.

## 👩‍💻 Project Information

**Project Name:** ShopEase – E-Commerce Website

**Internship:** CodeAlpha Full Stack Development Internship

**Project Domain:** Full Stack Web Development

**Backend:** Python & Django

**Frontend:** HTML, CSS & JavaScript

**Database:** SQLite

**Project Status:** Developed – Final testing and review

---

<p align="center">
  **Thank you for visiting ShopEase!**

Making Online Shopping Simple and Convenient.

</p>