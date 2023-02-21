#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    id = sys.argv[0]
    response = requests.get("https://jsonplaceholder.typicode.com/todos/'$id'")
    res = response.json()
    print(res)
