#coding:utf-8
import glob, sqlite3

def prepare_db(dbname):
   global conn
   global cur
   conn = sqlite3.connect(dbname)
   cur = conn.cursor()
   return conn, cur

def execute_sqls_all(dirname):
   fn_list = glob.glob(dirname + '/*.txt')
   for f in fn_list:
      ifile = open(f, 'r', encoding='utf-8')
      data = ifile.readlines()
      ifile.close()
      #set table name
      table_name = f[f.find('/') + 1:f.find('.txt')]

      sqls = []
      for i, line in enumerate(data):
         line = line.strip()
         if line == '' : continue
         cols = line.split('\t')

         if i == 0:
            f_cols = ['"'+ col + '"' for col in cols]
            tb_schema = ', '.join(f_cols)
            tb_schema += " Not Null, Primary Key (Album)"
            fields = ','.join(f_cols)
            f_sql = 'insert into ' + table_name + ' (' + fields + ') '
         
         else:
            v_cols = []
            for col in cols:
               col = col.replace('"', "'").replace("'",'\'')
               v_cols.append('"' + col + '"')
            values = ','.join(v_cols)
            v_sql = 'values (' + values + ')'
            sqls.append(f_sql + v_sql)
      
      tsql = 'create table if not exists %s (%s)' %(table_name, tb_schema)
      print(tsql)
      cur.execute(tsql)

      for sql in sqls:
         print("this is sql : ", sql)
         cur.execute(sql)
   conn.commit()

def select_with_condition(target, table, condition=''):
   if condition != '':
      cur.execute('select %s from %s where %s' %(target, table, condition))
   else:
      cur.execute('select %s from %s' %(target, table))
   conn.commit()
   rst = cur.fetchall()
   return rst

def select_union_with_condition(target, tables, condition=''): #tables=list
   temp = 0 #to distinguish first run with others
   for table in tables:
      #first run(without union)
      if temp == 0 and condition != '':
         union_execution = 'select %s from %s where %s' %(target, table,\
	 condition)
         temp = 1
      elif temp == 0:
         union_execution = 'select %s from %s' %(target, table)
         temp = 1
      #after first run(with union)
      elif temp == 1 and condition != '':
         union_execution += ' union select %s from %s where %s' %(target,\
	 table, condition)
      elif temp == 1:
         union_execution += ' union select %s from %s' %(target, table)
   
   cur.execute(union_execution)
    
   conn.commit()
   rst = cur.fetchall()
   return rst

if __name__ == "__main__":
   try:
      conn, cur = prepare_db('music.db')
      execute_sqls_all('music')
      conn.close()
   except Exception as e:
      print('\n')
      print(e)
