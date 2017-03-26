import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from app.users.schema import User, Role


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User)
    all_roles = SQLAlchemyConnectionField(Role)
    role = graphene.Field(Role)


schema = graphene.Schema(query=Query, types=[User, Role])

default_query = '''
{
  allUsers {
    edges {
      node {
        id,
        name,
        lastname,
        mail
        role {
          id,
          name
        }
      }
    }
  }
}'''.strip()