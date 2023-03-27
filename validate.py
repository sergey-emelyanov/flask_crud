def validation(user):
    errors = {}
    if not user["name"]:
        errors["name"] = "Cant be blanc"
    if not user["email"]:
        errors["email"] = "Cant be blanc"

    return errors