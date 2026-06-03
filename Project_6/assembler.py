def is_a_instruction(line):
    """ Return True if the line is an A instruction, else return False """
    return line.startswith('@') and line[1:].isdigit()


def is_c_instruction(line):
    """ Return True if the line is a C instruction, else return False """
    return not is_a_instruction(line) and not is_label(line) and " " not in line


def is_instruction(line):
    """
    Return True if the line is an A or a C instruction, else return False
    """
    return is_a_instruction(line) or is_c_instruction(line)


def is_label(line):
    """ Return True if the line is a label, else return False """
    return line.startswith("(") and line.endswith(")")


def get_comp(cinst):
    """
    Return the comp portion (as a string) of the given C instruction
    """
    if "=" in cinst:
        return cinst.split("=")[1].split(";")[0]
    else:
        return cinst.split(";")[0]


def get_dest(cinst):
    """ Return the dest portion (as a string) of the given C instruction """
    if "=" in cinst:
        return cinst.split("=")[0]
    else:
        return ""


def get_jump(cinst):
    """ Return the jump portion (as a string) of the given C instruction """
    if ";" in cinst:
        return cinst.split(";")[1]
    else:
        return ""


def get_symbol(line):
    """
    Given a label or A instruction line, return just the symbol portion.
    For example:
    given "(LOOP)", return "LOOP"
    given "@abc", return "abc"
    given "@12345", return "12345"
    """
    if is_label(line):
        return line.strip('()')
    elif is_a_instruction(line):
        return line.strip('@')
    else:
        raise ValueError("Not a label or A instruction: {}".format(line))


def convert_comp(comp_part):
    """
    Return the binary (1s and 0s) representation of the given comp string
    """
    comp_table = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
    }
    return comp_table[comp_part]


def convert_dest(dest_part):
    """
    Return the binary (1s and 0s) representation of the given dest string
    """
    dest_table = {
        "": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }
    return dest_table[dest_part]


def convert_jump(jump_part):
    """
    Return the binary (1s and 0s) representation of the given jump string
    """
    jump_table = {
        "": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }
    return jump_table[jump_part]


def convert_a_instruction(line):
    """
    convert a (numeric) A instruction value to a 16-bit binary value,
    displayed as a string of 1s and 0s.
    """
    value = int(line[1:])
    return format(value, '016b')


def convert_c_instruction(line):
    """
    given a line (which is known to contain a C instruction),
    convert the entire line into its binary format
    This function should utilize the "helper" functions:
    convert_dest, convert_comp, and convert_jump
    """
    dest_part = get_dest(line)
    comp_part = get_comp(line)
    jump_part = get_jump(line)
    return "111" + convert_comp(comp_part) + convert_dest(dest_part) + convert_jump(jump_part)


def normalize(raw_line):
    """ remove comments and whitespace from a line """
    return raw_line.strip().split("//")[0].replace("\t", "").replace(" ", "")


def assemble_phase_one(lines):
    """
    Given a list of strings representing the lines of the input .asm program,
    return a list of strings representing the binary .hack version of that same
    program.
    """
    output = []
    for raw_line in lines:
        line = normalize(raw_line)

        result = None
        if is_a_instruction(line):
            result = convert_a_instruction(line)

        elif is_c_instruction(line):
            result = convert_c_instruction(line)

        else:
            continue

        output.append(result)

    return output


def assemble_phase_two(lines):
    # Symbol table initialization with predefined symbols
    ST = {
        "R0": 0, "R1": 1, "R15": 15,
        "SCREEN": 16384, "KBD": 24576,
    }

    # First pass: Scan for labels and add them to symbol table
    instruction_counter = 0
    for line in lines:
        line = normalize(line)
        if is_label(line):
            label = get_symbol(line)
            ST[label] = instruction_counter
        elif is_instruction(line):
            instruction_counter += 1

    # Second pass: Scan for variables, add them to symbol table, and generate output
    variable_address = 16  # Starting address for variables
    output = []
    for line in lines:
        line = normalize(line)
        if is_c_instruction(line):
            result = convert_c_instruction(line)
        elif is_a_instruction(line):
            symbol = get_symbol(line)
            print("Processing symbol:", symbol)
            if symbol.isnumeric():
                print("Symbol is numeric")
                result = convert_a_instruction(line)
            else:
                if symbol not in ST:
                    print("Symbol not in ST, assigning address:", variable_address)
                    ST[symbol] = variable_address
                    variable_address += 1
                else:
                    print("Symbol already in ST")
                result = convert_a_instruction(ST[symbol])
        else:
            continue
        output.append(result)

    return output


if __name__ == "__main__":
    from pathlib import Path
    import sys

    if len(sys.argv) < 2:
        print("provide path to a hack assembly file (path/to/filename.asm)")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("provide 1 or 2 to indicate which phase to use")
        sys.exit(1)

    filename = sys.argv[1]
    phase = sys.argv[2]

    with open(filename) as f:
        file_lines = f.readlines()

    p = Path(filename)
    if p.suffix != ".asm":
        print("input filename must end in .asm")
        sys.exit(1)

    outfile = str(p.with_suffix(".hack"))

    if phase == "1":
        hack_lines = assemble_phase_one(file_lines)  
    elif phase == "2":
        hack_lines = assemble_phase_two(file_lines)  
    else:
        print("could not understand what phase to use (1 or 2)")
        sys.exit(1)

    with open(outfile, 'w') as output_file:
        for processed_line in hack_lines:
            print(processed_line, file=output_file)

