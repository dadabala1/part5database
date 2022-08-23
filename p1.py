import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user ="dadabala",
      password="123",
      host ="127.0.0.1",
      port="3307",
      database="showroom")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   print("...Execute database operations.....")
   # Execute database operations...

   my_cursor = cm_connection.cursor()

   player_query = ("SELECT showroom_id,showroom_name,location FROM showroom")

   my_cursor.execute(player_query)


   # Display results
   for row in my_cursor.fetchall():
      print("{}   {} {} ".format(row[0], row[1], row[2]))
   my_cursor.close()
   # displaying particular record
   customer_cursor = cm_connection.cursor()
   customer_query = ("SELECT showroom_id,showroom_name,location")
   customer_query += (" FROM showroom")
   customer_query += (" WHERE showroom_id = %s")

   rep_last = input("Enter showroom id ")

   rep_data = (rep_last,)  # Comma required for single value tuple
   customer_cursor.execute(customer_query, rep_data)
   for row in customer_cursor.fetchall():
      print("{} {} {} ".format(row[0], row[1], row[2]))
      customer_cursor.close()
      print("This is example is more complex. It uses functions, dictionaries and conditionals")
      # This is example is more complex. It uses functions, dictionaries and conditionals.

      import mysql.connector
      from mysql.connector import errorcode


      def get_status():
         statuses = {1: "APACHE", 2: "KTM", 3: "HERO"}
         for key in statuses:
            print("{}. {}".format(key, statuses[key]))
         status = int(input("Enter BRAND NAME or 0 for all orders: "))
         if 0 < status <= 3:
            return statuses[status]
         else:
            return "all"


      # main program

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
             user="dadabala",
             password="123",
             host="127.0.0.1",
             port="3307",
             database="showroom")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         brand = get_status()

         orders_cursor = cm_connection.cursor()
         orders_query = ("SELECT *")
         orders_query += ("FROM brand")

         if brand == "all":
            print("\n**All Orders**")
            print("{} {} {} {}".format("bike_id", "brand_name", "release_date","p_price"))
            print("-" * 77)
            orders_cursor.execute(orders_query)
            for (bike_id, brand_name, release_date,p_price) in orders_cursor:
               print("{} {} {} {}".format("bike_id", "brand_name", "release_date","p_price"), end="")
            # if shippedDate is None:
            #    print(" Not Shipped", end="")
            # else:
            #    print(" {:%m/%d/%Y} ".format(shippedDate), end="")
            print(" {}".format(brand_name))
         else:
            orders_query += (" WHERE brand_name = %s")
            status_data = (brand,)
            orders_cursor.execute(orders_query, status_data)
            print("\n**Status: {}**".format(brand))
            print("{} {} {} {}".format("bike_id", "brand_name", "release_date","p_price"))
            for (bike_id, brand_name, release_date,p_price) in orders_cursor:
               print("{} {} {} {}\n".format(bike_id, brand_name,release_date,p_price), end="",)
            # if shippedDate is None:
            #    print(" Not Shipped")
            # else:
            #    print(" {:%m/%d/%Y} ".format(shippedDate))

         orders_cursor.close()
         cm_connection.close()


   # Insert an bike mode
      print(".....Insert an bike....")
      import mysql.connector
      from mysql.connector import errorcode
      import random

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
             user="dadabala",
             password="123",
             host="127.0.0.1",
             port="3307",
             database="showroom")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         office_query = "SELECT bikeid,model_name,price FROM bikemode"
         office_cursor = cm_connection.cursor()
         office_cursor.execute(office_query)
         for row in office_cursor.fetchall():
            print("{}. {}".format(row[0], row[1]))
         office_cursor.close()

         bikeid = input("Enter bikeid ")
         model = input("Enter modelname: ")
         price = input("Enter price ")



         employee_query = ("INSERT INTO bikemode "
                           "(bikeid,model_name,price)"
                           "VALUES (%s, %s, %s)")

         employee_data = (bikeid,model,price)
         try:
            employee_cursor = cm_connection.cursor()
            employee_cursor.execute(employee_query, employee_data)
            cm_connection.commit()
            print("bike added")
            employee_cursor.close()
         except mysql.connector.Error as err:
          print("\nbike not added")
          print("Error: {}".format(err))
      cm_connection.close()
print("......Update bike.......")
# # Update an bike
import mysql.connector
from mysql.connector import errorcode


try:
   cm_connection = mysql.connector.connect(
       user="dadabala",
       password="123",
       host="127.0.0.1",
       port="3307",
       database="showroom")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   employee_last = input("Enter bikeid ")
   column = input("Enter item to update (bikeid,model_name,price) ")
   prompt = "Enter new value for {} ".format(column)
   value = input(prompt)

   employee_query = ("UPDATE bikemode "
                     "SET " + column + " =  %s "
                                       "WHERE bikeid = %s")
   employee_data = (value, employee_last)
   try:
      employee_cursor = cm_connection.cursor()
      employee_cursor.execute(employee_query, employee_data)
      cm_connection.commit()
      print("Updated bike")
      employee_cursor.close()
   except mysql.connector.Error as err:
    print("\nbike not updated")
    print("Error: {}".format(err))
    cm_connection.close()

   # Delete an bike
   print("Delete an bike")
   import mysql.connector
   from mysql.connector import errorcode

   # connect to DB
   try:
      cm_connection = mysql.connector.connect(
          user="dadabala",
          password="123",
          host="127.0.0.1",
          port="3307",
          database="showroom")

   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Invalid credentials")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database not found")
      else:
         print("Cannot connect to database:", err)

   else:
      employee_last = input("Enter bikeid to delete ")

      employee_query = ("DELETE FROM bikemode "
                        "WHERE bikeid = %s")
      employee_data = (employee_last,)
      try:
         employee_cursor = cm_connection.cursor()
         employee_cursor.execute(employee_query, employee_data)
         cm_connection.commit()
         print("Deleted bike")
         employee_cursor.close()
      except mysql.connector.Error as err:
         print("\nbike not deleted")
         print("Error: {}".format(err))
      cm_connection.close()

print(" connection Sucess!")
cm_connection.close()