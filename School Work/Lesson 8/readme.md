# Exceptions & Error Handling  
Anticipating errors is essential for writing resilient programs. An **exception** represents a situation where something *might* go wrong, and your code needs a safe, predictable way to respond.

## Why Exceptions Matter  
When interacting with external systems (printers, files, networks, APIs), failures are normal. Robust code anticipates these scenarios instead of crashing.

### Example: A Printer Might Fail Because  
- It has **no ink**  
- It has **no paper**  
- It has **no connection**  

These predictable failure states are ideal for exception handling.

## The Exception Handling Structure  
Most languages use a three‑part pattern:

```python
try:
    # Code that might fail
    print_document()
except PrinterError:
    # What to do if it fails
    handle_error()
finally:
    # Code that always runs
    cleanup()
```

### Blocks Explained  
- **TRY** — Contains code that may raise an exception  
- **EXCEPT** — Catches and handles the error  
- **FINALLY** — Executes regardless of success or failure (cleanup, closing files, releasing resources)

---

# Web Scraping  
Web scraping involves retrieving and processing information from websites. To scrape effectively, you must understand how URLs and HTTP responses work.

## What Is a URL?  
A **URL** (Uniform Resource Locator) is the address of a resource on the internet.

### Parts of a URL  
| Part | Description |
|------|-------------|
| **Protocol** | Defines how the browser and server communicate (e.g., `http`, `https`) |
| **Domain Name** | The unique identifier of the website (e.g., `example.com`) |
| **Path** | The specific file or directory on the server (e.g., `/products/laptops`) |

### Example  
```
https://example.com/products/laptops
└──┬───┘ └───────┬──────┘ └───────┬──────┘
  Protocol       Domain            Path
```

---

# Using `urllib.request` in Python  
`urllib.request` is a Python module that allows you to access internet resources such as webpages, APIs, and files.

### Common HTTP Status Codes  
| Code | Meaning |
|------|---------|
| **200** | Request successful |
| **301** | Resource moved permanently |
| **403** | Access forbidden |
| **404** | Resource not found |

These codes help you understand how the server responded to your request.

### Useful Methods  
- **`getcode()`** — Retrieves the HTTP status code from the server  
- **`read()`** — Returns the raw HTML content of the webpage  

### Example  
```python
from urllib import request

response = request.urlopen("https://example.com")

status = response.getcode()     # e.g., 200
html   = response.read()        # raw HTML bytes
```

For better formatting with getcode() we use the following command in our command promt
```
pip install beautifulsoup4
```

# Writing to a File  
In Python, writing to a file generally follows a simple pattern:

```python
file = open("file.txt", "w")   # "w" = write mode
file.write("words")
file.close()
```

### Common File Modes  
| Mode | Meaning |
|------|---------|
| **"w"** | Write (overwrites the file) |
| **"r"** | Read (default mode) |
| **"a"** | Append (adds to the end of the file) |
| **"w+"** | Write + Read |
| **"a+"** | Append + Read |

---

# Reading a File

```python
file = open("file.txt", "r")   # "r" = read mode
contents = file.read()
file.close()

print(contents)
```

### Other Useful Read Methods  
- **`read()`** — reads the entire file  
- **`readline()`** — reads one line at a time  
- **`readlines()`** — returns a list of all lines  

---

# Appending to a File

Appending lets you add new content without deleting what’s already there.

```python
file = open("file.txt", "a")   # "a" = append mode
file.write("\nNew line added!")
file.close()
```

---

# Best Practice: Using `with`  
Using `with` automatically closes the file for you — safer and cleaner.

```python
with open("file.txt", "w") as file:
    file.write("Hello world!")
```

```python
with open("file.txt", "r") as file:
    print(file.read())
```

```python
with open("file.txt", "a") as file:
    file.write("\nMore text")
```
