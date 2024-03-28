import requests
import json
import argparse
from datetime import datetime
from pathlib import Path
import time
import os

config = {"apiKey": "AIzaSyCHJj1IdzhOYxF4SRRrN1NB2_puGsFt1hw"} # Fine to be public.
login_user_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={config['apiKey']}"

def login(email: str, password: str) -> dict:
    """Login the user."""
    data = { "email": email, "password": password, "returnSecureToken": True}
    response = requests.post(login_user_url, json=data)
    if response.status_code != 200:
        raise ValueError("Login failed. Please check your password and make sure your account exists.")
    return response.json()

def submit_homework(data: str, token: str, uid: str) -> dict:
    """Submit the homework."""
    database_url = f'https://cs326-416215-default-rtdb.firebaseio.com/users/{uid}.json?auth={token}'
    response = requests.post(database_url, data=json.dumps(data))
    return response.json()

def check_score(token: str, uid: str, document: str) -> dict:
    """Check the score of the homework."""
    database_url = f'https://cs326-416215-default-rtdb.firebaseio.com/users/{uid}/{document}.json?auth={token}'
    response = requests.get(database_url)
    return response.json()

def get_username(args: argparse.Namespace) -> str:
    """Get the username."""
    if args.username:
        return args.username
    elif os.environ.get("CS326_USERNAME"):
        return os.environ.get("CS326_USERNAME")
    else:
        raise "Please provide a username with the --username flag or set the CS326_USERNAME environment variable."
    
def get_password(args: argparse.Namespace) -> str:
    """Get the password."""
    if args.password:
        return args.password
    elif os.environ.get("CS326_PASSWORD"):
        return os.environ.get("CS326_PASSWORD")
    else:
        raise "Please provide a password with the --password flag or set the CS326_PASSWORD environment variable."
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Submit homework to autograder')
    parser.add_argument('--homework', type=str, required=True, help='Local path to the python file you want to submit.')
    parser.add_argument("--username", type=str, help="Your Northwesern email address (netid@u.northwestern.edu).")
    parser.add_argument("--password", type=str, help="Your unique password, please don't use your NetID password.")
    args = parser.parse_args()

    # Get the username and password.
    username = get_username(args)
    password = get_password(args)
    login_info = login(username, password)

    # Submit the homework.
    submission = {
        "datetime": datetime.now().isoformat(),
        "username": username,
        "homework": Path(args.homework).name,
        "python_code": open(args.homework, 'r').read()
    }
    response = submit_homework(submission, login_info['idToken'], login_info["localId"])
    document_name = response["name"]

    # Check the score, wait up to 30 seconds while it is being graded.
    attempts = 0
    while "response" not in response.keys() and attempts < 30:
        response = check_score(login_info['idToken'], login_info["localId"], document_name)
        attempts += 1
        time.sleep(1)

    if "response" not in response.keys():
        print("Submission failed. Please try again.")
        exit()

    print(response["response"])
        
