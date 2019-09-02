import cx_Oracle
con=cx_Oracle.connect('system/cortana@127.0.0.1:1522/orcl')
#print(con.version)
cur=con.cursor()
a=1;
b=0;
c=cur.callproc('test1',[a,b])
print(c)

con.close()
