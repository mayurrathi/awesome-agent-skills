import os
import re

SKILLS_DIR = "skills"

def clean_yaml_name(content):
    # This regex looks for 'name: <number_prefix>', handling things like 'name: 1.5.1 Foo' or 'name: 20-foo'
    # We'll use a precise substitution for lines starting with 'name:'
    def replacer(match):
        prefix = match.group(1) # 'name: '
        value = match.group(2) # '1.5.1 Foo'
        # strip numbers, dots, dashes, and underscores at the very beginning of the value
        clean_value = re.sub(r'^[\d\.\-_]+', '', value).strip()
        # Title case to fix things like "andruia-niche-intelligence" to "Andruia Niche Intelligence"
        clean_value = clean_value.replace('-', ' ').replace('_', ' ').title()
        return f"{prefix}{clean_value}"
        
    # Apply to frontmatter name block
    new_content = re.sub(r'^(name:\s*)(.*?)$', replacer, content, flags=re.MULTILINE)
    return new_content

def process_files():
    count = 0
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            filepath = os.path.join(root, "SKILL.md")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = clean_yaml_name(content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                
    print(f"Updated names in {count} SKILL.md files.")

if __name__ == "__main__":
    process_files()
