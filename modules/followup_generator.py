def generate_followup(job_analysis):
    skills = ", ".join(job_analysis["found_skills"])

    followup = f"""Follow-up Message

Hello,

I wanted to follow up on my previous message regarding your project.

Based on the job requirements, I believe my experience with {skills} would allow me to build a practical and efficient solution for your needs.

I would be happy to discuss the project further and answer any questions.

Best regards,
Adam
"""

    return followup