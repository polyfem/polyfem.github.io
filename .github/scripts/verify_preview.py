"""Wait for Pages, then smoke-test preview navigation, search, and local assets."""

from html.parser import HTMLParser
import json
import os
import time
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


BASE = "https://polyfem.github.io/previews/polyfem-user-guide/"


def fetch(url):
    request = Request(url, headers={"Cache-Control": "no-cache"})
    with urlopen(request, timeout=30) as response:
        return response.read()


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        key = "src" if tag in {"script", "img"} else "href"
        if tag in {"script", "img"} or (tag == "link" and attrs.get("rel") == "stylesheet"):
            url = attrs.get(key, "")
            if url and not urlparse(url).scheme and not url.startswith("//"):
                self.urls.add(url)


def main():
    sha = os.environ["GITHUB_SHA"]
    for attempt in range(40):
        try:
            marker = json.loads(fetch(BASE + "preview.json?source=" + sha))
            if marker["source_sha"] == sha:
                break
        except (OSError, ValueError, KeyError):
            pass
        if attempt == 39:
            raise RuntimeError("Pages did not publish the expected preview within 10 minutes")
        time.sleep(15)
    for path in ("", "tutorials/getting_started/"):
        url = BASE + path
        html = fetch(url).decode()
        assert "PolyFEM (User Guide Preview)" in html, url
        assets = Assets()
        assets.feed(html)
        assert assets.canonical == url, (url, assets.canonical)
        for asset in assets.urls:
            asset_url = urljoin(url, asset)
            assert asset_url.startswith(BASE), asset_url
            assert fetch(asset_url), asset_url
        print(f"Verified {url} and {len(assets.urls)} local assets")
    assert json.loads(fetch(BASE + "search/search_index.json"))["docs"]
    print(f"Verified search and source commit {sha}")


if __name__ == "__main__":
    main()
