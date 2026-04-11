from connect import get_connection


def search(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    results = cur.fetchall()

    for row in results:
        print(row)

    conn.close()



def get_paginated(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    results = cur.fetchall()

    for row in results:
        print(row)

    conn.close()



def upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()

    conn.close()



def insert_many(names, phones):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()

    conn.close()



def delete(value):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    conn.close()


if __name__ == "__main__":
    upsert("Alice", "12345")
    upsert("Bob", "67890")

    insert_many(
        ["John", "Mike", "BadUser"],
        ["11111", "22222", "abc"]  
    )

    print("Search:")
    search("A")

    print("\nPagination:")
    get_paginated(2, 0)

    delete("Alice")