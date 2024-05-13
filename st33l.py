import subprocess

def harden_vm():
    log_file = "logs.log"
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Resetting firewall rules...\n")
    result = subprocess.run(["sudo", "ufw", "--force", "reset"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Successfully reset firewall rules.\n")
        
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all incoming connections by default...\n")
    result = subprocess.run(["sudo", "ufw", "deny", "out", "1:65535/tcp"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing tcp connections denied.\n")
                
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all incoming connections by default...\n")
    result = subprocess.run(["sudo", "ufw", "deny", "out", "1:65535/udp"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing udp connections denied.\n")
                
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all incoming connections by default...\n")
    result = subprocess.run(["sudo", "ufw", "deny", "in", "1:65535/tcp"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming tcp connections denied.\n")
                
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all incoming connections by default...\n")
    result = subprocess.run(["sudo", "ufw", "deny", "in", "1:65535/udp"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming udp connections denied.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing SSH (port 22) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "in", "22"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming SSH connections allowed.\n")
        
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing Git (port 9418) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "in" "9418"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming Git connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing HTTP (port 80) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "in" "80"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming HTTP connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing HTTPS (port 443) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "in" "443"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming HTTPS connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing outbound SSH (port 22) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "out", "22"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing SSH outbound connections allowed.\n")
        
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing outbound Git (port 9418) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "out", "9418"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing Git outbound connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing outbound HTTP (port 80) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "out", "80"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing HTTP outbound connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing outbound HTTPS (port 443) connections...\n")
    result = subprocess.run(["sudo", "ufw", "allow", "out", "443"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing HTTPS outbound connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Enabling firewall...\n")
    result = subprocess.run(["sudo", "ufw", "enable"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Firewall enabled.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Firewall hardened successfully.\n")

if __name__ == "__main__":
    harden_vm()
