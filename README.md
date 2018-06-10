# Sites Monitoring Utility

Utility to check the status of our sites. At the entrance-a text file with URL addresses to check. The output-the status of each site on the results of the following checks:
* the server responds to an HTTP 200 status request;
* the domain name of the site is paid for at least 1 month in advance.

# Installation
```bash
pip install -r requirements.txt # alternatively try pip3
```
# Usage
```bash
python check_sites_health.py -f urls.txt
Domains statuses:
Url                                                          |      Is URL ok       |    Domain status
----------------------------------------------------------------------------------------------------
https://service.jet.su                                       |         yes          |       expired
https://service.jet.sua                                      |          no          |        error
https://google.com                                           |         yes          |          OK
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
