import re

def extract_valid_servers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        server_name = None
        valid_entries = []
        
        for line in infile:
            server_match = re.search(r'=== Output from (.+) ===', line)
            if server_match:
                if valid_entries:
                    outfile.write(f"{server_name}\n")
                    outfile.writelines(valid_entries)
                    valid_entries = []
                server_name = server_match.group(1)
                continue
            
            if server_name:
                match = re.search(r'\s+(\S+):(\d+)\s+(\S+):(\d+)', line)
                if match:
                    local_address, local_port, foreign_address, foreign_port = match.groups()
                    
                    # Проверяем, является ли внешний адрес глобальным
                    if not (foreign_address.startswith("0.0.0.0") or 
                            foreign_address.startswith("localhost") or 
                            foreign_address.startswith("[::]")):
                        valid_entries.append(f"{server_name}: {foreign_address}:{foreign_port}\n")
        
        # Записываем последний сервер, если были найденные записи
        if valid_entries:
            outfile.write(f"{server_name}\n")
            outfile.writelines(valid_entries)

# Использование
extract_valid_servers('logs.txt', 'filtered_logs.txt')
