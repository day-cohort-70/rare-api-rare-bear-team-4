import sqlite3
import json


def post_post_tag(post_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO PostTags (post_id, tag_id)
            VALUES (?, ?)
            """,
            (
                post_data["postId"],
                post_data["tagId"],
            ),
        )

        number_of_rows_added = db_cursor.rowcount
    
    return True if number_of_rows_added > 0 else False


def get_one_post_tag(url):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        query = ("""
            SELECT 
                pt.id,
                pt.post_id,
                pt.tag_id,
                t.id tag_id,
                t.label
            FROM PostTags pt
            JOIN Tags t ON t.id = pt.tag_id
            WHERE pt.post_id = ?
        """)
        
        db_cursor.execute(query, (url["pk"],))
        query_results = db_cursor.fetchall()

        post_tags = []

        for row in query_results:
            post_tag = {
            "id": row["id"],
            "postId": row["post_id"],
            "tagId": row["tag_id"]
            }

            if "_expand" in url["query_params"]:
                post_tag["tag"] = {
                    "tagId": row["tag_id"],
                    "tagLabel": row["label"]
                }
            post_tags.append(post_tag)
    
    return json.dumps(post_tags)


def get_all_post_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                pt.id,
                pt.post_id,
                pt.tag_id
            FROM PostTags pt
        """)

        query_results = cursor.fetchall()

        post_tags = []
        for row in query_results:
            post_tags.append(dict(row))

    return json.dumps(post_tags)

def delete_post_tag(pk):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(""" 
            DELETE from PostTags
                WHERE id = ?
        """, (pk,))

        number_of_rows_deleted = cursor.rowcount

    return True if number_of_rows_deleted > 0 else False
