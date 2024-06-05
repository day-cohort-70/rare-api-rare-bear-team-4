import sqlite3
import json


def update_comment(id, comment_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Comments
            SET content =?
            WHERE id =?
            """,
            (comment_data["content"], id),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False


def delete_comment(pk):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        DELETE FROM Comments WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False


def retrieve_comments():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            s.id,
            s.author_id,
            s.post_id,
            s.content
        FROM Comments s
        """,
            (),
        )
        query_results = db_cursor.fetchall()

        # Convert each row to a dictionary and append to a list
        comments_list = []
        for row in query_results:
            comments_list.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_comments = json.dumps(comments_list)

    return serialized_comments

def retrieve_comments_by_post_id(post_id):
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            p.id,
            p.author_id,
            p.post_id,
            p.content
        FROM Comments p
        WHERE p.post_id = ?
        """,
            (post_id,),
        )
        query_results = db_cursor.fetchall()

        # Convert each row to a dictionary and append to a list
        comments_list = []
        for row in query_results:
            comments_list.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_comments = json.dumps(comments_list)

    return serialized_comments


def post_comment(comment_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Comments
            (author_id, post_id, content) VALUES(?, ?, ?)
            """,
            (comment_data["author_id"], comment_data["post_id"], comment_data["content"]),
        )
        new_comment_id = db_cursor.lastrowid

    conn.commit()
    ## Select and return using cursor.lastrow
    return json.dumps({
        'id': new_comment_id,
        'author_id': comment_data["author_id"],
        'post_id': comment_data["post_id"],
        'content': comment_data["content"]
        })