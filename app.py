from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def homework():
    return render_template('index.html')
    return render_template('female.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)