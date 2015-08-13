########################################
# Author : Jiang Qiqi
# Date : 2015, 8, 12
# E-mail : woshiqiqiye@gmail.com
# 
########################################
import os

class PhoneNumberLocation:
    def __init__(self, filename = 'mobilephones.txt'):
        "load date to deal with query"
        self._type_dict = {}
        self._area_dict = {}
        self._number_dict = {}
        filename = os.path.join(os.path.dirname(__file__), filename)
        self.load_data(filename)

    def _load_type(self, lines):
        for line in lines:
            words = line.strip().split(',')
            if len(words) == 2:
                self._type_dict[words[0]] = words[1] 
            
    def _load_area(self, lines):
        for line in lines:
            words = line.strip().split(',')
            if len(words) == 2:
                self._area_dict[words[0]] = words[1] 

    def _load_number(self, number, lines):
        if number not in self._number_dict:
            self._number_dict[number] = {}

        i = 0
        for line in lines:
            words = line.strip().split(',')
            if len(words) == 2:
                self._number_dict[number][i] = words
                i += 1
    
    def load_data(self,file_name):
        with open(file_name) as f:
            data = f.read().split('----------\n')
            
        for block in data:
            lines = block.split('\n')
            if lines[0] == 'type':
                self._load_type(lines[1:])
            elif lines[0] == 'area':
                self._load_area(lines[1:])
            elif lines[0].startswith("number-"):
                self._load_number(lines[0][7:], lines[1:])
            else:
                print("error occured")

    def query(self, phone_number):
        num_str = str(phone_number)
        i = num_str[0:3]
        j = int(num_str[3:7])

        if i in self._number_dict and j in self._number_dict[i]:
            info_str = self._number_dict[i][j]
            area_str = self._area_dict[info_str[0]]
            type_str = self._type_dict[info_str[1]]

            print(" ".join([area_str])) 
        #if self._number_dict[i] 

        
        
def main():
    db = PhoneNumberLocation('mobilephones.txt')
    db.query("13913482016")

if __name__ == '__main__':
    main()
