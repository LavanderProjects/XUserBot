import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

class Database:
  def __init__(self, user_id):
    self.user_id = user_id
    self.database = ""
