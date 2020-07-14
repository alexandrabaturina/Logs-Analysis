# Logs Analysis
## Overview
The **logs_analysis.py** is reporting tool to analyze the reader's activity on newspaper site. The database to analyze contains newspaper articles as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The **log_analysis.py** script is written as first assignment of [Full Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044) provided by Udacity.
## Features
The **logs_analysis.py** script prints out the following information from the **news** database:
  - Three most popular articles of all time
  - The most popular article authors of all time
  - Days when more than 1% of requests lead to errors
## Getting Started
### Prerequisites
To use LogsAnalysis, the following software and data are required:
  - *VirtualBox* – software to run the virtual machine. Download from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
  - *Vagrant* – software to configure virtual machine. Download the version for your operating system from [here](https://www.vagrantup.com/downloads.html)
  - The virtual machine configuration file. Download and unzip [this file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
  - The *newsdata.sql* file. Download from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip

### Starting the Virtual Machine
Change to the directory containing virtual machine files. Find the **vagrant** directory and change to it. Inside the **vagrant** directory, run the following command.
```sh
$ vagrant up
```
Once **vagrant up** is finished running, log in to the virtual machine using the following command.
```sh
$ vagrant ssh
```
### Loading the Data to the Database
Place the unziped *newsdata.sql* file to the **vagrant** directory. To load the data, from the **vagrant** directory, run the following command.
```sh
$ psql -d news -f newsdata.sql
```
### Creating Views
In the terminal, type the following commands to create __errors__ and __total__ views in the database.
```sh
$ create view errors as
$ select date(time) as time, count(*) as count_errors
$ from log
$ where status != '200 OK'
$ group by date(time);
```
```sh
$ create view total as
$ select date(time) as time, count(*) as count_requests
$ from log
$ group by date(time);
```
## Running
To run LogsAnalysis from the terminal, use the following command.
```sh
$  python LogsAnalysis.py
```
## Authors
  + Alexandra Baturina
