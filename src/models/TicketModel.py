from database.db import get_connection
from .entities.Ticket import Ticket


class TicketModel():
    @classmethod
    def get_tickets(self):
        try:
            connection = get_connection()
            tickets = []
            with connection.cursor() as cursor:
                cursor.execute('select * from tickets')
                results = cursor.fetchall()
                print('------------------')
                for row in results:
                    print(row[4])
                    print('-------')
                    ticket = Ticket(row[0], row[1], row[2],
                                    row[3], row[4])
                    tickets.append(ticket.to_json())

            connection.close()
            return tickets
        except Exception as ex:
            raise Exception(ex)
