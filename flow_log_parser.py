from collections import defaultdict
import csv

# Function to read the lookup table and create a dictionary for quick reference
def load_lookup_table(lookup_file):
    lookup_dict = {}
    with open(lookup_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # This line skips the header row which is not a part of the lookup table
        for row in reader:
            dst_port, protocol, tag = row
            # lowercase for consistency with the flow logs
            key = (dst_port.lower(), protocol.lower())
            lookup_dict[key] = tag  # store the key
    return lookup_dict
def process_flow_logs(flow_file, lookup_dict):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    with open(flow_file, 'r') as file:
        for line in file:
            # Split the line into parts, using a whitespace
            parts = line.strip().split()
            dst_port = parts[6]  # Destination port is the 7th element, 0th indexed
            protocol_num = parts[7]  # Protocol number is the 8th element, 0th indexed
            
            # Map the protocol number to its name
            if protocol_num == '6':
                protocol = 'tcp'
            elif protocol_num == '17':
                protocol = 'udp'
            elif protocol_num == '1':
                protocol = 'icmp'
            else:
                protocol = 'other'
            
            # Create a key from the destination port and protocol
            key = (dst_port.lower(), protocol.lower())
            tag = lookup_dict.get(key, "Untagged")
            # Update the counts
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1
    
    return tag_counts, port_protocol_counts

# Function to write the results into separate CSV files as instructed
def save_results(tag_counts, port_protocol_counts):
    #  tag_counts.csv
    with open("tag_counts.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tag", "Count"])
        for tag, count in sorted(tag_counts.items()):
            writer.writerow([tag, count])
    
    #  port_protocol_counts.csv
    with open("port_protocol_counts.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Protocol", "Count"])
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            writer.writerow([port, protocol, count])

if __name__ == "__main__":
    lookup_file = "lookup_table.csv"
    flow_file = "flow_logs.txt"
    # Load the lookup table into a dictionary
    lookup_dict = load_lookup_table(lookup_file)
    # Process the flow logs to get the counts
    tag_counts, port_protocol_counts = process_flow_logs(flow_file, lookup_dict)
    
    # Save the results to CSV files
    save_results(tag_counts, port_protocol_counts)
