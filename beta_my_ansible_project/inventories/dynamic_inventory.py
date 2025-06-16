#!/usr/bin/env python3

import json
import sys

def main():
    inventory = {
        "_meta": {
            "hostvars": {}
        },
        "staging": {
            "hosts": ["stage-web-01", "stage-app-01"],
            "vars": {
                "ansible_user": "ansible_admin",
            }
        },
        "production": {
            "hosts": ["prod-web-01", "prod-app-01"],
            "vars": {
                "ansible_user": "ansible_admin",
            }
        },
        "web_servers": {
            "hosts": ["stage-web-01", "prod-web-01"]
        },
        "app_servers": {
            "hosts": ["stage-app-01", "prod-app-01"]
        },
        "db_servers": {
            "hosts": ["stage-app-01", "prod-app-01"]
        }
    }

    inventory["_meta"]["hostvars"]["stage-web-01"] = {"ansible_host": "192.168.3.41"}
    inventory["_meta"]["hostvars"]["stage-app-01"] = {"ansible_host": "192.168.3.42"}
    inventory["_meta"]["hostvars"]["prod-web-01"] = {"ansible_host": "192.168.3.45"}
    inventory["_meta"]["hostvars"]["prod-app-01"] = {"ansible_host": "192.168.3.46"}

    print(json.dumps(inventory, indent=4))

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        main()
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps({}))
    else:
        main()
