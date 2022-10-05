from enum import Enum

class Role(Enum):
    """Enum for user roles."""
    ADMIN = 'ADMIN'
    USER = 'USER'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]