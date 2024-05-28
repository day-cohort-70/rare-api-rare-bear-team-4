import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


from views import create_user, login_user

# Add your imports below this line


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for shipping ships"""

    def do_GET(self):

        response_body = ""
        url = self.parse_url(self.path)

    def do_PUT(self):
        url = self.parse_url(self.path)
        pk = url["pk"]

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

    def do_DELETE(self):
        url = self.parse_url(self.path)
        pk = url["pk"]

    def do_POST(self):
        url = self.parse_url(self.path)
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "login":
            response = login_user(request_body)
        elif url["requested_resource"] == "register":
            response = create_user(request_body)
        else:
            response = json.dumps({"valid": False, "message": "Invalid endpoint"})

        self.response(response, status.HTTP_200_SUCCESS.value)


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
