import json

# --- DASHBOARD ---
dashboard_script = "return DCIM.get_devices()" # No filter
kpi_script = "return DCIM.get_device_count()"

dashboard_view = {
  "custom": {},
  "params": {},
  "props": { "defaultSize": { "height": 800, "width": 1280 } },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": { "direction": "column", "style": { "backgroundColor": "#121212", "padding": "20px", "gap": "20px" } },
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
                      "type": "tag",
                      "config": { "path": "[default]DataCenter/Hall1" },
                      "transforms": [ { "code": kpi_script, "type": "script" } ]
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
        "type": "ia.display.label",
        "meta": { "name": "SubTitle" },
        "props": { "text": "LIVE ASSET PERFORMANCE", "style": { "color": "#FF6600", "fontSize": "14px", "fontWeight": "bold" } }
      },
      {
        "type": "ia.display.flex-repeater",
        "meta": { "name": "Asset_Grid" },
        "position": { "grow": 1 },
        "propConfig": {
          "props.instances": {
            "binding": {
              "type": "tag",
              "config": { "path": "[default]DataCenter/Hall1" },
              "transforms": [ { "code": dashboard_script, "type": "script" } ]
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
    json.dump(dashboard_view, f, indent=2)

# --- NETWORK MAP ---
map_script_core = "return DCIM.get_devices('Core')"
map_script_compute = "return DCIM.get_devices('Compute')"
map_script_power = "return DCIM.get_devices('Power')"
map_script_edge = "return DCIM.get_devices('Edge')"

map_view = {
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
              { "type": "ia.display.label", "props": { "text": "CORE NETWORK", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
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
                      "transforms": [ { "code": map_script_core, "type": "script" } ]
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
              { "type": "ia.display.label", "props": { "text": "COMPUTE & STORAGE", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
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
                      "transforms": [ { "code": map_script_compute, "type": "script" } ]
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
              { "type": "ia.display.label", "props": { "text": "CRITICAL POWER", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
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
                      "transforms": [ { "code": map_script_power, "type": "script" } ]
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
              { "type": "ia.display.label", "props": { "text": "EDGE & IOT", "style": { "color": "#FFF", "fontWeight": "bold", "textAlign": "center", "marginBottom": "15px" } } },
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
                      "transforms": [ { "code": map_script_edge, "type": "script" } ]
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
    json.dump(map_view, f, indent=2)

# --- FLOOR PLAN ---
floor_script = "return DCIM.get_floorplan_instances()"

floor_view = {
  "custom": {},
  "params": {},
  "props": {
    "defaultSize": { "height": 800, "width": 1280 }
  },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": { "backgroundColor": "#F0F0F0", "padding": "20px" }
    },
    "children": [
      {
        "type": "ia.display.label",
        "meta": { "name": "Title" },
        "props": {
          "text": "DATA CENTER FLOOR PLAN (DYNAMIC)",
          "style": { "fontSize": "24px", "fontWeight": "bold", "marginBottom": "20px", "color": "#333" }
        }
      },
      {
        "type": "ia.display.viewcanvas",
        "meta": { "name": "FloorCanvas" },
        "position": { "grow": 1 },
        "propConfig": {
          "props.instances": {
            "binding": {
              "type": "tag",
              "config": { "path": "[default]DataCenter/Hall1" },
              "transforms": [
                {
                  "code": floor_script,
                  "type": "script"
                }
              ]
            }
          }
        },
        "props": {
          "canvasStyle": { "backgroundColor": "#FFFFFF", "border": "1px solid #CCC" }
        }
      }
    ]
  }
}

with open('/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/DCIM/FloorPlan/view.json', 'w') as f:
    json.dump(floor_view, f, indent=2)

print("Successfully updated ALL views to use DCIM library.")
