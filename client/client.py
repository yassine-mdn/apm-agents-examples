import random
import time
import requests
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def default():
    logging.info('request sent to http://localhost:3030/')
    requests.get("http://localhost:3030/")

def path():
    random_number = random.randint(1, 500)
    logging.info(f'request sent to http://localhost:3030/path/{random_number}')
    requests.get(f"http://localhost:3030/path/{random_number}")

def demo():
    logging.info('request sent to http://localhost:3030/demo')
    requests.get("http://localhost:3030/demo")

def error():
    logging.info('request sent to http://localhost:3030/error')
    requests.get("http://localhost:3030/error")

functions = [default, path, demo, error]
probabilities = [0.5, 0.2, 0.2, 0.1]  

while True:
    random_func = random.choices(functions, weights=probabilities)[0]
    random_func()
    time.sleep(random.randint(1, 5))
