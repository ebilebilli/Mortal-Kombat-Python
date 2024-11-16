from file_writer import file_name
def txt_reader(file_name:str = file_name):
    with open(file_name, 'r') as file:
        fighter_data = file.read()
        return fighter_data
    
txt_fighter_data = txt_reader()

if __name__ == '__main__':
    print(txt_fighter_data)
