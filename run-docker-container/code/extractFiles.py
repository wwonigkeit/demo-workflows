import base64
import cgi
import os

input = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTIwMjYxNzQ0NjI1MjE3NjE1ODU3ODMwOA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJweXRob25fZmlsZXMiOyBmaWxlbmFtZT0icmVxdWlyZW1lbnRzLnR4dCINCkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpbg0KDQpyZXF1ZXN0cw0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTIwMjYxNzQ0NjI1MjE3NjE1ODU3ODMwOA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJweXRob25fZmlsZXMiOyBmaWxlbmFtZT0icHl0aG9uX2V4YW1wbGUucHkiDQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbQ0KDQppbXBvcnQganNvbgppbXBvcnQgcmVxdWVzdHMKCnJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2pzb25wbGFjZWhvbGRlci50eXBpY29kZS5jb20vdG9kb3MiKQp0b2RvcyA9IGpzb24ubG9hZHMocmVzcG9uc2UudGV4dCkKCiMgUHJldHR5IFByaW50aW5nIEpTT04gc3RyaW5nIGJhY2sKcHJpbnQoanNvbi5kdW1wcyh0b2RvcywgaW5kZW50ID0gNCwgc29ydF9rZXlzPVRydWUpKQ0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTIwMjYxNzQ0NjI1MjE3NjE1ODU3ODMwOC0tDQo="
# boundary = "--------------------------202617446252176158578308"

base64_data = base64.b64decode(input)
multiform_data = base64_data.decode("utf-8")
print(multiform_data)

# data_array = multiform_data.decode("utf-8").split(boundary)

# for x in range(len(data_array)):
#     print(data_array[x])


# Parse form data
form = cgi.FieldStorage(fp=cgi.StringIO(multiform_data), environ={'REQUEST_METHOD': 'POST'})

# Extract files
file_names = []
for key in form.keys():
    if isinstance(form[key], cgi.FieldStorage):
        file_name = form[key].filename
        file_content = form[key].value

        # Save file
        with open(file_name, 'wb') as f:
            f.write(file_content)
        file_names.append(file_name)

print("Files extracted:", file_names)