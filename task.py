from datetime import datetime

class Task():
    
    # Tasks created by cli.
    def __init__(self, description, id_number=1, status='to do'):
        self.id = id_number
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
