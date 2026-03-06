import os
import re
import shutil
from collections import defaultdict

SKILLS_DIR = "skills"
FLAT_SKILLS_DIR = "skills_flat"
README_FILE = "README.md"

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

def slugify(text):
    # Convert to kebab-case
    text = re.sub(r'^[\d\.\-_]+', '', text).strip() # remove numeric prefixes
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def clean_name(text):
    clean = re.sub(r'^[\d\.\-_]+', '', text).strip()
    return clean.replace('-', ' ').replace('_', ' ').title()

def flatten_and_collect():
    skills = []
    
    if os.path.exists(FLAT_SKILLS_DIR):
        shutil.rmtree(FLAT_SKILLS_DIR)
    os.makedirs(FLAT_SKILLS_DIR, exist_ok=True)
    
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            md_path = os.path.join(root, "SKILL.md")
            dir_name = os.path.basename(root)
            
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            meta = parse_frontmatter(content)
            
            # Determine category from original path structure before it's lost
            if 'category' not in meta:
                parts = root.split(os.sep)
                if len(parts) > 1:
                    top_level = parts[1]
                    broad_category = clean_name(top_level).replace(' And ', ' & ')
                else:
                    broad_category = "General AI Skills"
                meta['category'] = broad_category
            
            # Name
            target_name = meta.get('name', '')
            if not target_name:
                target_name = clean_name(dir_name)
            else:
                target_name = clean_name(target_name)
            meta['name'] = target_name
                
            # ID (kebab-case)
            skill_id = slugify(dir_name)
            
            # Handle duplicates
            original_skill_id = skill_id
            counter = 1
            while os.path.exists(os.path.join(FLAT_SKILLS_DIR, skill_id)):
                skill_id = f"{original_skill_id}-{counter}"
                counter += 1
                
            meta['id'] = skill_id
            
            # Copy to new location
            new_dir = os.path.join(FLAT_SKILLS_DIR, skill_id)
            os.makedirs(new_dir, exist_ok=True)
            new_path = os.path.join(new_dir, "SKILL.md")
            
            # Write updated frontmatter to new file
            # Replace old name with cleaned name if present
            if 'name:' in content:
                content = re.sub(r'^(name:\s*).*?$', rf"\g<1>{target_name}", content, flags=re.MULTILINE)
            else:
                # Add name if missing
                content = re.sub(r'^---\n', f"---\nname: {target_name}\n", content)
                
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            skills.append(meta)
            
    print(f"Flattened {len(skills)} skills into {FLAT_SKILLS_DIR}/")
    return skills

def generate_readme_table(skills):
    # Group skills by category
    categories = defaultdict(list)
    for skill in skills:
        cat = skill.get('category', 'Uncategorized')
        categories[cat].append(skill)
        
    sorted_categories = sorted(categories.keys())

    markdown_lines = []
    
    for category in sorted_categories:
        markdown_lines.append(f"### 🤖 {category}")
        markdown_lines.append(f"<details><summary>View {len(categories[category])} Skills <i>(Click to expand)</i></summary>")
        markdown_lines.append("")
        
        cat_skills = sorted(categories[category], key=lambda x: x.get('name', ''))
        
        for skill in cat_skills:
            name = skill.get('name', '')
            desc = skill.get('description', '').replace('\n', ' ')
            if len(desc) > 120:
                desc = desc[:117] + "..."
            skill_id = skill.get('id', '')
            
            markdown_lines.append(f"#### `{skill_id}`")
            markdown_lines.append(f"*{name}* - {desc}")
            markdown_lines.append("```bash")
            markdown_lines.append(f"npx skills add mayurrathi/awesome-agent-skills --skill {skill_id}")
            markdown_lines.append("```")
            markdown_lines.append("---")
            markdown_lines.append("")
            
        markdown_lines.append("</details>")
        markdown_lines.append("")
        
    return "\n".join(markdown_lines)

def update_readme(skills):
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    new_table = generate_readme_table(skills)
    
    start_marker = "<!-- SKILLS_START -->"
    end_marker = "<!-- SKILLS_END -->"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx + len(start_marker)] + "\n\n" + new_table + "\n\n" + content[end_idx:]
        with open(README_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected NPX CLI blocks into README.md")
    else:
        print("Markers not found in README.md")

def main():
    if not os.path.exists(SKILLS_DIR):
        print(f"Error: Directory {SKILLS_DIR} not found.")
        return
        
    skills = flatten_and_collect()
    update_readme(skills)
    
    # Replace old skills folder with new one
    shutil.rmtree(SKILLS_DIR)
    os.rename(FLAT_SKILLS_DIR, SKILLS_DIR)
    print("Repository restructuring complete.")

if __name__ == "__main__":
    main()
