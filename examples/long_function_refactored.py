def validate_tld_allowed(tld):
    if tld not in ('edu', 'gov', 'net', 'org', 'com'):
        raise Exception("Email from invalid TLD")


def validate_no_special_chars(guess):
    for special in "&>()[];:,@\\":
        if special in guess:
            raise Exception("Special characters not allowed in email subdomains")


def validate_domain(domain):
    subdomain, tld = domain.split(".") 
    validate_tld_allowed(subdomain)
    validate_no_special_chars(subdomain)


def validate_shorter_than_sixty_chars(username):
    if len(username) > 60:
        raise Exception("Usernames in email cannot be longer than 60 characters")


def validate_username(username):
    validate_shorter_than_sixty_chars(username)
    validate_no_special_chars(username)


def validate_no_duplicate_emails(email):
    if "+" in email:
        username, domain = email.split("@")
        name, folder = username.split("+")
        normalized_email = "{}@{}".format(name, domain)
        if normalized_email in get_all_emails():
            raise Exception("Duplicate emails found for {}".format(normalized_email))


def validate_user_email(email):
    username, domain = email.split("@")
    validate_domain(domain)
    validate_username(username)
    validate_no_duplicate_emails(email)