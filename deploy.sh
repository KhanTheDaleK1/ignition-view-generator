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
docker cp "$DIR/resource.json" "$CONTAINER:$IGNITION_PATH/resource.json"

# Fix Permissions for View
echo "[3.1] Fixing View Permissions..."
docker exec -u 0 $CONTAINER chown -R ignition:ignition "$IGNITION_PATH"

# Check for Page Config and Deploy
PAGE_CONFIG="$DIR/config.json"
TARGET_PAGE_CONFIG="/usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/page-config/config.json"

if [ -f "$PAGE_CONFIG" ]; then
    echo "[3.5] Updating Page Configuration..."
    docker cp "$PAGE_CONFIG" "$CONTAINER:$TARGET_PAGE_CONFIG"
    docker exec -u 0 $CONTAINER chown ignition:ignition "$TARGET_PAGE_CONFIG"
    echo "[3.6] Updating page-config resource.json and touching to trigger rescan..."
    TMP_RES=$(mktemp)
    python3 - "$TMP_RES" <<'PY'
import json, sys
from datetime import datetime, timezone
out_path = sys.argv[1]
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
payload = {
    "scope": "G",
    "version": 1,
    "restricted": False,
    "overridable": True,
    "files": ["config.json"],
    "attributes": {
        "lastModification": {"actor": "external-tool", "timestamp": now},
        "lastModificationSignature": "0000000000000000000000000000000000000000000000000000000000000000"
    }
}
with open(out_path, "w") as f:
    json.dump(payload, f, indent=2)
PY
    docker cp "$TMP_RES" "$CONTAINER:/usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/page-config/resource.json"
    rm "$TMP_RES"
    docker exec -u 0 $CONTAINER chown ignition:ignition "/usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/page-config/resource.json"
    docker exec $CONTAINER sh -c "touch $TARGET_PAGE_CONFIG /usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/page-config/resource.json"
fi

echo "[3.7] Touching view and parent folder to trigger rescan..."
docker exec $CONTAINER sh -c "touch $IGNITION_PATH/view.json $IGNITION_PATH/resource.json"
# CRITICAL FIX: Touch the parent 'views' folder
docker exec $CONTAINER sh -c "touch /usr/local/bin/ignition/data/projects/$PROJECT/com.inductiveautomation.perspective/views"

echo "[4] Deployment Complete!"
echo "    Check: http://localhost:8088/data/perspective/client/$PROJECT/$VIEW_NAME"
