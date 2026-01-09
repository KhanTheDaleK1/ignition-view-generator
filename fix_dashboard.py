import json

def indent_code(code):
    return "\n".join(["\t" + line for line in code.strip().split("\n")])

# --- DASHBOARD SCRIPTS ---

# Script to fetch ALL devices (Recursive Browse)
script_get_all = (
    "try:\n"
    "    path = '[default]DataCenter/Hall1'\n"
    "    # Recursive browse to catch nested tags\n"
    "    tags = system.tag.browse(path, {'recursive': True})\n"
    "    if not tags: return []\n"
    "    \n"
    "    devices = []\n"
    "    for tag in tags:\n"
    "        # Only add UDT instances (devices), skip folders\n"
    "        if str(tag['tagType']) == 'UdtInstance':\n"
    "            type_id = str(tag.get('typeId', 'Unknown'))\n"
    "            full_path = str(tag['fullPath'])\n"
    "            name = str(tag['name'])\n"
    "            \n"
    "            dev_type = 'Server' # Default\n"
    "            if 'Switch' in type_id: dev_type = 'Switch'\n"
    "            elif 'UPS' in type_id: dev_type = 'UPS'\n"
    "            elif 'Sensor' in type_id: dev_type = 'Sensor'\n"
    "            elif 'PLC' in type_id: dev_type = 'PLC'\n"
    "            \n"
    "            devices.append({'tagPath': full_path, 'deviceType': dev_type, 'name': name})\n"
    "    return devices\n"
    "except:\n"
    "    return []"
)

# Slice Script
script_slice_page = (
    "try:\n"
    "    page = self.view.custom.page\n"
    "    size = self.view.custom.pageSize\n"
    "    data = value\n"
    "    if not data: return []\n"
    "    start = page * size\n"
    "    end = start + size\n"
    "    return data[start:end]\n"
    "except:\n"
    "    return []"
)

# KPI Script
script_count = (
    "try:\n"
    "    return str(len(self.view.custom.allDevices)) + 'DEVICES'\n"
    "except:\n"
    "    return '0DEVICES'"
)

# Pager Scripts
script_prev = (
    "if self.view.custom.page > 0:\n"
    "    self.view.custom.page -= 1"
)

script_next = (
    "max_page = self.view.custom.pageCount - 1\n"
    "if self.view.custom.page < max_page:\n"
    "    self.view.custom.page += 1"
)

script_page_label = (
    "return 'Page ' + str(self.view.custom.page + 1) + ' of ' + str(self.view.custom.pageCount)"
)

# Page Count Calc
script_calc_pages = (
    "import math\n"
    "total = len(value)\n"
    "size = self.view.custom.pageSize\n"
    "if size == 0: return 1\n"
    "return int(math.ceil(float(total) / size))"
)


