import requests
from time import perf_counter

def response_time(url):
    start_time=perf_counter()
    response =requests.get(url)
    end_time=perf_counter()
    print(start_time,end_time)
    print(f'process time :{end_time-start_time}')

response_time('https://www.google.com/')