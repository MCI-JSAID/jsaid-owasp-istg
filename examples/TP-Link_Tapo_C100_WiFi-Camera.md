# Device Analysis - TP-Link Tapo C100 WiFi-Camera

ISTG and ISTV applied from the viewpoint of the TP-Link Tapo C100 WiFi-Camera.

## Device Model

Version: V4

- Processing Unit
  - Ingenic T31

- Memory
  - XMC XM25QH64A NOR Flash PA-4, AA-3/ 4?
  - SD Card Slot, PA-3, AA-1?

- Firmware
  - Firmware Version 1.3.11, PA-4, AA-3/4?
  - GPL Code for V1, V4, V4.2, PA-1, AA-1

- Data Exchange Service
  - Rest Schnittstelle?
  - UDP Port?
  - Cloud anbindung

- Physical Interface: N.A.

- Wireless Inerface
  - Wi-Fi Chip: Realtek 8188FTV
    - WiFi 802.11 b/g/n

- Internal Interface
  - UART
  - uBoot Version

- User Interface
  - Mobile Application Package name, link to app,Version
  - Clud Webinterfeace?


## Attacker Model

- Processing Unit: PA-4, AA-1-4
 
- Memory:
  - NOR Flash: PA-4, AA-3/ 4
  - SD-Card PA-3, AA-1

- Firmware: PA-4

- Data Exchange Service: PA-2

- Internal Interface: PA-4

- Wireless Inerface: PA-2, AA-1-4

- Physical Interface: N.A.
  
- User Interface: PA-2, AA-1-4

### Access Levels

TODO



## Test Cases

### Processing Unit (ISTG-PROC)

Physical Acess Level PA-4

---

### Memory (ISTG-MEM)

SD Card: TODO

#### Information Gathering (ISTG-MEM-INFO)

##### Disclosure of Source Code and Binaries (ISTG-MEM-INFO-001)

- must be checked if uncompiled source code can be identified within the device memory.
- If uncompiled source code is detected, its content must be analyzed for the presence of sensitive data, which might be useful for potential attackers.
- Reverse-engineering of selected binaries should be performed in order to obtain useful information regarding the device implementation and the processing of sensitive data.

##### Disclosure of Implementation Details (ISTG-MEM-INFO-002)

- Accessible details regarding the implementation must be assessed in order to prepare further tests. For example, this includes:
  - Cryptographic algorithms in use
  - Authentication and authorization mechanism
  - Local paths and environment details

##### Disclosure of Ecosystem Details (ISTG-MEM-INFO-003)

- It must be determined if the data stored in the device memory, e.g., configuration files, contain relevant information about the surrounding ecosystem.

##### Disclosure of User Data (ISTG-MEM-INFO-004)

- It has to be checked whether user data can be accessed by unauthorized individuals.

#### Secrets (ISTG-MEM-SCRT)

##### Unencrypted Storage of Secrets (ISTG-MEM-SCRT-001)

- By searching the contents of the device memory, it must be determined whether it includes secrets in plaintext form.

#### Cryptography (ISTG-MEM-CRYPT)

##### Usage of Weak Cryptographic Algorithms (ISTG-MEM-CRYPT-001)

- The data, stored on the device, must be checked for the presence of encrypted data segments. In case that encrypted data segments are found, it must be checked whether the cryptographic algorithms in use can be identified.
- Furthermore, based on ISTG-MEM-INFO-001 and ISTG-MEM-INFO-002, it must be checked whether any source code, configuration files etc. disclose the usage of certain cryptographic algorithms.
- In case that cryptographic algorithms can be identified, it must be determined whether the algorithms in use and their configuration are providing a sufficient level of security at the time of testing, e.g., by consulting cryptography guidelines like the technical guideline TR-02102-1 by the BSI.

---

### Firmware (ISTG-FW)

Access Level PA-4

Only Software under GPL License is provided on the tp-link website not the Firmware itself. (e.g wifi-drivers )

- download GPL Part from https://www.tp-link.com/de/support/gpl-code/
- and extract: `tar -xvjf c100v4v4.2_GPL.tar.bz2`

---

### Data Exchange Services (ISTG-DES)

TODO

#### Authorization (ISTG-DES-AUTHZ)

#### Information Gathering (ISTG-DES-INFO)

#### Configuration and Patch Management (ISTG-DES-CONF)

#### Secrets (ISTG-DES-SCRT)

#### Cryptography (ISTG-DES-CRYPT)

#### Business Logic (ISTG-DES-LOGIC)

