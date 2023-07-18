
def find_Chromium():
    import subprocess

    find = "whereis chromedriver"
    cmd = find.split()
    print(cmd)

    return subprocess.run([cmd], shell=True, capture_output=True, text=True)
