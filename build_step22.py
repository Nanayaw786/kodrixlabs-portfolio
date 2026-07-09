with open("skills.html", "r") as file:
    content = file.read()

old_skills = """    <div class="section-tag">Skills</div>
    <h2>What I bring to the table</h2>
    <div class="skills-list" id="skillsList">
      <span class="skill-pill">Social Media Management</span>
      <span class="skill-pill">Content Strategy</span>
      <span class="skill-pill">Short-Form Video Creation</span>
      <span class="skill-pill">Graphic Design</span>
      <span class="skill-pill">Community Management</span>
      <span class="skill-pill">Analytics & Reporting</span>
      <span class="skill-pill">WordPress Management</span>
      <span class="skill-pill">Digital Marketing</span>
    </div>"""

new_skills = """    <div class="section-tag">Skills</div>
    <h2>What I bring to the table</h2>
    <div class="skills-list" id="skillsList">
      <span class="skill-pill">Software Development</span>
      <span class="skill-pill">Mobile App Development</span>
      <span class="skill-pill">Website Development</span>
      <span class="skill-pill">Digital Marketing</span>
      <span class="skill-pill">Social Media Management</span>
      <span class="skill-pill">Content Strategy</span>
      <span class="skill-pill">Short-Form Video Creation</span>
      <span class="skill-pill">Graphic Design</span>
      <span class="skill-pill">Community Management</span>
      <span class="skill-pill">Analytics & Reporting</span>
      <span class="skill-pill">WordPress Management</span>
    </div>"""

if old_skills in content:
    content = content.replace(old_skills, new_skills)
    print("Skills list section updated in skills.html")
else:
    print("WARNING: skills pattern not found in skills.html — no changes made")

old_tools = """    <div class="tools-grid" id="toolsGrid">
      <div class="tool-item">Canva</div>
      <div class="tool-item">CapCut</div>
      <div class="tool-item">Adobe Photoshop</div>
      <div class="tool-item">Meta Business Suite</div>
      <div class="tool-item">TikTok Studio</div>
      <div class="tool-item">WordPress</div>
      <div class="tool-item">Notion</div>
      <div class="tool-item">Google Analytics</div>
    </div>"""

new_tools = """    <div class="tools-grid" id="toolsGrid">
      <div class="tool-item">VS Code</div>
      <div class="tool-item">GitHub</div>
      <div class="tool-item">WordPress</div>
      <div class="tool-item">Figma</div>
      <div class="tool-item">Canva</div>
      <div class="tool-item">CapCut</div>
      <div class="tool-item">Adobe Photoshop</div>
      <div class="tool-item">Meta Business Suite</div>
      <div class="tool-item">TikTok Studio</div>
      <div class="tool-item">Notion</div>
      <div class="tool-item">Google Analytics</div>
      <div class="tool-item">Vercel</div>
    </div>"""

if old_tools in content:
    content = content.replace(old_tools, new_tools)
    print("Tools grid section updated in skills.html")
else:
    print("WARNING: tools pattern not found in skills.html — no changes made")

with open("skills.html", "w") as file:
    file.write(content)

print("skills.html saved successfully")