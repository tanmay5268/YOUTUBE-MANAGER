import json
import time
def loadvid() :
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file) #json.load ,file ke ander se jason format data ko python list me convert karta hai
            return test        
    except FileNotFoundError:
        return [] #agar file nahi hai to empty list return karega

def save_vid(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def listvid(videos):
    print("\n")
    print("="*70)
    if videos==[]:
        print("No videos in the list")
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']},duration:{video['time']}")
    print("="*70)
def addvid(videos):
    name= input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_vid(videos)
def updatevid(videos):
    listvid(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if index > 0 and index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1]['name'] = name
        videos[index-1]['time'] = time
        save_vid(videos)
    else :
        print("BHAI YE TO INDEX HI NAHI HAI ")

def deletevid(videos):
    listvid(videos)
    index = int(input("Enter the index of the video you want to delete: "))
    if index > 0 and index <= len(videos):
        del videos[index-1]
        save_vid(videos)
        for i in range(5):
            print(".",end = "")
            time.sleep(1)
        print("index",index,"deleted")       
    else:
        print("BHAI YE TO INDEX HI NAHI HAI ")

def main():
    videos = loadvid() #loading of list of info eg.name , time , links
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
