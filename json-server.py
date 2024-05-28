import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for shipping ships"""

    def do_GET(self):
  
    def do_PUT(self):
 
    def do_DELETE(self):
       
    def do_POST(self):
       


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()