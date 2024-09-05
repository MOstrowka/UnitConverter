
# Unit Converter

![image](https://github.com/user-attachments/assets/f4a2548a-b34f-4cfe-9f1b-2181f31ece65)

## Project Description

Unit Converter is a simple Django-based unit conversion project. The application allows users to convert values between various units of length, weight, and temperature.

### Features:
- Users can input a value to convert.
- Users can select the units to convert from and to.
- The converted result is displayed on the same page after submitting the form.
- Supported units:
  - **Length**: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
  - **Weight**: milligram, gram, kilogram, ounce, pound.
  - **Temperature**: Celsius, Fahrenheit, Kelvin.

This project was inspired by the following page:  
[Unit Converter Project Roadmap](https://roadmap.sh/projects/unit-converter)

## How it works?

The application does not use a database. The form is submitted to the server with the input data (value and selected units), and the server calculates the result and returns it to the same page for display.

- There are three pages for different types of conversions: length, weight, and temperature.  
- The user can enter data on each of these pages, and after form submission, the result is calculated and displayed dynamically.

## How to run the application?

### Step 1: Clone the repository
Clone the repository to your local environment:
```bash
git clone https://github.com/your-repository/unit-converter.git
```

### Step 2: Install Django
Make sure you have Django installed in your environment. You can install it with the following command:
```bash
pip install django==4.1
```

### Step 3: Run the application
Run the Django development server:
```bash
python manage.py runserver
```

### Step 4: Access the application
Open your browser and go to:
```
http://127.0.0.1:8000/
```

## Project Structure

- **converter**: Contains the logic for unit conversion.
- **static**: Static files (css).
- **templates**: HTML files for the conversion pages.

