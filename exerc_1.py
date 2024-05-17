from queue import Queue
import random

# Exercise 1
def generate_request(queue,request_id):
    request = f"Request №{request_id}"
    queue.put(request)

def process_request(queue,request_id):
    if not queue.empty():
        queue.get()
        print(f"The request №{request_id} has been processed")
    else:
        print("Queue is empty")

def main():
    queue = Queue()
    request_id = 0

    try:
        while True:
            if random.choice([True, False]):
                request_id += 1
                generate_request(queue, request_id)

            if random.choice([True, False]):
                process_request(queue,request_id)

    except KeyboardInterrupt:
        print("\nSession is over")


if __name__ == "__main__":
    main()