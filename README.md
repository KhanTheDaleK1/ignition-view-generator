# Ignition View Generator (IVG)

**Transform YAML into Ignition Perspective Views.**

IVG is a developer tool that decouples Ignition Perspective design from the visual Designer. It allows you to define views, components, and layouts using a clean, human-readable YAML syntax, which is then compiled into valid `view.json` resources ready for the Ignition Gateway.

## 🚀 Why?
*   **Rapid Scaffolding:** Generate 50 similar components in seconds using loops in your YAML generator (or copy-paste).
*   **Version Control:** YAML is far easier to diff and merge than the verbose JSON Ignition uses.
*   **External IDEs:** Build your dashboards in VS Code, Vim, or Sublime.

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/KhanTheDaleK1/ignition-view-generator.git
    ```
2.  Ensure you have Python 3 installed (PyYAML is required):
    ```bash
    pip install pyyaml
    ```

## 🛠️ Usage

1.  **Define your view** in a YAML file (see `examples/dashboard.yaml`).
2.  **Compile** it using the generator:
    ```bash
    python3 generator.py examples/dashboard.yaml
    ```
3.  **Deploy** the resulting `view.json` to your Ignition Project:
    *   Move `view.json` to `$IGNITION_DIR/data/projects/[YourProject]/com.inductiveautomation.perspective/views/[NewViewPath]/view.json`
    *   The Ignition Gateway will automatically detect the file and update the session.

## 📝 Syntax Guide

### Basic View
```yaml
meta:
  name: "MyDashboard"
  rootType: "flex" # 'flex' or 'coordinate'

root:
  direction: "column"
  style:
    backgroundColor: "#F0F0F0"

children:
  - type: "label"
    name: "Header"
    props:
      text: "Hello World"
      style:
        fontSize: "24px"
```

### Component Mapping
| YAML Type | Ignition Component |
| :--- | :--- |
| `label` | `ia.display.label` |
| `button` | `ia.input.button` |
| `display` | `ia.display.led` |
| `text-field` | `ia.input.text-field` |
| `container` | `ia.container.flex` |

*Edit `generator.py` to add more custom mappings.*

## 🤝 Contributing
Pull requests are welcome! We are looking to expand the component map and add support for Coordinate Container positioning logic.

## 📜 License
MIT