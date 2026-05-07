import sys 
import os
import yaml
import flask
import importlib


app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person:
    def __init__(self, name):
        self.name = name

"""
Prints the nametag
"""
def print_nametag(format_string, person):
    print(format_string.format(person=person))

"""
Fetches the website
"""
def fetch_website(urllib_version, url):
    # Validate urllib_version input
    if urllib_version not in ("2", "3"):
        raise ValueError("Only urllib2 and urllib3 are supported.")

    # Import the correct urllib module safely
    module_name = f"urllib{urllib_version}"
    try:
        urllib = importlib.import_module(module_name)
    except ImportError:
        print(f"Could not import {module_name}")
        return

    try:
        if not is_allowed_url(url):
            raise ValueError("URL is not allowed")
        if urllib_version == "3":
            http = urllib.PoolManager()
            r = http.request('GET', url)
        elif urllib_version == "2":
            response = urllib.urlopen(url)
            r = response.read()
    except Exception as e:
        print(f'Exception: {e}')

"""
Loads yaml file
"""
def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

