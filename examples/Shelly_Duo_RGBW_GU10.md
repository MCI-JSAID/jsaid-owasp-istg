# Device Analysis - Shelly Duo RGBW GU10

## Device Profile:

- Processing unit: ESP8266
- Memory:
    - Main Memory: 64 kB Befehlsspeicher, 96 kB Datenspeicher
    - Flash: externer Flashspeicher unbekannter Größe über Quad-SPI angeschlossen
    - Bootloader im internen ROM
- Firmware: Single Binary Firmware
	- Version: 20230913-111548/v1.14.0-gcb84623
- Data exchange service:
	- 80/TCP
		- Server: Mongoose/6.18
		- REST API
	- 5353/UDP
		- Zeroconf/mDNS
	- 5683/UDP
		- open|filtered according to nmap
		- CoAP?
- Internal interfaces: none
- Physical interfaces: none
- Wireless interfaces:
    -  ESP8266
	    - IEEE 802.11 b/g/n Wi-Fi
- User interfaces:
    - Webserver on 80/TCP

### Physical Access
- Processing Unit: PA-4
- Memory: PA-4
- Installed Firmware: PA-4
- Firmware Update Mechanism: PA-2
- Data Exchange Service: PA-2
- Internal Interface: PA-4
- Physical Interface: n/a
- Wireless Interface: PA-2
- User Interface: PA-2

### Authorization Access
- Firmware Update Mechanism: AA-1
- Data Exchange Service:
	- 80/TCP: AA-1
	- 5353/UDP: AA-1
	- 5683/UDP: ?
- User Interface: AA-1

### Data Security
- Wifi Passwords are stored on the device
- Sensitive Data (_DS-2_)?

### Security Impact
- It's a simple light bulb
- Insignificant Impact (_SI-1_)


## Backend Service Profile:

- ToDo

## Mobile App Profile: Shelly Smart Control App (Android)

- Package Name: cloud.shelly.smartcontrol
- App Store Link: https://play.google.com/store/apps/details?id=cloud.shelly.smartcontrol
- ToDo

## Test Cases

### Firmware (ISTG-FW)

