# Security & System Monitoring API (FastAPI)
This project demonstrates a multi‑endpoint backend system built with FastAPI.
It provides system status, hardware information, active nodes, security blacklists, firewall logs, and dynamic path parameters.

# Purpose
The API simulates a monitoring dashboard for a server or security system.
It exposes multiple GET endpoints that return structured JSON data.

## Features
- FastAPI application
- Multiple GET endpoints
- Static system information
- Security blacklist and firewall logs
- Dynamic URL parameters (server_id, country, node_id)
- In‑memory data structures for quick access

# Endpoints Overview
1. /status
Returns the current system status.

2. /system-info
Provides API version, security level, and hardware usage.

3. /active-nodes
Shows the number of active nodes and their locations.

4. /security/blacklist
Returns the number of blocked IPs and the blacklist contents.

5. /security/logs
Returns firewall events and severity levels.

6. /server/{server_id}
Dynamic endpoint returning information about a specific server.

7. /network/{country}/{node_id}
Dynamic endpoint returning information about a specific network node.


## Learning Purpose
This project helps practice:
- Building multiple GET endpoints
- Returning structured JSON responses
- Using lists and dictionaries as in‑memory data
- Handling dynamic path parameters
- Designing a simple monitoring/security API
- Understanding how backend services expose system information
