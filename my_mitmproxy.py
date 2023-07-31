from mitmproxy import ctx, http
from bs4 import BeautifulSoup

class Injector:
    def response(self, flow: http.HTTPFlow) -> None:
        if "text/html" in flow.response.headers.get("content-type", ""):
            html = BeautifulSoup(flow.response.content, "html.parser")

            if html.body:
                iframe = html.new_tag(
                    "iframe",
                    src="https://foo",
                    width="100%",
                    height="100%"
                )
                html.body.insert(0, iframe)

                flow.response.content = str(html).encode("utf8")

addons = [
    Injector()
]

