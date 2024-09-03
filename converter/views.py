from django.shortcuts import render

# Widok dla strony głównej
def home(request):
    return render(request, 'home.html')

# Widok dla konwertera długości
def length_converter(request):
    result = None
    error_message = None
    units = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]

    if request.method == 'POST':
        try:
            length = float(request.POST.get('length', 0))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')

            # Przykład konwersji dla długości
            conversion_factors = {
                "millimeter": 1,
                "centimeter": 10,
                "meter": 1000,
                "kilometer": 1000000,
                "inch": 25.4,
                "foot": 304.8,
                "yard": 914.4,
                "mile": 1609344
            }

            if from_unit not in conversion_factors or to_unit not in conversion_factors:
                raise ValueError("Invalid unit selection")

            result = length * conversion_factors[from_unit] / conversion_factors[to_unit]
            result_text = f"{length} {from_unit} = {result:.2f} {to_unit}"

        except ValueError:
            error_message = "Invalid input! Please enter a valid number and select correct units."

        return render(request, 'length_converter.html', {
            'result': result_text if not error_message else None,
            'error_message': error_message,
            'units': units
        })

    return render(request, 'length_converter.html', {'units': units})

# Widok dla konwertera wagi
def weight_converter(request):
    result = None
    error_message = None
    units = ["milligram", "gram", "kilogram", "ounce", "pound"]

    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight', 0))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')

            # Przykład konwersji dla wagi
            conversion_factors = {
                "milligram": 1,
                "gram": 1000,
                "kilogram": 1000000,
                "ounce": 28349.5,
                "pound": 453592
            }

            if from_unit not in conversion_factors or to_unit not in conversion_factors:
                raise ValueError("Invalid unit selection")

            result = weight * conversion_factors[from_unit] / conversion_factors[to_unit]
            result_text = f"{weight} {from_unit} = {result:.2f} {to_unit}"

        except ValueError:
            error_message = "Invalid input! Please enter a valid number and select correct units."

        return render(request, 'weight_converter.html', {
            'result': result_text if not error_message else None,
            'error_message': error_message,
            'units': units
        })

    return render(request, 'weight_converter.html', {'units': units})

# Widok dla konwertera temperatury
def temperature_converter(request):
    result = None
    error_message = None
    units = ["Celsius", "Fahrenheit", "Kelvin"]

    if request.method == 'POST':
        try:
            temperature = float(request.POST.get('temperature', 0))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')

            # Przykład konwersji dla temperatury
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (temperature * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (temperature - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = temperature + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = temperature - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (temperature - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (temperature - 273.15) * 9/5 + 32
            else:
                raise ValueError("Invalid unit selection")

            result_text = f"{temperature} {from_unit} = {result:.2f} {to_unit}"

        except ValueError:
            error_message = "Invalid input! Please enter a valid number and select correct units."

        return render(request, 'temperature_converter.html', {
            'result': result_text if not error_message else None,
            'error_message': error_message,
            'units': units
        })

    return render(request, 'temperature_converter.html', {'units': units})
