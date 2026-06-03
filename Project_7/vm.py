import sys

def translate_arithmetic(command, label_counter):
    asm_code = []

    if command == "add":
        asm_code.extend([
            "@SP",
            "AM=M-1",   # Decrement SP and set A to address of top stack value
            "D=M",      # Store value of top stack element in D
            "A=A-1",    # Move A back to address of second top stack value
            "M=D+M"     # Add top two stack values and store result in second top
        ])
    elif command == "sub":
        asm_code.extend([
            "@SP",
            "AM=M-1",   # Decrement SP and set A to address of top stack value
            "D=M",      # Store value of top stack element in D
            "A=A-1",    # Move A back to address of second top stack value
            "M=M-D"     # Subtract top two stack values and store result in second top
        ])
    elif command == "neg":
        asm_code.extend([
            "@SP",
            "A=M-1",    # Set A to address of top stack value
            "M=-M"      # Negate the value at the top of the stack
        ])
    elif command == "eq":
        true_label = f"TRUE_{label_counter}"
        end_label = f"END_{label_counter}"
        label_counter += 1

        asm_code.extend([
            "@SP",
            "AM=M-1",   # Decrement SP and set A to address of top stack value
            "D=M",      # Store second operand (y)
            "A=A-1",    # Move A back to address of first operand (x)
            "D=M-D",    # Compute x - y and store result in D
            f"@{true_label}",
            "D;JEQ",    # Jump to true_label if x == y
            "@SP",
            "A=M-1",
            "M=0",      # false (0) if not equal
            f"@{end_label}",
            "0;JMP",    # Unconditional jump to end_label
            f"({true_label})",
            "@SP",
            "A=M-1",
            "M=-1",     # true (-1) if equal
            f"({end_label})"
        ])
    elif command == "lt":
        true_label = f"TRUE_{label_counter}"
        end_label = f"END_{label_counter}"
        label_counter += 1

        asm_code.extend([
            "@SP",
            "AM=M-1",   # Decrement SP and set A to address of top stack value
            "D=M",      # Store second operand (y)
            "A=A-1",    # Move A back to address of first operand (x)
            "D=M-D",    # Compute x - y and store result in D
            f"@{true_label}",
            "D;JLT",    # Jump to true_label if x < y
            "@SP",
            "A=M-1",
            "M=0",      # false (0) if not less than
            f"@{end_label}",
            "0;JMP",    # Unconditional jump to end_label
            f"({true_label})",
            "@SP",
            "A=M-1",
            "M=-1",     # true (-1) if less than
            f"({end_label})"
        ])
    elif command == "and":
        asm_code.extend([
            "@SP",
            "AM=M-1",   # Decrement SP and set A to address of top stack value
            "D=M",      # Store value of top stack element in D
            "A=A-1",    # Move A back to address of second top stack value
            "D=D&M",    # Perform bitwise AND and store result in D
            "M=D"       # Store result back in second top stack value
        ])
    elif command == "or":
        asm_code.extend([
            "@SP",
            "AM=M-1",   # Decrement SP and set A to address of top stack value
            "D=M",      # Store value of top stack element in D
            "A=A-1",    # Move A back to address of second top stack value
            "D=D|M",    # Perform bitwise OR and store result in D
            "M=D"       # Store result back in second top stack value
        ])
    elif command == "not":
        asm_code.extend([
            "@SP",
            "A=M-1",    # Set A to address of top stack value
            "M=!M"      # Perform logical NOT on the value at the top of the stack
        ])
    elif command == "get":
        # No operation needed for "get" command
        pass

    return asm_code, label_counter

