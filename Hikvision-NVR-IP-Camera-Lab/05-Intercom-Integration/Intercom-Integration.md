Hikvision Door Station \& Indoor Monitor Integration



1\. Overview



As part of my Hikvision home lab, I investigated how to integrate my Hikvision door station with the existing NVR surveillance system.



The door station and indoor monitor already communicate successfully. My goal was to display the door station camera alongside the three outdoor cameras on the NVR.



2\. Equipment



Device



Model



IP Address



Door Station



DS-KD8003-IME1



192.168.60.202



Indoor Monitor



CD-KH6320-TE1



192.168.60.201



NVR



CDNR32P4-4C



10.10.10.222



3\. Intercom Network Configuration



The door station and indoor monitor use the 192.168.60.0/24 network.



Their configured network settings include:



Subnet mask: 255.255.255.0



Default gateway: 192.168.60.1



Door station management port: 8000



The intercom devices are connected through a powered Hikvision network device, with an Ethernet connection extending toward the NVR system.



4\. Working Features



I verified that:



The door station communicates with the indoor monitor.



The indoor monitor displays video from the door station.



The intercom video session works independently of the NVR.



The three existing outdoor cameras continue operating normally.



5\. NVR Integration Attempt



I configured NVR channel D1 to use the door station IP address 192.168.60.202 and management port 8000.



However, the NVR reported the camera as offline with a "Network Abnormal" message.



Additional testing indicated that a working network path to the door station had not been established.



6\. Troubleshooting Findings



The outdoor cameras use the 192.168.50.0/24 network, while the intercom devices use 192.168.60.0/24.



I investigated the network configuration and tested connectivity without changing the existing IP addresses.



The door station remained functional through the indoor monitor.



7\. Current Status



Intercom system: Operational



NVR door station integration: Unresolved



I preserved the working configuration and documented the remaining network issue for future investigation.



8\. Skills Demonstrated



IP intercom system troubleshooting



IPv4 addressing and subnetting



NVR camera channel configuration



Network connectivity testing



Device integration troubleshooting



Technical documentation


