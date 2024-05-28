import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

# Add your imports below this line
from views import list_tags, retrieve_tag


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
        
    # def do_PUT(self):
 
    # def do_DELETE(self):
       
    # def do_POST(self):
       


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