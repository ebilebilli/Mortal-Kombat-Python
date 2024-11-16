from fake_data import example
file_name = 'fighter_info.txt'

def txt_writer(data_count=20, mod='a'):
    for time in range(data_count):
        fighter = example() 
        with open(file_name, mod) as file:
            if time != 0:
                file.write('\n')
            file.write(str(fighter))  
txt_writer()


