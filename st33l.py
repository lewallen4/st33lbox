import os
import subprocess

def create_ecdsa_key():
    log_file = "logs.log"
    key_path = "/etc/ssh/ssh_host_ecdsa_key"
    
    # Ensure the directory exists
    key_dir = os.path.dirname(key_path)
    if not os.path.exists(key_dir):
        os.makedirs(key_dir, exist_ok=True)
    
    # Creating ECDSA key
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Creating ECDSA key...\n")
    keygen_command = [
        "ssh-keygen",
        "-t", "ecdsa",               # Specify ECDSA key type
        "-b", "521",                 # Key length
        "-f", key_path,              # Output file
        "-N", "",                    # No passphrase
        "-q"                         # Quiet mode
    ]
    result = subprocess.run(keygen_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        if result.returncode == 0:
            f.write("#$#$#$#$#$ ECDSA key created successfully.\n")
        else:
            f.write("#$#$#$#$#$ Error creating ECDSA key.\n")
    
    return key_path

def is_ssh_connection():
    return "SSH_CONNECTION" in os.environ

def reconnect_ssh(new_key_path):
    user = "root"
    hostname = "localhost"
    
    # Add new key to the known hosts
    subprocess.run(["ssh-keygen", "-R", hostname], check=True)  # Remove old key
    subprocess.run(["ssh-keyscan", "-H", hostname], stdout=open(os.path.expanduser("~/.ssh/known_hosts"), "a"), check=True)

    # Reconnect using the new ECDSA key
    ssh_command = f"ssh -i {new_key_path} {user}@{hostname} 'echo Reconnected successfully with ECDSA key'"
    result = subprocess.run(ssh_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    with open("logs.log", "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Reconnected successfully with ECDSA key.\n")

def delete_old_keys(new_key_path):
    key_dir = os.path.dirname(new_key_path)
    new_key_name = os.path.basename(new_key_path)
    
    for key_file in os.listdir(key_dir):
        if key_file != new_key_name and key_file.startswith("ssh_host_") and key_file.endswith("_key"):
            try:
                os.remove(os.path.join(key_dir, key_file))
                os.remove(os.path.join(key_dir, key_file + ".pub"))  # Remove corresponding public key
                with open("logs.log", "a") as f:
                    f.write(f"#$#$#$#$#$ Deleted old key: {key_file}\n")
            except FileNotFoundError:
                continue

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
    result = subprocess.run(["sudo", "firewall-cmd", "--zone=public", "--add-rich-rule", "rule family='ipv4' source address='0.0.0.0/0' reject"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
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
    ecdsa_key_path = create_ecdsa_key()
    delete_old_keys(ecdsa_key_path)
    
    if is_ssh_connection():
        reconnect_ssh(ecdsa_key_path)
    
    harden_vm()
