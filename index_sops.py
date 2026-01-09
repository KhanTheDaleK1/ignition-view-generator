import json
import os
import glob
from pypdf import PdfReader

VIEW_PATH = "/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/Knowledgebase/view.json"
WEBAPPS_PATH = "/mnt/projects/7. Ignition/webserver/webapps"

print(f"Loading view from {VIEW_PATH}")
with open(VIEW_PATH, 'r') as f:
    view_data = json.load(f)

sops = view_data.get('custom', {}).get('allSops', [])
print(f"Found {len(sops)} SOPs to index.")

updated_count = 0
for sop in sops:
    url = sop.get('url', '')
    if not url.endswith('.pdf'):
        continue
    
    # Resolve local path. URL is like /sops/...
    # Local path should be webapps/main/sops/...
    # Remove leading slash
    if url.startswith('/'):
        relative_path = url[1:]
    else:
        relative_path = url
        
    # Static files served from / are actually in webapps/main/
    local_path = os.path.join(WEBAPPS_PATH, "main", relative_path)
    # URL decoding might be needed (e.g. %20 -> space)
    import urllib.parse
    local_path = urllib.parse.unquote(local_path)
    
    if os.path.exists(local_path):
        try:
            reader = PdfReader(local_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + " "
            
            # Clean text: remove newlines, excessive spaces
            text = " ".join(text.split())
            
            # Limit keywords length to avoid huge JSONs (e.g., 2000 chars)
            # enough for search, not full content storage
            # Actually, user wants "search content", so we need meaningful text.
            # 5000 chars is probably fine for view.json custom prop.
            sop['keywords'] = text[:10000] 
            updated_count += 1
            print(f"Indexed: {sop['title']} ({len(text)} chars)")
        except Exception as e:
            print(f"Error reading {local_path}: {e}")
            sop['keywords'] = ""
    else:
        print(f"File not found: {local_path}")
        sop['keywords'] = ""

view_data['custom']['allSops'] = sops

print(f"Saving updated view.json with {updated_count} indexed files.")
with open(VIEW_PATH, 'w') as f:
    json.dump(view_data, f, indent=2)

print("Done.")
