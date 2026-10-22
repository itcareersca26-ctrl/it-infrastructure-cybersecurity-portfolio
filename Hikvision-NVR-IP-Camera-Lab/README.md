> **Privacy Notice:** IP addresses and network subnets in this public
> project have been anonymized for security and privacy.
> They represent the original network design but are not the
> actual addresses used during testing.
# Hikvision NVR & IP Camera Home Lab



Project Overview



This project documents my hands-on experience setting up, managing, and troubleshooting an IP camera surveillance system in my home IT lab.



I worked with a network video recorder (NVR), three operational outdoor IP cameras, a Hikvision door station, and an indoor intercom monitor.



My goal was to configure the surveillance system, establish reliable network connectivity, monitor camera status, and troubleshoot communication problems between devices.



Equipment and Software



Network Video Recorder: CDNR32P4-4C



Hikvision Door Station: DS-KD8003-IME1



Indoor Intercom Monitor: CD-KH6320-TE1



Three outdoor IP security cameras



Hikvision HiTools



Hikvision iVMS-4200



Windows PowerShell



Windows Server DNS



Ethernet and Power over Ethernet (PoE) networking



Work Completed



Configured the NVR with a static IP address.



Verified that three IP cameras were online and displaying live video.



Configured DNS resolution using camera.home.local.



Used Hikvision HiTools to discover and inspect network devices.



Used PowerShell to test IP connectivity and network ports.



Investigated different IP subnets and gateway settings.



Verified communication between the door station and indoor monitor.



Investigated the fourth NVR camera channel reporting a network error.



Troubleshooting Results



Three security cameras are operational and accessible through the NVR.



The door station and indoor monitor communicate successfully with each other.



The fourth NVR channel remains offline because communication between the NVR camera network and the door station's subnet has not been established.



I documented the issue and preserved the working camera and intercom configurations rather than making unverified changes.



Skills Demonstrated



IP camera and NVR administration



TCP/IP addressing and subnetting



Power over Ethernet (PoE)



Network troubleshooting



DNS configuration



PowerShell network diagnostics



Device discovery and management



Technical documentation



Project Status



Partially Completed â€” Three Cameras Operational



The surveillance system is operational with three working cameras. Door station integration into the NVR remains a future improvement.



Evidence



Screenshots and configuration notes will be added to the project folders after reviewing them for sensitive information.




