def chk(p):
    score = 0
    tips = []

    if len(p) >= 8:
        score += 1
    else:
        tips.append("use at least 8 characters")

    if len(p) >= 12:
        score += 1
    else:
        tips.append("use at least 12 characters for better security")

    for c in p:
        if any(c.islower()):
            score += 1
            break
        else:
            tips.append("add lowercase letters")

    for c in p:
        if any(c.isupper()):
            score += 1
            break
        else:
            tips.append("add uppercase letters")

    for c in p:
        if any(c.isdigit()):
            score += 1
            break
        else:
            tips.append("add numbers")

    for c in p:
        if any(not c.isalnum() for c in p):
            score += 1
            break
        else:
            tips.append("add special characters")

    if len(p) > 0 and len(set(p)) < len(p) * 0.65:
        score -= 1
        tips.append("avoid too many repeated characters")

    if score <= 2:
        level = "Weak"
    elif score <= 4:
        level = "Moderate"
    else:
        level = "Strong"

    print("Security tips:")
    if tips:
        for t in tips:
            print("-", t)
    else:
        print("- No major issues found.")

    return level
