# Website Status Checker

> A Python script that continuously monitors a website's availability and prints its status and page title every 2 minutes.

---

## Overview

A lightweight CLI tool that polls a given URL using `requests`, checks its HTTP status code, and parses the page title with `BeautifulSoup`. Useful for keeping an eye on whether a site is up or down without any external monitoring service.

---

## Features

- Checks if a website is up (`200 OK`) or down (with the status code)
- Handles connection errors gracefully
- Parses and displays the page `<title>` when the site is reachable
- Automatically re-checks every **2 minutes** in a continuous loop

---

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

## Usage

```bash
python checker.py
```

You'll be prompted to enter a URL:

```
Enter the website URL to check: https://example.com
Website https://example.com is Up.
Title: Example Domain
```

The script then re-checks every 120 seconds until you stop it with `Ctrl+C`.

---

## Sample Output

```
Website https://example.com is Up.
Title: Example Domain

Website https://down-site.com is Down (Unable to Connect).
```

---

## Project Structure

```
website_status_checker/
└── checker.py    # Single-file script — all logic lives here
```

---

## License

© 2026 Sheikh Muhammad Talha Bin Khalid. All Rights Reserved.
