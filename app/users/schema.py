
from graphene import relay, AbstractType
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


class Query(AbstractType):
    node = relay.Node.Field(User)
    all_users = SQLAlchemyConnectionField(User)
    all_roles = SQLAlchemyConnectionField(Role)
    role = relay.Node.Field(Role)


class AddUser(relay.ClientIDMutation):
    class Input:
        url = graphene.String(required=True)
        description = graphene.String()

    image = graphene.Field(ImageNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        pass
