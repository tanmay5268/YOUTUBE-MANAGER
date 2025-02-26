def listvid(videos):
    pass
def addvid(videos):
    pass
def updatevid():
    pass
def deletevid(videos):
    pass
def main():
    while True:
        print("\n HEY,Welcome to YOUTUBE Manager------select an option")
        print("1. List all videos")
        print("2. Add your fav videos")
        print("3. update a youtube video details")
        print("4. Delete video/s")
        print("5. Exit the app")
        option = input("what's your option?---")
        match option:
            case '1':
                listvid(videos)
            case '2':
                addvid(videos)
            case '3':
                updatevid(videos)
            case '4':
                deletevid(videos)
            case '5':
                break
            case _:
                print("\nBHAI OPTIONS NAHI DIKHTE KYA")
if __name__ == "__main__":
    main()

