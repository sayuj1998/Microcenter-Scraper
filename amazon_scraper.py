import requests, re

class Amazon:
    def __init__(self):
        """URL to search"""
        self.base_url = "https://www.amazon.com/s?k="

    def search(self, package: str):
        """Search for product based on the package"""
        url = f"{self.base_url}{package}"
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            self.parse_html(html)
        else:
            print(f" Failed: {response.status_code}")

    def parse_html(self, html: str):
        """Parse and extract information from the HTML"""
        title_pattern =
        link_pattern =





if __name__ == '__main__':
    amazon = Amazon()
    amazon.search("graphics card")