import json

from fastapi import FastAPI


app = FastAPI()





blacklisted_ips = ["192.168.1.5", "10.0.0.99"]

firewall_logs = [
    {"timestamp" : "07:00", "event" : "Brute Force Attack", "severity" : "HEIGH"},
    {"timestamp" : "07:05", "event" : "Port Scan Detected", "severity" : "MEDIUM"}
]


@app.get("/status")
def status_request():
    return {"status" : "online"}


@app.get("/system-info")
def get_info():
    return {
        "api_vesion" : "1.0.0",
        "security_level" : "maximum",
        "hardware": {
            "cpu_load_precent" : 12,
            "ram_usage_gb" : 4
        }
    }


@app.get("/active-nodes")
def get_nodes():
    return {
        "total_active" : 3,
        "locations" : ["Amsterdam", "Brabant", "Rotterdam"]
    }


@app.get("/security/blacklist")
def get_blacklist():
    return {"total_block" : 2, "ips" : blacklisted_ips}


@app.get("/security/logs")
def get_logs():
    return {"total_logs" : 2, "events" : firewall_logs}


@app.get("/server/{server_id}")
def get_specific_server(server_id: int):
    return {"message": f"Right now, you're watching server {server_id}"}


@app.get("/network/{country}/{node_id}")
def search_country_id(country: str, node_id: int):
    return {"message": f"Country: {country}, Node: {node_id}"}
