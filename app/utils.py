from urllib.parse import urljoin

def make_absolute(base_url: str, href: str | None) -> str | None:
    if not href:
        return None
    return urljoin(base_url, href)