from utils.helper import *

dbhelper = DBHelper()

sql_project = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''

# create a new project
project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
project_id = dbhelper.manipulate(sql_project, project)
print(project_id)

sql_task = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
# tasks
task_1 = ('Analyze the requirements of the app', 1,
          1, project_id, '2015-01-01', '2015-01-02')
task_2 = ('Confirm with user about the top requirements',
          1, 1, project_id, '2015-01-03', '2015-01-05')

# create tasks
dbhelper.manipulate(sql_task, task_1)
dbhelper.manipulate(sql_task, task_2)

# fetch records SQL
fetch_projects = ''' SELECT * FROM projects; '''
fetch_tasks = ''' SELECT * FROM tasks; '''

projects = dbhelper.fetch(fetch_projects)
print(projects)

tasks = dbhelper.fetch(fetch_tasks)
print(tasks)