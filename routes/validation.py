

def validate_description(desc) :
    if len(desc) <= 255 :
        return True

    message = "validation error : description must be less than or equal to 255 characters"
    return False,message


def validate_image_path(image_path) :
    if len(image_path) <= 100 :
        return True

    message = "validation error : image path must be less than or equals to 100 characters"
    return False,message


def validate_title(title) :
    title_len = len(title)
    if title_len>=5 and title_len<=100 :
        return True
    message = "validation error : image path must be greater than 5 and less than  or equals to 100 characters"
    return False,message


    
