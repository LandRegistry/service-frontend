from matching import check_user_match
from ownership import check_user_is_owner

def is_matched(user):
    return check_user_match(user)

def is_owner(user, title_number):
    return check_user_is_owner(user, title_number)
