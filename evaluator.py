def evaluate_repo(data):
    score = 0

    if data["has_readme"]:
        score += 20
    if data["commit_count"] > 10:
        score += 20
    if data["file_count"] > 5:
        score += 15
    if data["stars"] > 5:
        score += 15
    if data["language"] != "Unknown":
        score += 10

    if score > 85:
        level = "Advanced (Gold)"
    elif score > 60:
        level = "Intermediate (Silver)"
    else:
        level = "Beginner (Bronze)"

    return score, level
