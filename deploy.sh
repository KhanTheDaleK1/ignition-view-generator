#!/bin/bash
# deploy.sh - Compile and Deploy to Ignition Docker Container

# Resolve Script Directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PROJECT="OT_Sandbox"
VIEW_NAME="GeneratedDashboard"
CONTAINER="ignition_scada"
IGNITION_PATH="/usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/views/$VIEW_NAME"

echo "[1] Compiling YAML..."
python3 "$DIR/generator.py" "$DIR/examples/dashboard.yaml"
if [ $? -ne 0 ]; then
    echo "Error: Compilation failed."
    exit 1
fi

echo "[2] Ensuring Target Directory Exists..."
docker exec $CONTAINER mkdir -p "$IGNITION_PATH"

echo "[3] Deploying to Container..."
# The generator outputs view.json in the CWD, we need to move it
docker cp view.json "$CONTAINER:$IGNITION_PATH/view.json"

echo "[4] Deployment Complete!"
echo "    Check: http://localhost:8088/data/perspective/client/$PROJECT/$VIEW_NAME"