#### Input Validation (ISTG-DES-INPV)

---

### Internal Interface (ISTG-INT)

Physical Access Level PA-4

---

### Physical Interface (ISTG-PHY)

N.A.

---

### Wireless Interface (ISTG-WRLS)

- WLAN Access Point at Provisioning

`WiFI 4`

- Is the device using a secure method for initial setup and provisioning over the WLAN?
  ` No Authentication Required!`
- Are default credentials or open networks used during initial setup?
  ` open network`
- Home-Network
  - How does the device ensure secure connectivity to home networks? Is there any authentication or encryption method enforced?

`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`

#### Authorization (ISTG-WRLS-AUTHZ)

##### Unauthorized Access to the Interface (ISTG-WRLS-AUTHZ-001)

- Can the interface be accessed without proper credentials?
- What methods are available to secure the access (WPA2, WPA3, etc.)?

`Mobile App`

##### Privilege Escalation (ISTG-WRLS-AUTHZ-002)

- Based on ISTG-WRLS-AUTHZ-001
- can an authenticated user escalate privileges to access administrative functions on the device?

`no roles available, thus no privileges escalation`

#### Information Gathering (ISTG-WRLS-INFO)

- Is the information leakage only related to active connections, or can it also be passively gathered?
- How can an attacker gather information from the device via its wireless interface?

##### Disclosure of Implementation Details (ISTG-WRLS-INFO-001)

- What specific implementation details (firmware version, device model, etc.) can be disclosed?
- What methods can be used to secure against such disclosure?

##### Disclosure of Ecosystem Details (ISTG-WRLS-INFO-002)

- What ecosystem-specific information (connected devices, network topology) can be disclosed?

##### Disclosure of User Data (ISTG-WRLS-INFO-003)

- What types of user data can be intercepted or accessed through the wireless interface?
- What encryption or privacy measures are in place to protect user data?

#### Configuration and Patch Management (ISTG-WRLS-CONF)

- Which WiFi software packages and libraries are in use, and what are their versions?
- How often does the manufacturer release updates for these components?

It must also be verified that software packages, which are running on the device and listening on interfaces, are up-to-date as well.

##### Usage of Outdated Software (ISTG-WRLS-CONF-001)

- WiFi SW packages and libraries versions
- Manufacturer oriented?

##### Presence of Unnecessary Software and Functionalities (ISTG-WRLS-CONF-002)

- What built-in but non-essential (or risky) functionalities are present?
- What best practices can be applied to minimize the attack surface?

#### Secrets (ISTG-WRLS-SCRT)

- How are secrets, which should only be accessible via the wireless interface, protected?
- What encryption and access control methods are in place?

##### Access to Confidential Data (ISTG-WRLS-SCRT-001)

- How can secrets disclosed that are solely accessible via wireless interface?

#### Cryptography (ISTG-WRLS-CRYPT)

##### Usage of Weak Cryptographic Algorithms (ISTG-WRLS-CRYPT-001)

- Analyze network traffic for encryption patterns and headers.
- Use tools to intercept and analyze encrypted data.
- List currently accepted secure cryptographic algorithms and compare.

Cryptography can be implemented in various ways. However, due to evolving technologies, new algorithms and more computing power becoming available, many old cryptographic algorithms are nowadays considered weak or insecure. Thus, either new and stronger cryptographic algorithms have to be used or existing algorithms must be adapted, e.g., by increasing the key length or using alternative modes of operation.

- [ ] The data, processed by the data exchange service, must be checked for the presence of encrypted data segments In case that encrypted data segments are found, it must be checked whether the cryptographic algorithms in use can be identified.
- [ ] Furthermore, based on ISTG-DES-INFO-001, it must be checked whether headers, system messages etc. disclose the usage of certain cryptographic algorithms.
- [ ] In case that cryptographic algorithms can be identified, it must be determined whether the algorithms in use and their configuration are providing a sufficient level of security at the time of testing, e.g. list of secure algorithms.

- How to identify crypto algorithms?

Only strong, state of the art cryptographic algorithms should be used. Furthermore, these algorithms must be used in a secure manner
by setting proper parameters, such as an appropriate key length or mode of operation.

#### Business Logic (ISTG-WRLS-LOGIC)

Even if all other aspects of the data exchange service are securely implemented and configured, issues in the underlying logic itself might render the device vulnerable to attacks. Thus, it must be verified if the data exchange service and its functionalities are working as intended and if exceptions are detected and properly handled.

