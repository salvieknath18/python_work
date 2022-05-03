from abc import ABC, abstractmethod


class Bus(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_available_tickets(self):
        pass

    @abstractmethod
    def book_ticket(self):
        pass

    @abstractmethod
    def get_booking_info(self):
        pass


class SeatBus(Bus):

    def __init__(self, ac_available):
        super().__init__()
        self.ac_available = ac_available

    def get_available_tickets(self):
        pass

    def book_ticket(self):
        pass

    def get_booking_info(self):
        pass


class SleeperBus(Bus):

    def __init__(self, ac_available):
        super().__init__()
        self.ac_available = ac_available

    def get_available_tickets(self):
        pass

    def book_ticket(self):
        pass

    def get_booking_info(self):
        pass
