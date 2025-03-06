def parse_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    servers = {}
    current_server = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if ":" not in line:
            current_server = line
            servers[current_server] = []
        else:
            parts = line.split()
            if len(parts) == 2:
                servers[current_server].append(tuple(parts))
    
    return servers


def find_matches(servers):
    matches = []
    
    for server1, connections1 in servers.items():
        for server2, connections2 in servers.items():
            if server1 == server2:
                continue
            
            for conn1 in connections1:
                if conn1[::-1] in connections2:
                    matches.append(f"{server1} -> {server2}")
    
    return matches


def main():
    input_file = "input.txt"  # Укажите путь к входному файлу
    output_file = "output.txt"  # Укажите путь к выходному файлу
    
    servers = parse_file(input_file)
    matches = find_matches(servers)
    
    with open(output_file, "w") as file:
        for match in matches:
            file.write(match + "\n")
    
    print("Результаты сохранены в", output_file)


if __name__ == "__main__":
    main()
