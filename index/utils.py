import jwt
from datetime import datetime

class Helper:
    def __init__(self, request):
        self.request = request
        self.key = "NEWSECRETKEY" ### CHANGE THIS TO YOUR SECRET KEY
        self.algorithm = "HS256"

    def autheticated(self):
        try:
            jwt_str = self.request.headers.get("Authorization")
            payload = jwt.decode(jwt_str, self.key, algorithms=[self.algorithm])
            return {"status": True, "payload": payload}
        except:
            return {"status": False, "payload": ""}

    def get_token(self, id): ### This get token can be modified to suit your need
        payload = {
            "id": id,
            "exp": datetime.utcnow() + timedelta(minutes=3600),
            "iat": datetime.utcnow(),
        }
        return jwt.encode(payload, self.key, algorithm=self.algorithm)