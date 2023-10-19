from unittest import TestCase
from app import create_app
from models import User, Post, db


app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly_test"
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["TESTING"] = True

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


class TestFlaskApp(TestCase):
    def setUp(self) -> None:
        with app.app_context():
            user = User(first_name="John", last_name="Doe")
            db.session.add(user)
            db.session.commit()

            post = Post(
                title="The Force",
                content="Willpower is the key for...",
                user_id=user.id,
            )
            db.session.add(post)
            db.session.commit()
            self.client = app.test_client()
            self.user = user
            self.user_id = user.id

    def tearDown(self):
        with app.app_context():
            db.session.rollback()

    def test_user_list(self):
        res = self.client.get("/users")
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn("John", html)

    def test_profile_user(self):
        res = self.client.get(f"/users/{self.user_id}")
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn("John Doe", html)

    def test_new_user(self):
        data = {"first_name": "Bob", "last_name": "Doe", "image_url": ""}
        res = self.client.post(
            "/users/new",
            data=data,
            follow_redirects=True,
        )
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn("Bob", html)

    def test_edit_user(self):
        self.assertEqual(self.user.first_name, "John")
        data = {
            "first_name": "Zork",
            "last_name": "Doe",
            "image_url": self.user.image_url,
        }
        res = self.client.post(
            f"/users/{self.user_id}/edit", data=data, follow_redirects=True
        )
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn("Zork Doe", html)

    def test_delete_user(self):
        res = self.client.get(f"/users/{self.user.id}/delete", follow_redirects=True)
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertNotIn("John", html)
