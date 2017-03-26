import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from app.users.schema import Query as UsersQuery
from app.users.schema import Mutation as UsersMutations


class Query(UsersQuery, graphene.ObjectType):
    pass


class Mutation(UsersMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


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
