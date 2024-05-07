import subprocess

def harden_vm():
    print("Resetting firewall rules...")
    subprocess.run(["ufw", "reset", "--force"])
    print("Firewall rules reset.")

    print("Denying all incoming connections by default...")
    subprocess.run(["ufw", "default", "deny", "incoming"])
    print("Incoming connections denied.")

    print("Allowing SSH (port 22) connections...")
    subprocess.run(["ufw", "allow", "22"])
    print("SSH connections allowed.")

    print("Allowing HTTP (port 80) connections...")
    subprocess.run(["ufw", "allow", "80"])
    print("HTTP connections allowed.")

    print("Allowing HTTPS (port 443) connections...")
    subprocess.run(["ufw", "allow", "443"])
    print("HTTPS connections allowed.")

    print("Enabling firewall...")
    subprocess.run(["ufw", "enable"])
    print("Firewall enabled.")

    print("Firewall hardened successfully.")

if __name__ == "__main__":
    harden_vm()
