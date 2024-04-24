# 2.4 Analysis / Certification Process

In this chapter the process of analyzing the security of an IoT device including relevant parts of the IoT ecosystem is described.

ToDo: More detailed description

The analysis consists of following steps:

1. Create profile for IoT device
2. Create profiles for relevant backend systems and mobile apps
3. Specify scope of analysis and identify relevant test cases
4. Run test cases
5. Assess result

## 1st step: Create profiles for IoT device

The first step is to create a device profile describing the IoT device. The profile should list information for all device components together with relevant technical details.

Information for the device profile could also come directly from the device manufacturer (e.g. using a questionnaire send to the manufacturer).

- List internal components (processing unit, memory, internal interfaces, ...)
-    Add technical details as much as available.
-    Some components are not critical for basic certification (all components requiring PA-4). Despite this still add technical details (when you cant get a hold of them) to aid with execution of test cases and interpretation of results.
- List physical interfaces
-    Have a look at the documentation of the device and add all mentioned physical interfaces to the list.
-    Inspect the enclosure of the IoT device and verify interfaces mentioned in the documentation and add all interfaces not mentioned there.
-    Also remove any easy to remove covers and look under them.
-    Some interfaces may actually be internal interfaces that are also made accessible from outside (ToDo: Develop a proper method to confidently identity them).
- List wireless interfaces
-    Have a look at the documentation of the device and add all mentioned wireless interfaces to the list.
-    Use a wireless sniffer to verify the interfaces mentioned in the documentation and add any newly found interfaces.
- List internal interfaces
-    List all internal interfaces that have physical access level 3 (PA-3)
-    For the sake of simplicity (to avoid duplicating test cases) we still regard them as internal interfaces despite them also meeting the criteria of physical interfaces.
- List data exchange services
-    Have a look at the documentation of the device and add all mentioned data exchange services (e.g. REST APIs, ...) to the list.
-    Do a port scan (TCP & UDP) to verify data exchange services mentioned in the documentation and add any unknown open port to the list
-    Do a service detection for any open port and try do analyse service banners.
- List user interfaces
-    Have a look at the documentation of the device and add all mentioned user interfaces.
-    Inspect the enclosure of the IoT device and verify physical user interfaces mentioned in the documentation and add all interfaces not mentioned there.
-    Add any user interfaces found using a port scan.
- Determine physical access level
-    For the device as a whole
- Determine authorization access level
-    For each revelant component resp. part of the device individually
- Determine security level
-    ToDo: More detailed description

## 2nd step: Create profiles for relevant backend systems and mobile apps

The second step is to also create profiles for relevant backend services and mobile apps. The profiles should list information for all components together with relevant technical details.

Information for the profiles could also come directly from the device manufacturer (e.g. using a questionnaire send to the manufacturer).

- Identify relevant mobile apps
-    Look into the documentation  and list all mobile apps mentioned there
-    Search in relevant app stores
- Identify relevant backend systems
-    Look into the documentation  and list all backend services mentioned there
-    Sniff network traffic during normal device and app operation and record all endpoints the device or app talks to.
	-    Repeat this several times till you don't see new endpoints.
-    Decompile mobile apps and add any endpoint found there
-    Do a simple firmware analysis (e.g. using strings utility) and add any backend URLs found in the firmware
- Create app profiles
-    Similar to 1st step: list any relevant component of the app according to the device profile
-    You can skip internal physical components (processing unit, memory, ...)
-    Determine physical and authorization access and security levels
- Create backend profile
-    Similar to 1st step: list any relevant component of the app according to the device profile
-    You can skip internal physical components (processing unit, memory, ...)
-    Active analysis (port scans or similar) should be avoided unless you have permission of the service provides. Instead rely on passive analysis (e.g. network sniffing).
-    Determine physical and authorization access and security levels

## 3rd step: Specify scope of analysis and identify relevant test cases

In the 3rd step relevant test cases are identified using the profiles created in steps 1 and 2.

- Determine intended scope of the analysis
-    Scope is used to match the verification levels of the test cases.
-    The idea is to have certification profiles (e.g. basic certification, advanced certification, ...) that specify the intended verification levels on a component, category or even test case level.
- Select relevant test cases
-    Each test case comes with a "requirements" section that specifies access, security and verification levels and maybe some other requirements (e.g. firmware type)
-    The test case requirements are then matched against the device and certification profiles to select appropriate test cases.

## 4th step: Run test cases

In the 4th step the selected test cases are run.

- Run the test cases.
-    Each test cases comes with a detailed step-by-step description how the test case should be run for a specific device type.
-    This requires that for new devices type first detailed step-by-step descriptions need to be created before it can be analysed.
-    However, this allows us to easily reproduce device analyses and compare analyses done by different analysts.
-    Furthermore, this also helps with transparency.

## 5th step: Assess test case results

The last step ist about assessing test case results.

- Assess the test case results
-    Each test case comes with an "asssessment" section that describes how results should be correctly interpreted.
-    The correct interpretion of an individual result depends on several factors like e.g. access and security levels.
-    Also here, a detailed assessment section per test case is a requirement for repeatability, comparability and transparency.
-    How to come up with an overall "grade" of a specific device based on the individual test case results should be part of the certification profile.

