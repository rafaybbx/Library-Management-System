import mysql.connector as mysql

#Date
import datetime

tdate= datetime.date.today()


#variables
host = "localhost"
user = "root"
password = ""
#initializing our database
try:
    db = mysql.connect(host=host,user=user,password=password,database="library")
    print("Connected to library database succesfully")
except Exception as reason:
    print("Could not connect to library database")
    print(reason)
command_handler = db.cursor(buffered=True)



def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("")
        print("1.Register New Student")
        print("2.Delete existing Student")
        print("3.Register New Manager")
        print("4.Delete Existing Manager")
        print("5.Logout")


        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("REGISTER NEW STUDENT")
            print("")
            username = input(str("Create Username: "))
            password = input(str("Create Password: "))
            email = input(str("Enter Email: "))
            phone = input(str("Enter Phone Number: "))
            adress = input(str("Enter Adress: "))
            query_vals = (username,email,phone,password,adress)
            command_handler.execute("INSERT INTO users (username,email,phone,password,adress,privilage) VALUES (%s,%s,%s,%s,%s,'student')",query_vals)
            db.commit()
            print(username + " has been registered as a student")
        elif user_option == "3" :
                print("")
                print("REGISTER NEW MANAGER")
                username = input(str("Create Username: "))
                password = input(str("Create Password: "))
                phone = input(str("Enter Phone Number: "))
                email = input(str("Enter Email: "))
                adress = input(str("Enter Adress: "))
                query_vals = (username,email,phone,password,adress)
                command_handler.execute("INSERT INTO users (username,email,phone,password,adress,privilage) VALUES (%s,%s,%s,%s,%s,'manager')",query_vals)
                db.commit()
                print(username + " has been registered as a manager")
        elif user_option == "2":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student username: "))
            query_vals = (username,"student")
            command_handler.execute("DELETE FROM users WHERE username = %sAND privilage =%s ",query_vals)
            db.commit()
            if command_handler.rowcount <1 :
                print("User not found")
            else:
                print(username + "  has been removed as a student ")
        elif user_option == "4":
            print("")
            print("Delete Existing manager Account")
            username = input(str("manager username: "))
            query_vals = (username,"manager")
            command_handler.execute("DELETE FROM users WHERE username = %sAND privilage =%s ",query_vals)
            db.commit()
            if command_handler.rowcount <1 :
                print("User not found")
            else:
                print(username + "  has been removed as a manager")
        elif user_option == "5":
            break
        else :
            ("No Valid Option Selected")

def manager_session():
     while 1:
        print("")
        print("MANAGER'S MENU")
        print("")
        print("1.Add New Book")
        print("2.Remove Existing Book")
        print("3.Logout")

        user_option = input(str("Option: "))

        if user_option == "1":
            print("")
            print("ADD NEW BOOK")
            print("")
            bookname = input(str("Enter Book Name: "))
            author_name = input(str("Enter Author's Name: "))
            genre = input(str("Enter Book's Genre: "))

            query_vals = (bookname,author_name,genre)
            command_handler.execute("INSERT INTO books (name,author,genre) VALUES (%s,%s,%s)",query_vals)
            db.commit()
            print(bookname + "  has been added in the collection")
        elif user_option =="2":
            print("")
            print("REMOVE AN EXISTING BOOK")
            print("")
            bookname = input(str("Enter Book Name: "))
            query_vals = (bookname)
            command_handler.execute("DELETE FROM books WHERE name = %s",query_vals)
            db.commit()
            if command_handler.rowcount <1 :
                print("User not found")
            else:
                print(bookname + "  has been removed from the collection ")
        elif user_option == "3":
            break
        else:
            print("No Valid Option")

