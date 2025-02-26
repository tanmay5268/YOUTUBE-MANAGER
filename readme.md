# YouTube Manager

## Overview
The `youtube_main.py` script is a simple command-line application for managing a list of YouTube videos. It allows users to:

- View the list of saved videos
- Add new videos
- Update video details
- Delete videos
- Persist data using a JSON file (`youtube.txt`)

This application is written in Python and uses the `json` module to store and retrieve video details in a structured format.

---
## Features
### 1. Load Videos (`loadvid()`)
- Reads video data from `youtube.txt`.
- Uses JSON format to load and parse the data.
- Returns the list of videos.
- If the file does not exist, it returns an empty list.

### 2. Save Videos (`save_vid(videos)`)
- Saves the updated list of videos to `youtube.txt`.
- Uses JSON serialization to store the video details persistently.

### 3. List All Videos (`listvid(videos)`)
- Displays all saved videos along with their names and durations.
- Prints a message if the list is empty.

### 4. Add Video (`addvid(videos)`)
- Allows the user to input a video name and duration.
- Appends the new video to the list and saves it using `save_vid()`.

### 5. Update Video (`updatevid(videos)`)
- Displays the current list of videos.
- Prompts the user to select a video index to update.
- Updates the selected video's name and duration.
- Saves the updated list back to `youtube.txt`.
- If the input index is invalid, it prints an error message.

### 6. Delete Video (`deletevid(videos)`)
- Displays the list of saved videos.
- Prompts the user to enter the index of the video they want to delete.
- Removes the selected video from the list and updates the JSON file.
- Introduces a 5-second delay with a loading effect before confirming deletion.
- If an invalid index is entered, it prints an error message.

### 7. Main Menu (`main()`)
- Loads video data from `youtube.txt`.
- Displays a menu for the user to interact with the application.
- Provides options to list, add, update, delete, or exit the application.
- Uses Python's `match-case` for menu navigation.
- The program continues running until the user chooses to exit.

---
## JSON File (`youtube.txt`) and Its Importance
This script relies on a JSON file (`youtube.txt`) to store video data. JSON is used because:
- It provides a structured way to store data (key-value pairs).
- It ensures data persistence, allowing the program to remember saved videos even after it is closed.
- It is lightweight and easy to read and modify.

Each video entry in the JSON file follows this format:
```json
[
    {
        "name": "Sample Video",
        "time": "5:30"
    }
]
```

---
## How to Use the Script
### Running the Script
Make sure you have Python installed. Run the script using:
```bash
python youtube_main.py
```

### Menu Options
Once the script is running, you will see a menu like this:
```
HEY, Welcome to YOUTUBE Manager ------ select an option
1. List all videos
2. Add your fav videos
3. Update a YouTube video detail
4. Delete video/s
5. Exit the app
```
Enter a number corresponding to the action you want to perform.

### Example Usage
1. **Adding a Video**
   - Select option `2`.
   - Enter a video name: `Python Tutorial`.
   - Enter video time: `15:00`.
   - The video is saved and added to the list.

2. **Updating a Video**
   - Select option `3`.
   - Enter the index of the video to update.
   - Enter new details (name and time).

3. **Deleting a Video**
   - Select option `4`.
   - Enter the index of the video to delete.
   - The video is removed, and a loading effect is displayed before confirmation.

4. **Listing Videos**
   - Select option `1` to see all saved videos.

---
## Error Handling
- If `youtube.txt` is missing, `loadvid()` handles it by returning an empty list.
- If an invalid index is entered for update or delete, an error message is displayed.
- The script uses error handling for file operations to prevent crashes.

---
## Notes
- The script uses Hindi phrases in error messages (`BHAI YE TO INDEX HI NAHI HAI`, `BHAI OPTIONS NAHI DIKHTE KYA`) for a personalized touch.
- The script implements a simple CLI-based approach for easy user interaction.
- JSON ensures data persistence between runs.


---
## Conclusion
This script provides a simple yet effective way to manage a personal list of YouTube videos. By utilizing JSON for storage, it ensures that user data is retained across sessions. The well-structured functions make it easy to modify and expand upon the existing features.

