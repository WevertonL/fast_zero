from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='izabel',
        password='secret',
        email='izabel@manu.com.br',
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    user = session.scalar(select(User).where(User.username == 'wevertonl'))

    assert user.username == 'wevertonl'
