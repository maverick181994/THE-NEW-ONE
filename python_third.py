class society(object):

    def __init__(self, Building_number, apartment_number, parking_slot_no, apartment_meter_number ):

        self.Building_number = Building_number
        self.apartment_number = apartment_number
        self.parking_slot_no = parking_slot_no
        self.apartment_meter_number = apartment_meter_number

    def society_display_info(self):

        return f" society : {self.Building_number} {self.apartment_number} {self.parking_slot_no} {self.apartment_meter_number}"

class Society_Register(object):

      def __init__(self):

          self.society_dictionary = {}

      def add_society_details(self,Building_number, apartment_number, parking_slot_no, apartment_meter_number):

          if parking_slot_no not in self.society_dictionary:

              self.society_dictionary[parking_slot_no] = society(Building_number= Building_number, apartment_number=apartment_number ,
                                                            parking_slot_no= parking_slot_no, apartment_meter_number= apartment_meter_number)
          else:

              print("the people are staying in the apartment with the parking")


      def people_leaving_the_society(self, parking_slot_no):

         if parking_slot_no in self.society_dictionary:

            person_leaving = self.society_dictionary[parking_slot_no].society_display_info()

            del self.society_dictionary[parking_slot_no]

         else:
             print(f"No person found with parking slot {parking_slot_no}")

      def search_society_info(self):

         for key, value in self.society_dictionary.items():

              return value.society_display_info()

      def get_society_Detail(self, parking_slot_no) -> object:

          return self.society_dictionary[parking_slot_no]

if __name__ == "__main__":

 Main_society =  Society_Register()

Main_society.add_society_details("A", 101, 111, 12345)
Main_society.add_society_details("B", 102, 222, 22233)
Main_society.add_society_details("C", 103, 333, 22334)
Main_society.add_society_details("D", 103, 444, 33445)

Main_society.people_leaving_the_society(333)

society_one = Main_society.get_society_Detail(111)
society_two = Main_society.get_society_Detail(222)
society_four = Main_society.get_society_Detail(444)



print(Main_society.search_society_info())

