from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""

    if request.method == 'POST':
        number = int(request.form['number'])

        for i in range(1, 11):
            output += f"{number} x {i} = {number*i}<br>"

    return f'''
    <html>
        <head>
            <title>Table Calculator</title>
        </head>
        <body>
            <h2>Enter Your Number</h2>

            <form method="POST">
                <input type="number" name="number" required>
                <button type="submit">Calculate</button>
            </form>

            <h3>{output}</h3>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)