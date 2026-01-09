import json

def indent_code(code):
    return "\n".join(["\t" + line for line in code.strip().split("\n")])

# Define the script code for the repeaters using explicit tabs and paths
# OPTIMIZATION: Limit to top 25 devices per column to prevent browser lag
limit = 25

# 1. CORE SWITCHES
raw_script_core = (
    "try:\n"
    "    devices = []\n"
    "    path = '[default]DataCenter/Hall1'\n"
    "    tags = system.tag.browse(path)\n"
    "    if not tags: return []\n"
    "    for tag in tags:\n"
    "        type_id = str(tag.get('typeId', ''))\n"
    "        if 'Switch' in type_id:\n"
    "            devices.append({'tagPath': str(tag['fullPath']), 'deviceType': 'Switch'})\n"
    "    return devices[:25] # Optimization\n"
    "except: return []"
)

# 2. COMPUTE (Servers)
raw_script_compute = (
    "try:\n"
    "    devices = []\n"
    "    path = '[default]DataCenter/Hall1'\n"
    "    tags = system.tag.browse(path)\n"
    "    if not tags: return []\n"
    "    for tag in tags:\n"
    "        type_id = str(tag.get('typeId', ''))\n"
    "        if 'Server' in type_id or 'Workstation' in type_id:\n"
    "            devices.append({'tagPath': str(tag['fullPath']), 'deviceType': 'Server'})\n"
    "    return devices[:25] # Optimization\n"
    "except: return []"
)

# 3. POWER (UPS/PDU)
raw_script_power = (
    "try:\n"
    "    devices = []\n"
    "    path = '[default]DataCenter/Hall1'\n"
    "    tags = system.tag.browse(path)\n"
    "    if not tags: return []\n"
    "    for tag in tags:\n"
    "        type_id = str(tag.get('typeId', ''))\n"
    "        if 'UPS' in type_id:\n"
    "            devices.append({'tagPath': str(tag['fullPath']), 'deviceType': 'UPS'})\n"
    "        elif 'PDU' in type_id:\n"
    "            devices.append({'tagPath': str(tag['fullPath']), 'deviceType': 'UPS'})\n"
    "    return devices[:25] # Optimization\n"
    "except: return []"
)

# 4. EDGE (Sensors/PLC)
raw_script_edge = (
    "try:\n"
    "    devices = []\n"
    "    path = '[default]DataCenter/Hall1'\n"
    "    tags = system.tag.browse(path)\n"
    "    if not tags: return []\n"
    "    for tag in tags:\n"
    "        type_id = str(tag.get('typeId', ''))\n"
    "        if 'Sensor' in type_id:\n"
    "            devices.append({'tagPath': str(tag['fullPath']), 'deviceType': 'Sensor'})\n"
    "        elif 'PLC' in type_id:\n"
    "            devices.append({'tagPath': str(tag['fullPath']), 'deviceType': 'Sensor'})\n"
    "    return devices[:25] # Optimization\n"
    "except: return []"
)

