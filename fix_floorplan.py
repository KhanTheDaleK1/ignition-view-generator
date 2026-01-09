import json

# Define the script using explicit string concatenation and tabs (\t) for indentation
script_code = (
    "try:\n"
    "\t# 1. Browse Tags\n"
    "\ttags = system.tag.browse(value)\n"
    "\tif not tags:\n"
    "\t\treturn [{'viewPath': 'Page/DCIM/Rack_Template', \n"
    "\t\t         'viewParams': {'rackLabel': 'NoTags', 'deviceCount': 0}, \n"
    "\t\t         'position': {'top': '100px', 'left': '100px', 'width': '80px', 'height': '150px'}}]\n"
    "\t\n"
    "\t# 2. Build paths to read Parameters\n"
    "\tdevice_names = [str(t['name']) for t in tags]\n"
    "\tpaths = []\n"
    "\tfor name in device_names:\n"
    "\t\tpath_base = \"[default]DataCenter/Hall1/\" + name\n"
    "\t\tpaths.append(path_base + \"/Parameters.Location_Row\")\n"
    "\t\tpaths.append(path_base + \"/Parameters.Location_Rack\")\n"
    "\t\n"
    "\t# 3. Batch Read\n"
    "\tlimit = 50\n"
    "\tvalues = system.tag.readBlocking(paths[:limit*2])\n"
    "\t\n"
    "\t# 4. Group by Rack\n"
    "\tracks = {}\n"
    "\tfor i in range(0, len(values), 2):\n"
    "\t\trow = values[i].value\n"
    "\t\track_num = values[i+1].value\n"
    "\t\t\n"
    "\t\tif row and rack_num:\n"
    "\t\t\tkey = str(row) + str(rack_num)\n"
    "\t\t\tif key not in racks:\n"
    "\t\t\t\tracks[key] = {'row': row, 'col': rack_num, 'count': 0}\n"
    "\t\t\tracks[key]['count'] += 1\n"
    "\t\t\t\n"
    "\t# 5. Generate Instances\n"
    "\tinstances = []\n"
    "\tfor key, data in racks.items():\n"
    "\t\trow_idx = 0\n"
    "\t	if data['row'] == 'B': row_idx = 1\n"
    "\t	if data['row'] == 'C': row_idx = 2\n"
    "\t\t\n"
    "\t\ttry:\n"
    "\t	\tcol_idx = int(str(data['col']))\n"
    "\t	except:\n"
    "\t	\tcol_idx = 1\n"
    "\t\t\n"
    "\t\ttop = str(50 + (row_idx * 180)) + \"px\"\n"
    "\t\tleft = str(50 + (col_idx * 100)) + \"px\"\n"
    "\t\t\n"
    "\t\tinstances.append({\n"
    "\t\t\t\"viewPath\": \"Page/DCIM/Rack_Template\",\n"
    "\t\t\t\"viewParams\": {\n"
    "\t\t\t\t\"rackLabel\": key,\n"
    "\t\t\t\t\"deviceCount\": data['count'],\n"
    "\t\t\t\t\"maxTemp\": 72\n"
    "\t\t\t},\n"
    "\t\t\t\"position\": {\n"
    "\t\t\t\t\"top\": top,\n"
    "\t\t\t\t\"left\": left,\n"
    "\t\t\t\t\"width\": \"80px\",\n"
    "\t\t\t\t\"height\": \"150px\"\n"
    "\t\t\t},\n"
    "\t\t\t\"style\": {\"zIndex\": 1}\n"
    "\t\t})\n"
    "\t\t\n"
    "\tif not instances:\n"
    "\t\treturn [{'viewPath': 'Page/DCIM/Rack_Template', \n"
    "\t\t         'viewParams': {'rackLabel': 'Demo', 'deviceCount': 0}, \n"
    "\t\t         'position': {'top': '50px', 'left': '50px', 'width': '80px', 'height': '150px'}}]\n"
    "\t\t\n"
    "\treturn instances\n"
    "except Exception as e:\n"
    "\treturn [{'viewPath': 'Page/DCIM/Rack_Template', \n"
    "\t         'viewParams': {'rackLabel': 'Error', 'deviceCount': 0}, \n"
    "\t         'position': {'top': '50px', 'left': '50px', 'width': '80px', 'height': '150px'}}]"
)

view_data = {
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
                  "code": script_code,
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
    json.dump(view_data, f, indent=2)
print("Successfully generated FloorPlan view.json with FIXED TABS")
