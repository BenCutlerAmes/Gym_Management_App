from models.client import Client
import repositories.client_repository as client_repo
from models.instructors import Instructors
from models.lessons import Lessons

client_repo.delete_all()

client1 = Client("Kyle","1993-09-14","kyleiscool@gmail.com")
client_repo.add_client(client1)

client2 = Client("Josh","1992-05-24","joshhatestrees@aol.com")
client_repo.add_client(client2)




