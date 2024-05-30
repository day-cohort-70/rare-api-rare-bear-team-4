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
            p.image_url,
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

        params = []

        if "userId" in url["query_params"]:
            query += " WHERE p.user_id = ?"
            user_id = url["query_params"]["userId"][0]
            params.append(user_id)

        # Execute the query with the parameters
        cursor.execute(query, params)
        query_results = cursor.fetchall()

    posts = []

    for row in query_results:
        post = {
            "id": row["id"],
            "userId": row["user_id"],
            "categoryId": row["category_id"],
            "title": row["title"],
            "publicationDate": row["publication_date"],
            "imageUrl": row["image_url"],
            "content": row["content"],
            "approved": row["approved"],
        }

        if "_expand" in url["query_params"]:
            for item in url["query_params"]["_expand"]:

                if item == "category":
                    post["category"] = {
                        "categoryId": row["category_id"],
                        "categoryLabel": row["category_label"],
                    }
                if item == "user":
                    post["user"] = {
                        "userId": row["user_id"],
                        "userFirstName": row["first_name"],
                        "userLastName": row["last_name"],
                    }

        posts.append(post)

    return json.dumps(posts)


def get_one_post(pk):
    return "bubkis"


def delete_post(pk):
    with sqlite3.connect("db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        DELETE FROM Posts WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False


def update_post(id, post_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Posts
                SET
                    user_id = ?,
                    category_id = ?,
                    title = ?,
                    publication_date = ?,
                    image_url = ?,
                    content = ?,
                    approved = ?,
                    id = ?
            WHERE id = ?
            """,
            (
                post_data["user_id"],
                post_data["category_id"],
                post_data["title"],
                post_data["publication_date"],
                post_data["image_url"],
                post_data["content"],
                post_data["approved"],
                id,
                id,
            ),
        )

        rows_affected = db_cursor.rowcount

    return rows_affected > 0


def post_post(post_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                post_data["user_id"],
                post_data["category_id"],
                post_data["title"],
                post_data["publication_date"],
                post_data["image_url"],
                post_data["content"],
                post_data["approved"],
            ),
        )

        new_post_id = db_cursor.lastrowid

    return new_post_id
