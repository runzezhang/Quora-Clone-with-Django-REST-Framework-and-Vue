import requests


def main():
    # response = requests.get("http://google.com/")
    response = requests.get("http://google.com/efefef")
    print("Status Code:", response.status_code)
    print("Status Code:", response.headers)


if __name__ == "__main__":
    main()
