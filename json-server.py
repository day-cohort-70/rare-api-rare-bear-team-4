import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import list_tags, retrieve_tag
from views import create_user, login_user
from views import get_all_posts, get_one_post

class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for rare"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "tags":
            if url["pk"] != 0:
                response_body = retrieve_tag(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = list_tags()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        else:
            return self.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

        if url["requested_resource"] == "posts":
            if url["pk"] != 0:
                response_body = get_one_post(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = get_all_posts(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

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
    """Def main and port"""
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