def student_session(username):
    while 1:
        print("")
        print("")
        print("********** Welcome To Students Section "+ username +" **********")
        print("")
        print("")
        print("Please Select One Of The Availabe Options...")
        print("")
        print("1.Search Books")
        print("2.Lend Book")
        print("3.Return Book")
        print("4.Logout")
        print("")
        user_option = input(str("Option: "))

        if user_option == "1":
            print("")
            print("")
            print("1.Search By Name")
            print("2.Search By Id")
            print("3.Search By Author")
            print("4.Search By Genre")
            print("5.Go Back")
            print("")
            print("")
            user_secondoption = input(str("Enter Option: "))

            if user_secondoption == "1":
                print("")
                print("Name Search")
                print("")
                book_name = input(str("Enter Book Name: "))
                book_name = (str(book_name),)
                command_handler.execute("SELECT Id, name, author ,genre  FROM books WHERE name =%s",book_name)
                records = command_handler.fetchall()

                if command_handler.rowcount <=0 :
                    print("")
                    print("")
                    print("Sorry, We dont have any match for your particular search.")

                else:
                    print("")
                    print("")
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")
                    print("")
                    print("The information about the book you searched is as follows: ")
                    print("")
                    print(record)

            elif user_secondoption == "2":
                print("")
                print("Id search")
                print("")
                book_Id = input(str("Enter Book Id: "))
                book_Id = (str(book_Id),)
                command_handler.execute("SELECT Id, name, author ,genre  FROM books WHERE id =%s",book_Id)
                records = command_handler.fetchall()
                if command_handler.rowcount <=0 :
                    print("")
                    print("")
                    print("Sorry, We dont have any match for your particular search.")

                else:
                    print("")
                    print("")
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")
                    print("")
                    print("The information about the book you searched is as follows: ")
                    print("")
                    print(record)

            elif user_secondoption == "3":
                print("")
                print("Author's Search")
                author_name = input(str("Enter Book Author: "))
                author_name = (str(author_name),)
                command_handler.execute("SELECT Id, name, author ,genre  FROM books WHERE author =%s",author_name)
                records = command_handler.fetchall()
                if command_handler.rowcount <=0 :
                    print("")
                    print("")
                    print("Sorry, We dont have any match for your particular search.")

                else:
                    print("")
                    print("")
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")
                    print("")
                    print("The information about the book you searched is as follows: ")
                    print("")
                    print(record)

            elif user_secondoption == "4":
                print("")
                print("Genre Search")
                print("")
                genre_name = input(str("Enter Genre: "))
                genre_name = (str(genre_name),)
                command_handler.execute("SELECT Id, name, author ,genre  FROM books WHERE genre =%s",genre_name)
                records = command_handler.fetchall()
                if command_handler.rowcount <=0 :
                    print("")
                    print("")
                    print("Sorry, We dont have any match for your particular search.")

                else:
                    print("")
                    print("")
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")
                    print("")
                    print("The information about the book you searched is as follows: ")
                    print("")
                    print(record)

            elif user_secondoption == "5":
                pass
            else:
                print("")
                print("Invalid input")





        if user_option =="2":                                             #the logic in this is that first we check wheather the book is present or not
                                                                          # then we check if the particular user has or hasnot already lended this book

            key =0
            print("")
            print("LEND BOOK MENU")
            print("")
            book_id = input("Enter Book Id: ")
            book_iid = (str(book_id),)

            #Getting the name of the book
            command_handler.execute("SELECT name from books WHERE id = %s",book_iid)
            records = command_handler.fetchone()

            #checking our database to see if we even have the requested book.
            if command_handler.rowcount <=0 :
                    print("")
                    print("")
                    print("Sorry, We dont have any match for your particular search.")

            else:
                #Getting the userid (user_fk) from name
                name= username
                name_for_id = (str(name),)
                command_handler.execute("SELECT id from users WHERE username = %s",name_for_id)
                user_id =command_handler.fetchone()
                for userid in user_id:
                    userid = str(userid).replace("'","")
                    userid = str(userid).replace(",","")
                    userid = str(userid).replace("(","")
                    userid = str(userid).replace(")","")

                query_vals = (str(userid),)


                #Getting all the books that the particular user already has lend by using the previously fetched id
                command_handler.execute("SELECT book_fk from lending WHERE user_fk = %s",query_vals)
                boks_id =command_handler.fetchall()
                for bookid in boks_id:
                    bookid = str(bookid).replace("'","")
                    bookid = str(bookid).replace(",","")
                    bookid = str(bookid).replace("(","")
                    bookid = str(bookid).replace(")","")



                    if bookid == book_id :

                        print("")
                        print("You have already lended this book.")
                        key = 1
                    else:
                        pass


                #Lending the book :)
                if key == 1 :
                    pass
                else:
                    print("")
                    print("")
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace(",","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")

                    bookname = record


                    userdays= float(input("Enter the number of days you want to lend the book: "))
                    print("")
                    if userdays > 30 :
                        print("")
                        print("You Cannot Lend For More Than 30 days")
                    else:
                        tdelta = datetime.timedelta(days=userdays)
                        finaldate =tdate+tdelta

                        name= username

                        name_for_id = (str(name),)
                        command_handler.execute("SELECT id from users WHERE username = %s",name_for_id)
                        user_id =command_handler.fetchone()
                        for userid in user_id:
                            userid = str(userid).replace("'","")
                            userid = str(userid).replace(",","")
                            userid = str(userid).replace("(","")
                            userid = str(userid).replace(")","")

                        for bookid in book_id:
                            bookid = str(bookid).replace("'","")
                            bookid = str(bookid).replace(",","")
                            bookid = str(bookid).replace("(","")
                            bookid = str(bookid).replace(")","")

                        query_vals = (userid,bookid,tdate,finaldate)
                        command_handler.execute("INSERT INTO lending (user_fk,book_fk,lending_date,returning_date) VALUES (%s,%s,%s,%s)",query_vals)
                        db.commit()

                        print(bookname +" Has Been Lended Succesfully For "+ str(userdays)+ "Days")
                        print("Retun The Book By "+ str(finaldate) +" Or You Will be Charged a Fine of Rs.100!")






        if user_option =="3":
            print("")
            print("RETURN BOOK MENU")
            book_Id = input(str("Enter Id: "))

            name= username
            name_for_id = (str(name),)
            command_handler.execute("SELECT id from users WHERE username = %s",name_for_id)
            user_id =command_handler.fetchone()
            for userid in user_id:
                userid = str(userid).replace("'","")
                userid = str(userid).replace(",","")
                userid = str(userid).replace("(","")
                userid = str(userid).replace(")","")

            query_vals = (userid,book_Id)
            command_handler.execute("DELETE FROM lending WHERE user_fk = %s AND book_fk =%s ",query_vals)
            db.commit()
            if command_handler.rowcount <=0 :
                print("")
                print("")
                print("book not found")

            else:
                print("")
                print("")
                print("Book has been returned succesfully")

                # command_handler.execute("SELECT returning_date from lending WHERE user_fk = %s AND book_fk =%s",query_vals)
                # records = command_handler.fetchone()

                # for record in records:
                #     record = str(record).replace("'","")
                #     record = str(record).replace(",","")
                #     record = str(record).replace("(","")
                #     record = str(record).replace(")","")
                #     record = str(record).replace("'","")

                # returningdate = records

                # print(returningdate)

                # if tdate > returningdate:
                #     print("")
                #     print("You have been fined for reuturning the book late")

                #     command_handler.execute("SELECT fine from lending WHERE user_fk = %s",userid)
                #     records =command_handler.fetchall()
                #     for record in records:
                #         record = str(record).replace("'","")
                #         record = str(record).replace(",","")
                #         record = str(record).replace("(","")
                #         record = str(record).replace(")","")
                #         record = str(record).replace("'","")

                #     fine = int(fine) + 100
                #     query_vals = (fine,userid)
                #     command_handler.execute("INSERT INTO lending (fine) VALUES (%s)  WHERE user_fk = %s",query_vals)
                #     db.commit()

                # else:
                #     pass

        if user_option =="4":
            break

        else:
            print("")
            ("Invalid Input")

