# Autodesk Inventor Discord Rich Presence

A lightweight, robust background application that automatically updates your Discord Rich Presence to show what you are actively designing in Autodesk Inventor!

## Features
- **Smart Window Scanning:** Uses Windows APIs (`EnumChildWindows`) to dig into Inventor's tabs and find exactly what file you are working on, bypassing Microsoft Store and UAC sandbox restrictions.
- **Activity Detection:** Automatically changes your status to "Making a Part", "Assembling", "2D Layouting", or "Creating Presentation" based on your active file extension (`.ipt`, `.iam`, `.dwg`, `.idw`, `.ipn`).
- **Auto-Elevation:** The launcher automatically requests Administrator privileges so Windows security doesn't block it from talking to Discord.
- **Bulletproof Reconnection:** Automatically reconnects if you close and reopen Inventor or Discord.

---

## 🛠️ Setup Instructions (For You and Others)

### 1. Requirements
- Python 3.8+ installed on your system.
- Autodesk Inventor (Tested on 2027, but works on older versions).
- Discord Desktop Client.

### 2. Installation
1. Clone or download this repository to your computer.
2. Double-click the **`start_rpc.bat`** file.
3. It will automatically ask for Administrator privileges (click Yes).
4. It will install the required Python libraries (`pypresence` and `pywin32`) automatically.
5. The script will run in the background! Keep the black console window open while you work.

---

## ⚙️ Discord Developer Portal Guide (For the Repo Owner)

If you are hosting this code, here is exactly how you need to set up your Discord Application in the [Discord Developer Portal](https://discord.com/developers/applications) so it looks perfectly professional:

### General Information Tab
- **App Icon:** Upload the Autodesk Inventor square logo here.
- **Name:** `Autodesk Inventor` *(This is the large, bold text that appears at the top of the Discord status)*.
- **Description:** A custom Rich Presence integration for Autodesk Inventor.

### Rich Presence -> Art Assets Tab
- Click **Add Image(s)**.
- Upload a high-quality, square Autodesk Inventor logo.
- **CRITICAL:** Name the uploaded image exactly **`inventor_logo`** (all lowercase, no spaces). This is the key the script looks for to display the image next to your file name.

*Note: The Client ID is currently hardcoded in the script. Because of this, anyone who downloads your GitHub repo can use your exact setup without having to create their own Developer Application! If you delete your Developer App in the future, the integration will stop working for everyone.*
