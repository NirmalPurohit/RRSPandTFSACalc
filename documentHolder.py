class DocumentHolder:
    def __init__(self, **objs):
        self.__dict__.update(objs)