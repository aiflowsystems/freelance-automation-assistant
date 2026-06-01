def analyze_job(job_description):
    keywords = [
        "Python",
        "automation",
        "API",
        "OpenAI",
        "reporting",
        "AI",
        "workflow"
    ]

    found_skills = []

    for keyword in keywords:
        if keyword.lower() in job_description.lower():
            found_skills.append(keyword)

    return {
        "found_skills": found_skills,
        "skill_count": len(found_skills)
    }