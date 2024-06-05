import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import list_tags, retrieve_tag, update_tag, delete_tag, make_tag
from views import (
    create_user,
    login_user,
    update_user,
    delete_user,
    retrieve_user,
    list_users,
)
from views import get_all_posts, get_one_post, delete_post, update_post, post_post
from views import (
    list_categories,
    retrieve_categories,
    delete_categories,
    update_categories,
    post_categories,
)
from views import post_post_tag, get_post_tags, delete_post_tag
from views import (
    update_comment,
    retrieve_comment,
    retrieve_comments_by_post_id,
    post_comment,
    delete_comment
)


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

        elif url["requested_resource"] == "posts":
            if url["pk"] != 0:
                response_body = get_one_post(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = get_all_posts(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "categories":
            if url["pk"] != 0:
                response_body = retrieve_categories(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = list_categories()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "users":
            if url["pk"] != 0:
                response_body = retrieve_user(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = list_users()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        elif url["requested_resource"] == "post-tags":
                response_body = get_post_tags(url)
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        elif url["requested_resource"] == "comments":
            if url["pk"] != 0:
                response_body = retrieve_comment(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
                    # Get the request body JSON for the new data
            content_len = int(self.headers.get("content-length", 0))
            request_body = self.rfile.read(content_len)
            request_body = json.loads(request_body)
            response_body = retrieve_comments_by_post_id(request_body["post_id"])
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_PUT(self):
        """Handle PUT requests from a client"""
        url = self.parse_url(self.path)
        pk = url["pk"]

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "categories":
            if pk != 0:
                successfully_updated = update_categories(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        elif url["requested_resource"] == "posts":
            if pk != 0:
                successfully_updated = update_post(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
        elif url["requested_resource"] == "tags":
            if pk != 0:
                successfully_updated = update_tag(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        elif url["requested_resource"] == "users":
            if pk != 0:
                successfully_updated = update_user(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                
        elif url["requested_resource"] == "comments":
            if pk != 0:
                successfully_updated = update_comment(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )

    def do_DELETE(self):
        """Handle DELETE requests from a client"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "categories":
            if pk != 0:
                successfully_deleted = delete_categories(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        elif url["requested_resource"] == "posts":
            if pk != 0:
                successfully_deleted = delete_post(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        elif url["requested_resource"] == "tags":
            if pk != 0:
                successfully_deleted = delete_tag(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        elif url["requested_resource"] == "users":
            if pk != 0:
                successfully_deleted = delete_user(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )
        elif url["requested_resource"] == "post-tags":
            success = delete_post_tag(pk)
            if success:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            return self.response("Requested Resource not Found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
            
        elif url["requested_resource"] == "comments":
            if pk != 0:
                successfully_deleted = delete_comment(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

    def do_POST(self):
        url = self.parse_url(self.path)
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "login":
            response = login_user(request_body)

        elif url["requested_resource"] == "register":
            response = create_user(request_body)

        elif url["requested_resource"] == "categories":
            successfully_posted = post_categories(request_body["label"])
            if successfully_posted:
                return self.response(
                    successfully_posted, status.HTTP_201_SUCCESS_CREATED.value
                )
        elif url["requested_resource"] == "tags":
            successfully_posted = make_tag(request_body["label"])
            if successfully_posted:
                return self.response(
                    successfully_posted, status.HTTP_201_SUCCESS_CREATED.value
                )
            
        elif url["requested_resource"] == "comments":
            successfully_posted = post_comment(request_body)
            if successfully_posted:
                return self.response(
                    successfully_posted, status.HTTP_201_SUCCESS_CREATED.value
                )

        elif url["requested_resource"] == "posts":
            new_post_id = post_post(request_body)
            if new_post_id is not None:
                # Return the new ship's ID in the response
                response_body = json.dumps({"new_post_id": new_post_id})
                return self.response(
                    response_body, status.HTTP_201_SUCCESS_CREATED.value
                )
            else:
                # Handle the case where the post creation failed
                response_body = json.dumps({"error": "Failed to create post"})
                return self.response(
                    response_body, status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value
                )
        elif url["requested_resource"] == "post-tags":
            success = post_post_tag(request_body)
            if success:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

          
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