def auth_manager():
    print(" ")
    print("MANAGER'S LOGIN")
    print(" ")
    username = input(str("Username: "))
    password = input(str("Password: "))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilage = 'manager'",query_vals)


    if command_handler.rowcount <=0:
        print("Login not recognized")
    else :
        print("Welcome to Managers's menu "+ username)
        manager_session()

def auth_admin():
    print(" ")
    print("ADMIN'S LOGIN")
    print(" ")
    username = input(str("Username: "))
    password = input(str("Password: "))
    if username == "rafay" :
        if password == "dada1234":
            admin_session()
        else:
            print("Incorrect Password")
    else:
        print("Welcome to Admin's menu "+ username)
        print("Invalid username")

def auth_student():
    print(" ")
    print("STUDENT'S LOGIN")
    print(" ")
    username = input(str("Username: "))
    password = input(str("Password: "))




    query_vals = (username,password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilage = 'student'",query_vals)

    if command_handler.rowcount <=0:
        print("Login not recognized")
    else :

        student_session(username)

def main():
    while 1 :
        print(" ")
        print(" ")
        print("**********Welcome to 002's Library Management System**********")
        print(" ")
        print("1. Login as student")
        print("2. Login as admin")
        print("3. Login as a manager")
        print("4. Exit")

        print("")
        user_option = input(str("Please select one of the following options: "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_admin()
        elif user_option == "3":
            auth_manager()
        elif user_option == "4":
            break
        else:
            print("")
            print("Invalid input.....please select one of the two above mentioned options")


main()

