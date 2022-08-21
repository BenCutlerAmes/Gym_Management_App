class Lesson:
    def __init__(self, activity, duration, lesson_date, lesson_time, instructor,capacity, id = None):
        self.activity = activity
        self.duration = duration
        self.lesson_date = lesson_date
        self.lesson_time = lesson_time
        self.instructor = instructor
        self.capacity = capacity
        self.id = id