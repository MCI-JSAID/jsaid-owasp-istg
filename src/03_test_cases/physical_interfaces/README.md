# 3.6. Physical Interfaces (ISTG-PHY)

## Table of Contents
- [3.6. Physical Interfaces (ISTG-PHY)](#36-physical-interfaces-istg-phy)
	- [Table of Contents](#table-of-contents)
	- [Overview](#overview)
	- [Authorization (ISTG-PHY-AUTHZ)](#authorization-istg-phy-authz)
	  - [Unauthorized Access to the Interface (ISTG-PHY-AUTHZ-001)](#unauthorized-access-to-the-interface-istg-phy-authz-001)
	  - [Privilege Escalation (ISTG-PHY-AUTHZ-002)](#privilege-escalation-istg-phy-authz-002)
	- [Information Gathering (ISTG-PHY-INFO)](#information-gathering-istg-phy-info)
	  - [Disclosure of Implementation Details (ISTG-PHY-INFO-001)](#disclosure-of-implementation-details-istg-phy-info-001)
	  - [Disclosure of Ecosystem Details (ISTG-PHY-INFO-002)](#disclosure-of-ecosystem-details-istg-phy-info-002)
	  - [Disclosure of User Data (ISTG-PHY-INFO-003)](#disclosure-of-user-data-istg-phy-info-003)
	- [Configuration and Patch Management (ISTG-PHY-CONF)](#configuration-and-patch-management-istg-phy-conf)
	  - [Usage of Outdated Software (ISTG-PHY-CONF-001)](#usage-of-outdated-software-istg-phy-conf-001)
	  - [Presence of Unnecessary Software and Functionalities (ISTG-PHY-CONF-002)](#presence-of-unnecessary-software-and-functionalities-istg-phy-conf-002)
	- [Secrets (ISTG-PHY-SCRT)](#secrets-istg-phy-scrt)
	  - [Access to Confidential Data (ISTG-PHY-SCRT-001)](#access-to-confidential-data-istg-phy-scrt-001)
	- [Cryptography (ISTG-PHY-CRYPT)](#cryptography-istg-phy-crypt)
	  - [Usage of Weak Cryptographic Algorithms (ISTG-PHY-CRYPT-001)](#usage-of-weak-cryptographic-algorithms-istg-phy-crypt-001)
	- [Business Logic (ISTG-PHY-LOGIC)](#business-logic-istg-phy-logic)
	  - [Circumvention of the Intended Business Logic (ISTG-PHY-LOGIC-001)](#circumvention-of-the-intended-business-logic-istg-phy-logic-001)
	- [Input Validation (ISTG-PHY-INPV)](#input-validation-istg-phy-inpv)
	  - [Insufficient Input Validation (ISTG-PHY-INPV-001)](#insufficient-input-validation-istg-phy-inpv-001)
	  - [Code or Command Injection (ISTG-PHY-INPV-002)](#code-or-command-injection-istg-phy-inpv-002)




## Overview

This section includes test cases and categories for the component physical interface. Depending on whether the interface is connected to a network or not, it might be accessible with *PA-2*, *PA-3* or *PA-4*. Establishing a direct connection to a physical interface might require specific hardware equipment (e.g., a connector or adapter cable).

In regards of test case categories that are relevant for a physical interface, the following were identified:

- **Authorization:** Focuses on vulnerabilities that allow to get unauthorized access to the physical interface or to elevate privileges in order to access restricted functionalities.

- **Information Gathering:** Focuses on information that is handled by the physical interface and that might be disclosed to potential attackers if not being properly protected or removed.

- **Configuration and Patch Management:** Focuses on vulnerabilities and issues in the configuration of a physical interface and its software components.

- **Secrets:** Focuses on secrets that are handled by the physical interface in an insecure manner.

- **Cryptography:** Focuses on vulnerabilities in the cryptographic implementation.

- **Business Logic:** Focuses on vulnerabilities in the implementation of the physical interface.

- **Input Validation:** Focuses on vulnerabilities regarding the validation and processing of input from untrustworthy sources.



## Authorization (ISTG-PHY-AUTHZ)

Depending on the access model for a given device, only certain individuals might be allowed to access a physical interface. Thus, proper authentication and authorization procedures need to be in place, which ensure that only authorized users can get access.

### Unauthorized Access to the Interface (ISTG-PHY-AUTHZ-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 |  |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |


**Summary**

Depending on the specific implementation of a given device, access to a physical interface might be restricted to individuals with a certain authorization access level, e.g., *AA-2*, *AA-3* or *AA-4*. If the device fails to correctly verify access permissions, any attacker (*AA-1*) might be able to get access.

**Test Objectives**

- It must be checked if authorization checks for access to the physical interface are implemented.

- In case that authorization checks are in place, it must be determined whether there is a way to bypass them.

**Step-By-Step Execution**

ToDo

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to the physical interface is only possible for authorized individuals.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-AUTHZ-001](../data_exchange_services/README.md#unauthorized-access-to-the-data-exchange-service-istg-des-authz-001).

### Privilege Escalation (ISTG-PHY-AUTHZ-002)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

Depending on the specific implementation of a given device, access to some functionalities via a physical interface might be restricted to individuals with a certain authorization access level, e.g., *AA-3* or *AA-4*. If the interface fails to correctly verify access permissions, an attacker with a lower authorization access level than intended might be able to get access to the restricted functionalities.

**Test Objectives**

- Based on [ISTG-PHY-AUTHZ-001](#unauthorized-access-to-the-interface-istg-phy-authz-001), it must be determined whether there is a way to elevate the given access privileges and thus to access restricted functionalities.

**Step-By-Step Execution**

ToDo

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to restricted functionalities is only possible for individuals with the required authorization access levels.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-AUTHZ-002](../data_exchange_services/README.md#privilege-escalation-istg-des-authz-002).



## Information Gathering (ISTG-PHY-INFO)

Physical interfaces might disclose various information, which could reveal details regarding the inner workings of the device or the surrounding IoT ecosystem to potential attackers. This could enable and facilitate further, more advanced attacks.

### Disclosure of Implementation Details (ISTG-PHY-INFO-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

If details about the implementation, e.g., algorithms in use or the authentication procedure, are available to potential attackers, flaws and entry points for successful attacks are easier to detect. While the disclosure of such details alone is not considered to be a vulnerability, it facilitates the identification of potential attack vectors, thus allowing an attacker to exploit insecure implementations faster.

For example, relevant information might be included in service banners, response headers or error messages.

**Test Objectives**

- Accessible details regarding the implementation must be assessed in order to prepare further tests. For example, this includes:
  - Cryptographic algorithms in use

  - Authentication and authorization mechanisms

  - Local paths and environment details


**Step-By-Step Execution**

ToDo

**Remediation**

As mentioned above, the disclosure of such information is not considered a vulnerability. However, in order to impede exploitation attempts, only information, necessary for the device operation, should be displayed.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-FW-INFO-002](../firmware/README.md#disclosure-of-implementation-details-istg-fw-info-002).

### Disclosure of Ecosystem Details (ISTG-PHY-INFO-002)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

A physical interface might disclose information about the surrounding IoT ecosystem, e.g., sensitive URLs, IP addresses, software in use etc. An attacker might be able to use this information to prepare and execute attacks against the ecosystem.

For example, relevant information might be included in service banners, response headers or error messages.

**Test Objectives**

- It must be determined if the physical interface discloses relevant information about the surrounding ecosystem.

**Step-By-Step Execution**

ToDo

**Remediation**

The disclosure of information should be reduced to the minimum, which is required for operating the device. The disclosed information it has to be assessed and all unnecessarily included data should be removed.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-FW-INFO-003](../firmware/README.md#disclosure-of-ecosystem-details-istg-fw-info-003).

### Disclosure of User Data (ISTG-PHY-INFO-003)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

During runtime, a device is accumulating and processing data of different kinds, such as personal data of its users. If this data is disclosed, an attacker might be able to get access to it.

**Test Objectives**

- It has to be checked whether user data can be accessed by unauthorized individuals.

**Step-By-Step Execution**

ToDo

**Remediation**

Access to user data should only be granted to individuals and processes that need to have access to it. No unauthorized or not properly authorized individual should be able to access user data.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-FW[INST]-INFO-001](../firmware/installed_firmware.md#disclosure-of-user-data-istg-fw[inst]-info-001).



## Configuration and Patch Management (ISTG-PHY-CONF)

Since IoT devices can have a long lifespan, it is important to make sure that the software, running on the device, is regularly updated in order to apply the latest security patches. The update process of the firmware itself will be covered by [ISTG-FW[UPDT]](../firmware/firmware_update_mechanism.md). However, it must also be verified that software packages, which are running on the device and listening on interfaces, are up-to-date as well.

### Usage of Outdated Software (ISTG-PHY-CONF-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

Every piece of software is potentially vulnerable to attacks. For example, coding errors could lead to undefined program behavior, which then can be exploited by an attacker to gain access to data, processed by the application, or to perform actions in the context of the runtime environment. Furthermore, vulnerabilities in the used frameworks, libraries and other technologies might also affect the security level of a given piece of software.

Usually, developers release an update once a vulnerability was detected in their software. These updates should be installed as soon as possible in order to reduce the probability of successful attacks. Otherwise, attackers could use known vulnerabilities to perform attacks against the device.

**Test Objectives**

- The version identifiers of installed software packages as well as libraries and frameworks in use must be determined.

- Based on the detected version identifiers, it must be determined if the software version in use is up-to-date, e.g., by consulting the website of the software developer or public repositories.

- By using vulnerability databases, such as the [National Vulnerability Database](https://nvd.nist.gov) of the NIST, it has to be checked whether any vulnerabilities are known for the detected software versions.

**Step-By-Step Execution**

ToDo

**Remediation**

No outdated software packages should be running on the device. A proper patch management process, which ensures that applicable updates are installed once being available, should be implemented.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-FW-CONF-001](../firmware/README.md#usage-of-outdated-software-istg-fw-conf-001).

### Presence of Unnecessary Software and Functionalities (ISTG-PHY-CONF-002)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

Every piece of software, which is available on the device, broadens the attack surface since it might be used to perform attacks against the device. Even if the installed software is up-to-date, it might still be affected by unpublished vulnerabilities. It is also possible that a software program facilitates an attack without being vulnerable, e.g., by providing access to specific files or processes.

**Test Objectives**

- A list of functionalities, available via the interface, should be assembled.

- Based on the device documentation, its behavior and the intended use cases, it must be determined whether any of the available functionalities are not mandatory for the device operation.

**Step-By-Step Execution**

ToDo

**Remediation**

The attack surface should be minimized as much as possible by removing or disabling every software that is not required for the device operation.

Especially in case of general-purpose operating systems, such as Windows and Linux systems, it must be ensured that any unnecessary operating system features are disabled.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-FW-CONF-002](../firmware/README.md#presence-of-unnecessary-software-and-functionalities-istg-fw-conf-002).



## Secrets (ISTG-PHY-SCRT)

IoT devices are often operated outside of the control space of their manufacturer. Still, they need to establish connections to other network nodes within the IoT ecosystem, e.g., to request and receive firmware updates or to send data to a cloud API. Hence, it might be required that the device has to provide some kind of authentication credential or secret. These secrets need to be stored on the device in a secure manner to prevent them from being stolen and used to impersonate the device.

### Access to Confidential Data (ISTG-PHY-SCRT-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

Malfunctions, unintended behavior or improper implementation of a physical interface might enable an attacker to get access to secrets.

**Test Objectives**

- It has to be determined whether secrets can be accessed via the physical interface.

**Step-By-Step Execution**

ToDo

**Remediation**

Access to secrets should only be granted to individuals and processes that need to have access to them. No unauthorized or not properly authorized individual should be able to access secrets.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-SCRT-001](../data_exchange_services/README.md#access-to-confidential-data-istg-des-scrt-001).



## Cryptography (ISTG-PHY-CRYPT)

Many IoT devices need to implement cryptographic algorithms, e.g., to securely store sensitive data, for authentication purposes or to receive and verify encrypted data from other network nodes. Failing to implement secure, state of the art cryptography might lead to the exposure of sensitive data, device malfunctions or loss of control over the device.

### Usage of Weak Cryptographic Algorithms (ISTG-PHY-CRYPT-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

Cryptography can be implemented in various ways. However, due to evolving technologies, new algorithms and more computing power becoming available, many old cryptographic algorithms are nowadays considered weak or insecure. Thus, either new and stronger cryptographic algorithms have to be used or existing algorithms must be adapted, e.g., by increasing the key length or using alternative modes of operation.

The usage of weak cryptographic algorithms might allow an attacker to recover the plaintext from a given ciphertext in a timely manner.

**Test Objectives**

- The data, processed by the interface, must be checked for the presence of encrypted data segments. In case that encrypted data segments are found, it must be checked whether the cryptographic algorithms in use can be identified.

- Furthermore, based on [ISTG-PHY-INFO-001](#disclosure-of-implementation-details-istg-phy-info-001), it must be checked whether headers, system messages etc. disclose the usage of certain cryptographic algorithms.

- In case that cryptographic algorithms can be identified, it must be determined whether the algorithms in use and their configuration are providing a sufficient level of security at the time of testing, e.g., by consulting cryptography guidelines like the technical guideline [TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf __blob=publicationFile&v=10) by the BSI.

**Step-By-Step Execution**

ToDo

**Remediation**

Only strong, state of the art cryptographic algorithms should be used. Furthermore, these algorithms must be used in a secure manner by setting proper parameters, such as an appropriate key length or mode of operation.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-FW-CRYPT-001](../firmware/README.md#usage-of-weak-cryptographic-algorithms-istg-fw-crypt-001).



## Business Logic (ISTG-PHY-LOGIC)

Even if all other aspects of the physical interface are securely implemented and configured, issues in the underlying logic itself might render the device vulnerable to attacks. Thus, it must be verified if the physical interface and its functionalities are working as intended and if exceptions are detected and properly handled.

### Circumvention of the Intended Business Logic (ISTG-PHY-LOGIC-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

Flaws in the implementation of the business logic might result in unintended behavior or malfunctions of the device. For example, if an attacker intentionally misses to provide relevant input data or tries to skip or change important steps in the processing workflow the device might end up in an unknown, potentially insecure state.

**Test Objectives**

- Based on the specific business logic implementation, it has to be determined whether deviations from the defined workflows are properly detected and handled.

**Step-By-Step Execution**

ToDo

**Remediation**

The device should not end up in an unknown state. Anomalies in the workflow must be detected and exceptions have to be handled properly.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-LOGIC-001](../data_exchange_services/README.md#circumvention-of-the-intended-business-logic-istg-des-logic-001).



## Input Validation (ISTG-PHY-INPV)

In order to ensure that only valid and well-formed data enters the processing flows of a device, the input from a all untrustworthy sources, e.g., users or external systems, has to be verified and validated.

### Insufficient Input Validation (ISTG-PHY-INPV-001)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

If no input validation is performed or only an insufficient input validation mechanism is in place an attacker might be able to submit arbitrary and malformed data. Thus, the process, which handles the user input, or another downstream component might stop working properly due to not being able to process the data. This could result in malfunctions that might enable an attacker to manipulate the device behavior or render it unavailable.

**Test Objectives**

- It must be determined whether input to the physical interface is validated.

- In case that an input validation mechanism is implemented, it hast to be checked if there is a way to submit data, which does not comply with the intended data structure and value ranges.

**Step-By-Step Execution**

ToDo

**Remediation**

The device has to validate all input from untrustworthy sources. Malformed or otherwise invalid input must either be rejected or converted into a proper data structure, e.g., by encoding the input. However, it must be ensured that the input is not interpreted or executed when converting it.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-INPV-001](../data_exchange_services/README.md#insufficient-input-validation-istg-des-inpv-001).

### Code or Command Injection (ISTG-PHY-INPV-002)

**Requirements**

| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | PA-2 - PA-4 | depending on whether the interface is connected to a network or not |
| Authorization Access | PA-2 - PA-4 | depending on the access model for the given device |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |

**Summary**

If no input validation is performed or only an insufficient input validation mechanism is in place an attacker might be able to submit code or commands, which then might be executed by the system. It strictly depends on the specific implementation of the device and the physical interface which code and commands are potentially executable. For example, a possible injection attack is OS command injection.

**Test Objectives**

- Based on [ISTG-PHY-INPV-001](#insufficient-input-validation-istg-phy-inpv-001), it must be checked whether it is possible to submit code or commands, which are then executed by the system.

**Step-By-Step Execution**

ToDo

**Remediation**

The device has to validate all input from untrustworthy sources. Malformed or otherwise invalid input must either be rejected or converted into a proper data structure, e.g., by encoding the input. However, it must be ensured that the input is not interpreted or executed when converting it.

**Assessment**

ToDo

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-INPV-002](../data_exchange_services/README.md#code-or-command-injection-istg-des-inpv-002).



[iot_pentesting_guide]: https://www.iotpentestingguide.com	"IoT Pentesting Guide"