import logging
import random
import azure.functions as func

"""
    Main function handler

    :param HttpRequest req:
        Incoming request body
    
    :return HttpResponse:
        Response to client
"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'Received request for nth fibonacci number')
    
    try:
        # Randomize the chance of getting the sequence number or error
        error_check =random.randint(1,10)
        if error_check % 2 == 0:
            n = req.params.get('fib')
            response = fibonacci(int(n))
            return func.HttpResponse(f'Fibonacci number at sequence {n} is {response}', status_code=200)
        else:
            return func.HttpResponse(f'Random server error', status_code=500)
    except Exception as e:
        logging.error(f'An error occurred: ${e}')
        return func.HttpResponse(f'An error occurred: {e}', status_code=500)

"""
    Generate Fibonacci number at a given sequence 

    :param int sequence:
        What number in the sequence you want returned
    
    :return int:
        The Fibonacci sequence value
"""
def fibonacci(sequence: int, memo: dict = {}) -> int:
    if sequence in memo:
        return memo[sequence]
    if sequence == 0:
        return 0
    if sequence == 1 or sequence == 2:
        return 1
    else:
        memo[sequence] = fibonacci(sequence - 1, memo) + fibonacci(sequence - 2, memo)
        return memo[sequence]
