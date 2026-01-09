import json
import os
import urllib.parse
from pypdf import PdfReader

# --- CONFIGURATION ---
PROJECT_PATH = '/mnt/projects/7. Ignition/data/projects/OT_Sandbox'
VIEW_PATH = os.path.join(PROJECT_PATH, 'com.inductiveautomation.perspective/views/Page/Knowledgebase/view.json')
SOP_ROOT = '/mnt/projects/7. Ignition/webserver/webapps/main/sops'
WEB_URL_PREFIX = '/sops/'

# --- 1. SCAN AND INDEX PDFS ---
print(f"Scanning for PDFs in {SOP_ROOT}...")
indexed_sops = []

if os.path.exists(SOP_ROOT):
    for root, dirs, files in os.walk(SOP_ROOT):
        for file in files:
            if file.lower().endswith('.pdf'):
                full_file_path = os.path.join(root, file)
                
                # Extract metadata from filename/folder
                dept = "Production" 
                sop_type = "Work Instruction"
                
                if "Quality" in root: dept = "Quality"
                elif "Maintenance" in root: dept = "Maintenance"
                
                if "Plasma" in root: sop_type = "Plasma Cutting"
                elif "Welding" in root: sop_type = "Welding Procedure"
                elif "Press" in root: sop_type = "Press/Forming"
                elif "Fitting" in root: sop_type = "Fitting/Prep"
                elif "QA" in root or "Standards" in root: sop_type = "Standards/QA"
                
                # URL Encoding
                rel_path = os.path.relpath(full_file_path, SOP_ROOT)
                rel_path = rel_path.replace('\\', '/')
                # Encode each component
                encoded_path = "/".join([urllib.parse.quote(part) for part in rel_path.split('/')])
                full_url = WEB_URL_PREFIX + encoded_path
                
                # Content Extraction
                keywords = file.replace('_', ' ').replace('-', ' ')
                try:
                    reader = PdfReader(full_file_path)
                    text = ""
                    # Limit to first 5 pages
                    for page in reader.pages[:5]: 
                        text += page.extract_text() + " "
                    keywords += " " + " ".join(text.split())[:10000]
                except Exception as e:
                    print(f"Failed to read text from {file}: {e}")

                indexed_sops.append({
                    "id": file, 
                    "title": file.replace('.pdf', ''), 
                    "dept": dept,
                    "type": sop_type,
                    "version": "1.0",
                    "url": full_url,
                    "keywords": keywords
                })
                print(f"Indexed: {file}")
    print(f"Found {len(indexed_sops)} PDFs.")
else:
    print(f"ERROR: SOP Directory {SOP_ROOT} not found!")

# --- 2. DEFINE VIEW STRUCTURE ---
# Construct filter script safely
filter_script_lines = [
    "\tdept = self.view.custom.selectedDept",
    "\ttype_ = self.view.custom.selectedType",
    "\tsearch = self.view.custom.searchText.lower()",
    "\tfiltered = []",
    "\tfor sop in value:",
    "\t\tif (dept == 'All' or sop['dept'] == dept) and (type_ == 'All' or sop['type'] == type_) and (search == '' or search in sop['title'].lower() or search in sop.get('keywords', '').lower()):",
    "\t\t\tfiltered.append(sop)",
    "\treturn filtered"
]
filter_script = "\n".join(filter_script_lines)

