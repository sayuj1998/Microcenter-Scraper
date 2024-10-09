import requests, re

class Microcenter:
    def __init__(self):
        """URL to search"""
        self.base_url = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&storeid=181&Ntt="

    def search(self, query: str):
        """Search for product based on the package"""
        url = f"{self.base_url}{query}"
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            self.parse_html(html)
        else:
            print(f" Failed: {response.status_code}")

    def parse_html(self, html: str):
        """Parse and extract information from the HTML"""
        pattern = re.compile(r'data-name="([^"]*?)"\s+[^>]*?data-price="([^"]*?)"\s+[^>]*?data-position="([^"]*?)"\s+href="([^"]*?)".*?>',
            re.DOTALL)

        matches = re.findall(pattern, html)

        for match in matches:
            data_name, data_price, data_position, href = match
            full_link = f"https://www.microcenter.com{href}"
            print(f"Product: {data_name}")
            print(f"Price: ${data_price}")
            print(f"Stock: {data_position}")
            print(f"Link: {full_link}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == '__main__':
    microcenter = Microcenter()
    microcenter.search("1 tb ssd")