##### Circumvention of the Intended Business Logic (ISTG-WRLS-LOGIC-001)

- Perform functional testing with both standard and non-standard input.
- Use automated tools to simulate abnormal conditions.

The device should not end up in an unknown state. Anomalies in the workflow must be detected and exceptions have to be handled properly.

#### Input Validation (ISTG-WRLS-INPV)

##### Insufficient Input Validation (ISTG-WRLS-INPV-001)

- Are there specific wireless inputs that need validation (SSID names, passwords)?
- Test for buffer overflows, SQL injections, or XSS vulnerabilities through input fields.

##### Code or Command Injection (ISTG-WRLS-INPV-002)

- Difference to ISTG-WRLS-INPV-001?
- Focus on the potential for injecting executable commands through inputs that are supposed to be inert or data-only.

---

### User Interface (ISTG-UI)

- Mobile application
- Cloud application?

#### Authorization (ISTG-UI-AUTHZ)

##### Unauthorized Access to the Interface (ISTG-UI-AUTHZ-001)

- How to access UI? WiFi access and (static?) IP address, username and password (admin x2)
- Objective: Ensure that access to the UI is secured and requires authentication
- Method: Attempt to access the UI without credentials or using common defaults to test for vulnerabilities.

##### Privilege Escalation (ISTG-UI-AUTHZ-002)

- How to check?
  - Levels: 1 - implemented, 2 - theoretically secure, 3 - practically secure, 4 - 100% secure
- UI - Account User Group settings
- App: device sharing

#### Information Gathering (ISTG-UI-INFO)

- Examine the HTML source code, JavaScript, and network traffic for comments or metadata that reveal system details.

##### Disclosure of Implementation Details (ISTG-UI-INFO-001)

- UI scanning? How to check?
- Examine the HTML source code, JavaScript, and network traffic for comments or metadata that reveal system details.

##### Disclosure of Ecosystem Details (ISTG-UI-INFO-002)

- Review sections of the UI related to network setup or connected devices for potential information leakage.

##### Disclosure of User Data (ISTG-UI-INFO-003)

- Same
- IP addresses, MAC address
- Check data displayed or transmitted by the UI for personal identifiers, IP addresses, device IDs, etc.

#### Configuration and Patch Management (ISTG-UI-CONF)

- Validate the versions of all UI components against the latest releases and known vulnerability databases.

##### Usage of Outdated Software (ISTG-UI-CONF-001)

- Anything special for UI? compared to Firmware, WiFi, ...

##### Presence of Unnecessary Software and Functionalities (ISTG-UI-CONF-002)

- SameAudit the UI features and settings to identify non-critical components that can be disabled.

#### Secrets (ISTG-UI-SCRT)

##### Access to Confidential Data (ISTG-UI-SCRT-001)

- System Log
- IP addresses, MAC address
- Test the access controls for sensitive content and inspect how data is stored and transmitted.

#### Cryptography (ISTG-UI-CRYPT)

##### Usage of Weak Cryptographic Algorithms (ISTG-UI-CRYPT-001)

- Identify and test the cryptographic standards used for data protection in the UI to ensure they meet current security best practices.

#### Business Logic (ISTG-UI-LOGIC)

##### Circumvention of the Intended Business Logic (ISTG-UI-LOGIC-001)

- Conduct logical testing to evaluate if business rules are consistently enforced across the UI.

#### Input Validation (ISTG-UI-INPV)

##### Insufficient Input Validation (ISTG-UI-INPV-001)

- Fuzzying
- Known attacks
- Use both manual and automated input fuzzing techniques to identify input validation weaknesses.

##### Code or Command Injection (ISTG-UI-INPV-002)

- Inject malicious code snippets or commands in input fields and monitor the system for any unauthorized execution.

---

## ISVS

### User Space Application

#### Identification & Authentication

2.1.1 Unique identification of users

- difficult/how to check

  2.1.2 Unique identification of connected devices

- difficult/how to check

  2.1.3 Strong user and device authentication

  2.1.4 Common authentication framework (centrally managed)

- difficult/how to check

  2.1.5 Min. 12 characters long passwords for user authentication

- at UI? okay
- App?

  2.1.6 Strong password change functionality

- UI? okay

  2.1.7 Long and complex device authentication passwords

- How to check

  2.1.8 Credentials can be changed by authorized users

- UI/App? okay

  2.1.9 No hardcoded credentials (users, devices, services) in firmware or ecosystem applications

- difficult/how to check
- String search

  2.1.10 Unique provisioning credentials per device

