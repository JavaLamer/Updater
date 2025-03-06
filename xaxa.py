def parse_connections(input_file, output_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    server_map = {}
    current_server = None
    
    for line in lines:
        if not line[0].isdigit():  # Это название сервера
            current_server = line
            server_map[current_server] = []
        else:  # Это строка с соединением
            source, dest = line.split()
            server_map[current_server].append((source, dest))
    
    connections = {}
    for server, conns in server_map.items():
        for source, dest in conns:
            for target_server, target_conns in server_map.items():
                if server != target_server and any(dest in conn for conn in target_conns):
                    connections[server] = target_server
                    break
    
    with open(output_file, "w") as f:
        for src, dst in connections.items():
            f.write(f"{src} -> {dst}\n")

# Пример вызова:
parse_connections("input.txt", "output.txt")
