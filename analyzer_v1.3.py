def parse_magic_comments(source_code):
    # Define the pattern for magic comments
    pattern = r'#\s*ANALYZER:(.*)'

    # Search for magic comments in the source code
    matches = re.findall(pattern, source_code, re.MULTILINE)
    begin_time=0
    start_time = 0
    end_time = 0
    round_dec = 5
    analyzedBlockName = "_BlockNotNamed_"
    analyzedBlockCategory = "_NoCategory"
    # Execute actions based on the magic comments found
    for match in matches:
        # Here, you can define actions based on the content of the magic comment
        instruction = match.strip()

        if "begin" in instruction:
            begin_time = time.time()

        if ":" in instruction:
            analyzedBlockName = instruction.split(":")[1].strip()
            instruction = instruction.split(":")[0].strip()
        
        if "->" in instruction:
            analyzedBlockCategory = instruction.split("->")[1].strip()
            instruction = instruction.split("->")[0].strip()    

        if instruction == 'end':
            code = source_code.split(f"# ANALYZER: start -> {analyzedBlockCategory} : {analyzedBlockName}\n")[1].split(f"\n# ANALYZER: end -> {analyzedBlockCategory} : {analyzedBlockName}")[0]
            code = "start_time = time.time()\n" + code + "\nend_time = time.time()\nround_elapsed = round(end_time - start_time,round_dec)\ntimestamp=round(end_time - begin_time,round_dec)\nprint(f'[ANALYZER] {analyzedBlockCategory}/{analyzedBlockName}: {round_elapsed} seconds, at {timestamp} seconds timestamp')\nwith open('anlyzer_results.csv', 'a', newline='') as csvfile:\n\twriter = csv.writer(csvfile, delimiter=';')\n\twriter.writerow([analyzedBlockName,analyzedBlockCategory,round_elapsed,timestamp])"

            # Execute the code
            exec(code)


with open('anlyzer_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['SegmentName:','SegmentCategory:','ExecutionTime:','TimeStamp:'])

if __name__ == "__main__":
    # Read the source code of the analyzedCode module
    with open("analyzed_v1.3.py", 'r') as f:
        source_code = f.read()
    
    # Parse and execute magic comments
    parse_magic_comments(source_code)
