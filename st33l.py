import subprocess

def harden_vm():
    log_file = "logs.log"
    
    # Resetting firewall rules
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Resetting firewall rules...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--complete-reload"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Successfully reset firewall rules.\n")
    
    # Denying all incoming connections by default
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all incoming connections by default...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--zone=public", "--add-rich-rule", "'rule family='ipv4' source address='0.0.0.0/0' reject'"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming connections denied.\n")
    
    # Allowing SSH (port 22) connections
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing SSH (port 22) connections...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--zone=public", "--add-port=22/tcp", "--permanent"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming SSH connections allowed.\n")
    
    # Allowing Git (port 9418) connections
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing Git (port 9418) connections...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--zone=public", "--add-port=9418/tcp", "--permanent"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming Git connections allowed.\n")
    
    # Allowing HTTP (port 80) connections
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing HTTP (port 80) connections...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--zone=public", "--add-port=80/tcp", "--permanent"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming HTTP connections allowed.\n")
    
    # Allowing HTTPS (port 443) connections
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing HTTPS (port 443) connections...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--zone=public", "--add-port=443/tcp", "--permanent"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming HTTPS connections allowed.\n")
    
    # Enabling firewall
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Enabling firewall...\n")
    result = subprocess.run(["sudo", "firewall-cmd", "--reload"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Firewall enabled.\n")
    
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Firewall hardened successfully.\n")

if __name__ == "__main__":
    harden_vm()
