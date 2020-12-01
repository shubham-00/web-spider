from selenium import webdriver
from pyvirtualdisplay import Display

from app.models import UrlsLeft, UrlsDone, UrlsSaved

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import threading
from time import sleep
import os
import datetime
from timeit import default_timer as timer


# website_url = "https://ibm.com/us-en/"
# website_url = "https://towardsdatascience.com/"
# website_url = "https://machinelearningmastery.com/"
# website_url = "https://ai.googleblog.com/"
# website_url = "https://pyimagesearch.com/"
# website_url = "https://deepmind.com/"
# website_url = "https://digitalocean.com/"
# website_url = "https://linode.com/"
# website_url = "https://cloud.google.com/"
website_url = "https://arduino.cc/"
# website_url = "https://raspberrypi.org/"
# website_url = "https://kaggle.com/"
# website_url = "https://tensorflow.org/"
# website_url = "https://heroku.com/"
# website_url = "https://lastminuteengineers.com/"
# website_url = "https://thecodingtrain.com/"


domain = website_url.split("//")[1].split("/")[0]


obj = UrlsLeft(url=website_url)
obj.save()


urls_left = [i.url for i in UrlsLeft.objects.all()]
urls_done = [i.url for i in UrlsDone.objects.all()]


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}


def count_saved_urls():
    from app.models import UrlsSaved

    return UrlsSaved.objects.count()


def save_url(url):
    from app.models import UrlsSaved

    queryset = UrlsSaved.objects.filter(url=url)
    if not queryset.exists():
        obj = UrlsSaved(url=url)
        obj.save()


def add_urls_left(url):
    from app.models import UrlsLeft

    global urls_left

    urls_left.append(url)

    obj = UrlsLeft(url=url)
    obj.save()


def add_urls_done(url):
    from app.models import UrlsDone

    global urls_done

    urls_done.append(url)

    obj = UrlsDone(url=url)
    obj.save()


def remove_urls_left():
    from app.models import UrlsLeft

    global urls_left

    urls_left.pop(0)

    obj = UrlsLeft.objects.all().first()
    obj.delete()


while True:  # not urls_left == []:
    print(datetime.datetime.now())

    try:

        if urls_left == []:
            exit()

        url = urls_left[0]
        # url = url.split("?")[0]
        print("Urls completed", len(urls_done))
        print("Urls saved", count_saved_urls())
        print("Urls left", len(urls_left))
        print("Current url:", url)
        print()

        if url in urls_done:
            remove_urls_left()
            continue

        add_urls_done(url)

        save_url(url)

        remove_urls_left()

        if not domain in url or "/ufaqs/" in url or "/single-faq/" in url or "/downloads/cas/" in url:

            save_url(url)

            continue

        if (
            url.endswith(".pdf")
            or url.endswith(".jpg")
            or url.endswith(".jpeg")
            or url.endswith(".mp3")
            or url.endswith(".mp4")
            or url.endswith(".png")
            or url.endswith(".gif")
            or url.endswith(".zip")
            or "mediacenter.ibm.com" in url
        ):
            save_url(url)
            continue

        try:
            # page = requests.get(url, headers=headers)
            # print(page.content)

            # parser = "html.parser"
            # http_encoding = (
            #     page.encoding if "charset" in page.headers.get("content-type", "").lower() else None
            # )
            # html_encoding = EncodingDetector.find_declared_encoding(page.content, is_html=True)
            # encoding = html_encoding or http_encoding

            # soup = BeautifulSoup(page.content, parser, from_encoding=encoding)

            # links = soup.find_all("a", href=True)
            # for link in links:
            #     href = link["href"].split("#")[0]
            #     href = urljoin(url, href)

            #     if not href in urls_done and not href in urls_left:
            #         add_urls_left(href)

            # save_url(url)

            display = Display(visible=0, size=(800, 600))
            display.start()

            driver = webdriver.Chrome(r"/home/shubham/drivers/chromedriver")

            driver.get(url)

            driver.maximize_window()

            elements = driver.find_elements_by_tag_name("a")
            links = []

            for element in elements:
                links.append(element.get_attribute("href"))

            for link in links:
                try:
                    href = link.split("#")[0]
                    href = urljoin(url, href)

                    if not href in urls_done and not href in urls_left:
                        add_urls_left(href)
                except:
                    pass

            save_url(url)
            driver.close()
            display.stop()

        except Exception as e:
            print(e)

            save_url(url)
            try:
                driver.close()
            except:
                pass
            # print(f"Droped {url}")
            exit()
            continue
    except Exception as e:
        print(e)
        sleep(10)
        exit()
        continue
