from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import threading
from time import sleep

website_url = "https://example.com/"


file_name = website_url.split("//")[1].split("/")[0].split(".")[0] + ".txt"


with open(file_name, "w") as f:
    pass


urls_left = [website_url]
urls_done = []


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}


def get_urls_left():
    return urls_left


def get_urls_done():
    return urls_done


def add_urls_left(url):
    urls_left.append(url)


def add_urls_done(url):
    urls_done.append(url)


def remove_urls_left():
    urls_left.pop(0)


def remove_urls_done():
    urls_done.pop(0)


def scrape_now(urls_left=get_urls_left(), urls_done=get_urls_done()):
    while not urls_left == []:
        urls_left = get_urls_left()
        urls_done = get_urls_done()

        url = urls_left[0]
        # url = url.split("?")[0]

        if url in urls_done:
            remove_urls_left()
            continue

        add_urls_done(url)

        remove_urls_left()

        if (
            not url[8:13] in website_url
            or "/ufaqs/" in url
            or "/single-faq/" in url
            or "/downloads/cas/" in url
        ):
            print(f"other {url}")
            # add_urls_done(url)
            with open(file_name, "a") as f:
                f.write(url + "\n")
            remove_urls_left()
            continue

        if (
            url.endswith(".pdf")
            or url.endswith(".jpg")
            or url.endswith(".jpeg")
            or url.endswith(".png")
            or url.endswith(".gif")
        ):
            print(f"other {url}")
            # add_urls_done(url)
            with open(file_name, "a") as f:
                f.write(url + "\n")
            remove_urls_left()
            continue

        try:
            print("Urls completed", len(urls_done))
            print("Urls left", len(urls_left))
            print("Current url:", url)

            page = requests.get(url, headers=headers)

            parser = "html.parser"
            http_encoding = (
                page.encoding if "charset" in page.headers.get("content-type", "").lower() else None
            )
            html_encoding = EncodingDetector.find_declared_encoding(page.content, is_html=True)
            encoding = html_encoding or http_encoding

            soup = BeautifulSoup(page.content, parser, from_encoding=encoding)

            urls_left = get_urls_left()
            urls_done = get_urls_done()

            links = soup.find_all("a", href=True)
            for link in links:
                href = link["href"].split("#")[0]
                href = urljoin(website_url, href)

                if not href in get_urls_done() and not href in get_urls_left():
                    add_urls_left(href)

            # add_urls_done(url)
            with open(file_name, "a") as f:
                f.write(url + "\n")

            remove_urls_left()

        except Exception as e:
            print(e)
            remove_urls_left()

            with open(file_name, "a") as f:
                f.write(url + "\n")

            print(f"Droped {url}")
            continue


t1 = threading.Thread(target=scrape_now, args=[])
t2 = threading.Thread(target=scrape_now, args=[])
t3 = threading.Thread(target=scrape_now, args=[])
t4 = threading.Thread(target=scrape_now, args=[])
t5 = threading.Thread(target=scrape_now, args=[])
t6 = threading.Thread(target=scrape_now, args=[])
t7 = threading.Thread(target=scrape_now, args=[])
t8 = threading.Thread(target=scrape_now, args=[])
t9 = threading.Thread(target=scrape_now, args=[])
t10 = threading.Thread(target=scrape_now, args=[])
t11 = threading.Thread(target=scrape_now, args=[])
t12 = threading.Thread(target=scrape_now, args=[])
t13 = threading.Thread(target=scrape_now, args=[])
t14 = threading.Thread(target=scrape_now, args=[])
t15 = threading.Thread(target=scrape_now, args=[])


t1.start()
sleep(2)


t2.start()
sleep(2)


t3.start()
sleep(2)

t4.start()
sleep(2)


t5.start()
sleep(2)


t6.start()
sleep(2)

t7.start()
sleep(2)


t8.start()
sleep(2)


t9.start()
sleep(2)

t10.start()
sleep(2)


t11.start()
sleep(2)


t12.start()
sleep(2)

t13.start()
sleep(2)


t14.start()
sleep(2)


t15.start()
sleep(2)


t1.join()
sleep(2)


t2.join()
sleep(2)


t3.join()
sleep(2)

t4.join()
sleep(2)


t5.join()
sleep(2)


t6.join()
sleep(2)

t7.join()
sleep(2)


t8.join()
sleep(2)


t9.join()
sleep(2)

t10.join()
sleep(2)


t11.join()
sleep(2)


t12.join()
sleep(2)

t13.join()
sleep(2)


t14.join()
sleep(2)


t15.join()
sleep(2)
