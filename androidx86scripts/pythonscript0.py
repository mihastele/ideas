import subprocess
import os
from bs4 import BeautifulSoup
import requests


# Download latset android-x86 ISO
url = 'https://www.fosshub.com/Android-x86.html'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
    #print(html_content)
else:
    print(f"Failed to retrieve HTML file from {url}")

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.select_one('section[data-section-name="softwareDownload"]')
download_link = section.select_one('a[data-download="true"]')['href']

print(download_link)

# subprocess.run(['wget', download_link])



#####################

from bs4 import BeautifulSoup
import requests
import json

url = "https://www.fosshub.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print(f"Failed to retrieve HTML file from {url}")

soup = BeautifulSoup(html_content, 'html.parser')
scripts = soup.find_all('script')

cands = [script.text for script in scripts if not script.has_attr('src')]
cands = [cand for cand in cands if 'var settings =' in cand or 'let settings =' in cand]
cand = cands[-1]
d = json.loads(cand.split('settings = ')[-1].split(';')[0])
map = {it['n']: it for it in d['pool']['f']}

def download_element(callee, file_name_post_processor, e):
    e.preventDefault()
    e.stopPropagation()

    tgt = e.currentTarget
    fn = file_name_post_processor(tgt['data-file'])
    it = map.get(fn)

    fetch_url = 'https://api.fosshub.com/download/'
    fetch_headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
    }
    fetch_body = {
        'projectId': d['pool']['p'],
        'releaseId': it['r'],
        'projectUri': d['pool']['u'],
        'fileName': fn,
        'source': d['pool']['c']
    }
    fetch_response = requests.post(fetch_url, headers=fetch_headers, json=fetch_body)
    descr = fetch_response.json()
    tgt['href'] = descr['data']['url']
    tgt.removeEventListener('click', callee, True)
    tgt.removeEventListener('contextmenu', callee, True)
    tgt['style'] = 'text-shadow: cyan 0px 0px 1px, red 0px 0px 3px;'

def download_file_element(e):
    return download_element(download_file_element, lambda s: s, e)

def download_sig_element(e):
    return download_element(download_sig_element, lambda s: s + '.asc', e)

for el in soup.select('a[data-download=true]'):
    el['onclick'] = download_file_element
    el['oncontextmenu'] = download_file_element

for el in soup.select('a.fSignature'):
    el['onclick'] = download_sig_element
    el['oncontextmenu'] = download_sig_element

print(soup.prettify())


##################




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