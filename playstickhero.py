
#import python adb library
from ppadb.client import Client as ADB
import subprocess



#connect to the device through the adb bridge. default is host=127.0.0.2 and port = 5037

client = ADB(host="127.0.0.1", port=5037)
devices = client.devices()
if not devices:
    print("No devices connected.")
device = devices[0]
#print(device.serial)

#open the stick hero app
package_name = "com.ketchapp.stickhero"
launcher_name = "org.cocos2dx.cpp.AppActivity"

#define adb console commands as a list to run as a subprocess
adb_process = ["adb", "shell", "sh", "-c", f"ps | grep {package_name}"]
abd_launch = ["adb","shell", "am", "start", "-n",f"{package_name}/{launcher_name}"]

#function to check if app status. need to launch if it is not running, open if current status = sleep, nothing if open
def app_running(package_name):
    sps_output = subprocess.check_output(adb_process, text=True)
    if sps_output == "":
        return False
    return True
 
    
apprunoutput = app_running(package_name)
print("the app is running: ", apprunoutput)
    
#check if app is running
if not app_running(package_name):
    try: #launch adb shell, start app by passing "package name/MainActivity"
        subprocess.run(abd_launch)
        print("Launch")
    except subprocess.CalledProcessError:
        print("App is running")




x,y = 500, 500
time_ms = 350

device.shell(f"{x} {y} {x} {y} {time_ms}")
