def build_login_payload(username, password):
    """
    Build a payload for user login.
    
    :param username: The username of the user.
    :param password: The password of the user.
    :return: A dictionary representing the login payload.
    """
    return {
        "username": username,
        "password": password
    }


def build_user_payload(name, username, email):
    """
    Build a payload for creating a new user.
    
    :param name: The name of the user.
    :param username: The username of the user.
    :param email: The email address of the user.
    :return: A dictionary representing the user payload.
    """
    return {
        "name": name,
        "username": username,
        "email": email
    }


def build_post_payload(title, body, user_id):
    """
    Build a payload for creating a new post.
    
    :param title: The title of the post.
    :param body: The body content of the post.
    :param user_id: The ID of the user creating the post.
    :return: A dictionary representing the post payload.
    """
    return {
        "title": title,
        "body": body,
        "userId": user_id
    }