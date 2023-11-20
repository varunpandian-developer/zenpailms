import psycopg2

class CourseDatabase:
    def execute(self, query):
        result = []
        try:
            # Connect to the database
            con = psycopg2.connect(
                host="localhost",
                database="zenpaisolutions",
                user="postgres",
                password="admin"
            )

            cursor = con.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
           #print(rows)

            for row in rows:
                row_data=dict()
                for index, value in enumerate(row):
                    columnname=cursor.description[index].name
                    row_data[columnname]=value
                result.append(row_data)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            
        finally:
            # Close the cursor and connection, regardless of success or failure
            if 'cursor' in locals():
                cursor.close()
            if 'con' in locals():
                con.close()

        return result
    
#db = CourseDatabase()

#print(db.execute("SELECT * FROM coursedetails"))