# Autodesk Inventor Discord Rich Presence

A lightweight, robust background application that automatically updates your Discord Rich Presence to show what you are actively designing in Autodesk Inventor!

## Features
- **Smart Window Scanning:** Uses Windows APIs (`EnumChildWindows`) to dig into Inventor's tabs and find exactly what file you are working on, bypassing Microsoft Store and UAC sandbox restrictions.
- **Activity Detection:** Automatically changes your status to "Making a Part", "Assembling", "2D Layouting", or "Creating Presentation" based on your active file extension (`.ipt`, `.iam`, `.dwg`, `.idw`, `.ipn`).
- **Auto-Elevation:** The launcher automatically requests Administrator privileges so Windows security doesn't block it from talking to Discord.
- **Bulletproof Reconnection:** Automatically reconnects if you close and reopen Inventor or Discord.

---

## 🛠️ How to Use

### 1. Requirements
- **Python 3.8+** installed on your system.
- **Autodesk Inventor** (Tested on 2027, but works on older versions).
- **Discord Desktop Client** running in the background.

### 2. Installation & Setup
1. Go to the **[Releases](../../releases/latest)** page on the right side of this GitHub repository.
2. Download the source code `.zip` file from the latest release and extract it anywhere on your computer.
3. Double-click the **`start_rpc.bat`** file.
4. It will automatically ask for Administrator privileges (this is required to securely communicate with Discord). Click Yes.
5. The script will automatically install the required Python libraries and launch!
6. Keep the black console window open in the background while you design.

*That's it! You do not need to create your own Discord Developer application or token. The script uses a pre-configured Client ID, so the official Autodesk Inventor name and logo will automatically appear on your Discord profile!*
