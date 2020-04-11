import wakeonlan
import paramiko

def action(action):
    if action == "start":
        wakeonlan.send_magic_packet("00:08:9b:cf:ba:45")
        wakeonlan.send_magic_packet("00:08:9b:cf:ba:44")
    if action == "stop":
        sshconnection = paramiko.SSHClient()
        sshconnection.load_system_host_keys()
        sshconnection.connect("192.168.110.30", 22, "admin", "yIcrhUBmF0h6" )
        command == '/sbin/poweroff'
        sshconnection.exec_command(command)
        sshconnection.close


action(action = str (input("Do you want to start or stop NAS device?")))






