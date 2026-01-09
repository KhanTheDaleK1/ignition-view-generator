import json

def indent_code(code):
    return "\n".join(["\t" + line for line in code.strip().split("\n")])

# Define scripts using explicit string concatenation to avoid syntax errors
raw_import_script = (
    "import csv\n"
    "import os\n"
    "import system\n"
    "\n"
    "csv_path = \"/mnt/projects/12. DCIM_Assets/DTS_Scan_Clean.csv\"\n"
    "base_path = \"[default]DataCenter/Hall1\"\n"
    "\n"
    "udt_map = {\n"
    "    \"UPS\": \"Assets/Asset_UPS\",\n"
    "    \"PDU\": \"Assets/Asset_PDU\",\n"
    "    \"Sensor\": \"Assets/Env_Sensor\",\n"
    "    \"Server\": \"Assets/IT_Server\",\n"
    "    \"Switch\": \"Assets/Asset_Switch\",\n"
    "    \"PLC\": \"Assets/Asset_PLC\",\n"
    "    \"Workstation\": \"Assets/Asset_Workstation\"\n"
    "}\n"
    "\n"
    "status = \"Starting...\"\n"
    "if not os.path.exists(csv_path):\n"
    "    status = \"Error: CSV not found at \" + csv_path\n"
    "else:\n"
    "    try:\n"
    "        f = open(csv_path, 'r')\n"
    "        reader = csv.DictReader(f)\n"
    "        configs = []\n"
    "        \n"
    "        for row in reader:\n"
    "            ip = row.get('IP Address', row.get('IP', ''))\n"
    "            hostname = row.get('Hostname', '')\n"
    "            vendor = row.get('Vendor', row.get('MAC Vendor', ''))\n"
    "            \n"
    "            if not ip or ip == '[n/a]': continue\n"
    "            \n"
    "            if hostname and hostname not in ['[n/a]', '[s]', '']:\n"
    "                safe_name = hostname\n"
    "            else:\n"
    "                safe_name = \"Dev_\" + ip.replace('.', '_')\n"
    "            \n"
    "            safe_name = ''.join([c if c.isalnum() else '_' for c in safe_name])\n"
    "            \n"
    "            # Simple Mapping\n"
    "            v_lower = str(vendor).lower()\n"
    "            udt_id = \"Assets/IT_Server\"\n"
    "            if any(x in v_lower for x in [\"apc\", \"schneider\", \"american power\"]): udt_id = \"Assets/Asset_UPS\"\n"
    "            elif any(x in v_lower for x in [\"cisco\", \"ubiquiti\", \"netgear\"]): udt_id = \"Assets/Asset_Switch\"\n"
    "            elif any(x in v_lower for x in [\"beckhoff\", \"siemens\"]): udt_id = \"Assets/Env_Sensor\"\n"
    "            \n"
    "            configs.append({\n"
    "                \"name\": safe_name,\n"
    "                \"typeId\": udt_id,\n"
    "                \"tagType\": \"UdtInstance\",\n"
    "                \"parameters\": {\n"
    "                    \"IP_Address\": ip,\n"
    "                    \"Location_Row\": row.get('Location_Row', 'A'),\n"
    "                    \"Location_Rack\": row.get('Location_Rack', '1')\n"
    "                }\n"
    "            })\n"
    "            \n"
    "        f.close()\n"
    "        \n"
    "        if configs:\n"
    "            system.tag.configure(base_path, configs, \"o\")\n"
    "            status = \"Success! Imported %d devices.\" % len(configs)\n"
    "        else:\n"
    "            status = \"No valid devices found.\"\n"
    "            \n"
    "    except Exception as e:\n"
    "        status = \"Error: \" + str(e)\n"
    "\n"
    "self.view.custom.importStatus = status"
)

raw_browse_script = (
    "tags = system.tag.browse(\"[default]DataCenter/Hall1\")\n"
    "results = []\n"
    "for tag in tags:\n"
    "    results.append({\n"
    "        \"name\": str(tag['name']),\n"
    "        \"typeId\": str(tag.get('typeId', 'N/A'))\n"
    "    })\n"
    "self.view.custom.tagList = results\n"
    "self.view.custom.tagCount = len(results)"
)

view_data = {
  "custom": {
    "importStatus": "Ready",
    "tagList": [],
    "tagCount": 0
  },
  "params": {},
  "props": { "defaultSize": { "height": 800, "width": 1280 } },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": { "direction": "column", "style": { "backgroundColor": "#121212", "padding": "20px", "gap": "20px" } },
    "children": [
      {
        "type": "ia.display.label",
        "meta": { "name": "Title" },
        "props": { "text": "DCIM ADMIN CONSOLE", "style": { "color": "#FF6600", "fontSize": "24px", "fontWeight": "bold" } }
      },
      {
        "type": "ia.container.flex",
        "meta": { "name": "Actions" },
        "props": { "direction": "row", "gap": "20px", "alignItems": "center" },
        "children": [
          {
            "type": "ia.input.button",
            "meta": { "name": "ImportBtn" },
            "props": { "text": "RUN ROBUST IMPORT", "style": { "backgroundColor": "#00AAFF", "color": "#FFF", "fontWeight": "bold", "width": "250px" } },
            "events": {
              "component": {
                "onActionPerformed": { "config": { "script": indent_code(raw_import_script) }, "scope": "G", "type": "script" }
              }
            }
          },
          {
            "type": "ia.display.label",
            "meta": { "name": "StatusLabel" },
            "propConfig": { "props.text": { "binding": { "config": { "path": "view.custom.importStatus" }, "type": "property" } } },
            "props": { "style": { "color": "#FFF", "fontFamily": "monospace" } }
          }
        ]
      },
      {
        "type": "ia.container.flex",
        "meta": { "name": "BrowseRow" },
        "props": { "direction": "row", "gap": "20px", "alignItems": "center" },
        "children": [
          {
            "type": "ia.input.button",
            "meta": { "name": "RefreshBtn" },
            "props": { "text": "BROWSE TAGS", "style": { "backgroundColor": "#444", "color": "#FFF" } },
            "events": {
              "component": {
                "onActionPerformed": { "config": { "script": indent_code(raw_browse_script) }, "scope": "G", "type": "script" }
              }
            }
          },
          {
            "type": "ia.display.label",
            "meta": { "name": "CountLabel" },
            "propConfig": { "props.text": { "binding": { "config": { "expression": "'Found: ' + {view.custom.tagCount}" }, "type": "expr" } } },
            "props": { "style": { "color": "#AAA", "fontSize": "14px" } }
          }
        ]
      },
      {
        "type": "ia.display.table",
        "meta": { "name": "TagTable" },
        "position": { "grow": 1 },
        "props": {
          "data": { "binding": { "config": { "path": "view.custom.tagList" }, "type": "property" } },
          "columns": [
            { "field": "name", "header": { "title": "Tag Name" } },
            { "field": "typeId", "header": { "title": "Type ID" } }
          ],
          "pager": { "bottom": True },
          "rows": { "enabled": True, "perPage": 100 },
          "style": { "backgroundColor": "#FFF" }
        }
      }
    ]
  }
}

with open('/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/Admin/view.json', 'w') as f:
    json.dump(view_data, f, indent=2)
print("Successfully generated Admin view.json")
