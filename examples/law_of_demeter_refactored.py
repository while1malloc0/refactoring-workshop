def stores_near_user(user: User):
    if not user.has_location_preferences():
        raise Exception("User does not have location enabled")
    # zip_code function added to user class
    zip_code = user.zip_code()
    return get_six_nearest_stores(zip_code)


def get_six_nearest_stores(zip_code:  ZipCode):
    return stores_nearest_to(zip_code.normalize(), 6)