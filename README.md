# Network Utilization Monitor using Mininet and POX

## Project Overview

This project implements a Software Defined Networking (SDN)-based network monitoring system using Mininet and the POX controller. It measures and displays bandwidth utilization across a simulated network in real time.

The controller collects flow statistics from OpenFlow switches and computes bandwidth usage periodically.

---

## Objectives

* Simulate a network topology using Mininet
* Implement an SDN controller using POX
* Collect traffic statistics from switches
* Calculate bandwidth utilization
* Display real-time monitoring output

---

## Technologies Used

* Mininet – Network simulation
* POX Controller – SDN controller
* OpenFlow Protocol – Communication between switch and controller
* Python – Implementation

---

## Network Topology

* Single switch (s1)
* Multiple hosts (h1, h2, h3)
* Hosts connected to switch

---

## Installation and Setup

### Install Mininet

```bash
sudo apt update
sudo apt install mininet
```

### Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox.git
```

---

## How to Run

### Start POX Controller

```bash
cd ~/Desktop/pox
./pox.py forwarding.l2_learning monitor
```

### Run Mininet Topology

```bash
sudo mn --topo single,3 --controller=remote
```

### Test Connectivity

```bash
pingall
```

---

## Bandwidth Monitoring Logic

The controller periodically requests flow statistics from the switches. The total number of bytes transferred is tracked over time, and bandwidth is calculated using the difference between consecutive readings.

Bandwidth = (Current Bytes - Previous Bytes) / Time Interval

The output is displayed in Mbps.

---

## Results

* Successful creation of network topology
* Verified host connectivity
* Traffic generated using ping and iperf
* Real-time bandwidth monitoring achieved

---

## Project Structure

```
network-monitor-project/
│── monitor.py
│── README.md
│── screenshots/
```

---

## Challenges Faced

* Compatibility issues with Python versions
* Controller module import errors
* GitHub authentication using personal access tokens
* Mininet cleanup and interface conflicts

---

## Conclusion

This project demonstrates the use of SDN for network monitoring. It provides a flexible and scalable approach to measure bandwidth usage dynamically in a simulated environment.

---

## Future Scope

* Graphical visualization of bandwidth
* Integration with real-time dashboards
* Support for larger network topologies
* Alert mechanisms for abnormal traffic

---

## Author

Praakruthi
BTech CSE – PES University
