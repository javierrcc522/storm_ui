from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nameTemplate', methods=['POST'])
def name_template():
    name = request.form['name']
    if name:
        newName = str(name).title()
        return jsonify({'name' : newName})
    return jsonify({'error' : 'Missing Data!'})

if __name__ == '__main__':
   app.run(debug = True)
