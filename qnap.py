import wakeonlan
import paramiko

def action(action):
    if action == "start":
        print("Sending Start Signal")
        wakeonlan.send_magic_packet("00:08:9b:cf:ba:45")
        wakeonlan.send_magic_packet("00:08:9b:cf:ba:44")
    elif action == "stop":
        print("Sending Stop Signal")
        sshconnection = paramiko.SSHClient()
        sshconnection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshconnection.connect("192.168.110.30", 22, "admin", "yIcrhUBmF0h6" )
        command == '/sbin/poweroff'
        sshconnection.exec
    else:
        print("Unknown Command")

action(input("Do you want to start or stop NAS device? "))





