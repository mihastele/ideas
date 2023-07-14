import requests

def download_iso(url):
    response = requests.get(url, stream=True)
    with open('android-x86_64-9.0-r2.iso', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

if __name__ == '__main__':
    url = 'https://fosshub.com/android-x86_64-9.0-r2.iso/'
    download_iso(url)
