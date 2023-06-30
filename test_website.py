import requests

def check_url_accessibility(url):
    try:
        response = requests.head(url)
        response.raise_for_status()
        print(f"{url} is accessible (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"{url} is not accessible ({str(e)})")

def main():
    urls = [
        "https://www.pinknoiseplaylisting.com",
        "https://pinknoiseplaylisting.com/how-it-works",
        "https://pinknoiseplaylisting.com/for-curators",
        "https://pinknoiseplaylisting.com/contact",
        "https://pinknoiseplaylisting.com/album-art-generator",
        "inknoiseplaylisting.c/album"
        # Add more URLs to test
    ]

    for url in urls:
        check_url_accessibility(url)

if __name__ == "__main__":
    main()
