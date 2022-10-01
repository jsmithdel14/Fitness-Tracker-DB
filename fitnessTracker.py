import sqlite3
# Creating connections and global variables
conn = sqlite3.connect('fitness.db')
cursor = conn.cursor()
choice = None

# Create table (if it does not already exist)
cursor.execute("""CREATE TABLE IF NOT EXISTS fitness (
    name text,
    date text,
    time real,
    workout text,
    calories integer, 
    sleep real)""")
# get_row function selects all the data from a certain row
def get_row(cursor):
    cursor.execute("""SELECT name, date, time, workout, calories, sleep 
                  FROM fitness""")
    results = cursor.fetchall()
    
    for index in range(len(results)):
      print(f"{index+1}. {results[index]}")
    choice = int(input("Select> "))
    return results[choice-1]
# get_workout returns the top column workout based on the workout with lowest count
def get_workout(cursor):
  user_name = input('Enter your name: ')
  
  # Step 1 ask for users name 
  # Step 2 query all data under users name
  # Step 3 count the total times of each workout, recommend the least done workout
  cursor.execute("""
                SELECT name, workout, COUNT(workout) total_workout, AVG(time)
                FROM fitness
                WHERE name = '{user_name}'
                GROUP BY name, workout
                ORDER BY total_workout ASC""".format(user_name=user_name.capitalize()))
  print()
  print(f"Here is all your results {user_name.capitalize()}:")
  print("{:>10}  {:>10}  {:>10}  {:>10}".format("Name",       
  "Workout","Count","Average Time"))
  results = cursor.fetchall()
# for loop is printing the results
  for record in results:
    print("{:>10}  {:>10}  {:>10}  {:>10}".format(record[0], 
    record[1], record[2], record[3]))

  print()
  return results[0][1]
    
while choice != "6":
    # user menu display, type the number you want to do
    print("1. Display Past Days")
    print("2. Add Day")
    print("3. Update Past Day")
    print("4. Delete Past Day")
    print("5. Tell Me What To Do Today")
    print("6. Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display past results
        cursor.execute("SELECT * FROM fitness")
        
        print("{:>10}  {:>10}  {:>10}  {:>10}  {:>10}  {:>10}".format("Name", "Date", "Time", "Workout", "Calories", "Sleep"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}  {:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2], record[3], record[4], record[5]))

    elif choice == "2":
      
        # Add New Day
      try: 
        name = input("Name: ")
        date = input("Date: ")
        time = float(input("Time(mins): "))
        exercise = input("Exercise('chest','shoulders','legs','back','cardio','arms'): ")
        calories = int(input("Calories: "))
        sleep = float(input("Sleep(hrs): "))
        values = (name.capitalize(),date,time,exercise,calories,sleep)
        cursor.execute("INSERT INTO fitness VALUES (?,?,?,?,?,?)",values)
        conn.commit()
      except ValueError:
        print("not valid input")

    elif choice == "3":
        # Update Day
        # Choosing the column to be updated
        choice = input("What would you like to update?(column name) ")
        
        # Changing the choice/update
        if choice == 'name':
        # Using function to get values for each variable
        # Then use each variable as a where condition
        # I use this same block of code for each column
        # Should turn into a function
          row = get_row(cursor)
          name = row[0]
          date = row[1]
          time = row[2]
          workout = row[3]
          calories = row[4]
          sleep = row[5]
          update_item = input("Name: ")
          value = (update_item,name,date,time,workout,calories,sleep)
          cursor.execute("""
            UPDATE fitness 
            SET name = ? 
            WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",value)
          if cursor.rowcount == 0:
            print('Name does not exist')
          conn.commit()

          
        elif choice == "date":
        # Using function to get values for each variable
        # Then use each variable as a where condition
          row = get_row(cursor)
          name = row[0]
          date = row[1]
          time = row[2]
          workout = row[3]
          calories = row[4]
          sleep = row[5]
          update_item = input("Date: ")
          value = (update_item,name,date,time,workout,calories,sleep)
          cursor.execute("""
            UPDATE fitness 
            SET date = ? 
            WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",value)
          if cursor.rowcount == 0:
            print('Name does not exist')
          conn.commit()
          
        elif choice == 'time':
        # Using function to get values for each variable
        # Then use each variable as a where condition
          row = get_row(cursor)
          name = row[0]
          date = row[1]
          time = row[2]
          workout = row[3]
          calories = row[4]
          sleep = row[5]
          update_item = input("Time: ")
          value = (update_item,name,date,time,workout,calories,sleep)
          cursor.execute("""
            UPDATE fitness 
            SET time = ? 
            WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",value)
          if cursor.rowcount == 0:
            print('Name does not exist')
          conn.commit()

          
        elif choice == 'exercise':
        # Using function to get values for each variable
        # Then use each variable as a where condition
          row = get_row(cursor)
          name = row[0]
          date = row[1]
          time = row[2]
          workout = row[3]
          calories = row[4]
          sleep = row[5]
          update_item = input("Workout: ")
          value = (update_item,name,date,time,workout,calories,sleep)
          cursor.execute("""
            UPDATE fitness 
            SET workout = ? 
            WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",value)
          if cursor.rowcount == 0:
            print('Name does not exist')
          conn.commit()

          
        elif choice == 'calories':
        # Using function to get values for each variable
        # Then use each variable as a where condition
          row = get_row(cursor)
          name = row[0]
          date = row[1]
          time = row[2]
          workout = row[3]
          calories = row[4]
          sleep = row[5]
          update_item = input("Calories: ")
          value = (update_item,name,date,time,workout,calories,sleep)
          cursor.execute("""
            UPDATE fitness 
            SET calories = ? 
            WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",value)
          if cursor.rowcount == 0:
            print('Name does not exist')
          conn.commit()

          
        elif choice == 'sleep':
        # Using function to get values for each variable
        # Then use each variable as a where condition
          row = get_row(cursor)
          name = row[0]
          date = row[1]
          time = row[2]
          workout = row[3]
          calories = row[4]
          sleep = row[5]
          update_item = input("Sleep: ")
          value = (update_item,name,date,time,workout,calories,sleep)
          cursor.execute("""
            UPDATE fitness 
            SET sleep = ? 
            WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",value)
          if cursor.rowcount == 0:
            print('Name does not exist')
          conn.commit()

          
        else:
          print("invalid choice")
        

    elif choice == "4":
        # Delete employee
        # Using function to get values for each variable
        # Then use each variable as a where condition
        row = get_row(cursor)
        name = row[0]
        date = row[1]
        time = row[2]
        workout = row[3]
        calories = row[4]
        sleep = row[5]
        values = (name,date,time,workout,calories,sleep)
        cursor.execute("""DELETE FROM fitness WHERE name = ? 
            AND date = ?
            AND time = ?
            AND workout = ?
            AND calories = ?
            AND sleep = ?""",values)
        conn.commit()
    

    elif choice == "5":
        # Telling what the user should do based on their name
        print(f"You should do {get_workout(cursor)} today!")
        print()
        
  
# Close the database connection before exiting
conn.close()