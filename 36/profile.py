def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if len(sports) > 5:
        raise ValueError("Too many sports.")

    profile = {"name": name, "age": age}

    if sports:
        profile["sports"] = sorted(sports)

    if awards:
        profile["awards"] = awards

    return profile
