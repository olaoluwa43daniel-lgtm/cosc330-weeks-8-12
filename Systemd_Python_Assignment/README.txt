PYTHON PROGRAMS AND SYSTEMD SERVICES
Start here

This package contains two examples and a short explanation in Assignment_Explanation.txt.
Python 3 and Linux with a running systemd user manager are required.
No third-party Python packages are needed.

1. SET UP THE FILES
Extract the ZIP, open a terminal inside its Systemd_Python_Assignment folder,
and run:

    mkdir -p ~/systemd_python_assignment ~/.config/systemd/user
    cp simple_browser.py clock_daemon.py ~/systemd_python_assignment/
    cp browser_launcher.service clock_daemon.service ~/.config/systemd/user/
    systemctl --user daemon-reload

These are user services: use --user, without sudo.
The %h in ExecStart expands to your home directory.
The services are not enabled automatically at login.

2. EXAMPLE 1: OPEN A BROWSER
Use a terminal inside your logged-in Linux graphical desktop session:

    systemctl --user import-environment DISPLAY WAYLAND_DISPLAY XAUTHORITY
    systemctl --user start browser_launcher.service
    systemctl --user status browser_launcher.service --no-pager
    journalctl --user -u browser_launcher.service -n 20 --no-pager

Only variables present in your terminal can be imported; a warning about an
unset variable is possible. A working default graphical browser is required.
If the desktop environment is unavailable, this example cannot show a window.
It is not intended for a headless server or a browser-only CoCalc terminal.

Expected behavior (not a recorded result): a browser requests python.org.
Type=oneshot is used because the script launches the browser and exits.
After a successful run, inactive (dead) with an exit status of 0 is normal.
The browser window belongs to the desktop; stopping this finished launcher
does not close the window.

3. EXAMPLE 2: RUN THE BACKGROUND CLOCK
    systemctl --user start clock_daemon.service
    systemctl --user status clock_daemon.service --no-pager
    journalctl --user -u clock_daemon.service -n 20 --no-pager
    systemctl --user restart clock_daemon.service
    systemctl --user stop clock_daemon.service
    journalctl --user -u clock_daemon.service -n 20 --no-pager

Expected behavior (not a recorded result): the service becomes active (running),
status shows its latest time, and the journal records a time every five seconds.
Stopping it sends SIGTERM; the program sends STOPPING=1 and exits cleanly.

Optional: enable ONLY the clock to start with the user manager:
    systemctl --user enable clock_daemon.service
Undo that and stop it:
    systemctl --user disable --now clock_daemon.service

4. WHAT TO SHOW YOUR PROFESSOR
The package provides the code, service definitions, and explanation.
If demonstration evidence is required, run both examples on your Linux
computer and add your own screenshots of the browser, service status,
and journal output. Test_Results.txt states exactly what was checked here.

5. COMMON PROBLEMS
- "System has not been booted with systemd" or "Failed to connect to bus":
  use a Linux machine/VM with systemd and an active user login session.
- Missing script: check that the .py files are under
  ~/systemd_python_assignment/ exactly as shown.
- Permission denied: ensure the files are readable by your user.
- Browser fails: try python3 ~/systemd_python_assignment/simple_browser.py
  directly in your desktop terminal and check your default browser.
- A service file was edited: run systemctl --user daemon-reload again.
