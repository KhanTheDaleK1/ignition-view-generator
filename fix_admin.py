import json

def indent_code(code):
    """Indents the code block with one tab for Perspective script execution context."""
    return "\n".join(["\t" + line for line in code.strip().split("\n")])

# Define the import script (Standard Python indentation, will be indented by helper)
raw_import_script = """
import csv
import os
import system

csv_path = "/mnt/projects/12. DCIM_Assets/DTS_Scan_Clean.csv"
base_path = "[default]DataCenter/Hall1"

udt_map = {
    "UPS": "Assets/Asset_UPS",
    "PDU": "Assets/Asset_PDU",
    "Sensor": "Assets/Env_Sensor",
    "Server": "Assets/IT_Server",
    "Switch": "Assets/Asset_Switch",
    "PLC": "Assets/Asset_PLC",
    "Workstation": "Assets/Asset_Workstation"
}

status = "Starting..."
if not os.path.exists(csv_path):
    status = "CSV Not Found"
else:
    tags_to_configure = []
    try:
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                device_name = row.get('Hostname', 'Unknown').replace('.', '_').replace('\\', '_').replace('/', '_')
                ip_addr = row.get('IP Address', '0.0.0.0')
                dev_type = row.get('Type', 'Unknown')
                loc_row = row.get('Location_Row', '')
                loc_rack = row.get('Location_Rack', '')
                
                if dev_type in udt_map:
                    tags_to_configure.append({
                        "name": device_name,
                        "typeId": udt_map[dev_type],
                        "tagType": "UdtInstance",
                        "parameters": {
                            "IP_Address": ip_addr,
                            "Location_Row": loc_row,
                            "Location_Rack": loc_rack
                        }
                    })
        
        if tags_to_configure:
            system.tag.configure(base_path, tags_to_configure, "o")
            status = "Imported %d tags" % len(tags_to_configure)
        else:
            status = "No matching tags found"
    except Exception as e:
        status = "Error: " + str(e)
        
self.view.custom.importStatus = status
"""

raw_browse_script = """
tags = system.tag.browse("[default]DataCenter/Hall1")
results = []
for tag in tags:
    results.append({"name": str(tag['name']), "typeId": str(tag.get('typeId', 'N/A'))})
self.view.custom.tagList = results
self.view.custom.tagCount = len(results)
"""

view_data = {
  "custom": {
    "importStatus": "Ready",
    "tagList": [],
    "tagCount": 0
  },
  "params": {},
  "props": {
    "defaultSize": { "height": 800, "width": 1280 }
  },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": { "backgroundColor": "#121212", "padding": "20px", "gap": "20px" }
    },
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
            "props": { "text": "RUN TAG IMPORT", "style": { "backgroundColor": "#00AAFF", "color": "#FFF" } },
            "events": {
              "component": {
                "onActionPerformed": {
                  "config": {
                    "script": indent_code(raw_import_script)
                  },
                  "scope": "G",
                  "type": "script"
                }
              }
            }
          },
          {
            "type": "ia.display.label",
            "meta": { "name": "StatusLabel" },
            "propConfig": {
              "props.text": {
                "binding": { "config": { "path": "view.custom.importStatus" }, "type": "property" }
              }
            },
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
                "onActionPerformed": {
                  "config": {
                    "script": indent_code(raw_browse_script)
                  },
                  "scope": "G",
                  "type": "script"
                }
              }
            }
          },
          {
            "type": "ia.display.label",
            "meta": { "name": "CountLabel" },
            "propConfig": {
              "props.text": {
                "binding": { "config": { "expression": "\"Found: \" + {view.custom.tagCount}" }, "type": "expr" }
              }
            },
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
          "pager": { "bottom": True, "top": False },
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
