# Codex Documentation: Ignition View Generator (IVG)

This document provides technical details about the `Ignition View Generator` project for developers.

## Project Structure

The project is structured as follows:

*   `.git/`: Git version control files.
*   `examples/`: Example YAML files.
*   `config.json`: Configuration file.
*   `deploy.sh`: Deployment script.
*   `generator.py`: The main Python script for generating views.
*   `page-config.json`: Page configuration file.
*   `README.md`: Detailed project documentation.
*   `GEMINI.md`: Gemini interaction guide.
*   `robots.txt`: Search engine indexing rules.
*   `sitemap.xml`: Sitemap for crawlers.
*   `view.json`: Example output view.
*   `watch.py`: A script to watch for file changes.

## Key Files

*   `generator.py`: The core of the project. This Python script takes a YAML file as input and generates an Ignition `view.json` file.
*   `examples/dashboard.yaml`: An example YAML file that demonstrates how to define a view.
*   `README.md`: The main documentation file, which includes installation and usage instructions.

## Development Setup

This is a Python project that uses the `PyYAML` library. To get started, install the required dependency: `pip install pyyaml`. The main logic is in `generator.py`. You can extend the generator by adding more component mappings.

*This document is intended for developers and contributors.*
