from utils.helper import *

dbhelper = DBHelper()


sql = ''' UPDATE tasks
            SET priority = ? ,
                begin_date = ? ,
                end_date = ?
            WHERE id = ? '''

cur = conn.cursor()
cur.execute(sql, task)
conn.commit()


def main():
    database = "db/pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn, (2, '2015-01-04', '2015-01-06', 2))


if __name__ == '__main__':
    main()