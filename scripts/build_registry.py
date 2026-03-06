import os
import re
import json

SKILLS_DIR = "skills"
OUTPUT_FILE = "skills.json"

def parse_frontmatter(content):
    frontmatter = {}
    match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip("'\"")
    return frontmatter

def build_registry():
    skills = []
    
    if not os.path.exists(SKILLS_DIR):
        print(f"Error: Directory {SKILLS_DIR} not found.")
        return
        
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            md_path = os.path.join(root, "SKILL.md")
            item = os.path.basename(root)
            
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                    
                meta = parse_frontmatter(content)
                
                # Clean up name if it exists in frontmatter
                if 'name' in meta:
                    clean_name = re.sub(r'^[\d\.\-_]+', '', meta['name']).strip()
                    meta['name'] = clean_name.replace('-', ' ').replace('_', ' ').title()
                
                # Default categories based on common paths if not defined
                if 'category' not in meta:
                    parts = root.split(os.sep)
                    if len(parts) > 1:
                        top_level = parts[1]
                        # Strip numbering from root folder name
                        clean_top_level = re.sub(r'^[\d\.\-_]+', '', top_level).strip()
                        broad_category = clean_top_level.replace('_', ' ').replace(' and ', ' & ').title()
                    else:
                        broad_category = "General AI Skills"
                    meta['category'] = broad_category
                        
                # Provide defaults if missing
                if 'name' not in meta:
                    clean_item = re.sub(r'^[\d\.\-_]+', '', item).strip()
                    meta['name'] = clean_item.replace('_', ' ').title()
                    
                meta['id'] = re.sub(r'^[\d\.\-_]+', '', item).strip()
                
                # Extract copyable prompt (everything after frontmatter)
                prompt_content = re.sub(r'^---\s*(.*?)\s*---', '', content, flags=re.DOTALL).strip()
                meta['prompt'] = prompt_content
                
                skills.append(meta)

    # Ensure directory exists if needed
    out_dir = os.path.dirname(OUTPUT_FILE)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(skills, f, indent=2)
        
    print(f"✅ Successfully compiled {len(skills)} skills into {OUTPUT_FILE}")

if __name__ == "__main__":
    build_registry()
