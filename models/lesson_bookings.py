from datetime import datetime

class Lesson_Booking:
    def __init__(self,client,lesson,id = None ):
        self.client = client
        self.lesson = lesson
        self.id = id