def validate_user_email(email):
    username, domain = email.split("@")
    subdomain, tld = domain.split(".") 
    if tld not in ('edu', 'gov', 'net', 'org', 'com'):
        raise Exception("Email from invalid TLD")

    for special in "&>()[];:,@\\":
        if special in subdomain:
            raise Exception("Special characters not allowed in email subdomains")

    if len(username) > 60:
        raise Exception("User name can only be 60 characters or fewer")

    for special in "&>()[];:,@\\":
        if special in username:
            raise Exception("Special characters not allowed in email username")
    
    if "+" in username:
        name, folder = username.split("+")
        normalized_email = "{}@{}.{}".format(name, subdomain, tld)
        if normalized_email in get_all_emails():
            raise Exception("Duplicate emails found for {}".format(normalized_email))