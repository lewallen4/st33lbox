import subprocess

def harden_vm():
    log_file = "logs.log"
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Resetting firewall rules...\n")
    subprocess.run(["ufw", "reset", "--force"])
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Firewall rules reset.\n")

    subprocess.run(["ufw", "default", "deny", "incoming"])
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Incoming connections denied.\n")

    subprocess.run(["ufw", "allow", "22"])
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ SSH connections allowed.\n")

    subprocess.run(["ufw", "allow", "80"])
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ HTTP connections allowed.\n")

    subprocess.run(["ufw", "allow", "443"])
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ HTTPS connections allowed.\n")

    subprocess.run(["ufw", "enable"])
    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Firewall enabled.\n")

    with open(log_file, "a") as f:
        f.write("#$#$#$#$#$ Firewall hardened successfully.\n")

if __name__ == "__main__":
    harden_vm()
