import sqlite3
import json

def update_categories(id, Categories_data):
    with sqlite3.connect("./Categories.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Categories
                SET
                    name = ?,
                    hauler_id = ?
            WHERE id = ?
            """,
            (Categories_data['name'], Categories_data['hauler_id'], id)
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False

def delete_categories(pk):
    with sqlite3.connect("./Categories.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        DELETE FROM Categories WHERE id = ?
        """, (pk,)
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False


def list_categories():
    # Open a connection to the database
    with sqlite3.connect("./Categories.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            s.id,
            s.name,
            s.hauler_id
        FROM Categories s
        """)
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        categories=[]
        for row in query_results:
            categories.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_categories = json.dumps(categories)

    return serialized_categories

def retrieve_categories(pk):
    # Open a connection to the database
    with sqlite3.connect("./Categories.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            s.id,
            s.name,
            s.hauler_id
        FROM Categories s
        WHERE s.id = ?
        """, (pk,))
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        dictionary_version_of_object = dict(query_results)
        serialized_Categories = json.dumps(dictionary_version_of_object)

    return serialized_Categories

def post_categories(Categories_data):
    with sqlite3.connect("./Categories.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Categories
            (name, hauler_id)
                VALUES(
                    ?,
                    ?)
            """,
            (Categories_data['name'], Categories_data['hauler_id'])
        )
        new_Categories_id = db_cursor.lastrowid

    conn.commit()
    ## Select and return using cursor.lastrow
    return json.dumps({
            'id': new_Categories_id,
            'name': Categories_data['name'],
            'hauler_id': Categories_data['hauler_id']
        })