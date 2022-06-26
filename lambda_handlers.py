from bs4 import BeautifulSoup
from markdown import markdown
from release_exporter import get_latest_spoiler


def get_spoilers_handler(event, context):
    """This is a handler to pass the latest spoilers to lambda invokares"""
    latest_spoiler = get_latest_spoiler()

    html = markdown(latest_spoiler)
    text = "".join(BeautifulSoup(html, features="lxml").findAll(text=True))

    print(text)