view_data = {
  "custom": {},
  "params": {},
  "props": {
    "defaultSize": { "height": 1080, "width": 1920 }
  },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": { "backgroundColor": "#121212", "padding": "20px" }
    },
    "children": [
      {
        "type": "ia.display.label",
        "meta": { "name": "Title" },
        "props": {
          "text": "NETWORK TOPOLOGY DIAGRAM",
          "style": { "color": "#FF6600", "fontSize": "24px", "fontWeight": "bold", "marginBottom": "20px", "borderBottom": "2px solid #333" }
        }
      },
      {
        "type": "ia.container.flex",
        "meta": { "name": "DiagramBody" },
        "position": { "grow": 1 },
        "props": {
          "direction": "row",
          "style": { "gap": "40px", "height": "100%" }
        },
        "children": [
          {
            "type": "ia.container.flex",
            "meta": { "name": "Col_Core" },
            "position": { "grow": 1, "basis": "0" },
            "props": {
              "direction": "column",
              "style": { "backgroundColor": "#1E1E1E", "borderRadius": "10px", "padding": "15px", "borderTop": "5px solid #00AAFF" }
            },
            "children": [
              { "type": "ia.display.label", "props": { "text": "CORE NETWORK (TOP 25)", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
              { "type": "ia.display.image", "props": { "source": "/system/images/Icon_Switch.svg", "style": { "height": "64px", "marginBottom": "15px" } } },
              {
                "type": "ia.display.flex-repeater",
                "meta": { "name": "Switch_Repeater" },
                "position": { "grow": 1 },
                "propConfig": {
                  "props.instances": {
                    "binding": {
                      "type": "tag",
                      "config": { "path": "[default]DataCenter/Hall1" },
                      "transforms": [ { "code": indent_code(raw_script_core), "type": "script" } ]
                    }
                  }
                },
                "props": {
                  "path": "Page/DCIM/Device_Node_Template",
                  "direction": "column",
                  "style": { "gap": "5px", "overflowY": "auto" }
                }
              }
            ]
          },
          {
            "type": "ia.container.flex",
            "meta": { "name": "Col_Compute" },
            "position": { "grow": 1, "basis": "0" },
            "props": {
              "direction": "column",
              "style": { "backgroundColor": "#1E1E1E", "borderRadius": "10px", "padding": "15px", "borderTop": "5px solid #AA00FF" }
            },
            "children": [
              { "type": "ia.display.label", "props": { "text": "COMPUTE & STORAGE (TOP 25)", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
              { "type": "ia.display.image", "props": { "source": "/system/images/Icon_Server.svg", "style": { "height": "64px", "marginBottom": "15px" } } },
              {
                "type": "ia.display.flex-repeater",
                "meta": { "name": "Server_Repeater" },
                "position": { "grow": 1 },
                "propConfig": {
                  "props.instances": {
                    "binding": {
                      "type": "tag",
                      "config": { "path": "[default]DataCenter/Hall1" },
                      "transforms": [ { "code": indent_code(raw_script_compute), "type": "script" } ]
                    }
                  }
                },
                "props": {
                  "path": "Page/DCIM/Device_Node_Template",
                  "direction": "column",
                  "style": { "gap": "5px", "overflowY": "auto" }
                }
              }
            ]
          },
          {
            "type": "ia.container.flex",
            "meta": { "name": "Col_Power" },
            "position": { "grow": 1, "basis": "0" },
            "props": {
              "direction": "column",
              "style": { "backgroundColor": "#1E1E1E", "borderRadius": "10px", "padding": "15px", "borderTop": "5px solid #FF0000" }
            },
            "children": [
              { "type": "ia.display.label", "props": { "text": "CRITICAL POWER (TOP 25)", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
              { "type": "ia.display.image", "props": { "source": "/system/images/Icon_UPS.svg", "style": { "height": "64px", "marginBottom": "15px" } } },
              {
                "type": "ia.display.flex-repeater",
                "meta": { "name": "Power_Repeater" },
                "position": { "grow": 1 },
                "propConfig": {
                  "props.instances": {
                    "binding": {
                      "type": "tag",
                      "config": { "path": "[default]DataCenter/Hall1" },
                      "transforms": [ { "code": indent_code(raw_script_power), "type": "script" } ]
                    }
                  }
                },
                "props": {
                  "path": "Page/DCIM/Device_Node_Template",
                  "direction": "column",
                  "style": { "gap": "5px", "overflowY": "auto" }
                }
              }
            ]
          },
          {
            "type": "ia.container.flex",
            "meta": { "name": "Col_Edge" },
            "position": { "grow": 1, "basis": "0" },
            "props": {
              "direction": "column",
              "style": { "backgroundColor": "#1E1E1E", "borderRadius": "10px", "padding": "15px", "borderTop": "5px solid #00FF00" }
            },
            "children": [
              { "type": "ia.display.label", "props": { "text": "EDGE & IOT (TOP 25)", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
              { "type": "ia.display.image", "props": { "source": "/system/images/Icon_Sensor.svg", "style": { "height": "64px", "marginBottom": "15px" } } },
              {
                "type": "ia.display.flex-repeater",
                "meta": { "name": "Edge_Repeater" },
                "position": { "grow": 1 },
                "propConfig": {
                  "props.instances": {
                    "binding": {
                      "type": "tag",
                      "config": { "path": "[default]DataCenter/Hall1" },
                      "transforms": [ { "code": indent_code(raw_script_edge), "type": "script" } ]
                    }
                  }
                },
                "props": {
                  "path": "Page/DCIM/Device_Node_Template",
                  "direction": "column",
                  "style": { "gap": "5px", "overflowY": "auto" }
                }
              }
            ]
          }
        ]
      }
    ]
  }
}

with open('/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/DCIM/NetworkMap/view.json', 'w') as f:
    json.dump(view_data, f, indent=2)
print("Successfully generated NetworkMap view.json with LIMITS")