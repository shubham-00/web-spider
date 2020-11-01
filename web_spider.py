import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector


website_url = "https://www.emanueleferonato.com/"

urls_left = [website_url]
urls_done = []


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}


while not urls_left == []:
    url = urls_left[0]
    if url in urls_done:
        urls_left = urls_left[1:]
        continue

    if not url[:17] == website_url[:17]:
        urls_left = urls_left[1:]
        continue

    try:

        print("Urls completed", len(urls_done))
        print("Urls left", len(urls_left))
        print("Current url:", url)

        page = requests.get(url, headers=headers)
        # print(page.content)
        parser = "html.parser"
        http_encoding = (
            page.encoding
            if "charset" in page.headers.get("content-type", "").lower()
            else None
        )
        html_encoding = EncodingDetector.find_declared_encoding(
            page.content, is_html=True
        )
        encoding = html_encoding or http_encoding

        # soup = BeautifulSoup(page.raw, "html.parser")
        soup = BeautifulSoup(page.content, parser, from_encoding=encoding)

        links = soup.find_all("a", href=True)
        # print(links)
        for link in links:
            if not link in urls_done and not link in urls_left:
                urls_left.append(link["href"])
            # print(link["href"])

        urls_done.append(url)
        with open("urls.txt", "a") as f:
            f.write(url + "\n")
        # break
    except:
        urls_left = urls_left[1:]
        print(f"Droped {url}")
        continue