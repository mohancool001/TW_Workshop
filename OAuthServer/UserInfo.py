import uuid
import hashlib, binascii, os
from time import gmtime, strftime
from datetime import datetime, date, timedelta

class UserInfo(object):
    id = 0
    name = ""
    password = ""
    access_token = ""
    expiration_point = ""
    
    def __init__(self, name, password):
        self.id = uuid.uuid4()
        self.name = name
        self.password = self.hash_password(password)

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, provided_password):
        """Verify a stored password against one provided by user"""
        salt = self.password[:64]
        self.password = self.password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == self.password
    
    def generateAccessToken(self):
        self.access_token = uuid.uuid4()
        self.expiration_point = date.today() + timedelta(seconds=3600)
        return self.access_token
    
    def returnToken(self):
        return self.access_token
    
    def validateToken(self, accessToken):
        timeNow = date.today()
        if self.expiration_point >= timeNow and str(self.access_token) in accessToken:
            return True
        else:
            return False
    
    def refreshToken(self):
        timeNow = date.today()
        if self.expiration_point <= timeNow:
            self.generateAccessToken()
        return