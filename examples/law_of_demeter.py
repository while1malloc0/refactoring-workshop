def stores_near_user(user: User):
    if not user.has_location_preferences():
        raise Exception("User does not have location enabled")
    return get_six_nearest_stores(user)


def get_six_nearest_stores(user: User):
    zip_code = user.location().zip_code().normalize()
    return stores_nearest_to(zip_code, 6)