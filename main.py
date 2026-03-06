from typing import IO
import subprocess

def create_assembly_file(file_path: str):
    with open(file_path, "w") as file:
        # setup
        declare_start_section(file)
        add_start_label(file)
        # program data
        add_main_label(file)
        
        # setup
        add_exit_label(file)

def declare_start_section(file: IO[any]):
    file.write(
        "section .text\n" \
        "\tglobal _start\n" \
        "\n"
    )

def add_start_label(file: IO[any]):
    file.write(
        "start:\n" \
        "\tjmp main\n" \
        "\n"
    )

def add_main_label(file: IO[any]):
    file.write(
        "main:\n" \
        "\tjmp exit\n" \
        "\n"
    )

def add_exit_label(file: IO[any]):
    file.write(
        "exit:\n" \
        "\tmov rax, 60\n" \
        "\txor rdi, rdi\n" \
        "\tsyscall\n"
    )

def assemble(assembly_file_path:str, object_file_path:str):
    subprocess.run(["nasm", "-f", "elf64", "-o", object_file_path, assembly_file_path], check=True)

def link(object_file_path:str, executable_file_path:str):
    subprocess.run(["ld" "-o", executable_file_path, object_file_path], check=True)

def main():
    assemblyFilePath = "bin/out.s"
    objectFilePath = "bin/out.o"
    executableFilePath = "bin/out"
    create_assembly_file(assemblyFilePath)
    assemble(assemblyFilePath, objectFilePath)
    link(objectFilePath, executableFilePath)
    
if __name__ == "__main__":
    main()