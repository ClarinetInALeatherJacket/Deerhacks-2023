from main import db, User, app

if __name__ == "__main__":
    with app.app_context():
        # dummy data for users
        user_1 = User(name='Bobby',email='th@th.com',password='password')
        user_2 = User(name='Jason',email='grind@mind.com',password='password')
        db.session.add(user_1)
        db.session.add(user_2)
        db.session.commit()
        User.query.all()