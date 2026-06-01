import json
from pathlib import Path
from modules.job_analyzer import analyze_job
from modules.proposal_generator import generate_proposal
from modules.cover_letter_generator import generate_cover_letter
from modules.followup_generator import generate_followup

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]

Path(output_folder).mkdir(exist_ok=True)

with open("job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

job_analysis = analyze_job(job_description)
proposal = generate_proposal(job_analysis)
cover_letter = generate_cover_letter(job_analysis)
followup = generate_followup(job_analysis)

proposal_file = Path(output_folder) / config["proposal_file"]
with open(proposal_file, "w", encoding="utf-8") as file:
    file.write(proposal)

cover_letter_file = Path(output_folder) / config["cover_letter_file"]
with open(cover_letter_file, "w", encoding="utf-8") as file:
    file.write(cover_letter)

followup_file = Path(output_folder) / config["followup_file"]
with open(followup_file, "w", encoding="utf-8") as file:
    file.write(followup)

summary = f"""Freelance Automation Assistant Summary

Skills Found:
{", ".join(job_analysis["found_skills"])}

Skill Count:
{job_analysis["skill_count"]}

Generated Files:
- {proposal_file}
- {cover_letter_file}
- {followup_file}
"""

summary_file = Path(output_folder) / config["summary_file"]

with open(summary_file, "w", encoding="utf-8") as file:
    file.write(summary)

print("Freelance Automation Assistant")
print("==============================")
print()

print("Job Description Loaded")
print()

print(job_description[:300])

print()
print("Job Analysis")
print("------------")
print(f"Found Skills: {', '.join(job_analysis['found_skills'])}")
print(f"Skill Count: {job_analysis['skill_count']}")

print(f"Proposal generated: {proposal_file}")
print(f"Cover letter generated: {cover_letter_file}")
print(f"Follow-up message generated: {followup_file}")
print(f"Summary generated: {summary_file}")
