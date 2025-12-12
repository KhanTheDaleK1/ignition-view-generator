import yaml
import json
import sys
import os

# --- MAPPING CONSTANTS ---
# Maps simplified names to Ignition Component Types
COMPONENT_MAP = {
    "label": "ia.display.label",
    "button": "ia.input.button",
    "text-field": "ia.input.text-field",
    "display": "ia.display.led", # Just an example mapping
    "container": "ia.container.flex"
}

# Standard structure for an Ignition View Resource
def create_base_view(root_type="flex"):
    """Creates the scaffolding for view.json"""
    return {
        "custom": {},
        "params": {},
        "propConfig": {},
        "props": {},
        "root": {
            "children": [],
            "meta": {
                "name": "root"
            },
            "position": {}, # Only relevant for coordinate parents
            "props": {
                "direction": "column" if root_type == "flex" else None
            },
            "type": "ia.container.flex" if root_type == "flex" else "ia.container.coord"
        }
    }

def build_component(comp_def):
    """Converts a simplified YAML component definition to Ignition JSON."""
    
    # 1. Resolve Type
    simple_type = comp_def.get("type", "label")
    ignition_type = COMPONENT_MAP.get(simple_type, simple_type) # Fallback to passed type
    
    # 2. Build Object
    ignition_comp = {
        "meta": {
            "name": comp_def.get("name", "component")
        },
        "position": {
            # Defaults for coordinate containers (grow/shrink for flex)
            "height": 32,
            "width": 100,
            "x": 0,
            "y": 0,
            "grow": 0,
            "shrink": 0
        },
        "props": comp_def.get("props", {}),
        "type": ignition_type
    }
    
    # 3. Handle Nested Children (Recursion)
    if "children" in comp_def:
        ignition_comp["children"] = [build_component(child) for child in comp_def["children"]]
        
    return ignition_comp

def main():
    if len(sys.argv) < 2:
        print("Usage: python generator.py <input.yaml>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        sys.exit(1)

    # 1. Load YAML
    try:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)

    print(f"Processing: {data.get('meta', {}).get('name', 'Unknown View')}")

    # 2. Initialize Base Structure
    root_type = data.get("meta", {}).get("rootType", "flex")
    view_json = create_base_view(root_type)
    
    # 3. Apply Root Properties
    if "root" in data:
        # Merge props into the root container
        for key, value in data["root"].items():
            view_json["root"]["props"][key] = value

    # 4. Build Children
    if "children" in data:
        view_json["root"]["children"] = [build_component(child) for child in data["children"]]

    # 5. Output
    output_filename = "view.json"
    with open(output_filename, 'w') as f:
        json.dump(view_json, f, indent=2)
        
    print(f"Success! Generated {output_filename}")
    print("Copy this file to your Ignition Project's views folder.")

if __name__ == "__main__":
    main()
