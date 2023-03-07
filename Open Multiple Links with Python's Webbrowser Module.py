import webbrowser

def open_multiple_links():
    """
    Opens multiple links in the default web browser.

    The links to be opened are specified in the `urls` list.
    """
    browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    urls = ["stackoverflow.com", "github.com/PulkitGehlot81", "gmail.com", "google.co.in", "youtube.com"]

    for url in urls:
        print(f"Opening: {url}")
        try:
            webbrowser.get(browser_path).open(url)
        except Exception as e:
            print(f"Error opening {url}: {e}")

if __name__ == "__main__":
    open_multiple_links()