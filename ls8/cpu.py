"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = [0] * 256
        self.pc = 0  # program counter
        self.r0 = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.r5 = 0  # interrupt mask (IM)
        self.r6 = 0  # interrupt status (IS)
        self.r7 = 0  # stack pointer (SP)

    def ram_read(self, MAR):  # memory address register
        # return the value at the address
        try:
            return self.memory[MAR]
        except IndexError:
            return None

    def ram_write(self, MDR, MAR):  # memory data register
        # write the address to the value and don't return anthing
        self.memory[MAR] = MDR

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.memory[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X | %d | %02X %02X %02X |" % (
            self.pc,
            self.fl,
            self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        
        while True:
            IR = self.pc  # instruction register
            # print(f'IR is {IR}')
            opcode = self.ram_read(IR)
            operand_a = self.ram_read(IR + 1)
            operand_b = self.ram_read(IR + 2)

            if opcode == 0b10000010:  # LDI
                # register is operand_a
                # value is operand_b
                setattr(self,f'r{operand_a}' ,operand_b)
                
            elif opcode == 0b01000111:  # PRN
                # print the numeric value in register of operand_a
                # print(f'r{operand_a}')
                print(getattr(self, f'r{operand_a}'))
                pass
            elif opcode == 0b00000001:# HLT
                # terminate program
                sys.exit()
            elif opcode == 0b1:
                pass
            elif opcode == 0b1:
                pass
            elif opcode == 0b1:
                pass
            elif opcode == 0b1:
                pass
            elif opcode == 0b1:
                pass
            # increment the pc
            string_op_used = format(opcode, '#010b')[2:4] 
            self.pc += int(string_op_used, 2) +1
            