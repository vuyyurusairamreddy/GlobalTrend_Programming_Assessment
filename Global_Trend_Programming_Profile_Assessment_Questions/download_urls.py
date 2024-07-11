import requests
from time import sleep

def download_content(urls, max_retries=3):
    contents = []
    for url in urls:
        for attempt in range(max_retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                contents.append(response.text)
                print(f"Downloaded content from {url}")
                break
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1} failed for {url}: {e}")
                sleep(1)  # wait before retrying
        else:
            contents.append(None)
            print(f"Failed to download content from {url} after {max_retries} attempts")
    return contents

# Usage Example
if __name__ == "__main__":
    urls = ["http://example.com", "http://example.org", "http://nonexistenturl.xyz"]
    contents = download_content(urls)
    for i, content in enumerate(contents):
        if content:
            print(f"Content from URL {urls[i]}: {content[:100]}...")  # Print first 100 characters
        else:
            print(f"No content for URL {urls[i]}")
