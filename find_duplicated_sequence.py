import csv
from collections import defaultdict

# Specify the path to the CSV file
csv_file_path = 'bridge_events (4).csv'

sequence_to_tx_hashes = defaultdict(list)

def read_csv_file(file_path):
    encodings = ['utf-8', 'ISO-8859-1'] 
    for encoding in encodings:
        try:
            with open(file_path, mode='r', encoding=encoding) as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    sequence = row.get('sequence')
                    tx_hash = row.get('tx_hash')
                    if sequence and tx_hash: 
                        sequence_to_tx_hashes[sequence].append(tx_hash)
            return
        except UnicodeDecodeError as e:
            print(f"Failed to read file with encoding {encoding}. Trying next encoding... Error: {e}")
        except KeyError:
            print("The specified columns 'sequence' or 'txHash' were not found in the CSV file.")
            return
        except Exception as e:
            print(f"An unexpected error occurred while reading the CSV file: {e}")
            return

read_csv_file(csv_file_path)

if not sequence_to_tx_hashes:
    print("No sequences or transaction hashes were read from the file.")
else:
    duplicates = {sequence: tx_hashes for sequence, tx_hashes in sequence_to_tx_hashes.items() if len(tx_hashes) > 1}

    if duplicates:
        print("Duplicated Sequences with their Transaction Hashes:")
        for sequence, tx_hashes in duplicates.items():
            print(f"Sequence: {sequence}")
            for tx_hash in tx_hashes:
                print(f"  Transaction Hash: {tx_hash}")
    else:
        print("No duplicated sequences found.")
