#coding:utf-8
import sqlite3
import sys

def prepare_db(dbname):
   global conn
   global cur
   conn = sqlite3.connect(dbname)
   cur = conn.cursor()
   return conn, cur

def insert_txt2table(txtfn, table_name, key_const=''):
   ifile = open(txtfn, 'r', encoding='utf-8')
   lines = ifile.read().split('\n')
   ifile.close()

   #to make a table schema to create a table
   schema_line = lines[0]
   cols = schema_line.split('\t')
   #to make field names
   f_cols = ['"' + col.split(':')[0] + '"' for col in cols]
   #to make field types
   t_cols = [col.split(':')[1] for col in cols]
   x = len(f_cols)
   f_names_types = [f_cols[i] + ' ' + t_cols[i] for i in range(x)]
   tbl_schema = ','.join(f_names_types)
   #to reset data
   tsql = 'create table %s (%s %s)' %(table_name, tbl_schema, key_const)
   print(tsql)
   cur.execute(tsql)

   #to make every insert into table_name(field...) values(value...)
   f_sql = 'insert into ' + table_name + ' (' + ','.join(f_cols) + ') '
   sqls = []
   for i, line in enumerate(lines[1:]):
      if line == '' : continue
      cols = line.split('\t')
      val_on_type = lambda val, ftype: '"' + val + '"' if ftype == 'text'\
      else val
      v_cols = [val_on_type(col, t_cols[i]) for i, col in enumerate(cols)]
      v_sql = 'values (' + ','.join(v_cols) + ')'
      sqls.append(f_sql + v_sql)

   for sql in sqls:
      print(sql)
      cur.execute(sql)
   conn.commit()

def select_info_by_name(name):
   cur.execute('select names."Student ID", names.Name, \
   infos.department from names Join infos on \
   names."Student ID" = infos."Student ID"')
   cur.execute('select names.name, infos.department from names \
   join infos on names."Student ID" = infos."Student ID" where \
   names.name = '+ "'" + name + "'")
   conn.commit()
   rst = cur.fetchall()
   return rst

if __name__ == "__main__":
   try:
      prepare_db('students.sqlite3')
      insert_txt2table('student_name.txt', 'names',\
      ', Primary Key ("Student ID")')
      insert_txt2table('student_info.txt', 'infos',\
      ', Foreign Key ("Student ID") references names("Student ID")')
      print("\n<select_info_by_name>\n")
      print(select_info_by_name('정어진'))
      conn.close()
   except Exception as e:
      print(e, file=sys.stderr)

