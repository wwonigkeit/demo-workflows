import base64
import json
from requests_toolbelt.multipart import decoder
import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hb:c:",["body=","content="])
    except getopt.GetoptError:
        print ('extractFiles.py -b <body> -c <content>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('extractFiles.py -b <body> -c <content>')
            sys.exit()
        elif opt in ("-b", "--body"):
            body = arg
        elif opt in ("-c", "--content"):
            content_type = arg

    base64_data = base64.b64decode(body)

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