Hikvision Network Troubleshooting



1\. Problem Description



During my Hikvision home lab project, I investigated why the NVR could display three outdoor IP cameras but could not connect to the Hikvision door station on channel D1.



The NVR reported the D1 channel as offline with a "Network Abnormal" error.



2\. Network Information



Device



IP Address



Network



Windows PC



10.10.10.138



10.10.10.0/24



Home Router



10.10.10.1



10.10.10.0/24



Hikvision NVR



10.10.10.222



10.10.10.0/24



Outdoor Camera D2



192.168.50.3



192.168.50.0/24



Outdoor Camera D3



192.168.50.4



192.168.50.0/24



Outdoor Camera D4



192.168.50.5



192.168.50.0/24



Indoor Monitor



192.168.60.201



192.168.60.0/24



Door Station



192.168.60.202



192.168.60.0/24



3\. Troubleshooting Tools



I used the following tools:



Windows PowerShell



Test-NetConnection



ping



tracert



Hikvision HiTools



Hikvision NVR web management interface



4\. Network Connectivity Tests



NVR Connectivity



I used PowerShell to test communication with the NVR.



Test-NetConnection 10.10.10.222 -Port 9222

Test-NetConnection 10.10.10.222 -Port 8222



Both management ports were reachable during testing.



Door Station Connectivity



I investigated connectivity to the door station at 192.168.60.202.



ping 192.168.60.202

tracert 192.168.60.202



The tests did not establish successful communication with the door station.



The traceroute reached the home router at 10.10.10.1, but subsequent hops did not respond.



5\. Subnetting Investigation



The NVR home network uses 10.10.10.0/24.



The three operational outdoor cameras use 192.168.50.0/24.



The door station and indoor monitor use 192.168.60.0/24.



These are separate IPv4 subnets. Communication between them requires an appropriate network path, such as routing or a supported network configuration.



The existing tests did not confirm a working route from the NVR camera network to the door station.



6\. Device Status Investigation



I reviewed the NVR camera channels and found:



D1: Offline â€” Network Abnormal



D2: Online



D3: Online



D4: Online



An authenticated NVR status check also reported D1 as unreachable.



The door station and indoor monitor continued communicating with each other successfully.



7\. Troubleshooting Outcome



I confirmed that the NVR and three outdoor cameras were working.



I identified the different IP subnets involved in the door station integration issue.



I decided not to change the working device addresses or network connections without verifying a safe configuration.



The D1 connectivity issue remains unresolved and is documented for future troubleshooting.



8\. Skills Demonstrated



IPv4 subnetting



TCP/IP troubleshooting



PowerShell network diagnostics



Port connectivity testing



Network path investigation



NVR troubleshooting



Technical documentation


