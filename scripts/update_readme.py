import json
import re
from collections import defaultdict

def generate_readme_table():
    with open('skills.json', 'r', encoding='utf-8') as f:
        skills = json.load(f)

    # Group skills by category
    categories = defaultdict(list)
    for skill in skills:
        cat = skill.get('category', 'Uncategorized')
        categories[cat].append(skill)
        
    # Sort categories alphabetically
    sorted_categories = sorted(categories.keys())

    # Build markdown table string
    markdown_lines = []
    
    for category in sorted_categories:
        markdown_lines.append(f"### {category}")
        markdown_lines.append(f"<details><summary>View {len(categories[category])} Skills <i>(Click to expand)</i></summary>")
        markdown_lines.append("")
        markdown_lines.append("| Skill Name | Description |")
        markdown_lines.append("|---|---|")
        
        # Sort skills by name
        cat_skills = sorted(categories[category], key=lambda x: x.get('name', ''))
        
        for skill in cat_skills:
            name = skill.get('name', '')
            desc = skill.get('description', '').replace('\n', ' ')
            # Truncate description intelligently to keep tables clean
            if len(desc) > 80:
                desc = desc[:77] + "..."
            
            markdown_lines.append(f"| **{name}** | {desc} |")
            
        markdown_lines.append("")
        markdown_lines.append("</details>")
        markdown_lines.append("")
        
    return "\n".join(markdown_lines)

def update_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    new_table = generate_readme_table()
    
    start_marker = "<!-- SKILLS_START -->"
    end_marker = "<!-- SKILLS_END -->"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx + len(start_marker)] + "\n\n" + new_table + "\n\n" + content[end_idx:]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected skills into README.md")
    else:
        print("Markers not found in README.md")

if __name__ == "__main__":
    update_readme()
