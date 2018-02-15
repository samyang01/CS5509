''' Create a management program with the following requirements:
Your code should have at least five classes
Your code should have _init_ constructor in all the classes
Your code should show inheritance at least once
Your code should have one super call
Use of self is required
Use at least one private data member in your code
Use multiple Inheritance atleast once
Create instances of all classes and show the relationship between them
Your submission code should point out where all these things are present'''

'''ICU Nurse Staffing Management Program
This program was written to track the number of beds available at any given time in each of 3 ICUs
(intensive care units)'''

patient_list=[{'name': 'JV', 'diagnosis':'CVA', 'unit_type': 'Medical'},
{'name': 'AB', 'diagnosis': 'CVA', 'unit_type': 'Surgical'},
{'name': 'CD', 'diagnosis': 'HTN', 'unit_type': 'Neuro'},
{'name': 'EF', 'diagnosis': 'XLAP', 'unit_type': 'Medical'},
{'name': 'GD', 'diagnosis': 'MI', 'unit_type': 'Surgical'},
{'name': 'GT', 'diagnosis': 'Code', 'unit_type': 'Neuro'},
{'name': 'YR', 'diagnosis': 'CVA', 'unit_type': 'Medical'},
{'name': 'TA', 'diagnosis': 'MI', 'unit_type': 'Surgical'},
{'name': 'UI', 'diagnosis': 'Panc', 'unit_type': 'Neuro'}]

class Patient:
    def __init__(self,name,diagnosis):
        self.name=name
        self.diagnosis=diagnosis

class Admission(Patient):                          # admission class ties the patient and adding patient
    def __init__(self,name, diagnosis, unit_type): # to list as one object
        super().__init__(name, diagnosis)
        self.admission = {'name':name,'diagnosis':diagnosis,'unit_type': unit_type}
        patient_list.append(self.admission)

class Discharge(Patient):                          # discharge class ties the patient and removing patient
    def __init__(self,name, diagnosis, unit_type): # from the list as one object
        super().__init__(name, diagnosis)
        for patient in patient_list:
            i = patient_list.index(patient)
            if name in patient.values() and unit_type in patient.values():
                del patient_list[i]

class Beds_Avail:                                  # Beds_Avail class ties the unit_type name and number of beds
    def __init__(self, unit_type, num_beds):       # with a list containing only the patients in that unit and the
        self.unit_type = unit_type                 # number of beds remaining
        self.num_beds = num_beds
        unit_list = []

        for patient in patient_list:
            if unit_type in patient.values():
                unit_list.append(patient)
        print('There are {}/{} beds availabe in {}'.format(num_beds-len(unit_list),num_beds, unit_type))
        for patient in unit_list:
            print('Patients in '+ unit_type + 'ICU are: ' + patient['name']+', '+patient['diagnosis'])
def main():
    UI=Admission('UI', 'Xlap', 'Medical')
    PO=Admission('PO','DKA','Surgical')
    TR=Admission('TR','CVA', 'Neuro')
    TA=Discharge('TA', 'MI', 'Surgical')
    UI=Discharge('UI', 'Panc','Neuro')
    Monday=Beds_Avail('Neuro',8)
    Monday=Beds_Avail('Medical',12)
    Monday=Beds_Avail('Surgical',10)
main()
