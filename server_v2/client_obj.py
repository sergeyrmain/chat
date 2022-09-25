class ClientObject:
    def __init__(self, address, client):
        self.address = address
        self.name = None
        self.client = client

    def __repr__(self):
        return f'{self.name} {self.address}'

    def __str__(self):
        return f'{self.name} {self.address}'

    def set_name(self, name):
        self.name = name
