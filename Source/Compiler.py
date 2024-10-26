from LexerParser import *
import time
import subprocess as sp


class Interpreter:
    def __init__(self):
        self.env = {}  # Global environment to store variables
        self.functions = {}  # Store function definitions
        self.my_dict = {} #dict
        
    
    def eval(self, node):
        if isinstance(node, tuple):
            if node[0] == 'program':
                result = None
                for statement in node[1]:
                    result = self.eval(statement)
                return result

            elif node[0] == 'var_assign':
                value = self.eval(node[2])
                self.env[node[1]] = value
                return None
                
            elif node[0] == 'U++' :
                 self.env[node[1]] = self.env[node[1]] + 1
                 return None 
                 
            elif node[0] == 'U--' :
                 self.env[node[1]] = self.env[node[1]] - 1
                 return None 
                 
            elif node[0] == 'plus_equal':
                 if node[1] not in self.env:
                    raise KeyError(f"Variable {node[1]} is not defined.")
                 self.env[node[1]] = self.env[ node[1] ] + node[2]
                 return None
                 
            elif node[0] == 'minus_equal':
                 if node[1] not in self.env:
                    raise KeyError(f"Variable {node[1]} is not defined.")
                 self.env[node[1]] = self.env[ node[1] ] - node[2]
                 return None
                 
            elif node[0] == 'mul_equal':
                 if node[1] not in self.env:
                    raise KeyError(f"Variable {node[1]} is not defined.")
                 self.env[node[1]] = self.env[ node[1] ] * node[2]
                 return None
                 
            elif node[0] == 'div_equal':
            
                 if node[1] not in self.env:
                    raise KeyError(f"Variable {node[1]} is not defined.")
                    
                 def divide_without_division(dividend, divisor):
                     if divisor == 0: raise ValueError("Divisor cannot be zero.")
                     sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
                     dividend, divisor, quotient = abs(dividend), abs(divisor), 0
                     while dividend >= divisor:
                           dividend -= divisor
                           quotient += 1
                     return sign * quotient

                 self.env[node[1]] = divide_without_division( self.env[node[1]] , node[2])
                 return None
                 
            elif node[0] == 'mod_equal':
                 if node[1] not in self.env:
                    raise KeyError(f"Variable {node[1]} is not defined.")
                 self.env[node[1]] = self.env[ node[1] ] % node[2]
                 return None

            elif node[0] == 'multiple_assign':
                names, exprs = node[1], node[2]
                values = [self.eval(expr) for expr in exprs]
                for name, value in zip(names, values):
                    self.env[name] = value
                return None

            elif node[0] == 'var':
                if node[1] in self.env:
                   # Check if x is an int
                   if isinstance(self.env[node[1]], int):
                         return self.env[node[1]]
                   # Check if y is a str
                   if isinstance(self.env[node[1]], str):
                         return (self.env[node[1]]).replace('"',"")  
                else:
                    raise NameError(f"Variable '{node[1]}' is not defined")

            elif node[0] == 'num':
                return node[1]

            elif node[0] in ['add', 'sub', 'mul', 'div', 'mod']:
                left = self.eval(node[1])
                right = self.eval(node[2])
                if node[0] == 'add':
                    return left + right
                elif node[0] == 'sub':
                    return left - right
                elif node[0] == 'mul':
                    return left * right
                elif node[0] == 'div':
                     def divide_without_division(dividend, divisor):
                         if divisor == 0: raise ValueError("Divisor cannot be zero.")
                         sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
                         dividend, divisor, quotient = abs(dividend), abs(divisor), 0
                         while dividend >= divisor:
                              dividend -= divisor
                              quotient += 1
                         return sign * quotient

                     return  divide_without_division( left , right )
                    
                elif node[0] == 'mod':
                    return left % right

            elif node[0] == 'print':
                values = [self.eval(arg) if arg[0] != 'string' else arg[1].replace( '"' , "" ) for arg in node[1]]
                print(*values)
                return None
                
            elif node[0] == 'print_funcall' :
                 self.eval( ( 'fun_call' , node[1] , node[2] ) )
                 return None 
                 

            elif node[0] == 'if_stmt':
                if len(node) == 4:  # IF without ELSE
                    if self.eval(node[1]):
                        return self.eval_block(node[2])
                elif len(node) == 6:  # IF with ELSE
                    if self.eval(node[2]):
                        return self.eval_block(node[3])
                    else:
                        return self.eval_block(node[5])

            elif node[0] in ['condition_eqeq', 'condition_noteq', 'condition_gt', 'condition_st', 'condition_gteq', 'condition_steq']:
                left = self.eval(node[1])
                right = self.eval(node[2])
                if node[0] == 'condition_eqeq':
                    return left == right
                elif node[0] == 'condition_noteq':
                    return left != right
                elif node[0] == 'condition_gt':
                    return left > right
                elif node[0] == 'condition_st':
                    return left < right
                elif node[0] == 'condition_gteq':
                    return left >= right
                elif node[0] == 'condition_steq':
                    return left <= right

            elif node[0] == 'and':
                return self.eval(node[1]) and self.eval(node[2])

            elif node[0] == 'or':
                return self.eval(node[1]) or self.eval(node[2])

            elif node[0] == 'while_loop':
                while self.eval(node[1]):
                    self.eval_block( node[2] )
                return None
                
            elif node[0] == 'while_loopnum':
                if node[ 1 ] == 1 :
                    while True :
                        self.eval_block(node[2])
                elif node[ 1 ] > 1 :
                     tempiter = 0
                     while ( tempiter <= node[1] ) :
                            self.env[ 'whilei' ] = tempiter
                            self.eval_block( node[2] )
                            tempiter += 1
                else :
                     pass 
                return None
                
            elif node[0] == 'while_loopnumnum' :
                 if ( node[1]  <= node[2] ) :
                    for foriter in range( node[1] , node[2] ) :
                        self.env[ 'whilei' ] = foriter
                        self.eval_block( node[3] )
                 else :
                    print("Error in iter : while_loop ( " , node[1] ," is greater than " , node[ 2 ] , " ) " )
                 return None 
                 
            elif node[0] == 'while_loopname' :
                 node1 , node2 = self.env[ node[1] ] , self.env[ node[2] ]
                 if (  node1    <= node2 ) :
                    for foriter in range( node1 , node2 ) :
                        self.env[ 'whilei' ] = foriter
                        self.eval_block( node[3] )
                 else :
                    print("Error in iter : while_loop ( ", node[1] ," is greater than " , node[ 2 ] , " ) " )
                 return None 
                 
            elif node[0] == 'while_looponename' :
                    for foriter in range( self.env[ node[1] ] ) :
                        self.env[ 'whilei' ] = foriter
                        self.eval_block( node[2] )
                    return None

            elif node[0] == 'for_loop':
                self.eval(node[1][1])  # Initialize
                while self.eval(node[1][2]):  # Condition
                    self.eval_block(node[2])  # Body
                    self.eval(node[1][3])  # Increment
                return None
                
            elif node[0] == 'for_loopcon':
                while self.eval(node[1]):
                    self.eval_block( node[2] )
                return None
                
            elif node[0] == 'for_loopnum':
                if node[1] == 1 :
                   while True :
                         self.eval_block( node[2] )
                elif node[1] > 1 :
                     tempiter = 0
                     while ( tempiter <= node[1] ) :
                           self.env[ 'fori' ] = tempiter
                           self.eval_block( node[2] )
                           tempiter += 1
                else :
                     pass 
                return None
                
                
            elif node[0] == 'for_loopnumnum' :
                 if ( node[1]  <= node[2] ) :
                    for foriter in range( node[1] , node[2] ) :
                        self.env[ 'fori' ] = foriter
                        self.eval_block( node[3] )
                 else :
                    print("Error in iter : for_loop ( ", node[1] ," is greater than " , node[ 2 ] , " ) " )
                 return None 
                 
            elif node[0] == 'for_loopname' :
                 node1 , node2 = self.env[ node[1] ] , self.env[ node[2] ]
                 if (  node1    <= node2 ) :
                    for foriter in range( node1 , node2 ) :
                        self.env[ 'fori' ] = foriter
                        self.eval_block( node[3] )
                 else :
                    print("Error in iter : for_loop ( ", node[1] ," is greater than " , node[ 2 ] , " ) " )
                 return None 
                 
            elif node[0] == 'for_loopnumname' :
                 node1 , node2 =  node[1]  , self.env[ node[2] ]
                 if (  node1    <= node2 ) :
                    for foriter in range( node1 , node2 ) :
                        self.env[ 'fori' ] = foriter
                        self.eval_block( node[3] )
                 else :
                    print("Error in iter : for_loop ( ", node[1] ," is greater than " , node[ 2 ] , " ) " )
                 return None 
                 
            elif node[0] == 'for_looponename' :
                    for foriter in range( self.env[ node[1] ] ) :
                        self.env[ 'fori' ] = foriter
                        self.eval_block( node[2] )
                    return None
                 

            elif node[0] == 'do_while':
                do_block, condition = node[1], node[2]
                while True:
                    self.eval_block(do_block)
                    if not self.eval(condition):
                        break
                return None


            elif node[0] == 'function':
                function_name, params, body = node[1], node[2], node[3]
                self.functions[function_name] = (params, body)
                return None

            elif node[0] == 'fun_call':
                function_name = node[1]
                args = [self.eval(arg) for arg in node[2]]
                argsvar_list = [item[1] for item in self.functions[ function_name ][0]  ]
                #print( node[0] , argsvar_list , args )
                if function_name in self.functions:
                    names = argsvar_list
                    values = args
                    #print( function_name , args , names )
                    for name, value in zip(names, values):
                        self.env[name] = value
                    if function_name in self.functions:
                        params, body = self.functions[function_name]
                        # Evaluate the function body
                        result = self.eval_block( body )
                    
                    
                else:
                    raise NameError(f"Function '{function_name}' is not defined")
         
                return result
                
                
            elif node[0] == 'assign_funcall' :
                 #print( node[0] , node[1] , node[2] , node[3])
                 self.eval( ( 'fun_call' , node[2] , node[3] ) )
                 #print( self.returnvalue )
                 self.env[node[1]] = self.returnvalue
                 return None 
                                

            elif node[0] == 'return':
                returnvalue =  self.eval(node[1]) if node[1] is not None else None
                self.returnvalue = returnvalue
                return None
                
            elif node[0] == 'returnstr' :
                returnvalue =  self.eval(node[1]) if node[1] is not None else None
                self.returnvalue = returnvalue
                return None
                
            elif node[0] == 'str_inputws' :
                string = node[2].replace('"',"")
                inputval = str( input( string ) )
                self.env[node[1]] = inputval
                return None
                
            elif node[0] == 'int_inputws' :
                string = node[2].replace('"',"")
                inputval = int( input( string ) )
                self.env[node[1]] = inputval
                return None
                
            elif node[0] == 'str_inputstrws' :
                string = node[2].replace('"',"")
                inputval = str( input( string ) )
                self.env[node[1]] = inputval
                return None
                
            elif node[0] == 'str_inputwos' :
                inputval = str( input(  ) )
                self.env[node[1]] = inputval
                return None
                
            elif node[0] == 'int_inputwos' :
                inputval = int( input(  ) )
                self.env[node[1]] = inputval
                return None
                
            elif node[0] == 'str_inputstrwos' :
                inputval = str( input(  ) )
                self.env[node[1]] = inputval
                return None
                
            elif node[0] == 'time_sleep' :
                 time.sleep( node[1] )
                 return None
                 
            elif node[0] == 'time_time' :
                 print ( time.ctime() )
                 return None
                 
            elif node[0] == 'time_date' :
                 current_date = time.localtime()
                 print( time.strftime("%Y-%m-%d", current_date) )
                 return None
                 
            elif node[0] == 'copy' :
                 if( node[ 2 ] in self.env ) :
                      self.env[ node[ 1 ] ] = self.env[ node[ 2 ] ]
                 else :
                      print(f"NAME : { node[ 2 ] } not define.")
                 return None 
                 
            elif node[ 0 ] == 'index' :
                 if isinstance(self.env[node[2]], int):
                         print( node[2] ," = " , self.env[ node[2] ] ,"is a base 10 value." )
                         return None
                         
                 if isinstance(self.env[node[2]], str):
                              strvalue = self.env[ node[2] ].replace( '"' , "" )
                              self.env[ node[1] ] = strvalue[ self.eval( node[3] )  ] 
                              return None
                              
            elif node[ 0 ] == 'indexwon' :
                 if isinstance(self.env[node[1]], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                         
                 if isinstance(self.env[node[1]], str):
                              strvalue = self.env[ node[1] ].replace( '"' , "" )
                              print( strvalue[ self.eval( node[2] )  ] )
                              return None
                               
            elif node[ 0 ] == 'strindex' :
                 if isinstance(self.env[node[2]], int):
                         print( node[2] ," = " , self.env[ node[2] ] ,"is a base 10 value." )
                         return None
                 if isinstance( self.env[ node[ 2 ] ] , str ) :
                     strvalue = self.env[ node[ 2 ] ].replace( '"' , "" )
                     substr = node[ 3 ].replace( '"' , "" )
                     intvalue = strvalue.find( substr )
                     self.env[ node[1] ] = intvalue
                 return None
                 
            elif node[ 0 ] == 'strindexwon' :
                 if isinstance( self.env[ node[ 1 ] ] , str ) :
                     strvalue = self.env[ node[ 1 ] ].replace( '"' , "" ) 
                     substr = node[ 2 ].replace( '"' , "" )
                     intvalue = strvalue.find( substr )
                     print( intvalue )
                     return None
                 
            elif node[0] == 'upper' :
                 if isinstance(self.env[node[2]], int):
                         print( node[2] ," = " , self.env[ node[2] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[2]], str):
                         self.env[ node[1] ] = self.env[ node[2] ].upper().replace( '"' , "" )
                         return None
                 
            elif node[0] == 'upperwon' :
                 if isinstance(self.env[node[1]], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[1]], str):
                         print(  self.env[ node[1] ].upper().replace( '"' , "" ) )
                         return None
                        
            elif node[0] == 'strupper' :
                 if isinstance( node[1], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance( node[1] ,  str):
                         print( node[1].upper().replace( '"' , "" ) )
                         return None
                        
            elif node[0] == 'lower' :
                 if isinstance(self.env[node[2]], int):
                         print( node[2] ," = " , self.env[ node[2] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[2]], str):
                         self.env[ node[1] ] = self.env[ node[2] ].lower().replace( '"' , "" )
                         return None
                 
            elif node[0] == 'lowerwon' :
                 if isinstance(self.env[node[1]], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[1]], str):
                         print( self.env[ node[1] ].lower().replace( '"' , "" ) )
                         return None
                        
            elif node[0] == 'strlower' :
                 if isinstance( node[1], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance( node[1] ,  str):
                         print(  node[1].lower().replace( '"' , "" ) )
                         return None
                        
                        
            elif node[0] == 'isupper' :
                 if isinstance(self.env[node[2]], int):
                         print( node[2] ," = " , self.env[ node[2] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[2]], str):
                         self.env[ node[1] ] = 1 if self.env[ node[2] ].isupper() == True else 0
                         return None
                 
            elif node[0] == 'isupperwon' :
                 if isinstance(self.env[node[1]], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[1]], str):
                         print( 1 if self.env[ node[1] ].isupper() == True else 0 )
                         return None
                        
                        
            elif node[0] == 'strisupper' :
                 if isinstance( node[1], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance( node[1] ,  str):
                         print(  1 if node[1].isupper() == True else 0 )
                         return None
                      
                
                        
            elif node[0] == 'islower' :
                 if isinstance(self.env[node[2]], int):
                         print( node[2] ," = " , self.env[ node[2] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[2]], str):
                         self.env[ node[1] ] = 1 if self.env[ node[2] ].islower() == True else 0
                         return None
                 
            elif node[0] == 'islowerwon' :
                 if isinstance(self.env[node[1]], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance(self.env[node[1]], str):
                         print( 1 if self.env[ node[1] ].islower() == True else 0 )
                         return None
                      
                        
            elif node[0] == 'strislower' :
                 if isinstance( node[1], int):
                         print( node[1] ," = " , self.env[ node[1] ] ,"is a base 10 value." )
                         return None
                 if isinstance( node[1] ,  str):
                         print( 1 if node[1].islower() == True else 0 )
                         return None
                       
                        
            elif node[ 0 ] == 'len' :
                 self.env[ node[ 1 ] ] = len( self.env[ node[ 2 ] ].replace( '"' , "" )  )
                 return None
                 
            elif node[ 0 ] == 'strlen' :
                 self.env[ node[ 1 ] ] = len( node[ 2 ].replace( '"' , "" ) )
                 return None
                 
            elif node[ 0 ] == 'lenwon' :
                 print( len( self.env[ node[1] ].replace( '"' , "" )  ) )
                 return None
                 
            elif node[ 0 ] == 'strlenwon' :
                 print( len( node[1] ).replace( '"' , "" ) )
                 return None
                 
            elif node[ 0 ] == 'print_namelen' :
                 print( len( self.env[ node[ 1 ] ].replace( '"' , "" ) ) )
                 return None
                 
            elif node[ 0 ] == 'print_strlen' :
                 print( len( node[1].replace( '"' , "" ) ))
                 return None
                 
            elif node[ 0] == 'list' :
                 print( self.my_dict )
                 return None
                 
            elif node[ 0 ] == 'listadd' :
                 self.my_dict[ node[ 1 ] ] = self.env[ node[ 1 ] ]
                 return None
                 
            elif node[ 0 ] == 'listwrite' :
                 self.env[ node[ 2 ] ] = self.my_dict[ node[ 1 ] ] 
                 return None
                 
            elif node[ 0 ] == 'listwrite1' :
                 print( self.my_dict[ node[ 1 ] ]  )
                 return None
                 
            elif node[ 0 ] == 'jetray' :
                 if node[1] in self.env :
                    #print( "NAME : ", node[ 1 ] ," = ", self.env[ node[1] ] ," ( NOT NULL )" )
                    print( 1 )
                    return None
                 if node[ 1 ] not in self.env :
                    #print( "NAME : ", node[ 1 ] , " = ( NULL )")
                    print( -1 )
                    return None
                   
                   
            elif node[0] == 'web_search' :
                 sp.run(['tgpt' , "@web_search "+ str( node[1] ) ])
                 return None
                 
            elif node[0] == 'ai_search' :
                 sp.run(['tgpt' ,  str( node[1] ) ])
                 return None
                 
            elif node[0] == 'strmulnum' :
                 print ( node[2] * node[1].replace( '"' , "" )  )
                 return None
                 
            elif node[0] == 'nummulstr' :
                 print ( node[1] * node[2].replace( '"' , "" ) )
                 return None
                 
            elif node[0] == 'echo' :
                 print("\t")
                 return None
                 
            elif node[0] == 'echoecho' :
                 print("\n")
                 return None
                 
            elif node[0] == 'appendstr' :
                 self.env[ node[1] ] += node[2]
                 return None
                 
            elif node[0] == 'appendname' :
                 self.env[ node[1] ] += self.env[ node[2] ]
                 return None
                

        return node

    def eval_block(self, statements):
        result = None
        for stmt in statements:
            result = self.eval(stmt)
            if isinstance(stmt, tuple) and stmt[0] == 'return':
                break
        return result


# MAIN

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    interpreter = Interpreter()

    while True:
        try:
            text = input('basic > ')
        except EOFError:
            break
        if text:
            try:
                tree = parser.parse(lexer.tokenize(text))
                result = interpreter.eval(tree)
                if result is not None:
                    print(result)
            except Exception as e:
                print(f"Error: {e}")
                

         
