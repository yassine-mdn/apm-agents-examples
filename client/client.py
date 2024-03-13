import random
import time
import requests
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

base_urls = ["http://localhost:3030", "http://127.0.0.1:5000"]

def check_at_least_one_server_is_running(urls: list[str]) -> bool:
    for url in urls:
        try:
            response = requests.get(url)
            logging.info(f'{url} is running')
        except requests.exceptions.ConnectionError:
            base_urls.remove(url)
            logging.warning(f'{url} is offline')
            pass
    
    return len(base_urls) > 0 

def default(url : str):
    logging.info(f'request sent to {url}/')
    requests.get(f'{url}/')

def path(url : str):
    random_number = random.randint(1, 500)
    logging.info(f'request sent to {url}/path/{random_number}')
    requests.get(f'{url}/path/{random_number}')

def demo(url : str):
    logging.info(f'request sent to {url}/demo')
    requests.get(f'{url}/demo')

def error(url : str):
    logging.info(f'request sent to {url}/error')
    requests.get(f'{url}/error')

functions = [default, path, demo, error]
probabilities = [0.5, 0.2, 0.2, 0.1]  

while True:
    if check_at_least_one_server_is_running(base_urls):
        url = random.choice(base_urls)
        random_func = random.choices(functions, weights=probabilities)[0]
        random_func(url)
        time.sleep(random.randint(1, 5))
    else:
        logging.error("No server is running")
        exit()