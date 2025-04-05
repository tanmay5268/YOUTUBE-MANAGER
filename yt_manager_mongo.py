import pymongo
from pymongo import MongoClient
import pymongo.errors
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['yt_manager']
vid_collection = database['videos']
try:
    client.server_info()
    print('connection succeseful')
except pymongo.errors.ServerSelectionTimeoutError:
    print('somethimg went really wrong bro!!!!!!')
    exit()

def main():
    print('WELCOME TO MONGO--YT MANAGER')
    while True:
        print('1.list all videos')
        print('2.add your videos')
        print('3.update existing videos')
        print('4.delete videos')
        print('5.exit from heaven :)')
        choice=int(input('enter your choice:-'))
        match choice:
            case 1 :
                listvideos()
            case 2 :
                name =input('ENTER NAME OF NEW VIDEO:')
                time =int(input('ENTER DURATION:'))
                updatevideo(name,time)
            case 3:
                listvideos()
                index= int(input('ENTER VIDEO INDEX U WANNA CHANGE BLUD:'))
                newname = input('ENTER NEW NAME:')
                newtime = int(input('CHANGE TIME:'))
                updatevideos()
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


    


