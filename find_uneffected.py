import csv

input_csv_file_path = 'bridge_events (7).csv'
output_csv_file_path = 'uneffected_packets.csv'

uneffected_packets = []

def read_csv_file(file_path):
    encodings = ['utf-8', 'ISO-8859-1']  
    for encoding in encodings:
        try:
            with open(file_path, mode='r', encoding=encoding) as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    effected = row.get('effected')
                    if effected is not None and effected.strip() == '0': 
                        uneffected_packets.append(row)  
            return
        except UnicodeDecodeError as e:
            print(f"Failed to read file with encoding {encoding}. Trying next encoding... Error: {e}")
        except KeyError:
            print("The specified column 'effected' was not found in the CSV file.")
            return
        except Exception as e:
            print(f"An unexpected error occurred while reading the CSV file: {e}")
            return

def write_csv_file(output_file_path, data):
    if not data:
        print("No packets with effected = 0 to write.")
        return
    
    try:
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = data[0].keys() 
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            csv_writer.writeheader()
            csv_writer.writerows(data)
        
        print(f"Packets with effected = 0 have been written to {output_file_path}")
    
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")

read_csv_file(input_csv_file_path)

write_csv_file(output_csv_file_path, uneffected_packets)
