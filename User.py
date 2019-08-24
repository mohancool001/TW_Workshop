import uuid
class User(object):
    """ User class """

    id = 0
    name = ""
    address = []

    class Address():
        typeofAddr = ""
        primary = False
        address = "" 

        def __init__(self, typeofAddr, address):
            self.typeofAddr = typeofAddr
            self.address = address

        def setPrimary(self):
            self.primary = True

        def jsonifyMyself(self):
            jsonType = {
                "address" : self.address,
                "TypeofAddr": self.typeofAddr
            }
            if self.primary:
                jsonType['primary'] = True
            return jsonType
    
    def __init__(self, name, address = "", addressType = ""):
        self.id = uuid.uuid4()
        self.name = name
        if address and addressType:
            firstAddr = Address(addressType, address)
            firstAddr.setPrimary()
            self.address = [firstAddr]

    def addAddress(self, address = "", addressType = "", setPrimary=False):
        newAddr = Address(addressType, address)
        if (len(self.address) == 0) or setPrimary:
            newAddr.setPrimary() # Remove other primaries
        self.address.append(newAddr)
    
    def jsonifyMyself(self):
        jsonType = {
            "id" : self.id,
            "name": self.name,
            "address" : []
        }
        for addr in self.address:
            jsonType['address'].append(addr.jsonifyMyself())
        return jsonType

class Rating(object):
    id = 0
    ratingValue = 0
    ratingUserId = 0

    def __init__(self, ratingValue, ratingUserId):
        self.id = uuid.uuid4()
        self.ratingValue = ratingValue
        self.ratingUserId = ratingUserId
    
    def jsonifyMyself(self):
        jsonType = {
            "id": self.id,
            "rating": self.ratingValue,
            "userId": self.ratingUserId
        }
        return jsonType