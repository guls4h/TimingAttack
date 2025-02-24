
# **Timing Attack Example**

This project demonstrates a **Timing Attack** where an attacker can guess the password of a system by analyzing the response times to different password attempts. The server in this project deliberately introduces a timing vulnerability, where the time to process the password is influenced by the number of correct characters at the beginning of the guess.

### **Project Components:**
1. **Flask Application** (`app.py`): A simple Flask server that simulates a vulnerable login system. It compares passwords character by character, introducing delays as each correct character is processed.
2. **Timing Attack Script** (`attack.py`): A Python script that performs the timing attack. The attacker sends multiple password guesses and measures the response time to infer the correct password.

---

## **Flask Application Setup**

### 1. **Install Dependencies**

First, install the necessary Python dependencies:

```bash
pip install flask
```

### 2. **Running the Flask Application**

Run the Flask application (`app.py`) on your local machine:

```bash
python app.py
```

This will start the Flask server on `http://127.0.0.2:5000`. The `/login` route accepts `POST` requests with a `password` field and performs the insecure password check. If the password is correct, the server responds with a success message; otherwise, it returns an error.

The server introduces a small delay for each correct character in the password (`DELAY_PER_CHAR = 0.05` seconds). This is the vulnerability that will be exploited in the timing attack.

### **Flask Server Code Overview**:

- **Secret Password**: The correct password is hardcoded as `Sn6pcEkv5CiBXm`.
- **Insecure Password Check**: The `insecure_password_check` function compares the password character by character, introducing a delay for each correct character.
  
---

## **Timing Attack Script Setup**

### 1. **Install Dependencies**

The timing attack script uses the `requests` library to interact with the Flask server. Install it if you don't have it already:

```bash
pip install requests
```

### 2. **Running the Timing Attack**

Once the Flask server is running, execute the `attack.py` script:

```bash
python attack.py
```

The script will start the timing attack against the server. It tries to guess the password character by character, based on the response time for each guess. As it sends password guesses to the server, it measures the time taken to process each guess and uses the timing differences to infer the correct password.

The attack will print out the current guesses as it builds the correct password.

### **Timing Attack Script Code Overview**:

- **CHARSET**: The charset used for guessing the password includes uppercase and lowercase letters, and digits.
- **DELAY_THRESHOLD**: The time difference threshold used to determine when a character is likely correct. Adjust this value based on the server's response time.
- **`measure_response_time`**: This function sends a password guess and measures the time taken for the server to respond.
- **`timing_attack`**: The main function that iterates over each character in the password, adding one character at a time based on the best response time observed.

---

## **How Timing Attack Works**

1. The server introduces a small delay for each correct character of the password. The longer the response time, the more likely the guess is correct for that character.
2. The timing attack script sends a series of guesses and measures the response time for each guess.
3. By comparing the response times for different guesses, the script can identify the characters that match the password, one character at a time.
4. As the script continues to guess and refine the password, it prints out the current guess, gradually revealing the full password.

---

## **Important Notes**
- **Educational Purposes Only**: This project is designed for educational purposes to demonstrate a timing attack vulnerability. Do not use this technique for malicious purposes.
- **Local Environment**: Ensure that both the Flask app and the attack script are running on your local machine (`http://127.0.0.2:5000`), and the attack script is pointed to the correct URL.
- **Timing Sensitivity**: The success of the timing attack relies on the server introducing a detectable delay based on the correctness of the guessed characters. The attack may not work as effectively on production servers with optimized response times or security measures (such as rate limiting or random delays).

---



