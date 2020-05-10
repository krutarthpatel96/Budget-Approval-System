import cx_Oracle as c

conn = c.connect("system/2824@localhost/xe")

cur=conn.cursor()

print("1. Insert")
print("2. Delete")
print("3. Update")
print("4. Select")
print("5. Truncate")
print("6. Exit")

while True:

    ch=int(input("\nEnter your choice : "))

    if ch==4:
        cur.execute("select * from employee")
        print(cur.fetchall())
        cur.execute("select * from manager")
        print(cur.fetchall())
        cur.execute("select * from requests")
        if(str(cur)=='None'):
            print("Empty")
        else:
            print(cur.fetchall())
            print('total records : '+str(cur.rowcount))

    elif ch==5:
        cur.execute("Truncate table stu_info");
        print("Truncated!")

    elif ch==6:
        break;

    else:
        print("Invalid Choice!")
        
    conn.commit()
conn.commit()
conn.close()