view_data = {
  "custom": {
    "allSops": indexed_sops,
    "searchText": "",
    "selectedDept": "All",
    "selectedType": "All",
    "selectedMapUrl": "https://us.hamina.com/share/9914cd75-d81e-4d85-af1f-b198cd2d6119"
  },
  "params": {},
  "props": { "defaultSize": { "height": 800, "width": 1280 } },
  "root": {
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": { "backgroundColor": "#121212", "height": "100%", "overflow": "hidden" }
    },
    "children": [
      {
        "meta": { "name": "Header" },
        "position": { "basis": "auto", "shrink": 0 },
        "props": {
          "style": {
            "alignItems": "center", "backgroundColor": "#1F1F1F", "borderBottom": "4px solid #FF6600",
            "display": "flex", "justifyContent": "space-between", "padding": "10px 20px",
            "flexWrap": "wrap", "gap": "10px", "minHeight": "60px", "boxShadow": "0 2px 4px rgba(0,0,0,0.3)"
          }
        },
        "children": [
          {
            "meta": { "name": "Title" },
            "props": { "style": { "color": "#FFFFFF", "fontSize": "clamp(1.2rem, 3vw, 1.5rem)", "fontWeight": "bold" }, "text": "KNOWLEDGEBASE PORTAL" },
            "type": "ia.display.label"
          },
          {
            "meta": { "name": "SearchInput" },
            "position": { "basis": "250px", "grow": 1 },
            "propConfig": {
              "props.text": {
                "binding": { "config": { "bidirectional": True, "path": "view.custom.searchText" }, "type": "property" }
              }
            },
            "props": {
              "placeholder": "Search SOPs (Content or Title)...",
              "style": { "backgroundColor": "#2D2D2D", "color": "#FFF", "borderRadius": "4px", "border": "1px solid #FF6600" }
            },
            "type": "ia.input.text-field"
          }
        ],
        "type": "ia.container.flex"
      },
      {
        "meta": { "name": "ContentBody" },
        "position": { "grow": 1 },
        "props": { "direction": "row", "wrap": "wrap", "style": { "overflow": "hidden", "width": "100%", "height": "100%" } },
        "children": [
          {
            "meta": { "name": "Sidebar" },
            "position": { "basis": "300px", "grow": 1, "shrink": 0 },
            "props": { "direction": "column", "style": { "backgroundColor": "#1E1E1E", "borderRight": "2px solid #333", "padding": "20px", "gap": "20px", "overflowY": "auto", "minWidth": "250px" } },
            "children": [
              { "props": { "style": { "color": "#FF6600", "fontSize": "14px", "fontWeight": "bold", "textTransform": "uppercase" }, "text": "Filters" }, "type": "ia.display.label" },
              { "props": { "style": { "color": "#E0E0E0", "fontSize": "12px", "fontWeight": "bold", "marginTop": "10px" }, "text": "DEPARTMENT" }, "type": "ia.display.label" },
              {
                "meta": { "name": "DeptFilter" },
                "propConfig": { "props.value": { "binding": { "config": { "bidirectional": True, "path": "view.custom.selectedDept" }, "type": "property" } } },
                "props": {
                  "options": [ { "label": "All Departments", "value": "All" }, { "label": "Production", "value": "Production" }, { "label": "Quality", "value": "Quality" }, { "label": "Maintenance", "value": "Maintenance" } ],
                  "style": { "backgroundColor": "#2D2D2D", "color": "#FFF" }
                },
                "type": "ia.input.dropdown"
              },
              { "props": { "style": { "color": "#E0E0E0", "fontSize": "12px", "fontWeight": "bold", "marginTop": "10px" }, "text": "SOP TYPE" }, "type": "ia.display.label" },
              {
                "meta": { "name": "TypeFilter" },
                "propConfig": { "props.value": { "binding": { "config": { "bidirectional": True, "path": "view.custom.selectedType" }, "type": "property" } } },
                "props": {
                  "options": [ { "label": "All Types", "value": "All" }, { "label": "Work Instruction", "value": "Work Instruction" }, { "label": "Welding Procedure", "value": "Welding Procedure" }, { "label": "Plasma Cutting", "value": "Plasma Cutting" }, { "label": "Press/Forming", "value": "Press/Forming" }, { "label": "Fitting/Prep", "value": "Fitting/Prep" }, { "label": "Standards/QA", "value": "Standards/QA" }, { "label": "Maintenance", "value": "Maintenance" } ],
                  "style": { "backgroundColor": "#2D2D2D", "color": "#FFF" }
                },
                "type": "ia.input.dropdown"
              },
              { "props": { "style": { "borderTop": "1px solid #444", "marginTop": "20px" } }, "type": "ia.display.label" },
              { "props": { "style": { "color": "#FF6600", "fontSize": "14px", "fontWeight": "bold", "textTransform": "uppercase" }, "text": "Maps" }, "type": "ia.display.label" },
              {
                "meta": { "name": "SiteDropdown" },
                "propConfig": { "props.value": { "binding": { "config": { "bidirectional": True, "path": "view.custom.selectedMapUrl" }, "type": "property" } } },
                "props": {
                  "options": [
                    { "label": "Pineville Full Site", "value": "https://us.hamina.com/share/9914cd75-d81e-4d85-af1f-b198cd2d6119" },
                    { "label": "Pineville Plant 1", "value": "https://us.hamina.com/share/d9f7e46a-9a2b-4a27-94bf-a94081f2934d" },
                    { "label": "Pineville Plant 2", "value": "https://us.hamina.com/share/3b3a0e9f-5083-484c-8500-5be36c975b13" },
                    { "label": "Pineville Plant 3", "value": "https://us.hamina.com/share/ab7a57a0-aa95-40f8-a514-b8cf13b0aad2" },
                    { "label": "Pineville Plant 4", "value": "https://us.hamina.com/share/5e892eee-15cc-4887-b45b-bd642b431aa6" },
                    { "label": "Eunice", "value": "https://us.hamina.com/share/2b3b6251-51e8-4c7e-a1e6-7da2d7d9ac94" }
                  ],
                  "style": { "backgroundColor": "#2D2D2D", "color": "#FFF" }
                },
                "type": "ia.input.dropdown"
              },
              {
                "events": { "component": { "onActionPerformed": { "config": { "script": "\tsystem.perspective.navigate(url=self.view.custom.selectedMapUrl, newTab=True)" }, "scope": "G", "type": "script" } } },
                "props": { "style": { "backgroundColor": "#FF6600", "color": "#FFF", "fontWeight": "bold", "marginTop": "10px" }, "text": "OPEN INTERACTIVE MAP" },
                "type": "ia.input.button"
              }
            ],
            "type": "ia.container.flex"
          },
          {
            "meta": { "name": "MainResults" },
            "position": { "basis": "600px", "grow": 999, "shrink": 1 },
            "props": { "direction": "column", "style": { "backgroundColor": "#121212", "padding": "20px", "overflowY": "auto", "height": "100%" } },
            "children": [
              {
                "meta": { "name": "SOP_Repeater" },
                "propConfig": {
                  "props.instances": {
                    "binding": {
                      "config": { "path": "view.custom.allSops" },
                      "transforms": [ { "code": filter_script, "type": "script" } ],
                      "type": "property"
                    }
                  }
                },
                "props": { "direction": "row", "path": "Page/Knowledgebase/SOP_Card", "style": { "display": "flex", "flexWrap": "wrap", "gap": "20px", "justifyContent": "center", "alignContent": "flex-start" } },
                "type": "ia.display.flex-repeater"
              }
            ],
            "type": "ia.container.flex"
          }
        ],
        "type": "ia.container.flex"
      }
    ],
    "type": "ia.container.flex"
  }
}

# --- 3. WRITE FILE ---
with open(VIEW_PATH, 'w') as f:
    json.dump(view_data, f, indent=2)

print(f"Successfully rebuilt view.json with {len(indexed_sops)} SOPs.")