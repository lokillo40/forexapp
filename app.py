from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates, CurrencyCodes
from converter import convert_currency

app = Flask(__name__)
cr = CurrencyRates()
cc = CurrencyCodes()

@app.route('/', methods=['GET', 'POST'])
def index():
    """ The index route of the application which displays a form to the user
    and handles the conversion when the form is submitted."""

    error = None
    result = None

    # Fields for the form
    fields = [
        {"id": "from_currency", "label": "From Currency", "placeholder": "e.g., USD"},
        {"id": "to_currency", "label": "To Currency", "placeholder": "e.g., EUR"},
        {"id": "amount", "label": "Amount", "placeholder": "Enter amount to convert"}
    ]

    # Handle the form submission
    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = request.form.get('amount')

        if not cc.get_symbol(from_currency) or not cc.get_symbol(to_currency):
            error = 'Invalid currency code. Please enter a valid three letter currency code (eg, USD, EUR, JPY).'
        elif not amount.replace('.', '', 1).isdigit():
            error = 'Invalid amount. Please enter a valid number.'
        else:
            result = convert_currency(from_currency, to_currency, amount)

    # Render the template with the form and the result
    return render_template('base.html', error=error, result=result, fields=fields)

if __name__ == '__main__':
    """Run the application."""

    app.run(debug=True)
