import base64, json, os, getopt, sys

def main(argv):
   headerin = ''
   payloadin = ''
   
   try:
      opts, args = getopt.getopt(argv,"he:s:p:",["header=","payload="])
   except getopt.GetoptError:
      print ('decodePaylopad.py -e <header> -p <payload>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('decodePaylopad.py -e <header> -p <payload>')
         sys.exit()
      elif opt in ("-e", "--header"):
         headerin = arg
      elif opt in ("-p", "--payload"):
         payloadin = arg         
   
   # Header
   header = json.loads( base64.urlsafe_b64decode( headerin + "="*divmod(len(headerin),4)[1] ) )
   # Payload
   payload = json.loads( base64.urlsafe_b64decode( payloadin + "="*divmod(len(payloadin),4)[1] ) )

   fix_payload = json.dumps(payload)
   fix_payload = fix_payload.replace("\'", "\"")
   fix_payload = fix_payload.replace("\\", "")
   fix_payload = fix_payload.replace("\"{", "{")
   fix_payload = fix_payload.replace("}\"", "}")

   payload = json.loads(fix_payload)
   
   dict = {}
   dict["header"] = header
   dict["payload"] = payload

   print(json.dumps(dict, ensure_ascii=False, indent=3))


if __name__ == "__main__":
   main(sys.argv[1:])

