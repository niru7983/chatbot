# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = f"You said: {user_input}"  # Simple echo response
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
