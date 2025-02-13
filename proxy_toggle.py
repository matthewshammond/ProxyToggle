# pip install rumps pyinstaller
# pyinstaller --noconsole --onefile --windowed --name=ProxyToggle --icon=ProxyToggle.icns --add-data "ProxyToggle.icns:." proxy_toggle.py
# pyinstaller --noconsole --onefile --windowed --name=ProxyToggle --icon=ProxyToggle.icns --add-data "ProxyToggle_on.icns:." --add-data "ProxyToggle_off.icns:." proxy_toggle.py
import rumps
import subprocess
import os

plist_path = os.path.expanduser("~/.pyenv/versions/ProxyToggle/bin/Info.plist")
if not os.path.exists(plist_path):
    subprocess.run(
        [
            "/usr/libexec/PlistBuddy",
            "-c",
            "Add :CFBundleIdentifier string 'rumps'",
            plist_path,
        ],
        check=False,
    )

PID_FILE = os.path.expanduser("~/.proxy_tunnel.pid")

# Define icon paths
ICON_ON = "ProxyToggle_on.icns"
ICON_OFF = "ProxyToggle_off.icns"


class ProxyToggleApp(rumps.App):
    def __init__(self):
        super(ProxyToggleApp, self).__init__("ProxyToggle", icon=ICON_OFF)
        self.menu = [rumps.MenuItem("Toggle Proxy", callback=self.toggle_proxy)]
        self.proxy_on = False

    def toggle_proxy(self, sender):
        if self.proxy_on:
            self.stop_proxy()
        else:
            self.start_proxy()

    def start_proxy(self):
        rumps.notification("Proxy Status", "Starting", "Enabling SOCKS proxy...")

        subprocess.run(
            ["networksetup", "-setsocksfirewallproxy", "Wi-Fi", "127.0.0.1", "8181"],
            check=True,
        )
        subprocess.run(
            ["ssh", "-fN", "-o", "ExitOnForwardFailure=yes", "-D", "8181", "apollo"]
        )

        # Grab the correct PID of the SSH process
        pid = (
            subprocess.check_output(
                ["pgrep", "-f", "ssh -fN -o ExitOnForwardFailure=yes -D 8181 apollo"]
            )
            .decode()
            .strip()
        )

        # Save the correct PID to the file
        with open(PID_FILE, "w") as f:
            f.write(pid)

        self.proxy_on = True
        self.icon = ICON_ON  # Change to "ON" icon
        rumps.notification("Proxy Status", "Active", "Proxy is now ON")

    def stop_proxy(self):
        rumps.notification("Proxy Status", "Stopping", "Disabling SOCKS proxy...")

        subprocess.run(
            ["networksetup", "-setsocksfirewallproxystate", "Wi-Fi", "off"], check=True
        )

        if os.path.exists(PID_FILE):
            with open(PID_FILE, "r") as f:
                pid = f.read().strip()

            # Check if the process is still running before killing it
            if (
                subprocess.run(["ps", "-p", pid], stdout=subprocess.PIPE).returncode
                == 0
            ):
                subprocess.run(
                    ["kill", "-9", pid], check=False
                )  # Use check=False to avoid exceptions
            else:
                print(f"Process {pid} not found, likely already stopped.")

            os.remove(PID_FILE)

        self.proxy_on = False
        self.icon = ICON_OFF  # Change to "OFF" icon
        rumps.notification("Proxy Status", "Inactive", "Proxy is now OFF")


if __name__ == "__main__":
    app = ProxyToggleApp()
    app.run()
