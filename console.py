from datetime import datetime,timedelta

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


client1 = Client("Kyle Van Der Merwe","1993-09-14","kyleiscool@gmail.com")
client_repo.add_client(client1)
client2 = Client("Josh Marks","1992-05-24","joshhatestrees@aol.com")
client_repo.add_client(client2)
client3 = Client( "Millie Chapman","1989-12-09","themills@hotmail.com")
client_repo.add_client(client3)
client4 = Client( "Beverley","1956-02-01","badbev@gmail.com")
client_repo.add_client(client4)
client1=Client("Aldis Vicioso","1983-1-12","avicioso3@psu.edu")
client_repo.add_client(client1)
client1=Client("Aldis Vicioso","1983-1-12","avicioso3@psu.edu")
client_repo.add_client(client1)
client1=Client("Lewiss Scibsey","1990-2-28","lscibsey4@forbes.com")
client_repo.add_client(client1)
client1=Client("Hillier Sneezem","1990-1-14","hsneezem5@usgs.gov")
client_repo.add_client(client1)
client1=Client("Malvina Strainge","1986-2-19","mstrainge6@whitehouse.gov")
client_repo.add_client(client1)
client1=Client("Ryon McKune","1982-1-31","rmckune7@go.com")
client_repo.add_client(client1)
client1=Client("Donalt Ecclesall","1983-4-9","decclesall8@usnews.com")
client_repo.add_client(client1)
client1=Client("Lek Elliston","1996-3-21","lelliston9@jigsy.com")
client_repo.add_client(client1)
client1=Client("Reg Poultney","2000-5-1","rpoultneya@noaa.gov")
client_repo.add_client(client1)
client1=Client("Corri Messum","1986-9-9","cmessumb@nymag.com")
client_repo.add_client(client1)
client1=Client("Morly Schubbert","1984-2-27","mschubbertc@google.pl")
client_repo.add_client(client1)
client1=Client("Corilla Morkham","1985-2-23","cmorkhamd@cargocollective.com")
client_repo.add_client(client1)
client1=Client("Dori Sivier","2003-3-16","dsiviere@google.ru")
client_repo.add_client(client1)
client1=Client("Federica Stoyle","1991-3-14","fstoylef@timesonline.co.uk")
client_repo.add_client(client1)
client1=Client("Northrup Pidgen","2003-3-30","npidgeng@g.co")
client_repo.add_client(client1)
client1=Client("Winona Speir","1997-10-18","wspeirh@dailymail.co.uk")
client_repo.add_client(client1)
client1=Client("Franciskus Obey","1986-3-30","fobeyi@buzzfeed.com")
client_repo.add_client(client1)
client1=Client("Tildy Dearden","1990-8-6","tdeardenj@slate.com")
client_repo.add_client(client1)
client1=Client("Onfroi Lawie","2003-1-2","olawiek@aboutads.info")
client_repo.add_client(client1)
client1=Client("Kacie Langridge","1987-12-29","klangridgel@washingtonpost.com")
client_repo.add_client(client1)
client1=Client("Caspar Halbeard","2002-1-13","chalbeardm@edublogs.org")
client_repo.add_client(client1)
client1=Client("Shelley Lithcow","2002-5-4","slithcown@illinois.edu")
client_repo.add_client(client1)
client1=Client("Izzy Ferminger","2001-6-29","ifermingero@wikipedia.org")
client_repo.add_client(client1)
client1=Client("Pauly Sugar","1994-9-20","psugarp@elpais.com")
client_repo.add_client(client1)
client1=Client("Joli Orteaux","1978-1-1","jorteauxq@ucoz.com")
client_repo.add_client(client1)
client1=Client("Tallulah Gouly","1988-6-10","tgoulyr@blogs.com")
client_repo.add_client(client1)
client1=Client("Linette Drust","2002-2-7","ldrusts@merriam-webster.com")
client_repo.add_client(client1)
client1=Client("Anson Jeans","1982-8-21","ajeanst@mysql.com")
client_repo.add_client(client1)
client1=Client("Lissy Pochin","1997-11-19","lpochinu@disqus.com")
client_repo.add_client(client1)
client1=Client("Myranda Mendez","1998-11-16","mmendezv@jugem.jp")
client_repo.add_client(client1)
client1=Client("Skipton Lovelady","1993-1-25","sloveladyw@msu.edu")
client_repo.add_client(client1)
client1=Client("Bernardine Scade","2002-5-3","bscadex@hubpages.com")
client_repo.add_client(client1)
client1=Client("Ly Staten","1980-9-28","lstateny@imgur.com")
client_repo.add_client(client1)
client1=Client("Baily Dominighi","1990-11-20","bdominighiz@feedburner.com")
client_repo.add_client(client1)
client1=Client("Roslyn Osan","1997-12-30","rosan10@wikipedia.org")
client_repo.add_client(client1)
client1=Client("Ad Cleveley","1990-10-11","acleveley11@altervista.org")
client_repo.add_client(client1)
client1=Client("Matthew Lampart","1993-6-12","mlampart12@1688.com")
client_repo.add_client(client1)
client1=Client("Christoforo MacRory","1989-1-21","cmacrory13@nps.gov")
client_repo.add_client(client1)
client1=Client("Mela Cowherd","1999-1-21","mcowherd14@howstuffworks.com")
client_repo.add_client(client1)
client1=Client("Annette Lawson","1998-6-16","alawson15@tuttocitta.it")
client_repo.add_client(client1)
client1=Client("Sybil Penswick","1989-8-20","spenswick16@bbb.org")
client_repo.add_client(client1)
client1=Client("Lancelot Baterip","2004-2-19","lbaterip17@digg.com")
client_repo.add_client(client1)
client1=Client("Carry Lavery","1984-1-8","clavery18@ibm.com")
client_repo.add_client(client1)
client1=Client("Lilyan Ruoff","2000-1-17","lruoff19@google.de")
client_repo.add_client(client1)
client1=Client("Elayne Lartice","2002-9-22","elartice1a@usgs.gov")
client_repo.add_client(client1)
client1=Client("Ross Biaggi","1982-9-13","rbiaggi1b@marriott.com")
client_repo.add_client(client1)
client1=Client("Susann Fergyson","1991-8-18","sfergyson1c@indiatimes.com")
client_repo.add_client(client1)
client1=Client("Charisse Cawtheray","1992-1-13","ccawtheray1d@springer.com")
client_repo.add_client(client1)


