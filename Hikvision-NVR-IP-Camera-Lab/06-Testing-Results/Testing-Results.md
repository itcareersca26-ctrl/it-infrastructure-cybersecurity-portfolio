Hikvision NVR \& IP Camera Testing Results



1\. Testing Overview



I performed network connectivity and camera status tests to verify the operation of my Hikvision surveillance system.



I used Windows PowerShell, the Hikvision NVR web interface, HiTools, and iVMS-4200.



2\. Test Results



Test



Result



Status



NVR network connectivity



NVR reachable at 10.10.10.222



PASS



NVR management port 9222



TCP connection successful



PASS



NVR web port 8222



TCP connection successful



PASS



DNS resolution



camera.home.local resolves to 10.10.10.222



PASS



Camera D2



Online and displaying video



PASS



Camera D3



Online and displaying video



PASS



Camera D4



Online and displaying video



PASS



Door station to indoor monitor



Video communication working



PASS



NVR channel D1



Network Abnormal



FAIL



Door station connectivity from Windows PC



No successful network connection established



FAIL



3\. PowerShell Network Tests



I used these commands to check the NVR:



Test-NetConnection 10.10.10.222 -Port 9222

Test-NetConnection 10.10.10.222 -Port 8222



Both tests confirmed successful TCP connectivity.



I also investigated the door station using:



ping 192.168.60.202

tracert 192.168.60.202



The tests did not confirm connectivity to the door station.



4\. Camera Verification



I checked the NVR camera management interface and verified that three outdoor cameras were online.



I also confirmed that live video was available through the NVR and iVMS-4200.



5\. Troubleshooting Outcome



The NVR and three outdoor cameras are operational.



The door station and indoor monitor are also functioning together.



However, channel D1 remains offline because the NVR has not established communication with the door station.



I preserved the working configuration and documented the issue for future troubleshooting.



6\. Final Project Status



Three IP cameras operational â€” NVR accessible â€” Intercom operational â€” D1 integration unresolved.


