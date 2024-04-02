import logging
from azure.functions import TimerRequest
from typing import List
import urllib.request
import random
from concurrent.futures import ThreadPoolExecutor

endpoint = f'https://fibonacci-testing.azurewebsites.net/api/HttpTrigger1?fib='
max_numbers = 5
max_worker_pool = 5

"""
    Main function handler

    :param TimerRequest mytimer:
        Incoming timer request body
    
    :return None:
"""
def main(mytimer: TimerRequest) -> None:
    logging.info('Triggering Fibonacci API endpoint')

    try:
        # Generate 5 random numbers between 1-30
        numbers = []
        for _ in range(max_numbers):
            numbers.append(random.randint(0, 30))

        response = send_api_requests(numbers)

        # Log the response
        logging.info(f'Response from API: {response}')

    except Exception as e:
        logging.error(f'Error occurred: {e}')

"""
    Send api requests 

    :param nums List[int]:
        List of Fibonacci sequence numbers

    :return List[str]:
        List of response strings
"""
def send_api_requests(nums: List[int]) -> List[str]:
    results: List[str] = []

    logging.info(nums)

    def send_request(number: int):
        try:
            response = urllib.request.urlopen(endpoint + str(number))
            results.append(response.read().decode('utf-8'))
        except Exception as e:
            logging.error(f'Error with request: {e}')

    try: 
        with ThreadPoolExecutor(max_workers=max_worker_pool) as executor:
            for n in nums:
                executor.submit(send_request, n)
    except Exception as e:
        logging.error(f'Error sending multiple requests: {e}')

    return results
