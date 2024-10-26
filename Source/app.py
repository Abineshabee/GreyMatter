import argparse
import subprocess as sp
from Compiler import *

def read_file_without_newlines(file_path):
    with open(file_path, 'r') as file:
        content = file.read().replace('\n', ' ').replace('\r', ' ')
    return content

# MAIN 
if __name__ == '__main__':
    # Parse command line arguments
    parser_arg = argparse.ArgumentParser(description='Process a source file.')
    parser_arg.add_argument('file_path', type=str, help='Path to the source text file')
    args = parser_arg.parse_args()

    file_path = args.file_path
    content = read_file_without_newlines( "Samples/" + file_path )

    lexer = BasicLexer()
    parser = BasicParser()
    interpreter = Interpreter()

    # sp.run(['clear'])

    try:
        #print(content)
        tree = parser.parse(lexer.tokenize(content))
        # print(tree)
        result = interpreter.eval(tree)
        if result is not None:
            print(result)
    except Exception as e:
        print(f"Error: {e}")

