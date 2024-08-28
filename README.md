# Illumio_Takehome_Assessment
# Flow Log Parser

# Overview
This project is a flow log parser that processes flow logs, maps them to tags based on a lookup table, and generates two output files: one containing tag counts and another containing port/protocol combination counts.

# Assumptions
Log Format: The program assumes the default log format provided in the instructions. Custom formats are not supported.
Log Version: The parser supports only version 2 of the log format.
Case Sensitivity: The lookup table and flow logs are processed in a case-insensitive manner.
Default Behavior: Any port/protocol combination not found in the lookup table is categorized under the "Untagged" tag.


# Files
lookup_table.csv: The CSV file containing the destination port, protocol, and corresponding tag mappings.
flow_logs.txt: The text file containing the flow logs to be processed.
tag_counts.csv: The output CSV file that lists each tag and the count of occurrences.
port_protocol_counts.csv: The output CSV file that lists each unique port/protocol combination and its count.
How to Run the Program


# Dependencies:

Python 3.x
No external libraries are required.

# Instructions:

Place the lookup_table.csv and flow_logs.txt in the same directory as the script.
Run the script in the terminal using the following command:
python3 flow_log_parser.py
The output files tag_counts.csv and port_protocol_counts.csv will be generated in the same directory.


# Testing
Test Data: The script has been tested with a variety of flow logs and lookup table combinations to ensure accuracy. The test cases included standard log formats, missing data, and various protocol numbers.

# Output Verification: The output files were manually verified against expected results.
Analysis
Performance: The script performs efficiently on the provided dataset. For larger datasets, optimizations may be necessary.
Error Handling: The script includes basic error handling to skip invalid lines in the input files. More robust error handling could be added in a production environment.
Extensibility: The script is modular, making it easy to extend for additional features, such as supporting custom log formats or additional protocols.


# Conclusion
The Flow Log Parser is a simple and effective tool for processing flow logs. It meets the requirements of the assignment and can be easily extended or adapted for more complex scenarios.
