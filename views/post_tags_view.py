import sqlite3
import json


def post_post_tag(post_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO PostTags (post_id, tag_id)
            VALUES (?, ?)
            """,
            (
                post_data["post_id"],
                post_data["tag_id"],
            ),
        )

        new_post_tag_id = db_cursor.lastrowid

    return new_post_tag_id