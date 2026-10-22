Hikvision IP Camera Setup



1\. Overview



In this part of my home lab, I worked with three outdoor IP cameras connected to my Hikvision Network Video Recorder (NVR).



I used the NVR management interface and Hikvision iVMS-4200 to check camera connectivity, verify their status, and view live video.



2\. Camera Network Configuration



NVR Channel



IP Address



Status



D2



192.168.50.3



Online



D3



192.168.50.4



Online



D4



192.168.50.5



Online



The three cameras use the 192.168.50.0/24 subnet.



This is separate from the NVR's home LAN address of 10.10.10.222.



3\. Power over Ethernet (PoE)



The surveillance setup uses Ethernet and PoE connections.



PoE allows compatible network cameras to receive electrical power and network connectivity through Ethernet cabling.



I inspected the NVR camera connections and investigated how the camera network communicates with the recorder.



4\. Camera Testing



I performed the following checks:



Opened the Hikvision NVR management interface.



Checked the camera management page.



Verified that channels D2, D3, and D4 were online.



Confirmed live video was available.



Used iVMS-4200 to access the surveillance system.



Reviewed the camera IP addresses and network configuration.



5\. Results



All three outdoor IP cameras were operational during testing.



The NVR successfully displayed live video from the connected cameras.



The fourth channel, D1, was configured for the Hikvision door station but remained offline. This issue is documented separately in the network troubleshooting section.



6\. Skills Demonstrated



IP camera administration



IPv4 addressing



Network segmentation



PoE networking fundamentals



NVR channel management



Camera connectivity testing



Technical troubleshooting


