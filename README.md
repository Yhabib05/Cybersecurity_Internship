# Cybersecurity_Internship
This repository contains codes and documents used or created by me during my cybersecurity internship.

The internship was divided into three parts. The **first part** focused on gaining foundational knowledge about cybersecurity SIEM/XDR systems. I explored their basic concepts and functionality. Additionally, I worked with an open-source SIEM called Wazuh. I learned how Wazuh operates, integrated it with useful tools to enhance its detection capabilities, and implemented various use cases, including performing simple attacks and learning how to prevent them.

You can find more details about Wazuh and SIEM/XDR in the following link: [Wazuh: SIEM/XDR](https://hackmd.io/@yh0rookie/SJjAL-vu3)

The **second part** of the internship revolved around penetration testing. I conducted various attacks and focused on making Wazuh detect them by customizing rules. This phase provided an opportunity to gain hands-on experience with different attack techniques such as phishing pages and process injection. I also attempted to integrate a machine-learning model with Wazuh, although it was not successful. However, It's still a log analysis model for intrusion detection using a Python interface. Please note that the logs should be in a specific format that contains a lot of variables, that are explained in the file(main.py), due to the absence of training data. To try out the model, you can run the main.py file. Additionally, within the code, you can find a log example and can try to change the variables of this log to observe the model's predictions for intrusion detection.

For more information about cybersecurity pen-testing and machine learning, please refer to: [Cybersecurity: Pentest, Machine Learning](https://hackmd.io/@yh0rookie/BkLP_PiU3/edit)

The **third part** of the internship involved simulating a real attack scenario. My task was to perform post-exploitation activities. I utilized Metasploit, an open-source tool commonly used for pen testing and hacking. After identifying various ways to exploit the vulnerable machine, I focused on the detection aspect. I implemented custom rules in Wazuh to detect the attack, including a reverse shell attack.

To learn more about simulating an attack, exploring vulnerabilities, testing, and remediation, please refer to: 
[Simulating an attack: Exploring vulnerabilities, testing, and correcting them](https://hackmd.io/@yh0rookie/SJjAL-vu3)

**NB**: To test the phishing attack, It's better to remove the dir "PyPhiser" and install the Pyphiser library directly by cloning the original git depository "PyPhiser".
