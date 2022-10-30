class BaseModel():

     def __init__(self,id,created_at,updated_at):
         self.id=str(uuid.uuid4())
         self.created_at=datetime.now()
         self.updated_at=datetime.now()

     def save(self):
     
     def to_dict(self):
          
