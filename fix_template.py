import json

# Use ONE-LINER scripts to avoid indentation issues in JSON

# Script for Name label
script_name = "return str(value).split('/')[-1] if value else 'Unknown'"

# Script for Icon
script_icon = "return {'Server':'material/dns', 'UPS':'material/battery_charging_full', 'Sensor':'material/thermostat', 'Switch':'material/router'}.get(value, 'material/device_unknown')"

# Script for Status Color
script_status = "return '#00FF00' if value is not None and value < 50 else '#FF0000'"

# Script for Metric Label
script_metric_label = "return {'Server':'CPU Load', 'UPS':'Battery', 'Sensor':'Temp'}.get(value, 'Ping')"

# Script for Metric Path
script_metric_path = "return {'Server':'CPU_Load', 'UPS':'Battery Level', 'Sensor':'Temperature_F', 'Switch':'Ping_Latency'}.get(value, 'Ping_Latency')"

# Script for Suffix
script_suffix = "return {'Server':'%', 'UPS':'%', 'Sensor':'°F'}.get(value, 'ms')"

# Script for Metric Value Text
script_metric_val = "return str(value) + ' ' + self.view.custom.suffix"

# Script for Progress Bar
script_progress = "return value if isinstance(value, (int, float)) else 0"

# Script for Progress Bar Visibility
script_progress_vis = "return value in ['Server', 'UPS', 'PLC']"

view_data = {
  "custom": {
    "metricPath": "Ping_Latency",
    "suffix": "ms"
  },
  "params": {
    "tagPath": "[default]DataCenter/Hall1/Server-01",
    "deviceType": "Server"
  },
  "propConfig": {
    "custom.metricPath": {
      "binding": {
        "config": { "path": "view.params.deviceType" },
        "transforms": [ { "code": script_metric_path, "type": "script" } ],
        "type": "property"
      }
    },
    "custom.suffix": {
      "binding": {
        "config": { "path": "view.params.deviceType" },
        "transforms": [ { "code": script_suffix, "type": "script" } ],
        "type": "property"
      }
    },
    "params.tagPath": { "paramDirection": "input" },
    "params.deviceType": { "paramDirection": "input" }
  },
  "props": { "defaultSize": { "height": 80, "width": 250 } },
  "root": {
    "type": "ia.container.flex",
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": { "backgroundColor": "#2D2D2D", "borderRadius": "8px", "padding": "10px", "border": "1px solid #444", "gap": "5px" }
    },
    "children": [
      {
        "type": "ia.container.flex",
        "meta": { "name": "Header" },
        "props": { "justify": "space-between", "alignItems": "center" },
        "children": [
          {
            "type": "ia.container.flex",
            "meta": { "name": "TitleGroup" },
            "props": { "alignItems": "center", "gap": "10px" },
            "children": [
              {
                "type": "ia.display.icon",
                "meta": { "name": "Icon" },
                "propConfig": {
                  "props.path": {
                    "binding": {
                      "config": { "path": "view.params.deviceType" },
                      "transforms": [ { "code": script_icon, "type": "script" } ],
                      "type": "property"
                    }
                  }
                },
                "props": { "color": "#FF6600", "style": { "width": "20px", "height": "20px" } }
              },
              {
                "type": "ia.display.label",
                "meta": { "name": "Name" },
                "propConfig": {
                  "props.text": {
                    "binding": {
                      "config": { "path": "view.params.tagPath" },
                      "transforms": [ { "code": script_name, "type": "script" } ],
                      "type": "property"
                    }
                  }
                },
                "props": { "style": { "color": "#FFF", "fontWeight": "bold", "fontSize": "12px" } }
              }
            ]
          },
          {
            "type": "ia.display.icon",
            "meta": { "name": "StatusDot" },
            "propConfig": {
              "props.color": {
                "binding": {
                  "type": "tag",
                  "config": { "mode": "indirect", "references": { "path": "{view.params.tagPath}" }, "tagPath": "{path}/Ping_Latency" },
                  "transforms": [ { "code": script_status, "type": "script" } ]
                }
              }
            },
            "props": { "path": "material/circle", "style": { "width": "12px", "height": "12px" } }
          }
        ]
      },
      {
        "type": "ia.container.flex",
        "meta": { "name": "MetricRow" },
        "props": { "justify": "space-between", "alignItems": "center" },
        "children": [
          {
            "type": "ia.display.label",
            "meta": { "name": "MetricLabel" },
            "propConfig": {
              "props.text": {
                "binding": {
                  "config": { "path": "view.params.deviceType" },
                  "transforms": [ { "code": script_metric_label, "type": "script" } ],
                  "type": "property"
                }
              }
            },
            "props": { "style": { "color": "#AAA", "fontSize": "10px" } }
          },
          {
            "type": "ia.display.label",
            "meta": { "name": "MetricValue" },
            "propConfig": {
              "props.text": {
                "binding": {
                  "type": "tag",
                  "config": { "mode": "indirect", "references": { "path": "{view.params.tagPath}", "metric": "{view.custom.metricPath}" }, "tagPath": "{path}/{metric}" },
                  "transforms": [ { "code": script_metric_val, "type": "script" } ]
                }
              }
            },
            "props": { "style": { "color": "#FFF", "fontSize": "12px", "fontWeight": "bold" } }
          }
        ]
      },
      {
        "type": "ia.display.progress",
        "meta": { "name": "ProgressBar" },
        "propConfig": {
          "props.value": {
            "binding": {
              "type": "tag",
              "config": { "mode": "indirect", "references": { "path": "{view.params.tagPath}", "metric": "{view.custom.metricPath}" }, "tagPath": "{path}/{metric}" },
              "transforms": [ { "code": script_progress, "type": "script" } ]
            }
          },
          "position.display": {
             "binding": {
                "config": { "path": "view.params.deviceType" },
                "transforms": [ { "code": script_progress_vis, "type": "script" } ],
                "type": "property"
             }
          }
        },
        "props": { "max": 100, "style": { "height": "6px", "classes": "" }, "trackColor": "#444", "color": "#FF6600" }
      }
    ]
  }
}

with open('/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/DCIM/Device_Node_Template/view.json', 'w') as f:
    json.dump(view_data, f, indent=2)
print("Successfully generated Device_Node_Template view.json with ONE-LINERS")
