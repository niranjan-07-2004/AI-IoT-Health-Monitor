def predict_risk(heart_rate, temperature, movement):

    score = 0

    # Heart rate rules
    if heart_rate > 120 or heart_rate < 50:
        score += 2
    elif heart_rate > 100:
        score += 1

    # Temperature rules
    if temperature > 39:
        score += 2
    elif temperature > 38:
        score += 1

    # Movement stress
    if movement == 2 and heart_rate > 100:
        score += 1

    # Risk levels
    if score >= 3:
        return 2   # HIGH RISK
    elif score == 2:
        return 1   # MEDIUM RISK
    else:
        return 0   # NORMAL
