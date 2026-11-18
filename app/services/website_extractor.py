import httpx
import socket
import ipaddress
from bs4 import BeautifulSoup
from urllib.parse import urlparse


async def extract_website_content(url: str):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only HTTP and HTTPS URLs are allowed")

    if not parsed.hostname:
        raise ValueError("Invalid website URL")

    if parsed.username or parsed.password:
        raise ValueError("Credentials in URLs are not allowed")

    # Prevent requests to private or internal IP addresses
    try:
        addresses = socket.getaddrinfo(
            parsed.hostname,
            parsed.port or (443 if parsed.scheme == "https" else 80),
            type=socket.SOCK_STREAM,
        )

        for address in addresses:
            ip = ipaddress.ip_address(address[4][0])

            if not ip.is_global:
                raise ValueError("Private or internal URLs are not allowed")

    except socket.gaierror:
        raise ValueError("Unable to resolve website address")

    headers = {"User-Agent": "Mozilla/5.0 WebsiteAnalyzer/1.0"}

    async with httpx.AsyncClient(
        timeout=20,
        follow_redirects=False,
    ) as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()

        content_type = response.headers.get("content-type", "")

        if "text/html" not in content_type.lower():
            raise ValueError("The URL does not return an HTML page")

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary elements
        for element in soup(
            ["script", "style", "nav", "footer", "header", "noscript"]
        ):
            element.decompose()

        title = soup.title.string if soup.title else ""

        description_tag = soup.find(
            "meta",
            attrs={"name": "description"},
        )
        description = (
            description_tag.get("content", "") if description_tag else ""
        )

        content = soup.get_text(separator=" ", strip=True)

        return {
            "title": title,
            "description": description,
            "content": content[:12000],
        }