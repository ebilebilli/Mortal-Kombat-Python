from file_reader import txt_fighter_data
from Chtr_design import Character

fighters_list = []

def fighter_list_count(count: int = 15):   
    
    fighter_data_lines = txt_fighter_data.split("\n")  
    
    for x in range(count):
        fighter_info = fighter_data_lines[x].split(",")
        fighters_list.append(Character(fighter_info[0], fighter_info[1], fighter_info[2], fighter_info[3]))

if __name__ == '__main__':
    fighter_list_count()