def translate_memory_access(parts, filename):
    command, segment, index = parts
    asm_code = []

    if command == "push":
        if segment == "constant":
            asm_code.extend([
                f"@{index}",    # Load constant value to A register
                "D=A"           # Store constant value in D register
            ])
        elif segment == "static":
            asm_code.extend([
                f"@{filename}.{index}",  # Load static variable address
                "D=M"                   # Get value at static variable
            ])
        elif segment in ["local", "argument", "this", "that"]:
            segment_map = {
                "local": "LCL",
                "argument": "ARG",
                "this": "THIS",
                "that": "THAT"
            }
            base_address = segment_map[segment]
            asm_code.extend([
                f"@{base_address}",     # Load base address
                "D=M",                  # Get base address value
                f"@{index}",            # Load offset/index
                "A=D+A",                # Calculate target address (base_address + index)
                "D=M"                   # Get value at target address
            ])
        elif segment == "pointer":
            pointer_map = {
                "0": "THIS",
                "1": "THAT"
            }
            pointer_reg = pointer_map[index]
            asm_code.extend([
                f"@{pointer_reg}",  # Load pointer register address
                "D=M"               # Get value at pointer register
            ])
        elif segment == "temp":
            asm_code.extend([
                f"@{5 + int(index)}",   # Load base address of temp segment
                "D=M"                   # Get value at target temp address
            ])
        
        asm_code.extend([
            "@SP",      # Load stack pointer
            "A=M",      # Move to stack pointer address
            "M=D",      # Store value from D into stack
            "@SP",      # Load stack pointer
            "M=M+1"     # Increment stack pointer
        ])

    elif command == "pop":
        if segment in ["local", "argument", "this", "that"]:
            segment_map = {
                "local": "LCL",
                "argument": "ARG",
                "this": "THIS",
                "that": "THAT"
            }
            base_address = segment_map[segment]
            asm_code.extend([
                f"@{base_address}",     # Load base address
                "D=M",                  # Get base address value
                f"@{index}",            # Load offset/index
                "D=D+A",                # Calculate target address (base_address + index)
                "@R13",                 # Store target address in R13
                "M=D",                  # Save target address
                "@SP",                  # Load stack pointer
                "AM=M-1",               # Decrement stack pointer and set A to new stack top
                "D=M",                  # Get value from stack top
                "@R13",                 # Load target address from R13
                "A=M",                  # Move to target address
                "M=D"                   # Store value from stack into target address
            ])
        elif segment == "pointer":
            pointer_map = {
                "0": "THIS",
                "1": "THAT"
            }
            pointer_reg = pointer_map[index]
            asm_code.extend([
                "@SP",      # Load stack pointer
                "AM=M-1",   # Decrement stack pointer and set A to new stack top
                "D=M",      # Get value from stack top
                f"@{pointer_reg}",  # Load pointer register address
                "M=D"       # Store value from stack into pointer register
            ])
        elif segment == "temp":
            asm_code.extend([
                "@SP",                  # Load stack pointer
                "AM=M-1",               # Decrement stack pointer and set A to new stack top
                "D=M",                  # Get value from stack top
                f"@{5 + int(index)}",   # Load base address of temp segment
                "M=D"                   # Store value from stack into target temp address
            ])
        
    return asm_code

def translate_vm(filename):
    asm_code = []
    label_counter = 0
    basename = filename.split('/')[-1].split('.')[0]  # Extract the base name without path and extension

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("//"):
                parts = line.split()
                command = parts[0]

                if command in ["add", "sub", "neg", "eq", "lt", "and", "or", "not", "get"]:
                    translated_code, label_counter = translate_arithmetic(command, label_counter)
                    asm_code.extend(translated_code)
                elif command in ["push", "pop"]:
                    translated_code = translate_memory_access(parts, basename)
                    asm_code.extend(translated_code)

    return asm_code

def main():
    if len(sys.argv) != 2:
        print("Usage: python vm.py <inputFile.vm>")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace(".vm", ".asm")

    asm_code = translate_vm(input_file)

    with open(output_file, 'w') as file:
        file.write("\n".join(asm_code) + "\n")

if __name__ == "__main__":
    main()

