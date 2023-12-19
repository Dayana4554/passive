Passive

Introduction

Passive is a tool designed for passive reconnaissance, a crucial step in penetration testing and open source intelligence gathering. The tool automates the process of collecting information without directly interacting with the target, making it an essential asset for ethical hackers and cybersecurity researchers.

Objective

The primary goal of Passive is to familiarize users with open-source investigative methods, enhancing their skills in passive information gathering. This tool is intended to streamline the process of collecting actionable intelligence in a non-intrusive manner.

Guidelines

Passive is a versatile tool capable of recognizing and processing different types of input:

-Full Name: Searches directories for telephone numbers and addresses associated with the given name.
-IP Address: Displays the city and the name of the internet service provider for the provided IP.
-Username: Checks if the username is used on at least 5 known social networks.

The results are stored in a text file (result.txt, result2.txt if the file already exists).

Bonus Features

-Additional API integrations for broader reconnaissance capabilities.

Usage

Passive is easy to use with command-line options for various types of searches:

```bash
$> passive --help
Welcome to passive v1.0.0
OPTIONS:
    -fn         Search with full-name
    -ip         Search with ip address
    -u          Search with username
```

Examples

-Searching with a full name:

```bash

$> passive -fn "Jean Dupont"
```

Output:

```

First name: Jean
Last name: Dupont
Address: 7 rue du Progrès
75016 Paris
Number: +33601010101
Saved in result.txt
```

-Searching with an IP address:

```bash

$> passive -ip 127.0.0.1
```

Output:

```
ISP: FSociety, S.A.
City Lat/Lon: (13.731) / (-1.1373)
Saved in result2.txt
```

-Searching with a username:

```bash
$> passive -u "@user01"
```

Output:

```
Facebook : yes
Twitter : yes
Linkedin : yes
Instagram : no
Skype : yes
Saved in result3.txt
```
