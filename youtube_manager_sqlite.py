import sqlite3
conn = sqlite3.connect('videos.db')
cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )

''')
def lstvid():
    cursor.execute("SELECT * FROM videos")
    for i in cursor.fetchall():
        print(i)
def addvid(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    conn.commit()
def updatevid(id,name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name,time,id))
    conn.commit()
def deletevid(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()



def main():
    while True:
        print("\n HEY,Welcome to YOUTUBE Manager with DB------select an option")
        print("1. List all videos")
        print("2. Add your fav videos")
        print("3. update a youtube video details")
        print("4. Delete video/s")
        print("5. Exit the app")
        option = input("what's your option?---")
        if option =="1":
            lstvid()
        elif option == "2":
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            addvid(name,time)
        elif option == "3":
            id = input("Enter the id of the video: ")
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            updatevid(id ,name,time)
        elif option == "4":
            id = input("Enter the id of the video: ")
            deletevid(id)
        elif option == "5":
            break
        else:
            print("Invalid option, please select a valid option")
    
    conn.close()
        
if __name__ =="__main__":
    main()