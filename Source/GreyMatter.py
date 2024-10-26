from Compiler import *
import pyfiglet

def calvin_s() :
    print('_' * 40)
    print( )
    print(pyfiglet.figlet_format("GREYMATTER", font='calvin_s') , end="" )
    print('_' * 40)
    
def tinker_toy():
    print(pyfiglet.figlet_format("GREYMATTER", font='tinker-toy') , end="" )
    
def ansi_shadow() :
    print("\033[1;32m")
    print('_' * 100 )
    print("\n")
    fig = pyfiglet.Figlet(font='ansi_shadow', width=100)  
    print(fig.renderText(' GREYMATTER') ,end='')
    print('_' * 100 )
    

def about() :
    
    
    #calvin_s()
    ansi_shadow()
    #tinker_toy()
    
    text = '''
                         \033[1;37m   A toy language is a simple, often experimental programming language developed for learning or research purposes. It usually focuses on a specific subset of programming concepts or paradigms and might have limited functionality compared to full-scale languages like Python or C. It is typically used to explore language design, parsing, and interpretation without the complexities of handling full-featured compilers or interpreters.
                             
\033[1;33mToy languages are often used to teach or explore: \033[1;37m

       1. \033[1;32m Basic language design (syntax, semantics, and grammar). \033[1;37m
       2. \033[1;32m Parsing and lexing (turning text into tokens and then interpreting them). \033[1;37m
       3. \033[1;32m Interpreter or compiler development (execution of code written in the language). \033[1;37m
     
\033[1;33m### 1. **Purpose of Greymatter** \033[1;32m

\033[1;34m     The primary goal of \033[1;32m**GREYMATTER**\033[1;34m is to combine the strengths of Python and C: \033[1;32m

     - \033[1;34m**Python-like simplicity** : \033[1;32m Greymatter aims for clear, human-readable syntax that is easy to learn and work with.
     - \033[1;34m**C-like performance and control** : \033[1;32m It provides the ability to manipulate memory and hardware efficiently, allowing for more low-level system control, which is often a limitation in higher-level languages like Python.

By blending these two paradigms, **greymatter** can serve a wide audience, from beginners who appreciate Python's simplicity to seasoned developers who need the fine-grained control that C offers.

\033[1;33m### 2. **Key Features**\033[1;32m

      - \033[1;34m**Simple syntax** : \033[1;32m Borrowing from Python’s clean and readable structure, greymatter makes code easy to understand, reducing the need for excessive syntax rules.
      - \033[1;34m**Efficiency** : \033[1;32m Like C, greymatter allows developers to write high-performance applications by offering access to system resources and memory management, which can be particularly useful for performance-critical tasks.
      - \033[1;34m**Dynamic typing with optional type declarations** : \033[1;32m Greymatter might allow flexibility in variable declarations like Python, but for performance-critical parts, it could provide C-style type declarations, enabling both dynamic and static typing.
      - \033[1;34m**Cross-Platform Compatibility** : \033[1;32m Following in Python's footsteps, it can aim to be cross-platform, running on major operating systems with minimal differences in code.
  
\033[1;33m### 3. **Use Cases** \033[1;32m

      - \033[1;34m**Learning and Education** : \033[1;32m Greymatter can serve as a bridge for students transitioning from Python (focused on simplicity) to C (focused on systems programming). It can help them understand lower-level programming concepts while retaining ease of use.
      - \033[1;34m**Systems Programming** : \033[1;32m Due to its C-like characteristics, greymatter would allow direct hardware manipulation and memory management, making it suitable for writing operating systems, embedded systems, and performance-critical software.
      - \033[1;34m**General Application Development** : \033[1;32m Greymatter could handle everyday programming tasks, including web development, scripting, and automation, thanks to its Python-inspired simplicity.

\033[1;33m### 4. **Core Philosophy** \033[1;32m

      - \033[1;34m**Ease of learning** : \033[1;32m The language is built with beginners in mind, reducing complexity while teaching core concepts like memory management and type systems.
      - \033[1;34m**Scalability** : \033[1;32m Although designed to be easy, greymatter is scalable, allowing experienced developers to write efficient, high-performance code when necessary.
      - \033[1;34m**Minimalistic yet Powerful** : \033[1;32m The idea is to have a language that's minimalistic in terms of syntax and rules but powerful enough to handle complex and diverse programming needs.

\033[1;33m### 5. **Development and Community Potential** \033[1;32m

      - \033[1;34m**Extensibility** : \033[1;32m Greymatter could have a modular design that allows for libraries and modules, similar to Python's vast library ecosystem. Over time, a community could form to contribute libraries for various tasks like networking, data processing, and more.
      - \033[1;34m**Strong Developer Tools** : \033[1;32m It could include user-friendly development tools, such as an interpreter or compiler, with an emphasis on debugging, testing, and documentation generation.

\033[1;33m### 6. **Conclusion** \033[1;32m

      \033[1;32mIn summary, \033[1;37m**GREYMATTER** \033[1;32m stands as a fusion of the best of Python and C. It offers simplicity for those new to programming but scales up to offer performance and control, making it ideal for both beginner and advanced users. The result is a versatile language that can be used in a wide range of applications, from learning environments to system-level programming.

'''
    
    print( text )



def help() :
    print("\033[1;32m")
    calvin_s()
    print("\n\n")
    

# MAIN

print("\033[1;31m$ \033[1;32mGreyMatter  \033[1;34m<\033[1;32m--version 0.01 \033[1;31m<\033[1;33m\\\033[1;31m> ")
print("\033[1;31m$\033[1;32m Release On Sept 25  \033[1;34m<\033[1;32m--@--\033[1;34m>\033[1;32m 2024 \033[1;31m<\033[1;33m\\\033[1;31m> \n")

lexer = BasicLexer()
parser = BasicParser()
interpreter = Interpreter()

help()

while True :
	try :
		while True :
			
			code = ""
			
			while True :
				
				text = str( input("\033[1;32m>>>\033[1;31m>\033[1;37m ") )
				
				if( text.replace( " " , "") in [ 'about()' ] ) :
				    if( text.replace(" " , "") == 'about()' ) :
				         about()
				
				if ( text == '' ) :
					break
					
				iseval = (text[0].replace( " " , "" )).isdigit() == True  and  (text[-1].replace( " " , "")).isdigit() == True
				
				if ( iseval == True ) :
					 print(eval(text))
					 
				if ( iseval == False ) :
				    code += " " + text
				        
				if ( (text.lower()).replace( " " , "" ) == "exit" ) :
				     print("\033[0;37m")
				     exit()
				
			tree = parser.parse(lexer.tokenize(code))
			result = interpreter.eval(tree)
			if result is not None:
			    print(result)
			    
			code = ""
	
	except Exception as e:
	      
	      error_message = str(e)
	      print("\033[1;31mAn error occurred:", error_message , "\033[1;32m")
    

	
