from UserInfo import UserInfo

class OAuthApp(object):
    """ OAuth App Functionality Rests Here """
    fullUsers = []
    fullATokens = []
    def __init__(self):
        pass
    
    def createUser(self, userName, userPass):
        userObj = UserInfo(userName, userPass)
        self.fullUsers.append(userObj)
    
    def loginUser(self, userName, Password):
        """ Search and check for users """
        access_token = ''
        for user in self.fullUsers:
            if userName in user.name:
                if(user.verify_password(Password)):
                    access_token = user.generateAccessToken()
                    self.fullATokens.append((user, access_token))
                    return access_token, True

        return access_token, False

    def validateToken(self, access_token):          
        """ Validate the token """
        for (user, token) in self.fullATokens:
            if(user.validateToken(access_token)):
                return True
        
        return False