import os, json, urllib.parse

history_dir = os.path.expanduser('~/Library/Application Support/Code/User/History')
workspace_prefix = 'file:///Users/selmalier/Downloads/Saga%20nettside/'

best_files = {}

for root, dirs, files in os.walk(history_dir):
    if 'entries.json' in files:
        entries_path = os.path.join(root, 'entries.json')
        try:
            with open(entries_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            res = data.get('resource', '')
            if res.startswith(workspace_prefix) and res.endswith('.html'):
                file_name = urllib.parse.unquote(res.replace(workspace_prefix, ''))
                
                # get latest non-empty file
                valid_entries = []
                for entry in data.get('entries', []):
                    entry_path = os.path.join(root, entry['id'])
                    if os.path.exists(entry_path) and os.path.getsize(entry_path) > 10: # > 10 bytes to be safe
                        valid_entries.append((entry['timestamp'], entry_path))
                
                if valid_entries:
                    valid_entries.sort(key=lambda x: x[0], reverse=True)
                    best_entry = valid_entries[0][1]
                    
                    if file_name not in best_files or best_files[file_name][0] < valid_entries[0][0]:
                        best_files[file_name] = (valid_entries[0][0], best_entry)
        except Exception as e:
            pass

print('Found backups:')
for f_name, (_, backup_path) in best_files.items():
    print(f_name, os.path.getsize(backup_path), backup_path)
    # Restore it!
    try:
        with open(backup_path, 'r', encoding='utf-8') as src:
            with open(f_name, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
        print(f"Restored {f_name}")
    except Exception as e:
        print(f"Failed to restore {f_name}: {e}")

