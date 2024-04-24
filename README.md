# JSAID OWASP IoT Security Testing Guide


Link to [**JSAID OWASP IoT Security Testing Guide**](./src/README.md)


## JSAID
The Josef Ressel Centre for Security Analysis of IoT Devices (JSAID) is a research center supported by the Christian Doppler Forschungsgesellschaft. JSAID focuses on the security analysis of Consumer IoT (CIoT) devices, which are physical objects connected to a network, such as routers, smartphones, fridges, door locks, and toys. With the proliferation of IoT devices, ensuring their security has become crucial, especially in smart homes where personal data privacy is at risk.

JSAID aims to systematically and reliably evaluate the security of various IoT devices, primarily those used in consumer IoT and smart city sectors. The focus lies on assessing devices' security against both cyber and physical attacks, as well as the security of data transmission. The ultimate goal is to establish an independent certification process for IoT devices, enabling consumers to make informed choices about their purchases.

The consortium behind JSAID comprises three partners: MCI (University of Applied Sciences, Innsbruck, Austria), IKB (Municipal Infrastructure Services Company, Innsbruck, Austria), and AV-Comparatives (Antivirus Software Testing Company, Innsbruck, Austria). Together, their aim is to work towards enhancing the security standards of IoT devices to safeguard user privacy and data integrity.

## Changes compared to original ISTG

- We introduce the [certification process](./src/02_framework/analysis_process.md) as a guidline for penetration testers
  - Prior, only a list of tests was provided by ISTG.
  - We guide testers through the process and assessment of the tests.
- Extended [Device Model Scheme](./src/02_framework/device_model.md#device-model-scheme)
  - ISTG did not consider (Cloud) backend or mobile devices that run applications to use and control the IoT device.
  - For us, the firmware and data exchange service is closely tied to the physical, wireless, and user interface of the IoT device, as opposed to the original ISTG.
  - This is also pictured in the [analysis process](./src/02_framework/analysis_process.md#1st-step-create-profiles-for-iot-device).
- We require a device profile that systematically structures the main components of the device and defines subsequent tests. 
  - As an example, depending on the processing unit and the operating system, different tests have to be conducted if there is embedded Linux running on an IoT device or just a microcontroller running a binary blob of code.
  - This is mapped into the second step of the [analysis process](./src/02_framework/analysis_process.md#2nd-step-create-profiles-for-relevant-backend-systems-and-mobile-apps).
- We introduce additional [security categories](./src/02_framework/attacker_model.md#security-levels), each with four different levels, considering
  - Data Security (DS): Non-Critical Data (DS-1), Sensitive Data (DS-2), Privacy Related Data (DS-3), Confidential Data (DS-4)
  - Security Impact (SI): Insignificant Impact (SI-1), Minor Impact (SI-2), Major Impact (SI-3), Critical Impact (SI-4)
- Within the [Testing Methodology](./src/02_framework/methodology.md) we
    - introduce [Verification Levels](./src/02_framework/methodology.md#verification-levels) to specify the effort required to run a specific test case and to what extend the subject of investigation will be analyzed verification levels are used: Formal verification (VL-1), Method verification (VL-2), Implementation verification (VL-3), Overall verification (VL-4).
    - extend the [Structure of Test Cases](./src/02_framework/methodology.md/#structure-of-test-cases)
        - Requirments: (previously comprised required physical and authentication access levels) Now, includes (besides physical and authentication access level) the data security level, security impact level, verification level, and the firmware type - mapped into the [analysis process](./src/02_framework/analysis_process.md#3rd-step-specify-scope-of-analysis-and-identify-relevant-test-cases).
        - Step-By-Step Execution: detailed list of steps that should be done to execute the test case - mapped into the [analysis process](./src/02_framework/analysis_process.md#4th-step-run-test-cases).
        - Assessment: how the results of the test case should be interpreted - mapped into the [analysis process](./src/02_framework/analysis_process.md#5th-step-assess-test-case-results).
- Example analyses of specific IoT devices (work in progress)
  - [Shelly Duo RGBW GU10](./examples/Shelly_Duo_RGBW_GU10.md)
  - [TP-Link Tapo C100](./examples/TP-Link_Tapo_C100_WiFi-Camera.md)

## Current Activities

- We are currently defining a formal process to include new test cases
  - We already have a pool of potential interesting test cases we want to include.
  - Each test case has a unique permanent identifier that shouldn't be reused, therefore we don't want to burn too many identifiers by being too sloppy.
  - OWASP most probably will also expand their test cases in the future and we need to avoid name collisions.
- We are currently expanding the descriptions of the test cases.
  - Add security and verification levels
  - Refine other sections
  - Add step-by-step descriptions
  - Start with assessment section
- We are currently completing security analyses for selected devices
  - Shelly device, IP cameras and vacuum robots
  - Insights gained will be used for the step-by-step descriptions of the test cases

## ToDo

- How to assess the test case results
  - We need to define how the final "grade" of a device analysis looks like (only Pass/Fail, grades like in school, Percentage of tests passed)
  - Required to finalize assessment sections of test cases
  - Requires further input
- Find more relevant test cases.
  - Do more literature research
  - Talk with interested partners
  - ...
- Do example analyses for more IoT devices
