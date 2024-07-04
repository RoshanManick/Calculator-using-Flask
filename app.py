from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Simple Calculator</h1>
    <form action="/calculate" method="post">
        <input type="text" name="num1" placeholder="Enter first number"/>
        <input type="text" name="num2" placeholder="Enter second number"/>
        <select name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>
        <input type="submit" value="Calculate"/>
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 'Invalid operation'
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
