
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.users.models import User as UserModel
from app.users.models import Role as RoleModel


class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
        only_fields = ('id', 'name', 'lastname', 'mail', 'city')


class Role(SQLAlchemyObjectType):

    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )