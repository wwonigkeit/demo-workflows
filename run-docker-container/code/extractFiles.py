import base64
import cgi
import os
import io
import re

# input = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTIwMjYxNzQ0NjI1MjE3NjE1ODU3ODMwOA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJweXRob25fZmlsZXMiOyBmaWxlbmFtZT0icmVxdWlyZW1lbnRzLnR4dCINCkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpbg0KDQpyZXF1ZXN0cw0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTIwMjYxNzQ0NjI1MjE3NjE1ODU3ODMwOA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJweXRob25fZmlsZXMiOyBmaWxlbmFtZT0icHl0aG9uX2V4YW1wbGUucHkiDQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbQ0KDQppbXBvcnQganNvbgppbXBvcnQgcmVxdWVzdHMKCnJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2pzb25wbGFjZWhvbGRlci50eXBpY29kZS5jb20vdG9kb3MiKQp0b2RvcyA9IGpzb24ubG9hZHMocmVzcG9uc2UudGV4dCkKCiMgUHJldHR5IFByaW50aW5nIEpTT04gc3RyaW5nIGJhY2sKcHJpbnQoanNvbi5kdW1wcyh0b2RvcywgaW5kZW50ID0gNCwgc29ydF9rZXlzPVRydWUpKQ0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTIwMjYxNzQ0NjI1MjE3NjE1ODU3ODMwOC0tDQo="
# # boundary = "--------------------------202617446252176158578308"

# base64_data = base64.b64decode(input)
# multiform_data = base64_data.decode("utf-8")
# print(multiform_data)



# Sample multipart form-data payload
form_data = """
----------------------------202617446252176158578308
Content-Disposition: form-data; name="python_files"; filename="requirements.txt"
Content-Type: text/plain

requests
----------------------------202617446252176158578308
Content-Disposition: form-data; name="python_files"; filename="python_example.py"
Content-Type: application/octet-stream

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Pretty Printing JSON string back
print(json.dumps(todos, indent = 4, sort_keys=True))
----------------------------202617446252176158578308--
"""

# Regular expression to extract parts of the payload
pattern = re.compile(r'filename="([^"]+)"\r\n\r\n([\s\S]+?)\r\n')

# Extract files
file_names = []
matches = pattern.findall(form_data)
for match in matches:
    filename, content = match
    with open(filename, 'wb') as f:
        f.write(content.encode('utf-8'))
    file_names.append(filename)

print("Files extracted:", file_names)