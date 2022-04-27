import json
from typing import List
from flask_login import UserMixin
from sqlalchemy import func
from toohak.data.db_session import *
from toohak.data.users import User
from toohak.data.completions import Completion
from toohak.data.quizes import Quiz
from toohak.forms import RegisterForm, AddQuizForm


def add_new_user(form: RegisterForm) -> None:
    session = create_session()
    user = User()
    user.login = form.login.data
    user.email = form.email.data
    user.set_password(form.password.data)
    session.add(user)
    session.commit()


def get_user_by_id(user_id: str) -> User:
    session = create_session()
    return session.query(User).get(user_id)


def get_user_by_email(email:str) -> User:
    session = create_session()
    return session.query(User).filter(User.email == email).first()


def get_user_by_login(login) -> User:
    session = create_session()
    return session.query(User).filter(User.login == login).first()


def increase_user_pts(user_id, n):
    session = create_session()
    user = session.query(User).get(user_id)
    user.points = user.points + float(n)
    session.commit()


def get_leaders():
    session = create_session()
    return session.query(User).order_by(-User.points).limit(50).all()
    

def add_new_quiz(form: AddQuizForm, user) -> None:
    session = create_session()
    quiz = Quiz()
    quiz.name = form.name.data
    quiz.description = form.description.data
    quiz.creator = user.get_id()
    quiz.add_questions(form.questions.data)
    session.add(quiz)
    session.commit()

def get_quiz_by_id(quiz_id: str) -> Quiz:
    session = create_session()
    return session.query(Quiz).filter(Quiz.id == int(quiz_id)).first()


def get_all_quizes_for_page(user_id, by_user=False) -> List[Quiz]:
    session = create_session()
    all_quizes = session.query(Quiz).join(User)
    if by_user:
        all_quizes = all_quizes.filter(User.id == user_id)
    out = []
    for quiz in all_quizes:
        max_compl = get_max_completion(user_id, quiz.id)
        out.append((quiz, max_compl))
    return out


def add_new_completion(user_id, quiz_id, score, percents):
    session = create_session()
    completion = Completion(user_id=user_id, quiz_id=quiz_id, score=score, percents=percents)
    session.add(completion)
    session.commit()


def get_completions(user_id, quiz_id):
    session = create_session()
    return session.query(Completion).filter((Completion.user_id == user_id) & (Completion.quiz_id == quiz_id)).all()


def get_max_completion(user_id, quiz_id):
    session = create_session()
    return session.query(func.max(Completion.percents)).filter((Completion.user_id == user_id) & (Completion.quiz_id == quiz_id)).first()[0]