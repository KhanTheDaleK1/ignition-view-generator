#!/bin/bash
# deploy.sh - Compile and Deploy to Ignition Docker Container

# Resolve Script Directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Arguments
INPUT_FILE="${1:-$DIR/examples/dashboard.yaml}"

# Derive View Name from Filename (e.g., "test_page.yaml" -> "test_page")
FILENAME=$(basename -- "$INPUT_FILE")
VIEW_NAME="${FILENAME%.*}"

PROJECT="OT_Sandbox"
CONTAINER="ignition_scada"
IGNITION_PATH="/usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/views/$VIEW_NAME"

echo "[1] Compiling YAML: $INPUT_FILE"
echo "    Target View: $VIEW_NAME"

python3 "$DIR/generator.py" "$INPUT_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Compilation failed."
    exit 1
fi

echo "[2] Ensuring Target Directory Exists..."
docker exec $CONTAINER mkdir -p "$IGNITION_PATH"

echo "[3] Deploying to Container..."
docker cp view.json "$CONTAINER:$IGNITION_PATH/view.json"

# Check for Page Config and Deploy
PAGE_CONFIG="$DIR/page-config.json"
TARGET_PAGE_CONFIG="/usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/page-config.json"

if [ -f "$PAGE_CONFIG" ]; then
    echo "[3.5] Updating Page Configuration..."
    docker cp "$PAGE_CONFIG" "$CONTAINER:$TARGET_PAGE_CONFIG"
fi

echo "[4] Deployment Complete!"
echo "    Check: http://localhost:8088/data/perspective/client/$PROJECT/$VIEW_NAME"
