# Ignition View Generator (IVG)

**Transform YAML into Ignition Perspective Views.**

IVG is a developer tool that decouples Ignition Perspective design from the visual Designer. It allows you to define views, components, and layouts using a clean, human-readable YAML syntax, which is then compiled into valid `view.json` resources ready for the Ignition Gateway.

## 🚀 Why?
*   **Rapid Scaffolding:** Generate 50 similar components in seconds using loops in your YAML generator (or copy-paste).
*   **Version Control:** YAML is far easier to diff and merge than the verbose JSON Ignition uses.
*   **External IDEs:** Build your dashboards in VS Code, Vim, or Sublime.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KhanTheDaleK1/ignition-view-generator.git
    cd ignition-view-generator
    ```
2.  **Install Python Dependencies:**
    IVG requires Python 3 and its dependencies can be installed via `pip`:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Docker (for deployment):**
    Ensure you have Docker installed and a running Ignition Docker container if you plan to use `deploy.sh`.

## 🛠️ Usage

### 1. Define Your View
Create your Ignition Perspective view definition in a YAML file. See the `examples/` directory for sample configurations like `examples/dashboard.yaml` and `examples/test_page.yaml`.

### 2. Generate `view.json`
Use the `generator.py` script to compile your YAML definition into Ignition's `view.json` format:
```bash
python3 generator.py examples/dashboard.yaml -o output_view.json
```
This will also create an accompanying `resource.json` file.

### 3. Automated Deployment (Recommended)
For seamless deployment to an Ignition Docker container, use the `deploy.sh` script:
```bash
./deploy.sh examples/dashboard.yaml
```
This script will:
*   Compile the YAML using `generator.py`.
*   Copy `view.json` and `resource.json` to your specified Ignition project in the Docker container.
*   Update Ignition's `page-config/config.json` and `resource.json` if `config.json` exists in the IVG project root, allowing for dynamic page routing.
*   Automatically trigger a rescan in the Ignition Gateway to load your new/updated view.

### 4. Watch Mode for Development
For rapid development, you can use the `watch.py` script. It monitors your YAML file for changes and automatically recompiles and redeploys the view using `generator.py` and `deploy.sh`.
```bash
python3 watch.py examples/test_page.yaml
```

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

### `config.json` for Page Routing
If you have a `config.json` file in the root of this project, it will be automatically deployed by `deploy.sh` to Ignition's `page-config` directory. This allows you to define custom URLs that map to your generated views.
Example `config.json`:
```json
{
  "pages": [
    {
      "url": "/my_custom_page",
      "viewPath": "MyGeneratedView"
    }
  ]
}
```

## 🤝 Contributing
Pull requests are welcome! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines. We are looking to expand the component map, add support for Coordinate Container positioning logic, and integrate more advanced Ignition features.

## 📜 License
MIT
