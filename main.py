from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import CourseDatabase

api = FastAPI() # create new instance
db = CourseDatabase() #create instance

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@api.get("/courses")
def get_courses():
    return [
        {
            "id": 1,
            "name": "Course 1"
        },
        {
            "id": 2,
            "name": "Course 2"
        },
        {
            "id": 3,
            "name": "Course 3"
        },
        {
            "id": 4,
            "name": "Course 4"
        },
        {
             "id": 5,
            "name": "Course 5"

        }
         {
             "id": 6,
            "name": "Course 5"

        }
         {
             "id": 7,
            "name": "Course 5"

        }
    ]

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return a+b

@api.get("/courses-details/")
def coursesdetails():
    return db.execute("SELECT * FROM coursedetails")


# @api.get("/course/{course_id}/thumbnail")
# def get_course_thumbnail_by_id(course_id: str):
#     return {"thumbnail": course_id}


#       return [
#     {
#         "title": "fastapi",
#         "description": "In this video, we'll demystify the world of APIs, breaking down complex concepts into easy-to-understand terms",
#         "imageSrc": "../images/fastapi-images-1.png",
#         "url": "courseplayer.html"
#     },
#     {
#         "title": "fastapi-beginner",
#         "description": "In this video, we'll demystify the world of APIs, breaking down complex concepts into easy-to-understand terms",
#         "imageSrc": "../images/fastapi-images-2.jpeg",
#         "url": "courseplayer.html"
#     }
# ]