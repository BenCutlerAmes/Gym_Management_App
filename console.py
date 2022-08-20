from models.client import Client
import repositories.client_repository as client_repo
from models.instructors import Instructor
import repositories.instructor_repository as instructor_repo
from models.lessons import Lesson

client_repo.delete_all()

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

