import os
from flask import Flask, request, redirect, url_for

def ip_analyzer(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        print(f"L'adresse IP {ip_address} correspond à l'hôte {host_name[0]}")
    except socket.herror:
        print(f"Impossible de trouver l'hôte correspondant à l'adresse IP {ip_address}")
        
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
