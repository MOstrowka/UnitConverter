from django.shortcuts import render, redirect


# Widok strony głównej
def home(request):
    return redirect('length_converter')


def determine_precision(value):
    """
    Determine the number of decimal places based on the magnitude of the value.
    """
    if value < 0.000001:
        return 8
    elif value < 0.0001:
        return 6
    elif value < 0.01:
        return 4
    else:
        return 2


# Widok konwertera długości
def length_converter(request):
    result = None
    error_message = None
    units = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
    abbreviations = {
        "millimeter": "mm",
        "centimeter": "cm",
        "meter": "m",
        "kilometer": "km",
        "inch": "in",
        "foot": "ft",
        "yard": "yd",
        "mile": "mi"
    }

    from_unit = None
    to_unit = None

    if request.method == 'POST':
        try:
            length = request.POST.get('length')
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')

            if not length or not length.replace('.', '', 1).isdigit():
                raise ValueError("Invalid input! Please enter a numeric value.")

            length = float(length)

            if not from_unit or not to_unit:
                raise ValueError("Please select both units for conversion.")

            if from_unit == to_unit:
                raise ValueError("Selected units are the same. Please choose different units.")

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

            precision = determine_precision(result)
            result_text = f"{length} {abbreviations[from_unit]} = {result:.{precision}f} {abbreviations[to_unit]}"

        except ValueError as e:
            error_message = str(e)

        return render(request, 'length_converter.html', {
            'result': result_text if not error_message else None,
            'error_message': error_message,
            'units': units,
            'selected_from_unit': from_unit,
            'selected_to_unit': to_unit
        })

    return render(request, 'length_converter.html', {'units': units})


# Widok konwertera wagi
def weight_converter(request):
    result = None
    error_message = None
    units = ["milligram", "gram", "kilogram", "ounce", "pound"]
    abbreviations = {
        "milligram": "mg",
        "gram": "g",
        "kilogram": "kg",
        "ounce": "oz",
        "pound": "lb"
    }

    from_unit = None
    to_unit = None

    if request.method == 'POST':
        try:
            weight = request.POST.get('weight')
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')

            if not weight or not weight.replace('.', '', 1).isdigit():
                raise ValueError("Invalid input! Please enter a numeric value.")

            weight = float(weight)

            if not from_unit or not to_unit:
                raise ValueError("Please select both units for conversion.")

            if from_unit == to_unit:
                raise ValueError("Selected units are the same. Please choose different units.")

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

            # Determine precision
            precision = determine_precision(result)
            result_text = f"{weight} {abbreviations[from_unit]} = {result:.{precision}f} {abbreviations[to_unit]}"

        except ValueError as e:
            error_message = str(e)

        return render(request, 'weight_converter.html', {
            'result': result_text if not error_message else None,
            'error_message': error_message,
            'units': units,
            'selected_from_unit': from_unit,
            'selected_to_unit': to_unit
        })

    return render(request, 'weight_converter.html', {'units': units})


# Widok konwertera temperatury
def temperature_converter(request):
    result = None
    error_message = None
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    abbreviations = {
        "Celsius": "°C",
        "Fahrenheit": "°F",
        "Kelvin": "K"
    }

    if request.method == 'POST':
        try:
            # Sprawdzenie, czy wpisana wartość temperatury jest liczbą
            temperature_input = request.POST.get('temperature', '').strip()
            if not temperature_input or not temperature_input.replace('.', '', 1).isdigit():
                raise ValueError("Invalid input! Please enter a numeric value.")

            temperature = float(temperature_input)
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')

            # Sprawdzenie, czy wybrane jednostki są poprawne
            if not from_unit or not to_unit:
                raise ValueError("Please select both units for conversion.")
            if from_unit == to_unit:
                raise ValueError("Selected units are the same. Please choose different units.")

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

            result_text = f"{temperature} {abbreviations[from_unit]} = {result:.2f} {abbreviations[to_unit]}"

        except ValueError as e:
            error_message = str(e)
            return render(request, 'temperature_converter.html', {
                'result': None,
                'error_message': error_message,
                'units': units,
                'selected_from_unit': request.POST.get('from_unit', ''),
                'selected_to_unit': request.POST.get('to_unit', '')
            })

        return render(request, 'temperature_converter.html', {
            'result': result_text,
            'error_message': None,
            'units': units,
            'selected_from_unit': from_unit,
            'selected_to_unit': to_unit
        })

    return render(request, 'temperature_converter.html', {'units': units})
