import subprocess

def harden_vm():
    log_file = "logs.log"
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Resetting firewall rules...\n")
    result = subprocess.run(["ufw", "reset", "--force"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Successfully reset firewall rules.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all incoming connections by default...\n")
    result = subprocess.run(["ufw", "default", "deny", "incoming"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Incoming connections denied.\n")
        
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Denying all outgoing connections by default...\n")
    result = subprocess.run(["ufw", "default", "deny", "outgoing"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Outgoing connections denied.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing SSH (port 22) connections...\n")
    result = subprocess.run(["ufw", "allow", "22"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ SSH connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing HTTP (port 80) connections...\n")
    result = subprocess.run(["ufw", "allow", "80"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ HTTP connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Allowing HTTPS (port 443) connections...\n")
    result = subprocess.run(["ufw", "allow", "443"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ HTTPS connections allowed.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Enabling firewall...\n")
    result = subprocess.run(["ufw", "enable"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(log_file, "a") as f:
        f.write(result.stdout + "\n")
        f.write("#$#$#$#$#$ Firewall enabled.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Firewall hardened successfully.\n")

if __name__ == "__main__":
    harden_vm()
