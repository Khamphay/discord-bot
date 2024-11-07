# Initialize 
### 1. Update and upgrade package (Only for Linux and macOS)
``` cmd
sudo apt update && sudo apt upgrade -y
```

### 2.Install Python (Only for Linux and macOS)
``` cmd
sudo apt install python3 python3-pip python3-venv -y
```

### 3. Create virtual environment
``` cmd
cd /path/to/your/bot_project
python3 -m venv venv
source .venv/bin/activate 
# or . .venv/bin/activate
```

### 4. Install Package
``` cmd
pip install -r requirements.txt
```

---
# Configure for run Bot as the service
## For Linux (systemd)

### 1. Create file service
``` cmd
sudo nano /etc/systemd/system/discord-bot.service
```

After that, Copy and paste this command:
``` wsgi
[Unit]
Description=Discord Bot Service
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/path/to/your/bot_project
Environment=PYTHONPATH=/path/to/your/bot_project
ExecStart=/path/to/your/venv/bin/python main.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

### 2. Enable and start service
``` cmd
sudo systemctl enable discord-bot.service
sudo systemctl start discord-bot.service
```

### 3. Check status service
``` cmd
sudo systemctl status discord-bot.service
```

### 4. Check log service
``` cmd
sudo journalctl -u discord-bot.service
```

---
## For Windows (batch)
### 1. Create a batch file (e.g., start-bot.bat) and paste below code:
``` batch
@echo off
cd /d "C:\path\to\your\bot_project"
"C:\path\to\your\venv\Scripts\python.exe" main.py
pause
```

### 2. Use Task Scheduler:
- Open Task Scheduler
- Create Basic Task
- Name it "Discord Bot"
- Trigger: "When computer starts"
- Action: Start a program
- Program/script: Select your batch file
- Check "Run with highest privileges"
- Set "Run whether user is logged in or not"

### 3. Check log service
- Windows: Check Event Viewer

---
## For macOS
### 1. Create a plist file and paste below code:
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.discord.bot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/your/venv/bin/python</string>
        <string>/path/to/your/bot_project/main.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>/path/to/your/bot_project</string>
    <key>StandardErrorPath</key>
    <string>/tmp/discord-bot.err</string>
    <key>StandardOutPath</key>
    <string>/tmp/discord-bot.out</string>
</dict>
</plist>
```

### 2. Load the service
``` cmd
sudo launchctl load /path/to/your/plist/file
```

### 3. Check log service
- macOS: Check `/tmp/discord-bot.err` and `/tmp/discord-bot.out`
