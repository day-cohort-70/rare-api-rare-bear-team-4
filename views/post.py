import sqlite3
import json

def get_all_posts(url):
    with sqlite3.connect("db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        query = """
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            p.approved,
            ct.id category_id,
            ct.label category_label,
            u.id user_id,
            u.first_name,
            u.last_name
        FROM Posts p
        JOIN Categories ct ON ct.id = p.category_id
        JOIN Users u ON u.id = p.user_id
        """

        cursor.execute(query)
        query_results = cursor.fetchall()

    posts = []

    for row in query_results:
        post = {
            "id": row["id"],
            "userId": row["user_id"],
            "categoryId": row["category_id"],
            "title": row["title"],
            "publicationDate": row["publication_date"],
            "content": row["content"],
            "approved": row["approved"]
        }

        if "_expand" in url["query_params"]:
            for item in url["query_params"]["_expand"]:

                if item == "category":
                    post["category"] = {
                        "categoryId": row["category_id"],
                        "categoryLabel": row["category_label"]
                    }
                if item == "user":
                    post["user"] = {
                        "userId": row["user_id"],
                        "userFirstName": row["first_name"],
                        "userLastName": row["last_name"]
                    }

        posts.append(post)

    return json.dumps(posts)

def get_one_post():
    return "bubkis"