instructor1 = Instructor("Alex","alex@thefitnessfactory.com")
instructor_repo.add_instructor(instructor1)
instructor2 = Instructor("Meera","meera@thefitnessfactory.com")
instructor_repo.add_instructor(instructor2)
instructor3 = Instructor("John","john@thefitnessfactory.com")
instructor_repo.add_instructor(instructor3)
instructor4 = Instructor("Stuart","stuart@thefitnessfactory.com")
instructor_repo.add_instructor(instructor4)
instructor5 = Instructor("Eric","eric@thefitnessfactory.com")
instructor_repo.add_instructor(instructor5)

lesson1 = Lesson("Zumba",60,"2022-08-27","13:00",instructor1,20)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1
        

lesson1 = Lesson("Bodypump",60,"2022-08-28","14:00", instructor1,1)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1

lesson1 = Lesson("Legs Bums & Tums",30,"2022-08-24","11:00",instructor3,10)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1

lesson1 = Lesson("Swimming",90,"2022-08-28","16:00",instructor5,10)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1

lesson1 = Lesson("Cage Fighting",15,"2022-08-26","09:00",instructor4,4)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1

lesson1 = Lesson("Boxercise",60,"2022-08-23","13:00",instructor2,10)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1

lesson1 = Lesson("AquaFit",60,"2022-08-23","05:30",instructor5,10)
i=0
while i < 52:
    lesson_repo.add_lesson(lesson1)
    old = datetime.fromisoformat(str(lesson1.lesson_date))
    new = old + timedelta(7)
    lesson1.lesson_date = new
    i+=1




