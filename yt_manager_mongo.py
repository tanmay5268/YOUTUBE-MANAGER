import pymongo
from pymongo import MongoClient
import pymongo.errors
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['yt_manager']
vid_collection = database['videos']
try:
    client.server_info()
    print('*'*50)
    print('connection succeseful')
    print('*'*50)
except pymongo.errors.ServerSelectionTimeoutError:
    print('somethimg went really wrong bro!!!!!!')
    exit()

def listvideos():
    videos= vid_collection.find()
    if vid_collection.count_documents({}) == 0:
        print("No videos found. Add some videos first!")
        return
        
    print("\n=== Your Videos ===")
    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    print("==================")
def addvideo(name,time):
    video_data={
        'name':name,'time':time
    }
    result=vid_collection.insert_one(video_data)
    print(f"Videos added with id:{result.inserted_id}")
def updatevideos(index,newname,newtime):
    try:
        object_id=ObjectId(index)
        result = vid_collection.update_one(
            {"_id":object_id},{"$set":{'name':newname,'time':newtime}}
              )
        if vid_collection.modified_count > 0:
            print(f"video id {index} updated succesfully")
        else:
            print(f"video id{index} not found!!!!")
        listvideos()
    except Exception as f:
        print(f"some error occured: {f}")

def main():
    print('\n')
    print('WELCOME TO MONGO--YT MANAGER')
    print('*'*50)
    while True:
        print('1.list all videos')
        print('2.add your videos')
        print('3.update existing videos')
        print('4.delete videos')
        print('5.exit from heaven :)')
        print('*'*50)
        choice=int(input('enter your choice:-'))
        print('*'*50)
        match choice:
            case 1 :
                listvideos()
            case 2 :
                name =input('ENTER NAME OF NEW VIDEO:')
                time =input('ENTER DURATION:')
                addvideo(name,time)
            case 3:
                listvideos()
                index= input('ENTER VIDEO INDEX U WANNA CHANGE BLUD:')
                newname = input('ENTER NEW NAME:')
                newtime = input('CHANGE TIME:')
                updatevideos(index,newname,newtime)
            case 4:
                listvideos()
                index= int(input('ENTER VIDEO INDEX U WANNA DELETE BLUD:')) 
                deletevideos()             
            case 5:
               break
            case _:
                print('U REALLY HAVE A SERIOUS PROBLEM BLUD ')
             

if __name__=="__main__":
    main()


    


