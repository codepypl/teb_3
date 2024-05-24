from datetime import timedelta, datetime


class Event:
    next_id = 1

    def __init__(self, name, date, time, localisation, max_tickets):
        self.event_id = Event.next_id
        Event.next_id += 1
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.time = time  # Godzina jako string
        self.localisation = localisation
        self.max_tickets = max_tickets
        self.tickets = []

    def available_tickets(self):
        return self.max_tickets - len(self.tickets)


class Ticket:
    def __init__(self, event, seat_num):
        self.event = event
        self.seat_num = seat_num
        self.reservation_date = datetime.now()

    def __repr__(self):
        return f" na {self.event.name}, dnia {self.event.date} {self.event.time} miejsce nr {self.seat_num}"


class TicketMgr:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        print(f"Wydarzenie {event.name} o id {event.event_id} zostało dodane")

    def list_events(self):
        if not self.events:
            print("Brak wydarzeń w bazie danych... ")
        else:
            for event in self.events:
                print(f"{event.event_id}: {event.name} - {event.date.strftime('%Y-%m-%d')} o {event.time}")

    def reserve_ticket(self, event_id, seat_num):
        for event in self.events:
            if event.event_id == event_id:
                if len(event.tickets) < event.max_tickets:
                    ticket = Ticket(event, seat_num)
                    event.tickets.append(ticket)
                    print(f"Miejsce {seat_num} na wydarzenie {event.name} zostało zarezerwowane")
                    return
                else:
                    print("Brak dostępnych biletów na to wydarzenie.")
                    return
        print("Nie znaleziono wydarzenia o podanym ID.")

    def cancel_ticket(self, event_id, seat_num):
        for event in self.events:
            if event.event_id == event_id:
                for ticket in event.tickets:
                    if ticket.seat_num == seat_num:
                        if datetime.now() <= event.date - timedelta(days=3):
                            event.tickets.remove(ticket)
                            print(f"Bilet {ticket} został anulowany")
                            return
                        else:
                            print("Anulowanie rezerwacji nie jest możliwe. Wydarzenie odbędzie się za mniej niż 3 dni")
                            return
                print("Bilet nie został odnaleziony w systemie")
                return
        print("Nie ma takiego wydarzenia w systemie")

    def available_tickets(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event.available_tickets()
        print("Nie odnaleziono wydarzenia w systemie")
        return None


def menu():
    print('Wybierz czynność:')
    print('1. Lista wydarzeń')
    print('2. Dodanie wydarzenia')
    print('3. Rezerwacja biletu')
    print('4. Sprawdzenie dostępnych biletów')
    print('5. Anulowanie biletu')


def main():
    ticket_manager = TicketMgr()
    while True:
        menu()
        choice = input("Wybierz co chcesz zrobić: ")
        if choice == '1':
            print("Lista wydarzeń w systemie: ")
            ticket_manager.list_events()
        elif choice == '2':
            name = input("Wpisz nazwę wydarzenia: ")
            date = input("Data wydarzenia (YYYY-MM-DD): ")
            time = input("Godzina wydarzenia (HH:MM): ")
            localisation = input("Miejsce wydarzenia: ")
            max_tickets = int(input("Maksymalna liczba biletów na wydarzenie: "))
            event = Event(name, date, time, localisation, max_tickets)
            ticket_manager.add_event(event)
        elif choice == '3':
            event_id = int(input("Wpisz id wydarzenia: "))
            seat_num = input("Numer miejsca: ")
            ticket_manager.reserve_ticket(event_id, seat_num)
        elif choice == '4':
            event_id = int(input("Wpisz id wydarzenia: "))
            available = ticket_manager.available_tickets(event_id)
            if available is not None:
                print(f"Liczba dostępnych biletów na wydarzenie: {available}")
            else:
                print("Na to wydarzenie nie ma już miejsc!")
        elif choice == '5':
            event_id = int(input("Wpisz id wydarzenia: "))
            seat_num = input("Wpisz numer miejsca: ")
            ticket_manager.cancel_ticket(event_id=event_id, seat_num=seat_num)
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == '__main__':
    main()
