from app import app
from models import db, User, Post

with app.app_context():
    db.drop_all()
    db.create_all()

users = [
    User(
        first_name="John",
        last_name="Wick",
        image_url="https://avatarfiles.alphacoders.com/336/336452.jpg",
    ),
    User(
        first_name="Mace",
        last_name="Windu",
        image_url="https://comicvine.gamespot.com/a/uploads/scale_medium/11122/111226069/4817468-6565664823-tumbl.jpg",
    ),
    User(
        first_name="Anakin",
        last_name="Skywalker",
        image_url="https://i.redd.it/vwm1lqdtymj91.jpg",
    ),
    User(
        first_name="John",
        last_name="Nolan",
        image_url="https://tv-fanatic-res.cloudinary.com/iu/s--faBe1hrA--/t_full/cs_srgb,f_auto,fl_strip_profile.lossy,q_auto:420/v1679686940/john-nolan-the-rookie-s5e19.png",
    ),
    User(
        first_name="Naruto",
        last_name="Uzumaki",
        image_url="https://comicvine.gamespot.com/a/uploads/scale_medium/11117/111178336/5603895-dcc2d502-6c35-49c9-c93c-6eae7f44d551.jpg",
    ),
    User(
        first_name="Hera",
        last_name="Syndulla",
        image_url="https://upload.wikimedia.org/wikipedia/en/e/e3/Hera_Syndulla_Ahsoka.jpg",
    ),
    User(
        first_name="Bo-Katan",
        last_name="Kryze",
        image_url="https://i.redd.it/0d2d1q6qm0k61.jpg",
    ),
    User(
        first_name="Ahsoka",
        last_name="Tano",
        image_url="https://i.redd.it/4spfxs2x0ie61.jpg",
    ),
    User(first_name="Ghost", last_name="Unknown"),
]

post = Post(
    title="The Force",
    content="The Force was an energy field created by all life that bound everything in the universe together. It was known by a variety of names throughout galactic history: It was called the Ashla by the Lasats, It by the dianoga Omi, the Life Current by the Mustafarians, the Tide by the Lew'elans, the Sight by the Chiss, the Life Wind by the Zeffonians, the Great Presence by the Pathfinders of the Chaos, the Luminous Mist by the Mist-Weavers, the Unity by the Sorcerers of Tund, and as the Beyond by the Magys and her people. The Force was created by life, and therefore it resided in all life forms. It was especially powerful in a select group of individuals who were born with a high concentration of midi-chlorians—microscopic, intelligent lifeforms that formed a symbiotic relationship with and communicated the will of the Force to their host—in their blood. These people were deemed Force-sensitive, and were capable of consciously sensing the Force. With this conscious sense of the Force came the ability to harness it, allowing Force-sensitives to access various Force powers. Unlike organic beings, droids and other artificial constructs existed outside of the Force. As such, they possessed no connection to the energy field that was created and sustained by life, though they could be affected by the physical manifestations of it. Apart from its scientific aspect, the Force was the basis of various religious organizations, who held differing views as to the nature and purpose of the Force. These included the Church of the Force, the Guardians of the Whills, and most notably the Jedi and Sith Orders. In addition, the Lasats believed that the Force was the 'spirit' of the galaxy.",
    user_id=1,
)

with app.app_context():
    db.session.add_all(users)
    db.session.commit()
    db.session.add(post)
    db.session.commit()