- Check provisioning process

  2.1.11 (L3) Authentication schemes can revoke credentials of compromised or decommissioned devices.

#### Authorization

2.2.1 Common authorization framework

2.2.2 Concept of least privilege

2.2.3 Ownership validation

2.2.4 (L2) Debug capabilities only accessible by approved staff

#### Data Protection

2.3.1 Strong encryption of personal information

2.3.2 Ability to remove credentials and personal information before change of owner

2.3.3 Marking as decommissioned in a central database

2.3.4 (L2) Overwriting personal information with zeros

#### Cryptography

2.4.1 Unique secrets and keys per device

- manufacturer!?

  2.4.2 Strong algorithms with adequate key size and secure implementation

- maybe algorithm is checkable
- secure implementation: would require side-channel attacks to check

(2.4.3 - 2.4.6: L2)

### Software Platform

#### Bootloader

L2 only

#### OS Configuration

3.2.1 Configured according to industry best practices, benchmarks, and uses secure defaults

- What does that mean exactly (best practices)?

  3.2.2 Remove or disable unnecessary network services and interfaces

- How to check if a service is unncessary?

  3.2.3 No legacy/ insecure protocols (Telnet, FTP)

- How to check?

  3.2.4 OS kernel is up-to-date without known vulnerabilities

- How to check?

  3.2.5 (L2) Encrypted persistent filesystem storage volumes

  3.2.6 (L2) Applications use the security features of the OS or kernel.

  3.2.7 (L2) Memory protection controls (ASLR, DEP) are enabled.

(3.2.8 - 3.2.11: L3)

#### Linux

L2 only

#### Software Updates

- How to check if there is no update pending or users cannot install a specific SW version?

  3.4.1 (L2) Package and user-space application updates over-the-air decoupled from firmware updates

  3.4.2 Automatic update functionality (pre-defined schedule)

- If not communicated to user, how to check?

  3.4.3 Cryptographically signed updates

  3.4.4 No time-of-check to time-of-use (TOCTOU) vulnerability. Update right after authentication

- How to check, if there is no update pending?

  3.4.5 Updates do not modify user-configured preferences or settings

- If specific updates pass the verification, how to conclude for the general case?

  3.4.6 (L2) No downgrading to vulnerable versions

- Are such versions available?
- Is a downgrade possible?

  3.4.7 Revert to backup image after update failure

- How to penetrate update failure?

  3.4.8 Unsigned debug pre-production firmware not flashable

- Is such a firmware available?

  3.4.9 (L2) Encrypted firmware is securely decrpyted

  3.4.10 Authentication of the device to the update server prior to downloading

  3.4.11 (L2) Firmware updates are stored encrypted server-side

  3.4.12 Update communication is encrypted

- How to check?

#### Security chip integration

L2 only

#### Kernel space application

3.6.1 (L2)

3.6.2 Only required kernel modules are enabled during runtime

- How to check?

### Communication

#### General

4.1.1 Communication over secure channel (C,I)

4.1.2 Only strong cipher suites

- Means what exactly?

  4.1.3 TLS: device cryptographically verifies X.509 certificate

- Means?

(4.1.4 - 4.1.7: L2/L3, 4.1.5 is missing)

#### Machine-to-Machine

4.2.1 Unencrypted communication only non-sensitive data

- How to check - except for naive sniffing and analysis? What to look for?

  4.2.2 MQTT brokers only allow authorized devices

- How to check?

  4.2.3 Certificates are favored over native username/ password

- Are both supported? How to decide on "favored over"?

#### Bluetooth

4.3.1 Pairing and discovery blocked unless necessary

4.3.2 No easily guessable PINs or PassKeys (0000, 1234)

- PIN necessary?
- What is the pin

  4.3.3 Old Bluetooth versions require a PIN for pairing

- connect and check

  4.3.4 Six digits for SSP authentication (except "Just Works")

- What is "Just Works"

  4.3.5 Maximum and adequate encryption key size

- How to check?

  4.3.6 Most secure Bluetooth pairing

  4.3.7 Strongest Bluetooth Security Mode and Level is used

#### Wi-Fi

4.4.1 Wi-Fi is disabled except when required

- How to check?

  4.4.2 WPA2 or higher

- Example for others too: Documentation or is a systematic way?

  4.4.3 WPA -> AES encryption is used

  4.4.4. No WPS for Wi-Fi connection between devices

#### Zigbee

not applicable

#### LoRaWAN

not applicable

### Hardware Platform

L2/L3 only
