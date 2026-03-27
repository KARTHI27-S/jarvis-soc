🚨 JARVIS-SOC v2.0

CLI-Based Security Operations Center (SOC) Workflow Engine

---

🧠 Overview

JARVIS-SOC is a command-line based security analysis tool that simulates a real Security Operations Center (SOC) workflow.

It is designed to detect, investigate, and analyze system-level threats using real-time logs and system data.

This project demonstrates how SOC analysts:

- Monitor system activity
- Detect threats
- Investigate incidents
- Correlate events
- Generate alerts

---

⚙️ Key Features

🔍 Detection

- SSH brute-force attack detection
- Suspicious process identification
- Network connection analysis

🧪 Investigation

- Incident timeline reconstruction
- Active network connection inspection
- Process-level analysis

🧠 Correlation

- Multi-source threat evaluation
- System-wide threat scoring engine

🚨 Alerting

- Structured SOC alert generation
- Severity classification (LOW / MEDIUM / HIGH)

---

📌 Available Commands

No| Command| Description
1| dashboard| System monitoring panel
2| net-info| Show network information
3| process-check| Investigate running processes
4| port-scan| Scan open ports
5| log-check| Analyze authentication logs
6| hash-file| Generate file hash
7| password-gen| Generate strong password
8| monitor| Start real-time monitoring
9| test-alert| Trigger SOC security alert
10| menu| Show command menu
11| ip-reputation| Check IP threat intelligence
12| generate-report| Generate SOC incident report
13| detect-bruteforce| Detect brute-force login attempts
14| incident-timeline| Reconstruct event timeline
15| net-connections| Analyze active network connections
16| detect-suspicious| Detect abnormal processes
17| threat-score| Calculate system threat level
18| exit| Exit JARVIS

---

🔄 SOC Workflow Model

JARVIS-SOC follows a structured SOC pipeline:

Detection → Investigation → Correlation → Alerting

---

🖥️ Screenshots
<img width="1920" height="1080" alt="Screenshot_2026-03-27_14-44-16" src="https://github.com/user-attachments/assets/ad00256e-cd84-4993-967a-3d2c57f39fa8" />
<img width="1920" height="1080" alt="Screenshot_2026-03-27_14-47-52" src="https://github.com/user-attachments/assets/48a6bb78-ce0e-42a5-b1de-edce92960e79" />



---

🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/KARTHI27-S/jarvis-soc.git

2️⃣ Navigate to Project Directory

cd jarvis-soc

3️⃣ Install Required Dependencies

pip install -r requirements.txt

4️⃣ Run the Application

sudo python jarvis.py

---

📦 Requirements

- Python 3.x
- Linux environment (Kali Linux recommended)
- "journalctl" access (for SSH logs)
- "ss" command (network analysis)

---

⚠️ Disclaimer

This tool is intended for:

- Educational purposes
- Security research
- SOC workflow simulation

Not intended for production deployment.

---

🚀 Future Improvements (v3 Roadmap)

- Real-time log streaming
- Persistent incident storage
- Threat intelligence API integration
- Automated alerting system
- Web-based dashboard

---

👨‍💻 Author

Karthi
Cybersecurity Student

---

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
