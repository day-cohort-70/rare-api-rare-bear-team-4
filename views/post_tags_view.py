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
                post_data["post_id"],
                post_data["tag_id"],
            ),
        )

        number_of_rows_added = db_cursor.rowcount
    
    return True if number_of_rows_added > 0 else False