def generate_proposal(job_analysis):
    skills = ", ".join(job_analysis["found_skills"])

    proposal = f"""Freelance Proposal

Hello,

I can help you with this project.

Based on your job description, the key skills required include:
{skills}

I have experience building Python automation tools, AI-powered workflows, reporting systems, and OpenAI API integrations.

I can build a clean, practical solution that helps automate your workflow and reduce manual work.

Best regards,
Adam
"""

    return proposal