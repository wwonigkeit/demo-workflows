import base64
import json
from requests_toolbelt.multipart import decoder
import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hb:c:",["body=","content="])
    except getopt.GetoptError:
        print ('extractFiles.py -b <body> -o <content>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('extractFiles.py -b <body> -c <content>')
            sys.exit()
        elif opt in ("-b", "--body"):
            body = arg
        elif opt in ("-c", "--content"):
            content_type = arg

    # input = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTU2MjYwMzY5ODM2OTE1MDE4MTU1NDE5MQ0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJweXRob25fZmlsZXMiOyBmaWxlbmFtZT0icmVxdWlyZW1lbnRzLnR4dCINCkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpbg0KDQpyZXF1ZXN0cw0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTU2MjYwMzY5ODM2OTE1MDE4MTU1NDE5MQ0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJweXRob25fZmlsZXMiOyBmaWxlbmFtZT0icHl0aG9uRXhhbXBsZS5weSINCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtDQoNCmltcG9ydCBqc29uCmltcG9ydCByZXF1ZXN0cwoKcmVzcG9uc2UgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vanNvbnBsYWNlaG9sZGVyLnR5cGljb2RlLmNvbS90b2RvcyIpCnRvZG9zID0ganNvbi5sb2FkcyhyZXNwb25zZS50ZXh0KQoKIyBQcmV0dHkgUHJpbnRpbmcgSlNPTiBzdHJpbmcgYmFjawpwcmludChqc29uLmR1bXBzKHRvZG9zLCBpbmRlbnQgPSA0LCBzb3J0X2tleXM9VHJ1ZSkpDQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tNTYyNjAzNjk4MzY5MTUwMTgxNTU0MTkxLS0NCg=="
    base64_data = base64.b64decode(body)
    # content_type = "multipart/form-data; boundary=--------------------------562603698369150181554191"

    files_data = []

    for part in decoder.MultipartDecoder(base64_data, content_type).parts:
        headers = {key.decode(): value.decode() for key, value in part.headers.items()}
        content_disposition = headers.get('Content-Disposition', '')
        if content_disposition:
            parts = content_disposition.split(';')
            for party in parts:
                if 'filename' in party:
                    _, file_name = party.strip().split('=')
                    file_name = file_name.strip('"')
                    files_data.append({"fname": file_name, "content": part.text})

    print(json.dumps(files_data, indent=4))

if __name__ == "__main__":
   main(sys.argv[1:])