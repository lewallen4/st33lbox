import subprocess

def harden_vm():
    # Clear existing firewall rules
    subprocess.run(["ufw", "reset", "--force"])

    # Deny all incoming connections by default
    subprocess.run(["ufw", "default", "deny", "incoming"])

    # Allow SSH (port 22) connections
    subprocess.run(["ufw", "allow", "22"])

    # Allow HTTP (port 80) connections
    subprocess.run(["ufw", "allow", "80"])

    # Allow HTTPS (port 443) connections
    subprocess.run(["ufw", "allow", "443"])

    # Enable firewall
    subprocess.run(["ufw", "enable"])

    print("Firewall hardened successfully.")

if __name__ == "__main__":
    harden_vm()
