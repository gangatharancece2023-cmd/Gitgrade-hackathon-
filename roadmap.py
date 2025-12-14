def generate_feedback(data):
    summary = []
    roadmap = []

    if not data["has_readme"]:
        summary.append("Missing documentation.")
        roadmap.append("Add a detailed README.md")

    if data["commit_count"] < 5:
        summary.append("Low commit activity.")
        roadmap.append("Commit regularly with meaningful messages")

    if data["stars"] == 0:
        roadmap.append("Improve project visibility with better description")

    if not roadmap:
        roadmap.append("Add automated tests and CI/CD pipelines")

    return " ".join(summary) or "Good project structure.", roadmap
  
