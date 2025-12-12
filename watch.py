#!/usr/bin/env python3
"""
Simple watch mode: recompiles YAML to view.json and redeploys on file changes.
Uses mtime polling (no extra dependencies). Good enough for local dev loops.
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"[watch] Command failed: {' '.join(cmd)} (exit {result.returncode})")
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Watch YAML and redeploy on change.")
    parser.add_argument("yaml", help="YAML file to watch (e.g., examples/test_page.yaml)")
    parser.add_argument("--interval", type=float, default=1.0, help="Poll interval seconds")
    parser.add_argument("--deploy-script", default="deploy.sh", help="Deploy script path")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    yaml_path = (repo_root / args.yaml).resolve()

    if not yaml_path.exists():
        print(f"[watch] File not found: {yaml_path}")
        sys.exit(1)

    last_mtime = yaml_path.stat().st_mtime
    print(f"[watch] Watching {yaml_path} (poll every {args.interval}s). Press Ctrl+C to stop.")

    # Initial build/deploy
    run([sys.executable, "generator.py", str(yaml_path)], cwd=repo_root)
    run([str(repo_root / args.deploy_script), str(yaml_path)], cwd=repo_root)

    try:
        while True:
            time.sleep(args.interval)
            try:
                current_mtime = yaml_path.stat().st_mtime
            except FileNotFoundError:
                continue
            if current_mtime != last_mtime:
                last_mtime = current_mtime
                print(f"[watch] Change detected, rebuilding + deploying...")
                run([sys.executable, "generator.py", str(yaml_path)], cwd=repo_root)
                run([str(repo_root / args.deploy_script), str(yaml_path)], cwd=repo_root)
    except KeyboardInterrupt:
        print("[watch] Stopped.")


if __name__ == "__main__":
    main()
