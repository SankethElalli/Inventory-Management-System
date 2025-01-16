# Inventory Management System

This is a web-based Inventory Management System built with Django and MongoDB using the `djongo` package. The system allows users to manage products, suppliers, sale orders, and stock levels.

## Features

- Dashboard with an overview of the inventory
- Manage products, suppliers, and sale orders
- Check stock levels
- Responsive design using Flowbite and Tailwind CSS

## Requirements

- Python 3.12
- Django 4.1.13
- MongoDB
- djongo

## Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SankethElalli/Inventory-Management-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Inventory-Management-System
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Database Configuration
1. Ensure you have MongoDB installed and running on your local machine.
2. The project is configured to connect to MongoDB at `mongodb://localhost:27017`.

## Running the Project
1. Run the migrations to set up the database:
   ```bash
   python3 run.py makemigrations
   python3 run.py migrate
   ```
2. Start the development server:
   ```bash
   python3 run.py runserver 8001
   ```
3. Open your browser and navigate to `http://127.0.0.1:8001/` to access the application.
