# **Project: Load Balancer Configuration**

## 0x0F. Load balancer

![qfdked8](https://github.com/waltertaya/alx-system_engineering-devops/assets/126944679/ac49527a-1ad3-4de6-ab3f-9ea584d6f367)

---

### Project Overview

In this project, the goal is to enhance the web stack by introducing redundancy for web servers using a load balancer. This setup aims to improve traffic handling capacity and increase infrastructure reliability. The project involves configuring web servers, installing and configuring a load balancer, and automating tasks using Bash and Puppet scripts.

---

### Project Details

#### Task 0: Double the number of webservers

- **Objective**: Configure web-02 to be identical to web-01 and add a custom Nginx response header.
- **Requirements**:
  - Configure Nginx to include a custom header (X-Served-By) containing the hostname of the server.
  - Write a Bash script (0-custom_http_response_header) to configure a new Ubuntu machine according to task requirements.
- **Instructions**: Utilize Bash scripting to automate the configuration of web servers.

#### Task 1: Install your load balancer

- **Objective**: Install and configure HAproxy on lb-01 server to distribute traffic to web-01 and web-02.
- **Requirements**:
  - Configure HAproxy to use round-robin algorithm for load distribution.
  - Ensure HAproxy can be managed via an init script.
  - Ensure servers are configured with correct hostnames ([STUDENT_ID]-web-01 and [STUDENT_ID]-web-02).
- **Instructions**: Develop a Bash script (1-install_load_balancer) to configure a new Ubuntu machine to meet task requirements.

#### Task 2: Add a custom HTTP header with Puppet (Advanced)

- **Objective**: Automate the creation of a custom HTTP header response using Puppet.
- **Requirements**:
  - Create a custom HTTP header (X-Served-By) with the server's hostname.
  - Write a Puppet script (2-puppet_custom_http_response_header.pp) to configure a new Ubuntu machine accordingly.
- **Instructions**: Employ Puppet configuration management to automate task execution.

---

### Project Repository

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/waltertaya/alx-system_engineering-devops)
- **Directory**: 0x0F-load_balancer

---

### Project Management

- **Project Start**: Mar 4, 2024 6:00 AM
- **Project End**: Mar 5, 2024 6:00 AM
- **Checker Release**: Mar 4, 2024 12:00 PM
- **Auto Review**: Will be launched at the deadline

---

### Additional Notes

- Ensure all Bash scripts are executable and pass Shellcheck without errors.
- Use Ubuntu 16.04 LTS for script interpretation.
- Include a README.md file at the root of the project folder.

---

### Resources

- [How does Software and Hardware Load Balancer Work? (Load balancer Algorithms Explained examples)](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
- [Intro to Load Balancing for Developers – The Algorithms](https://community.f5.com/kb/technicalarticles/intro-to-load-balancing-for-developers-%E2%80%93-the-algorithms/273759)

---

### Author

- **@waltertaya**

---

**Copyright © 2024 ALX, All rights reserved.**
