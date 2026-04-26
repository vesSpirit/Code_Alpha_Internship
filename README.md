# 🔐 CodeAlpha Cyber Security Internship Projects

A collection of practical cybersecurity projects completed during the CodeAlpha Cyber Security Internship. These tasks focus on core areas such as network monitoring, phishing awareness, and secure coding practices.

---

## 👨‍💻 Intern Details

| Field | Details |
|------|--------|
| Name | Ahmad Raza Attari |
| Student ID | CA/DF1/42025 |
| Program | Cyber Security |
| Internship | CodeAlpha Cyber Security Internship |

---

## 📂 Repository Contents

| Task | Description |
|------|------------|
| Task 1 | Basic Network Packet Sniffer |
| Task 2 | Phishing Awareness Training |
| Task 3 | Secure Coding Review |

---

## 📡 Task 1 — Basic Network Sniffer

This project demonstrates a simple network packet sniffer developed in Python using the Scapy library. It captures and inspects network traffic in real time.

### Features
- Monitors live network packets  
- Displays source and destination IP addresses  
- Identifies protocol information  
- Provides insight into network communication  

### Code
```python
from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("Source:", packet[IP].src)
        print("Destination:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

sniff(prn=packet_callback, count=10)
```

### Learning Outcomes
- Basics of packet capturing  
- Understanding network traffic flow  
- Introduction to protocol-level inspection  

---

## 🎣 Task 2 — Phishing Awareness Training

This task is centered on educating users about phishing attacks and the tactics used in social engineering.

### Topics Covered
- Definition and purpose of phishing  
- Common phishing attack methods  
- Examples of fake emails and login pages  
- Strategies for prevention  

### Prevention Tips
- ✅ Always verify the sender’s email address  
- ✅ Avoid clicking on unknown or suspicious links  
- ✅ Use two-factor authentication wherever possible  
- ✅ Carefully examine URLs before entering credentials  

---

## 🔒 Task 3 — Secure Coding Review

This task involves analyzing a basic login system, identifying its security flaws, and improving it using better coding practices.

### ❌ Vulnerable Code
```python
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Access Denied")
```

### Vulnerabilities Found
- Hardcoded login credentials  
- Password stored in plain text  
- No encryption mechanism  
- No protection against brute-force attacks  

### ✅ Secure Implementation
```python
import hashlib

stored_password = hashlib.sha256("1234".encode()).hexdigest()

username = input("Enter Username: ")
password = input("Enter Password: ")

entered_password = hashlib.sha256(password.encode()).hexdigest()

if username == "admin" and entered_password == stored_password:
    print("Login Successful")
else:
    print("Access Denied")
```

### Security Improvements
- Password hashing using SHA-256  
- Safer credential comparison  
- Improved authentication approach  

---

## 🛠 Technologies Used

- Python 3.x  
- Scapy  
- Hashlib  
- Cybersecurity fundamentals  
- Network traffic analysis  

---

## 🚀 How to Run

### Clone Repository
```bash
git clone https://github.com/MAK554267/CodeAlpha_CyberSecurity_Internship.git
cd CodeAlpha_CyberSecurity_Internship
```

### Run Network Sniffer
```bash
python Task1_NetworkSniffer/network_sniffer.py
```

### Run Secure Login Program
```bash
python Task3_SecureCodingReview/secure_login.py
```

⚠️ Note: Running the network sniffer requires administrator/root privileges to capture packets.

---

## 📚 Learning Outcomes

During this internship, I developed:

- ✔ Practical skills in packet analysis  
- ✔ Awareness of phishing and social engineering attacks  
- ✔ Knowledge of secure coding practices  
- ✔ Ability to identify common vulnerabilities  
- ✔ Strong foundation in cybersecurity concepts  

---

## ⭐ Author

**Ahmad Raza Attari**  
Cyber Security Student — University of Wah  

🔗 GitHub: [vesSpirit](https://github.com/vesSpirit) 

---

Made with 💻 as part of the CodeAlpha Cyber Security Internship
