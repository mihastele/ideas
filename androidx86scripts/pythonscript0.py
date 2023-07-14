# import subprocess
# import os
# from bs4 import BeautifulSoup
# import requests


# # Download latset android-x86 ISO
# url = 'https://www.fosshub.com/Android-x86.html'

# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.content
#     #print(html_content)
# else:
#     print(f"Failed to retrieve HTML file from {url}")

# soup = BeautifulSoup(html_content, 'html.parser')
# section = soup.select_one('section[data-section-name="softwareDownload"]')
# download_link = section.select_one('a[data-download="true"]')['href']

# print(download_link)

# # subprocess.run(['wget', download_link])



import requests
from bs4 import BeautifulSoup

# Download latest android-x86 ISO
# url = 'https://www.fosshub.com/Android-x86.html'
url = 'https://www.fosshub.com/Android-x86.html?dwl=android-x86_64-9.0-r2.iso' # TRY NOT TO HARDCODE

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print(f"Failed to retrieve HTML file from {url}")

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.select_one('section[data-section-name="softwareDownload"]')
download_link = section.select_one('a[data-download="true"]')['href']


def download_file(url):
    local_filename = url.split('/')[-1] # get the file name from the url
    # use stream=True to download the file in chunks
    with requests.get(url, stream=True) as r:
        r.raise_for_status() # check for errors
        with open(local_filename, 'wb') as f: # open a local file for writing
            for chunk in r.iter_content(chunk_size=8192): # iterate over the chunks
                f.write(chunk) # write the chunk to the file
    return local_filename # return the file name


download_file(download_link)

# print(download_link)

# # Download the ISO file
# response = requests.get(download_link)

# if response.status_code == 200:
#     with open('android-x86.iso', 'wb') as f:
#         f.write(response.content)
# else:
#     print(f"Failed to download ISO file from {download_link}")





exit()


# # Download the Android ISO
# subprocess.run(['wget', 'https://www.fosshub.com/Android-x86.html?dwl=android-x86_64-9.0-r2.iso'])

# Mount the ISO
os.mkdir('iso_mount')
subprocess.run(['sudo', 'mount', '-o', 'loop', 'android-x86_64-9.0-r2.iso', 'iso_mount'])

# Copy the ISO contents to a directory
os.mkdir('android_iso')
subprocess.run(['cp', '-r', 'iso_mount/*', 'android_iso/'])

# Unmount the ISO
subprocess.run(['sudo', 'umount', 'iso_mount'])
os.rmdir('iso_mount')

# Modify the ISO contents
# ...

# Create a new ISO
subprocess.run(['mkisofs', '-o', 'preconfigured_android.iso', 'android_iso/'])