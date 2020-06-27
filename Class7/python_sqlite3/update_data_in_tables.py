from utils.helper import *

dbhelper = DBHelper()


sql = ''' UPDATE tasks
            SET priority = ? ,
                begin_date = ? ,
                end_date = ?
            WHERE id = ? '''

updated_task = (5, '2015-01-04', '2015-01-06', 2)

# create tasks
dbhelper.manipulate(sql, updated_task)

fetch_tasks = ''' SELECT * FROM tasks WHERE id=2; '''
tasks = dbhelper.fetch(fetch_tasks)
print(tasks)