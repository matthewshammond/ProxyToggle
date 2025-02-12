🚀 ProxyToggle - macOS SOCKS Proxy & SSH Tunnel Toggle

A macOS menu bar app that allows you to easily toggle a SOCKS proxy and SSH tunnel on and off. Built with Python and Rumps, packaged into a .app using PyInstaller.

📌 Features

✅ One-click toggle for SOCKS proxy & SSH tunnel
✅ Runs in the macOS menu bar for easy access
✅ Automatically detects & kills the correct SSH process
✅ Option to auto-launch at login
✅ Fully packaged as a .app for macOS


🔧 Installation

1️⃣ Install Dependencies

You’ll need Python 3.12+ and PyInstaller:

`pip install -r requirements.txt`

2️⃣ Build the App

Run the following command to package ProxyToggle.app:
`pyinstaller --noconsole --onefile --windowed --name=ProxyToggle --icon=ProxyToggle.icns --add-data "ProxyToggle.icns:." proxy_toggle.py`

The app will be available in the dist/ folder.

3️⃣ Move to Applications Folder
`mv dist/ProxyToggle.app /Applications/`

🚀 Usage

🔹 Start ProxyToggle

Run manually via:
`/Applications/ProxyToggle.app/Contents/MacOS/ProxyToggle &`
or:
`nohup /Applications/ProxyToggle.app/Contents/MacOS/ProxyToggle > /dev/null 2>&1 &`


🔹 Toggle Proxy

Click the menu bar icon to enable/disable the SOCKS proxy.

🛠 Built With
	•	Python 3.12
	•	Rumps (menu bar app framework)
	•	PyInstaller (to package as .app)

💡 Future Improvements

🚀 Add status indicators for SSH connection
🚀 Auto-detect network changes and re-enable proxy
🚀 Customizable proxy & SSH settings
🚀 Allow app to work when not initialized from the commandline
🚀 Integrate the plist file

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Matt Hammond
🔗 matthammond.com
