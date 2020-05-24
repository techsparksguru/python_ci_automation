from utils.helper import *

dbhelper = DBHelper()

# Delete tasks query
delete_sql_by_id = ''' DELETE FROM tasks WHERE id=?; '''

delete_all_sql = ''' DELETE FROM tasks; '''

delete_by_id = dbhelper.manipulate(delete_sql_by_id, '2')
delete_all = dbhelper.execute(delete_all_sql)

print(dbhelper.fetch(''' SELECT * FROM tasks; '''))