view_data = {
  "custom": {
    "allDevices": [],
    "page": 0,
    "pageSize": 50,
    "pageCount": 1
  },
  "params": {},
  "props": { "defaultSize": { "height": 800, "width": 1280 } },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": { "direction": "column", "style": { "backgroundColor": "#121212", "padding": "20px", "gap": "20px" } },
    "propConfig": {
        "custom.allDevices": {
            "binding": {
                "type": "tag",
                "config": { "path": "[default]DataCenter/Hall1" },
                "transforms": [ { "code": indent_code(script_get_all), "type": "script" } ]
            }
        },
        "custom.pageCount": {
            "binding": {
                "config": { "path": "view.custom.allDevices" },
                "transforms": [ { "code": indent_code(script_calc_pages), "type": "script" } ],
                "type": "property"
            }
        }
    },
    "children": [
      {
        "type": "ia.display.label",
        "meta": { "name": "Header" },
        "props": {
          "text": "DATA CENTER ASSET MONITOR",
          "style": { "color": "#FFFFFF", "fontSize": "28px", "fontWeight": "bold", "borderBottom": "4px solid #FF6600", "paddingBottom": "10px" }
        }
      },
      {
        "type": "ia.container.flex",
        "meta": { "name": "GlobalKPIs" },
        "position": { "basis": "120px", "shrink": 0 },
        "props": { "direction": "row", "style": { "gap": "20px" } },
        "children": [
          {
            "type": "ia.container.flex",
            "meta": { "name": "Total_Devices_Card" },
            "position": { "grow": 1, "basis": "0" },
            "props": { "direction": "column", "style": { "backgroundColor": "#1E1E1E", "borderRadius": "8px", "padding": "15px", "borderLeft": "5px solid #FF6600" } },
            "children": [
              { "type": "ia.display.label", "props": { "text": "NETWORK ASSETS", "style": { "color": "#AAA", "fontSize": "12px" } } },
              {
                "type": "ia.display.label",
                "propConfig": {
                  "props.text": {
                    "binding": {
                      "config": { "path": "view.custom.allDevices" },
                      "transforms": [ { "code": indent_code(script_count), "type": "script" } ],
                      "type": "property"
                    }
                  }
                },
                "props": { "style": { "color": "#FFF", "fontSize": "24px", "fontWeight": "bold" } }
              }
            ]
          },
          {
            "type": "ia.container.flex",
            "meta": { "name": "UPS_Health_Card" },
            "position": { "grow": 1, "basis": "0" },
            "props": { "direction": "column", "style": { "backgroundColor": "#1E1E1E", "borderRadius": "8px", "padding": "15px", "borderLeft": "5px solid #00FF00" } },
            "children": [
              { "type": "ia.display.label", "props": { "text": "SYSTEM STATUS", "style": { "color": "#AAA", "fontSize": "12px" } } },
              { "type": "ia.display.label", "props": { "text": "OPTIMAL", "style": { "color": "#00FF00", "fontSize": "24px", "fontWeight": "bold" } } }
            ]
          }
        ]
      },
      {
        "type": "ia.container.flex",
        "meta": { "name": "Controls" },
        "props": { "justify": "space-between", "alignItems": "center" },
        "children": [
            {
                "type": "ia.display.label",
                "meta": { "name": "SubTitle" },
                "props": { "text": "CRITICAL ASSET LIST", "style": { "color": "#FF6600", "fontSize": "14px", "fontWeight": "bold" } }
            },
            {
                "type": "ia.container.flex",
                "meta": { "name": "PagerControls" },
                "props": { "gap": "10px", "alignItems": "center" },
                "children": [
                    {
                        "type": "ia.input.button",
                        "meta": { "name": "PrevBtn" },
                        "props": { "text": "Prev", "style": { "backgroundColor": "#444", "color": "#FFF" } },
                        "events": { "component": { "onActionPerformed": { "config": { "script": indent_code(script_prev) }, "scope": "G", "type": "script" } } }
                    },
                    {
                        "type": "ia.display.label",
                        "meta": { "name": "PageLabel" },
                        "propConfig": {
                            "props.text": {
                                "binding": {
                                    "config": { "path": "view.custom.page" }, # Bind to page, transform uses both
                                    "transforms": [ { "code": indent_code(script_page_label), "type": "script" } ],
                                    "type": "property"
                                }
                            }
                        },
                        "props": { "style": { "color": "#FFF" } }
                    },
                    {
                        "type": "ia.input.button",
                        "meta": { "name": "NextBtn" },
                        "props": { "text": "Next", "style": { "backgroundColor": "#444", "color": "#FFF" } },
                        "events": { "component": { "onActionPerformed": { "config": { "script": indent_code(script_next) }, "scope": "G", "type": "script" } } }
                    }
                ]
            }
        ]
      },
      {
        "type": "ia.display.flex-repeater",
        "meta": { "name": "Asset_Grid" },
        "position": { "grow": 1 },
        "propConfig": {
          "props.instances": {
            "binding": {
              "config": { "path": "view.custom.allDevices" },
              "transforms": [ { "code": indent_code(script_slice_page), "type": "script" } ],
              "type": "property"
            }
          }
        },
        "props": {
          "path": "Page/DCIM/Device_Node_Template",
          "direction": "column",
          "useDefaultViewWidth": False,
          "useDefaultViewHeight": True,
          "style": { "gap": "10px", "overflowY": "auto" }
        }
      }
    ]
  }
}

with open('/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/DCIM/Dashboard/view.json', 'w') as f:
    json.dump(view_data, f, indent=2)
print("Successfully generated Dashboard view.json with Custom Pager")