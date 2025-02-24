from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

SECRET_PASSWORD = "Sn6pcEkv5CiBXm"  # Change this to any password you want
DELAY_PER_CHAR = 0.05  # Small delay to simulate timing vulnerability

def insecure_password_check(guess):
    """Compares the guessed password character by character with a delay."""
    for i, c in enumerate(guess):
        if i >= len(SECRET_PASSWORD) or c != SECRET_PASSWORD[i]:
            return False
        time.sleep(DELAY_PER_CHAR)  # Vulnerability: time-based check
    return len(guess) == len(SECRET_PASSWORD)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        guess = request.form.get("password", "")
        if insecure_password_check(guess):
            return jsonify({"success": True, "message": "Access Granted"})
        return jsonify({"success": False, "message": "Access Denied"})
    
    return render_template('login.html')



if __name__ == "__main__":
    app.run(host="127.0.0.2", port=5000, debug=True)

