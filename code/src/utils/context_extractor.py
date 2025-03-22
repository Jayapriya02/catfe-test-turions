from playwright.sync_api import sync_playwright

def extract_context(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        page_info = {
            "title": page.title(),
            "buttons": [el.inner_text() for el in page.query_selector_all("button")],
            "links": [el.get_attribute("href") for el in page.query_selector_all("a")],
            "inputs": [el.get_attribute("name") for el in page.query_selector_all("input")]
        }

        browser.close()
        return page_info

if __name__ == "__main__":
    url = "https://example.com"
    print(extract_context(url))
