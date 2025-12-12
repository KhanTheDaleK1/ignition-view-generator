import argparse
import json
import os
import sys
from datetime import datetime, timezone

import yaml

# --- MAPPING CONSTANTS ---
# Maps simplified names to Ignition Component Types and defaults
COMPONENT_MAP = {
    "label": {
        "type": "ia.display.label",
        "defaults": {
            "props": {"text": "Label"}
        }
    },
    "button": {
        "type": "ia.input.button",
        "defaults": {
            "props": {"text": "Click Me"}
        }
    },
    "text-field": {
        "type": "ia.input.text-field",
        "defaults": {
            "props": {"text": ""}
        }
    },
    "display": {
        "type": "ia.display.led",
        "defaults": {
            "props": {"value": 0}
        }
    },
    "container": {
        "type": "ia.container.flex",
        "defaults": {
            "props": {"direction": "row", "gap": 8}
        }
    }
}

def resolve_component_type(simple_type: str):
    mapping = COMPONENT_MAP.get(simple_type)
    if mapping:
        return mapping["type"], mapping.get("defaults", {})
    return simple_type, {}

def merge_dict(a, b):
    """Shallow merge helper: values from b override a."""
    merged = dict(a)
    merged.update(b or {})
    return merged

# Standard structure for an Ignition View Resource
def create_base_view(root_type="flex"):
    """Creates the scaffolding for view.json"""
    root_component = "ia.container.flex" if root_type == "flex" else "ia.container.coord"
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
            "type": root_component
        }
    }

def build_component(comp_def):
    """Converts a simplified YAML component definition to Ignition JSON."""
    
    # 1. Resolve Type
    simple_type = comp_def.get("type", "label")
    ignition_type, default_fields = resolve_component_type(simple_type)
    
    # 2. Build Object
    props = merge_dict(default_fields.get("props", {}), comp_def.get("props", {}))

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
        "props": props,
        "type": ignition_type
    }
    
    # 3. Handle Nested Children (Recursion)
    if "children" in comp_def:
        ignition_comp["children"] = [build_component(child) for child in comp_def["children"]]
        
    return ignition_comp

def validate_yaml(data):
    """Lightweight structural validation; raises ValueError on errors."""
    if not isinstance(data, dict):
        raise ValueError("Top-level document must be a mapping.")
    if "meta" not in data or not isinstance(data["meta"], dict):
        raise ValueError("Missing required 'meta' section (mapping).")
    if "rootType" in data.get("meta", {}) and data["meta"]["rootType"] not in ("flex", "coordinate", "coord"):
        raise ValueError("meta.rootType must be one of: flex, coordinate/coord.")
    if "root" not in data or not isinstance(data["root"], dict):
        raise ValueError("Missing required 'root' section (mapping).")
    if "children" not in data or not isinstance(data["children"], list):
        raise ValueError("Missing required 'children' array at top level.")
    for idx, child in enumerate(data["children"]):
        if not isinstance(child, dict):
            raise ValueError(f"Child at index {idx} must be a mapping.")
        if "type" not in child:
            raise ValueError(f"Child at index {idx} missing 'type'.")

def write_resource_json(path: str):
    """Write a resource.json alongside view.json with current timestamp."""
    # Ignition expects UTC without fractional seconds
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    resource = {
        "scope": "G",
        "version": 1,
        "restricted": False,
        "overridable": True,
        "files": [
            "view.json"
        ],
        "attributes": {
            "lastModification": {
                "actor": "external-tool",
                "timestamp": now
            },
            "lastModificationSignature": "0000000000000000000000000000000000000000000000000000000000000000"
        }
    }
    with open(path, "w") as f:
        json.dump(resource, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Generate Ignition Perspective view.json from YAML.")
    parser.add_argument("input", help="Input YAML file")
    parser.add_argument("-o", "--output", default="view.json", help="Output view JSON path")
    parser.add_argument("--resource", default="resource.json", help="Output resource.json path")
    args = parser.parse_args()

    input_file = args.input

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

    try:
        validate_yaml(data)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)

    print(f"Processing: {data.get('meta', {}).get('name', 'Unknown View')}")

    # 2. Initialize Base Structure
    root_type_raw = data.get("meta", {}).get("rootType", "flex")
    root_type = "flex" if root_type_raw in ("flex", None) else "coordinate"
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
    with open(args.output, 'w') as f:
        json.dump(view_json, f, indent=2)

    # 6. Resource descriptor
    if args.resource:
        write_resource_json(args.resource)
        
    print(f"Success! Generated {args.output}")
    print("Copy this file (and resource.json) to your Ignition Project's views folder.")

if __name__ == "__main__":
    main()
