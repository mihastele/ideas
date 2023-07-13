import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

def get_image_urls(search_query):
    # Set up initial search URL
    search_query = urllib.parse.quote(search_query)
    url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    
    # Send the search request and retrieve HTML response
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }


    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract image URLs from the HTML response
    image_urls = []
    for img in soup.find_all("img"):
        if img.has_attr("src"):
            print(f"{img['src']} {img['src']} {img['src']} {img['src']} {img['src']}")
            start_index = max(
            img["src"].find("http://"),
            img["src"].find("https://"),
            img["src"].find("www.")
            )
            print(f"start_index {start_index} {start_index} {start_index} {start_index}")
            # Remove everything before the first occurrence of http, https, or www in the URL
            if start_index != -1:
                img["src"] = img["src"][start_index:]
            image_urls.append(img["src"])
    
    return image_urls

# def download_images(image_urls, folder_path):
#     # Download and save images to the specified folder path
#     for i, image_url in enumerate(image_urls):
#         file_path = f"{folder_path}/image_{i+1}.jpg"
#         urllib.request.urlretrieve(image_url, file_path)
#         print(f"Downloaded image {i+1}/{len(image_urls)}")

def download_image(image_url, file_path):
    start_index = min(
        image_url.find("http://"),
        image_url.find("https://"),
        image_url.find("www.")
    )
    
    # Remove everything before the first occurrence of http, https, or www in the URL
    if start_index != -1:
        image_url = image_url[start_index:]

    # Prepend http:// if URL does not start with http:// or https://
    if not image_url.startswith("http://") and not image_url.startswith("https://"):
        image_url = "http://" + image_url
    
    urllib.request.urlretrieve(image_url, file_path)
    print(f"Downloaded image from {image_url} to {file_path}")


def download_images(image_urls, folder_path):
    # Download and save images to the specified folder path
    for i, image_url in enumerate(image_urls):
        file_path = f"{folder_path}/image_{i+1}.jpg"

        print(f"Downloading image {i+1}/{len(image_urls)}")
        print(f"Image URL: {image_url}")
        download_image(image_url, file_path)

# Example usage
search_query = "movie title cards"
image_urls = get_image_urls(search_query)
download_images(image_urls, "movie_title_cards")
