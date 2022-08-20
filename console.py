from models.client import Client
import repositories.client_repository as client_repo

from models.instructors import Instructor
import repositories.instructor_repository as instructor_repo

from models.lessons import Lesson
import repositories.lesson_repository as lesson_repo

from models.lesson_bookings import Lesson_Booking
import repositories.lesson_booking_repository as lesson_booking_repo

client_repo.delete_all()
instructor_repo.delete_all()
lesson_repo.delete_all()
# lesson_booking_repo.delete_all()


client1 = Client("Kyle","1993-09-14","kyleiscool@gmail.com")
client_repo.add_client(client1)

client2 = Client("Josh","1992-05-24","joshhatestrees@aol.com")
client_repo.add_client(client2)

client3 = Client( "Millie","1989-12-09","themills@hotmail.com")
client_repo.add_client(client3)


instructor1 = Instructor("Alex","doyouevenlift@hotmail.com")
instructor_repo.add_instructor(instructor1)

instructor2 = Instructor("Meera","smallbutmighty@gmail.com")
instructor_repo.add_instructor(instructor2)

lesson1 = Lesson("Zumba",45,"2022-08-27","12:30",instructor1)
lesson_repo.add_lesson(lesson1)

lesson2 = Lesson("Bodypump",30,"2022-08-27","14:00", instructor1)
lesson_repo.add_lesson(lesson2)

lesson3 = Lesson("GetSwolFast",90,"2022-08-28","13:00",instructor2)
lesson_repo.add_lesson(lesson3)

booking1 = Lesson_Booking(client1, lesson1)
lesson_booking_repo.add_booking(booking1)

booking2 = Lesson_Booking(client2, lesson1)
lesson_booking_repo.add_booking(booking2)

booking3 = Lesson_Booking(client1,lesson3)
lesson_booking_repo.add_booking(booking3)
