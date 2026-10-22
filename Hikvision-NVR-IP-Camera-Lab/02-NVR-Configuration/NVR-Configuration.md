Hikvision NVR Configuration



1\. NVR Information



Setting



Configuration



NVR Model



CDNR32P4-4C



Firmware



V4.30.216



IP Address



10.10.10.222



Subnet Mask



255.255.255.0



Default Gateway



10.10.10.1



DNS Hostname



camera.home.local



Web Management Port



8222



Device Management Port



9222



2\. Network Configuration



I configured the NVR with a static IPv4 address on my home network.



The NVR is connected to the 10.10.10.0/24 network, which allows my Windows PC to communicate with it.



I also configured a DNS record on my Windows Server so the NVR could be accessed using camera.home.local.



3\. IP Camera Channels



Channel



Camera IP Address



Status



D1



192.168.60.202



Offline â€” Network Abnormal



D2



192.168.50.3



Online



D3



192.168.50.4



Online



D4



192.168.50.5



Online



4\. Testing and Verification



I verified that the NVR was reachable from my Windows PC.



I tested network connectivity using PowerShell and confirmed that the NVR management ports were accessible.



I also used Hikvision iVMS-4200 and the NVR web interface to confirm that three outdoor cameras were online and displaying live video.



5\. Troubleshooting



Channel D1 was configured to connect to the Hikvision door station at 192.168.60.202 using management port 8000.



The channel reported a Network Abnormal error.



The door station and indoor monitor are on a different subnet from the three working IP cameras. Testing did not establish a working network path between the NVR camera network and the door station.



I documented the issue without changing the working camera and intercom configurations.



6\. Results



NVR accessible from the home network.



DNS hostname configured.



Three outdoor IP cameras online.



Live camera viewing verified.



Door station integration remains unresolved.


