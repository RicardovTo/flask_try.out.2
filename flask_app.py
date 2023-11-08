from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<p>GOOD morning world</p>"

# antwoord op vraag 4
# switched to a new branch 'main'
# ik denk dat je nu gewoon een andere tak aan het gebruiken bent

if __name__ == '__main__':
    app.run(port=5000,debug=True)