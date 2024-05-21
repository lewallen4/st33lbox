import os
import subprocess

def harden_vm():
    log_file = "firewall/logs.log"
    
    def run_command(command, description):
        message = f"#$#$#$#$#$ {description}..."
        print(message)
        with open(log_file, "a") as f:
            f.write(message + "\n")
        
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print(result.stdout)
        with open(log_file, "a") as f:
            f.write(result.stdout + "\n")
        
        if result.returncode == 0:
            success_message = f"#$#$#$#$#$ {description} successful."
            print(success_message)
            with open(log_file, "a") as f:
                f.write(success_message + "\n")
        else:
            error_message = f"#$#$#$#$#$ {description} failed. Error: {result.stderr}"
            print(error_message)
            with open(log_file, "a") as f:
                f.write(error_message + "\n")

    # Resetting firewall rules
    run_command(["sudo", "firewall-cmd", "--complete-reload"], "Resetting firewall rules")
    
    # Denying all incoming connections by default
    run_command(["sudo", "firewall-cmd", "--zone=public", "--add-rich-rule", "rule family='ipv4' source address='0.0.0.0/0' reject"], "Denying all incoming connections by default")
        
    # Allowing Git (port 9418) connections
    run_command(["sudo", "firewall-cmd", "--zone=public", "--add-port=9418/tcp", "--permanent"], "Allowing Git (port 9418) connections")
    
    # Allowing openSSL (port 9812) connections
    run_command(["sudo", "firewall-cmd", "--zone=public", "--add-port=9812/tcp", "--permanent"], "Allowing SSL (port 9812) connections")
    
    # Allowing HTTP (port 80) connections
    run_command(["sudo", "firewall-cmd", "--zone=public", "--add-port=80/tcp", "--permanent"], "Allowing HTTP (port 80) connections")
    
    # Allowing HTTPS (port 443) connections
    run_command(["sudo", "firewall-cmd", "--zone=public", "--add-port=443/tcp", "--permanent"], "Allowing HTTPS (port 443) connections")
    
    # TEMP Allowing SSH (port 22) connections
    run_command(["sudo", "firewall-cmd", "--zone=public", "--add-port=22/tcp", "--permanent"], "Allowing HTTP (port 22) connections")
    
    # Enabling firewall
    run_command(["sudo", "firewall-cmd", "--reload"], "Enabling firewall")
    
    final_message = "#$#$#$#$#$ Firewall hardened successfully."
    print(final_message)
    with open(log_file, "a") as f:
        f.write(final_message + "\n")
        
def openSSL():
    log_file = "logs.log"
    
    def run_command(command, description):
        message = f"#$#$#$#$#$ {description}..."
        print(message)
        with open(log_file, "a") as f:
            f.write(message + "\n")
        
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print(result.stdout)
        with open(log_file, "a") as f:
            f.write(result.stdout + "\n")
        
        if result.returncode == 0:
            success_message = f"#$#$#$#$#$ {description} successful."
            print(success_message)
            with open(log_file, "a") as f:
                f.write(success_message + "\n")
        else:
            error_message = f"#$#$#$#$#$ {description} failed. Error: {result.stderr}"
            print(error_message)
            with open(log_file, "a") as f:
                f.write(error_message + "\n")

    # moving to ssl directory
    os.chdir("ssl")
    
    # Resetting firewall rules
    run_command(["sudo", "bash", "server.sh"], "Creating SSL certificate then starting listen server")
    
    # Resetting firewall rules
    run_command(["echo", "'open'"], "Opening SSL tunnel")
        
    final_message = "#$#$#$#$#$ Server Online"
    print(final_message)
    with open(log_file, "a") as f:
        f.write(final_message + "\n")

harden_vm()
openSSL()