"""Routes for the course resource.
"""

import datetime
from decimal import Decimal
from http import HTTPStatus
from flask import request

import data
from run import app


@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    course = data.courses.get(id)
    if not course :
        message = "Course {} does not exist".format(id)
        return {"message": message}, 404
    ret_course = course.copy()
    ret_course.pop('id')
    return {'data' : ret_course}


@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of course, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use default of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    page_number = request.args.get('page-number', type=int, default=1)
    page_size = request.args.get('page-size', type=int, default=10)
    title_words = request.args.get('title_words')

    title_words_list = []
    if title_words :
        title_words_list = [ word.strip() for word in title_words.split(",") ]
    
    keys = list(data.courses.keys())

    record_count = len(keys)
    page_count = record_count // page_size

    start_page_index = page_size * (page_number -1)
    end_page_index = start_page_index + page_size
    
    ret_courses = [ data.courses.get(key) for key in keys[start_page_index:end_page_index]]
    
    metadata = {
            "page_count" : page_count,
            "page_number" : page_number,
            "page_size" : page_size,
            "record_count": record_count
            }

    return { "data" : ret_courses , "metadata" : metadata}


@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    title = request.json.get('title')
    price = request.json.get('price')
    description = request.json.get('description')
    discount_price = request.json.get('discount_price')
    on_discount = request.json.get('on_discount')
    image_path = request.json.get('image_path')

    date_created = datetime.datetime.now().isoformat()
    date_updated = date_created

    data.last_id = data.last_id +1
    _id = data.last_id


    course = {
            'title': title,
            'price': price,
            'description': description,
            'discount_price': discount_price,
            'on_discount': on_discount,
            'image_path': image_path,
            'date_created': date_created,
            'date_updated': date_updated,
            'id': _id
            }
    data.courses[_id] = course

    return {"data": course}, 201


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE
    _id = request.json.get('id')
    title = request.json.get('title')
    price = request.json.get('price')
    description = request.json.get('description')
    discount_price = request.json.get('discount_price')
    on_discount = request.json.get('on_discount')
    image_path = request.json.get('image_path')

    if id != _id :
        message =  "the id does not match the payload"
        return {"message": message}, 400

    course = data.courses.get(id)
    if not course :
        message = "Course {} does not exist".format(id)
        return {"message": message}, 404
    
    course['title'] = title
    course['price'] = price
    course['description'] = description
    course['discount_price'] = discount_price
    course['image_path'] = image_path
    course['on_discount'] = on_discount

    ret_course = course.copy()
    ret_course.pop('date_created')
    return {"data": ret_course}




@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    message = ""
    course = data.courses.get(id)

    if not course :
        message = "Course {} does not exist".format(id)
        return {"message": message}, 404

    del data.courses[id]
    message = "The Specified course was deleted"
    return {"message": message}, 200
    

