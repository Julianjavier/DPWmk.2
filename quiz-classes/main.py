#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        s= Student()
        self.response.write(s.name_id())
        self.response.write(s.date_of_birth(30, 12, 1991))

        so= Soldier()
        self.response.write(so.soldier_id())
        self.response.write(so.date_enlistment(25, 10, 2010))

        c= Car()
        self.response.write(c.compleat(1995))
        self.response.write(c.gas_mile(40, 23))


##student class
class Student(object):
    def __init__(self):
        self._student_id = 12345
        self.__student_name= "Julian Rodriguez"
        self.year= 0
        self.month= 0
        self.day= 0

    ### method to join student id to student name
    def name_id(self):
        student_info = "Student "+ str(self._student_id) + " is " + self.__student_name
        return student_info

    ### method to show the date of birth pf a student
    def date_of_birth(self, d, m, y):
        date = str(d) + "/" + str(m) + "/" + str(y)
        return date

##soldier class
class Soldier(object):
    def __init__(self):
        self._soldier_id = "dbs1204_o4"
        self.__soldier_name= "Ivan Charkof"
        self.year= 0
        self.month= 0
        self.day= 0

    ### method to join SOLDIER id to SOLDIER name
    def soldier_id(self):
        soldier_info = "Private " + self.__soldier_name + " ID.No "+self._soldier_id
        return soldier_info

    ### method to calculate when a soldier will finish his enlistment time
    def date_enlistment(self, d, m, y):
        enlistment = str(d) + "/" + str(m) + "/" + str(y + 5)
        return enlistment

##car class
class Car(object):
    def __init__(self):
        self._model = "Montero"
        self.__make = "Mitsubishy"
        self.year_made = 0
        self.tank_size = 0
        self.mpg = 0

    ### Method to join the make, model and year of the car
    def compleat(self, y):
        compleat_info = self.__make +" "+ self._model +" "+ str(y)
        return compleat_info

    def gas_mile(self, t, m):
        gas_info = "This model has a tank of "+ str(t) +" gallons and an MPG of "+ str(m)
        return gas_info

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
