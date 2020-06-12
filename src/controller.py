class Controller:
    __subject = None
    def __init__(self):
        pass

    @property
    def subject(self):
        return Controller.__subject
    @subject.setter
    def subject(self, new_subject):
        Controller.__subject = new_subject

    def make_subject_mover(self, direction: str):
        def mover():
            Controller.__subject.move_to(direction)

        return mover

    def take_item(self, item: str):
        Controller.__subject.take(item)