- Access Level: PA-1 (im Internet verfügbar, e.g. http://archive.shelly-tools.de/, http://api.shelly.cloud/files/firmware)
- Authorization Level: AA-1 (im Internet anonym verfügbar)
- How to analyse:
	- strings
	- binwalk
	- ToDo: Kann OneKey mittlerweile ESP8266 Firmware analysieren

#### Information Gathering (ISTG-FW-INFO)
##### Disclosure of Source Code and Binaries (ISTG-FW-INFO-001)

Notes:
- Macht nicht viel Sinn
- Source Code ist sehr unwahrscheinlich
- Binaries in dem Sinne gibt es nicht

##### Disclosure of Implementation Details (ISTG-FW-INFO-002)

Notes:
- Klassische statische Binärcodeanalyse (e.g. mit IDA Pro)

##### Disclosure of Ecosystem Details (ISTG-FW-INFO-003)

- Notes
	- Firmware-Image nach Strings durchsuchen
	- Firmware-Image nach Datenmustern durchsuchen

#### Configuration and Patch Management (ISTG-FW-CONF)

##### Usage of Outdated Software (ISTG-FW-CONF-001)

- Notes
	- Inwieweit können wir das bei ESP8266 Images bestimmen?

##### Presence of Unnecessary Software and Functionalities (ISTG-FW-CONF-002)

- Notes
	- Inwieweit können wir das bei ESP8266 Images bestimmen?


#### Configuration and Patch Management (ISTG-FW-CONF)

##### Secrets Stored in Public Storage (ISTG-FW-SCRT-001)

- Notes
	- Gibt es überhaupt "Public Storage Spaces"?

##### Unencrypted Storage of Secrets (ISTG-FW-SCRT-002)

- Notes
	- Nach Strings und Datenmustern im Firmware-Image suchen

##### Usage of Hardcoded Secrets (ISTG-FW-SCRT-003)

- Notes
	- Dependency zu ISTG-FW-INFO-001 (sollte nicht auch eine Dependency)
	- Möglich wäre String- bzw. Mustersuche, aber wie Ergebnisse interpretieren?


#### Configuration and Patch Management (ISTG-FW-CONF)

##### Usage of Weak Cryptographic Algorithms (ISTG-FW-CRYPT-001)

- Notes
	- Inwieweit macht das auf Firmwareebene Sinn hier?


### Installed Firmware (ISTG-FW\[INST])

#### Authorization (ISTG-FW\[INST]-AUTHZ)

##### Unauthorized Access to the Firmware (ISTG-FW\[INST]-AUTHZ-001)

- Notes
	- Zugriff auf installierte Firmware benötigt PA-4

##### Privilege Escalation (ISTG-FW\[INST]-AUTHZ-002)

- Notes
	- Zugriff auf installierte Firmware benötigt PA-4

#### Information Gathering (ISTG-FW\[INST]-INFO)

##### Disclosure of User Data (ISTG-FW\[INST]-INFO-001)

- Notes
	- Zugriff auf installierte Firmware benötigt PA-4
	- Was ist aber nach Entsorgung des Geräts?

#### Cryptography (ISTG-FW\[INST]-CRYPT)

##### Insufficient Verification of the Bootloader Signature (ISTG-FW\[INST]-CRYPT-001)

- Notes
	- Zugriff auf installierte Firmware benötigt PA-4
	- Bootloader ist im ROM und damit nicht änderbar


### Firmware Update Mechanism (ISTG-FW\[UPDT])

#### Authorization (ISTG-FW\[UPDT]-AUTHZ)

##### Unauthorized Firmware Update (ISTG-FW\[UPDT]-AUTHZ-001)

- Notes
	- Firmware Update kann defaultmässig mit PA-2 und AA-1 durchgeführt werden (über REST API)
	- AA-2 muss konfiguriert werden
	- Siehe: http://archive.shelly-tools.de/

#### Cryptography (ISTG-FW\[UPDT]-CRYPT)

##### Insufficient Firmware Update Signature (ISTG-FW\[UPDT]-CRYPT-001)

- Notes
	- Es gibt keine digitale Signatur
	- Bei Shelly ist das aber auch ein Feature (Installation von Tasmota)

##### Insufficient Firmware Update Encryption (ISTG-FW\[UPDT]-CRYPT-002)

- Notes
	- Firmware Update nicht verschlüsselt

##### Insecure Transmission of the Firmware Update (ISTG-FW\[UPDT]-CRYPT-003)

- Notes
	- Mitsniffen und Trafficanalyse (wird TLS verwendet, was sind die TLS Parameter)
	- Firmware Update über SSL-Proxy umleiten und MitM probieren

##### Insufficient Verification of the Firmware Update Signature (ISTG-FW\[UPDT]-CRYPT-004)

- Notes
	- Nicht zutreffend, da ISTG-FW\[UPDT]-CRYPT-001 schon nicht erfüllt


#### Business Logic (ISTG-FW\[UPDT]-LOGIC)

##### Insufficient Rollback Protection (ISTG-FW\[UPDT]-LOGIC-001)

- Notes
	- Rollback Protection nicht vorhanden
	- Bei Shelly ist das aber auch ein Feature (Downgrade im Fall von Problemen)
		- Siehe z.B. https://smarthome-forum.eu/forum/thread/21940-downgradelinks-zu-0-14-x/

### Data Exchange Services (ISTG-DES)

#### Authorization (ISTG-DES-AUTHZ)

##### Unauthorized Access to the Data Exchange Service (ISTG-DES-AUTHZ-001)

Note:
	- AA-2 muss für REST API konfiguriert werden
	- ToDo: Bypass Überprüfung

##### Privilege Escalation (ISTG-DES-AUTHZ-002)

Note:
	- Nicht zutreffend, da es nicht mehrere Authorisierungslevels gibt

#### Information Gathering (ISTG-DES-INFO)

##### Disclosure of Implementation Details (ISTG-DES-INFO-001)

Note:
	- Stehen in Shelly-Dokumentation

##### Disclosure of Ecosystem Details (ISTG-DES-INFO-002)

Note:
	- Wie relevant für REST API
	- ToDo: Cloud Anbindung

##### Disclosure of User Data (ISTG-DES-INFO-003)

Note:
	- Ältere Versionen der REST API hatten hier ein Problem
		- Laut Doku: In order to prevent security issues (e.g. when forwarding logs to 3rd parties), since v1.7.0 the `password` attribute for login protected devices is no longer returned on the API call.
	- ToDo: Cloud Anbindung

#### Configuration and Patch Management (ISTG-DES-CONF)

##### Usage of Outdated Software (ISTG-DES-CONF-001)

Note:
	- Wie an Liste von verwendeter Software bzw. Libraries kommen?
	- Mögliche Informationsquellen:
		- Servicebanner
	- Shelly verwendet Mongoose/6.18
		- https://www.cvedetails.com/vulnerability-list/vendor_id-16334/product_id-41402/version_id-646458/Cesanta-Mongoose-6.18.html

##### Presence of Unnecessary Software and Functionalities (ISTG-DES-CONF-002)

Note:
	- ToDo: Wie sowas herausfinden?

#### Secrets (ISTG-DES-SCRT)

##### Access to Confidential Data (ISTG-DES-SCRT-001)

Note:
	- ToDo: Wie sowas herausfinden?

#### Cryptography (ISTG-DES-CRYPT)

##### Usage of Weak Cryptographic Algorithms (ISTG-DES-CRYPT-001)

Note:
	- Mitsniffen und Trafficanalyse (TLS-Verbindungsparameter)

#### Business Logic (ISTG-DES-LOGIC)

##### Circumvention of the Intended Business Logic (ISTG-DES-LOGIC-001)

Note:
	- ToDo: Wie sowas herausfinden?

#### Input Validation (ISTG-DES-INPV)

##### Insufficient Input Validation (ISTG-DES-INPV-001)

Note:
	- ToDo: Wie sowas (automatisiert) herausfinden?
	- Fuzzying?
	- Bekannte Attacken (e.g. SQL-Injection) durchprobieren?

##### Code or Command Injection (ISTG-DES-INPV-002)

Note:
	- ToDo: Wie sowas herausfinden?

### Internal Interfaces (ISTG-INT)

Note:
- Irrelevant, da PA-4


### Physical Interfaces (ISTG-PHY)

Note:
- Irrelevant, da nicht zutreffend

### Wireless Interfaces (ISTG-WRLS)

#### Authorization (ISTG-WRLS-AUTHZ)

##### Unauthorized Access to the Interface (ISTG-WRLS-AUTHZ-001)

Note:
- Wifi AP ist standardmäßig ohne Password
- Verhalten älterer Firmware Versionen war, dass bei Konfiguration als Wifi Client trotzdem Wifi AP angeschalten war

##### Privilege Escalation (ISTG-WRLS-AUTHZ-002)

Note:
	- ToDo: Wie sowas herausfinden?

#### Information Gathering (ISTG-WRLS-INFO)

##### Disclosure of Implementation Details (ISTG-WRLS-INFO-001)

Note:
	- Wie relevant ist das für eine physische Schnittstelle

##### Disclosure of Ecosystem Details (ISTG-WRLS-INFO-002)

Note:
	- Wie relevant ist das für eine physische Schnittstelle

##### Disclosure of User Data (ISTG-WRLS-INFO-003)

Note:
	- Wie relevant ist das für eine physische Schnittstelle


#### Configuration and Patch Management (ISTG-WRLS-CONF)

##### Usage of Outdated Software (ISTG-WRLS-CONF-001)


Note:
	- Wie relevant ist das für eine physische Schnittstelle
	- Schnittstellen-Treiber?

##### Presence of Unnecessary Software and Functionalities (ISTG-WRLS-CONF-002)

Note:
	- Wie relevant ist das für eine physische Schnittstelle
	- Schnittstellen-Treiber?

#### Secrets (ISTG-WRLS-SCRT)

##### Access to Confidential Data (ISTG-WRLS-SCRT-001)

Note:
	- Wie relevant ist das für eine physische Schnittstelle

#### Cryptography (ISTG-WRLS-CRYPT)

##### Usage of Weak Cryptographic Algorithms (ISTG-WRLS-CRYPT-001)

Note:
	- Wifi: Welcher Standard wird implementiert (WEP/WPA/WPA2/WPA3)?

#### Business Logic (ISTG-WRLS-LOGIC)

Note:
	- Inwieweit macht diese Kategorie Sinn


#### Input Validation (ISTG-WRLS-INPV)

Note:
	- Inwieweit macht diese Kategorie Sinn


### User Interfaces (ISTG-UI)

#### Authorization (ISTG-UI-AUTHZ)

##### Unauthorized Access to the Interface (ISTG-UI-AUTHZ-001)

Note:
- Standardmäßig AA-1
- AA-2 kann konfiguriert werden

##### Privilege Escalation (ISTG-UI-AUTHZ-002)

Note:
- ToDo: Wie Herausfinden?

#### Information Gathering (ISTG-UI-INFO)

##### Disclosure of Implementation Details (ISTG-UI-INFO-001)

Note:
- ToDo: Wie herausfinden

##### Disclosure of Ecosystem Details (ISTG-UI-INFO-002)

Note:
- ToDo: Wie herausfinden

##### Disclosure of User Data (ISTG-UI-INFO-003)

Note:
- ToDo: Wie herausfinden

#### Configuration and Patch Management (ISTG-UI-CONF)

##### Usage of Outdated Software (ISTG-UI-CONF-001)

Note:
- ToDo: Wie herausfinden
- Mögliche Informationsquellen:
	- Servicebanner

##### Presence of Unnecessary Software and Functionalities (ISTG-UI-CONF-002)

Note:
- ToDo: Wie herausfinden


#### Secrets (ISTG-UI-SCRT)

##### Access to Confidential Data (ISTG-UI-SCRT-001)

Note:
- ToDo: Wie herausfinden


#### Cryptography (ISTG-UI-CRYPT)

##### Usage of Weak Cryptographic Algorithms (ISTG-UI-CRYPT-001)

Note:
- Mitsniffen und Trafficanalyse
- SSL-Proxy


#### Business Logic (ISTG-UI-LOGIC)

##### Circumvention of the Intended Business Logic (ISTG-UI-LOGIC-001)

Note:
- ToDo: Wie herausfinden

#### Input Validation (ISTG-UI-INPV)

##### Insufficient Input Validation (ISTG-UI-INPV-001)

Note:
	- ToDo: Wie sowas (automatisiert) herausfinden?
	- Fuzzying?
	- Bekannte Attacken (e.g. SQL-Injection) durchprobieren?

##### Code or Command Injection (ISTG-UI-INPV-002)

Note:
	- ToDo: Wie herausfinden?


### Fehlende Punkte

- Default Config
	- Mit was für Konfiguration werden Geräte ausgeliefert?
	- Ist die Default Config sinnvoll bzw. sicher?
	- Wird der User gezwungen bzw. darauf aufmerksam gemacht, unsichere Config zu ändern (z.B. Default Passwort)
- Device Provisioning
	- Wie wird das Gerät initialisiert?
	- Ist die verwendete Methode sinnvoll bzw. sicher?
	- Verknüpft mit Default Config: Wird der User gezwungen bzw. darauf aufmerksam gemacht, unsichere Config zu ändern



