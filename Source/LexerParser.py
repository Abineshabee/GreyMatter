from sly import Lexer
from sly import Parser

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF,  ELSE, FOR, FUNCTION, EQEQ , PRINT  , GTEQ , STEQ , NOTEQ , GT , ST , COMMA , WHILE , AND , OR , DO  , INPUT , INT , STR , FEEDBACK  , PARADOX , SLEEP , UNITIME , UNIDATE , DITTO , ECHOECHO , ECHO , FASTTRACK , WAYBIG , NANOMECH ,ISWAYBIG , ISNANOMECH , LEN , BRAINSTORM , READ , STORE , WRITE , IN , GET , JETRAY , WEB_SEARCH , AI , BREAK }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' , '%'  , '{' , '}' , '//'  , '.' , '@' , '_'  }
    
    # Define tokens
    IF = r'IF'
    #THEN = r'THEN'
    ELSE = r'ELSE'
    FOR = r'FOR'
    FUNCTION = r'FUNCTION'
    #TO = r'TO'
    PRINT = r'PRINT'
    #RETURN= r'RETURN'
    #ARROW = r'->'
    COMMA = r','
    WHILE = r'WHILE'
    AND = r'AND'
    OR = r'OR'
    DO = r'DO'
    INPUT = r'INPUT'
    INT = r'INT'
    STR = r'STR'
    LEN = r'LEN'
    WEB_SEARCH = r'WEB_SEARCH'
    AI = r'AI'
    BREAK = r'BREAK'
    
    #aliens and its kes
    
    FEEDBACK = r'FEEDBACK'
    PARADOX  = r'PARADOX'
    SLEEP    = r'SLEEP'
    UNITIME  = r'UNITIME'
    UNIDATE  = r'UNIDATE'
    DITTO    = r'DITTO'
    ECHOECHO = r'ECHOECHO'
    ECHO     = r'ECHO'
    FASTTRACK = r'FASTTRACK'
    WAYBIG    = r'WAYBIG'
    NANOMECH  = r'NANOMECH'
    ISWAYBIG  = r'ISWAYBIG'
    ISNANOMECH = r'ISNANOMECH'
    BRAINSTORM = r'BRAINSTORM'
    READ       = r'READ'
    STORE      = r'STORE'
    WRITE      = r'WRITE'
    IN         = r'IN'
    GET        = r'GET'
    JETRAY     = r'JETRAY'
    
    EQEQ = r'=='
    GTEQ = r'>='
    STEQ = r'<='
    NOTEQ = r'!='
    GT = r'>'
    ST = r'<'
    
    
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    
    

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*#')
    @_(r'//.*//')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

class BasicParser(Parser):
    tokens = BasicLexer.tokens

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('nonassoc', 'EQEQ', 'NOTEQ', 'GT', 'ST', 'GTEQ', 'STEQ'),
        ('left', '+', '-'),
        ('left', '*', '/' , '%'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }
        
    
        
    #NULL statements ===========================================================================
    
    @_('statements')
    def program(self, p):
        return ('program', p.statements)

    @_('statement')
    def statements(self, p):
        return ( [p.statement] )

    @_('statements statement')
    def statements(self, p):
        return ( p.statements + [p.statement] )
        
    @_('')
    def statement(self, p):
        pass
        

        
    #RETURN ====================================================================================
        
    @_('FEEDBACK "(" expr ")"')
    def statement(self, p):
        return ('return', p.expr)
        
    @_('FEEDBACK "(" STRING ")"')
    def statement( self , p ) :
        return ( 'returnstr' , p.STRING )

    @_('FEEDBACK')
    def statement(self, p):
        return ('return', None)
        
    @_('FEEDBACK "(" ")"')
    def statement(self, p):
        return ('return', None)
        
    #PRINT ========================================================================================

    
    @_('PRINT "(" print_args ")"')
    def statement(self, p):
        return ('print', p.print_args)
        
    @_('PRINT "(" NAME "(" arg_list ")" ")"')
    def statement(self, p):
        return ('print_funcall', p.NAME , p.arg_list )
        
    @_('expr')
    def print_args(self, p):
        return [p.expr]

    @_('print_args COMMA expr')
    def print_args(self, p):
        return p.print_args + [p.expr]

    @_('print_args COMMA STRING')
    def print_args(self, p):
        return p.print_args + [('string', p.STRING)]

    @_('STRING')
    def print_args(self, p):
        return [('string', p.STRING)]
        
    @_('PRINT "(" STRING "*" NUMBER ")"')
    def statement( self , p ) :
        return ('strmulnum' , p.STRING , p.NUMBER )
        
    @_('PRINT "(" NUMBER "*" STRING ")"')
    def statement( self , p ) :
        return ('nummulstr' , p.NUMBER , p.STRING )
        
    #FOR ================================================================================================

    @_('FOR "(" var_assign ";" condition ";" var_assign ")" "{" statements "}"')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign0, p.condition, p.var_assign1), p.statements)
        
        
    @_('FOR "(" NUMBER ")" "{" statements "}"')
    def statement(self, p):
        return ('for_loopnum', p.NUMBER , p.statements)
        
    @_('FOR "(" NAME ")" "{" statements "}"')
    def statement(self, p):
        return ('for_looponename', p.NAME , p.statements)
        
    @_('FOR "(" NUMBER COMMA NUMBER ")" "{" statements "}"')
    def statement(self, p):
        return ('for_loopnumnum', p.NUMBER0 , p.NUMBER1 , p.statements)
    
    @_('FOR "(" NAME COMMA NAME ")" "{" statements "}"')
    def statement(self, p):
        return ('for_loopname', p.NAME0 , p.NAME1 , p.statements)
        
    @_('FOR "(" NUMBER COMMA NAME ")" "{" statements "}"')
    def statement(self, p):
        return ('for_loopnumname', p.NUMBER , p.NAME , p.statements)
        
    @_('FOR "(" condition ")" "{" statements "}"') 
    def statement( self , p ) :
        return ('for_loopcon', p.condition , p.statements )
        
   
        
    #WHILE ================================================================================================
    
    @_('WHILE "(" condition ")" "{" statements "}"') 
    def statement( self , p ) :
        return ('while_loop', p.condition , p.statements )
        
    @_('WHILE "(" NAME ")" "{" statements "}"')
    def statement(self, p):
        return ('while_looponename', p.NAME , p.statements)
        
    @_('WHILE "(" NUMBER ")" "{" statements "}"') 
    def statement( self , p ) :
        return ('while_loopnum', p.NUMBER ,  p.statements )
        
    @_('WHILE "(" NUMBER COMMA NUMBER ")" "{" statements "}"') 
    def statement( self , p ) :
        return ('while_loopnumnum', p.NUMBER0 , p.NUMBER1 ,  p.statements )
        
    @_('WHILE "(" NAME COMMA NAME ")" "{" statements "}"')
    def statement(self, p):
        return ('while_loopname', p.NAME0 , p.NAME1 , p.statements)
        
    #DO_WHILE =============================================================================================
    
    @_('DO "{" statements "}" WHILE "(" condition ")" ')
    def statement( self , p ):
        return ('do_while' , p.statements , p.condition )
        
    #IF ===================================================================================================

    @_('IF "(" condition ")" "{" statements "}" ELSE "{" statements "}"')
    def statement(self, p):
        return ('if_stmt', 'if' , p.condition ,  p.statements0,'else',p.statements1 )
        
    @_('IF "(" condition ")" "{" statements "}"')
    def statement(self, p):
        return ('if_stmt', p.condition, p.statements, None)
        
    @_('condition OR condition')
    def condition(self, p):
        return ( 'or',p.condition0, p.condition1)

    @_('condition AND condition')
    def condition(self, p):
        return ( 'and', p.condition0,p.condition1)
        
    #FUN_ARROW ================================================================================================
    # Function Definition Rule
    @_('FUNCTION NAME "(" arg_list ")" "{" statements "}" ')
    def statement(self, p):
        return ('function', p.NAME, p.arg_list, p.statements)

    # Function Call Rule (no arguments)
    @_('NAME "(" ")"')
    def statement(self, p):
        return ('fun_call', p.NAME, [])

    # Function Call Rule (with arguments)
    @_('NAME "(" arg_list ")"')
    def statement(self, p):
        return ('fun_call', p.NAME, p.arg_list)

    # Argument List Rule (single argument)
    @_('expr')
    def arg_list(self, p):
        return [p.expr]

    # Argument List Rule (multiple arguments)
    @_('arg_list COMMA expr')
    def arg_list(self, p):
        return p.arg_list + [p.expr]

    # Empty Argument List Rule
    @_('')
    def arg_list(self, p):
        return []

    # Statements (in case empty function body is allowed)
    @_('')
    def statements(self, p):
        return []

    #INPUT ======================================================================================================

    @_('NAME "=" INPUT "(" STRING ")"')
    def statement( self , p ):
        return ('str_inputws', p.NAME ,p.STRING )
        
    @_('NAME "=" INT "(" INPUT "(" STRING ")" ")"')
    def statement( self , p ):
        return ('int_inputws', p.NAME ,p.STRING )
        
    @_('NAME "=" STR "(" INPUT "(" STRING ")" ")"')
    def statement( self , p ):
        return('str_inputstrws' , p.NAME , p.STRING )
        
    @_('NAME "=" INPUT "("  ")"')
    def statement( self , p ):
        return ('str_inputwos', p.NAME  )
        
    @_('NAME "=" INT "(" INPUT "("  ")" ")"')
    def statement( self , p ):
        return ('int_inputwos', p.NAME  )
        
    @_('NAME "=" STR "(" INPUT "(" ")" ")"')
    def statement( self , p ):
        return('str_inputstrwos' , p.NAME  )
        
    #COMPARE ====================================================================================================
    
    @_('condition')
    def statement( self , p ) :
         return( p.condition )
         
    @_('expr EQEQ expr')
    def condition(self, p):
        return ( 'condition_eqeq',p.expr0,  p.expr1)
    
    @_('expr GTEQ expr')
    def condition(self, p):
        return ( 'condition_gteq',p.expr0,  p.expr1)

    @_('expr STEQ expr')
    def condition(self, p):
        return ( 'condition_steq',p.expr0,  p.expr1)

    @_('expr NOTEQ expr')
    def condition(self, p):
        return ( 'condition_noteq',p.expr0,  p.expr1)
    
    @_('expr GT expr')
    def condition(self, p):
        return ('condition_gt',p.expr0,  p.expr1)

    @_('expr ST expr')
    def condition(self, p):
        return ( 'condition_st',p.expr0,  p.expr1)
        
    #VAR_ASSIGN =================================================================================================
    
    @_('NAME COMMA name_list "=" expr COMMA expr_list')
    def statement(self, p):
        names = [p.NAME] + p.name_list
        exprs = [p.expr] + p.expr_list
        return ('multiple_assign', names, exprs)

    @_('NAME COMMA name_list')
    def name_list(self, p):
        return ( [p.NAME] + p.name_list )

    @_('NAME')
    def name_list(self, p):
        return ( [p.NAME] )

    @_('expr COMMA expr_list')
    def expr_list(self, p):
        return ( [p.expr] + p.expr_list )

    @_('expr')
    def expr_list(self, p):
        return ( [p.expr] )
        
    #len
    @_('NAME "=" LEN "(" NAME ")"')
    def statement( self , p ) :
        return ( 'len' , p.NAME0 , p.NAME1 )
        
    @_('NAME "=" LEN "(" STRING ")"')
    def statement( self , p ) :
        return ( 'strlen' , p.NAME , p.STRING )
        
    @_('LEN "(" NAME ")"')
    def statement( self , p ) :
        return ( 'lenwon' , p.NAME )
        
    @_('LEN "(" STRING ")"')
    def statement( self , p ) :
        return ( 'strlenwon' , p.STRING )
        
    @_('PRINT "(" LEN "(" NAME ")" ")"')
    def statement( self , p ) :
        return ('print_namelen' , p.NAME )
        
    @_('PRINT "(" LEN "(" STRING ")" ")"')
    def statement( self , p ) :
        return ('print_strlen' , p.STRING)

        
    #assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)
        
    @_('NAME "+" "+"')
    def var_assign( self , p ) :
        return ( 'U++' , p.NAME )
        
    @_('NAME "-" "-"')
    def var_assign( self , p ) :
        return( 'U--' , p.NAME )
        
    @_('NAME "+" "+"')
    def statement( self , p ) :
        return ( 'U++' , p.NAME )
        
    @_('NAME "-" "-"')
    def statement( self , p ) :
        return( 'U--' , p.NAME )
        
    @_('NAME "+" "=" NUMBER')
    def statement(self, p):
        return ('plus_equal', p.NAME, p.NUMBER)
        
    @_('NAME "-" "=" NUMBER')
    def statement(self, p):
        return ('minus_equal', p.NAME, p.NUMBER)
        
    @_('NAME "*" "=" NUMBER')
    def statement(self, p):
        return ('mul_equal', p.NAME, p.NUMBER)
        
    @_('NAME "/" "=" NUMBER')
    def statement(self, p):
        return ('div_equal', p.NAME, p.NUMBER)
        
    @_('NAME "%" "=" NUMBER')
    def statement(self, p):
        return ('mod_equal', p.NAME, p.NUMBER)

        
    #statement
    
    @_('NAME "=" expr')
    def statement(self, p):
        return ('var_assign', p.NAME, p.expr)
        
    @_('NAME "=" STRING')
    def statement(self, p):
        return ('var_assign', p.NAME, p.STRING)
        
    @_('NAME "+" "=" STRING')
    def statement( self , p ) :
        return ('appendstr' , p.NAME , p.STRING )
        
    @_('NAME "+" "=" NAME')
    def statement( self , p ):
        return ('appendname' , p.NAME0 , p.NAME1 )
        
    @_('NAME "=" NAME "(" arg_list ")"')
    def statement( self, p ):
        return('assign_funcall', p.NAME0 , p.NAME1 , p.arg_list )

    @_('expr')
    def statement(self, p):
        return (p.expr)
        
    #expr =========================================================================================================

    @_('expr "+" expr')
    def expr(self, p):
        return ( 'add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ( 'sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ( 'mul',p.expr0,  p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ('div',  p.expr0, p.expr1)
        
    @_('expr "%" expr')
    def expr(self, p):
        return ( 'mod',p.expr0,  p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr
        
    #NAME

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)
        
    #NUMBER

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)
        
    #XXXX ====================================================================================================================
    
    @_('PARADOX "." SLEEP "(" NUMBER ")"')
    def statement( self , p ) :
        return ('time_sleep' , p.NUMBER )
        
    @_('PARADOX "." UNITIME "(" ")"')
    def statement( self , p ) :
        return ('time_time' , 1 )
        
    @_('PARADOX "." UNIDATE "(" ")"')
    def statement( self , p ) :
        return ('time_date' , 1 )
        
    #string
    
    @_('NAME "=" NAME "." DITTO "("  ")"')
    def statement( self , p ) :
        return ('copy' , p.NAME0 , p.NAME1 )
        
    @_('ECHOECHO')
    def statement( self , p ) :
        return ('echoecho' , 1 )
        
    @_('ECHO')
    def statement( self , p ) :
        return ('echo' , 1 )
        
    #---------------------------------------------------------
        
    @_('NAME "=" NAME "." FASTTRACK "(" expr ")"')
    def statement( self , p ) :
        return ( 'index' , p.NAME0 , p.NAME1 , p.expr )
        
    @_('NAME "." FASTTRACK "(" expr ")"')
    def statement( self , p ) :
        return ( 'indexwon' ,  p.NAME , p.expr )
        
    @_('NAME "=" NAME "." FASTTRACK "(" STRING ")"')
    def statement( self , p ) :
        return ( 'strindex' ,  p.NAME0 , p.NAME1 , p.STRING )
        
    @_('NAME "." FASTTRACK "(" STRING ")"')
    def statement( self , p ) :
        return ( 'strindexwon' ,  p.NAME , p.STRING )
        
    @_('NAME "=" NAME "." WAYBIG "(" ")"')
    def statement( self , p ) :
        return ( 'upper' , p.NAME0 , p.NAME1 )
        
    @_('NAME "." WAYBIG "(" ")"')
    def statement( self , p ) :
        return ( 'upperwon' , p.NAME )
        
    @_('STRING "." WAYBIG "(" ")"')
    def statement( self , p ) :
        return ( 'strupper' , p.STRING )
        
    #--------------------------------------
        
    @_('NAME "=" NAME "." NANOMECH "(" ")"')
    def statement( self , p ) :
        return ( 'lower' , p.NAME0 , p.NAME1 )
        
    @_('NAME "." NANOMECH "(" ")"')
    def statement( self , p ) :
        return ( 'lowerwon' , p.NAME )
        
    @_('STRING "." NANOMECH "(" ")"')
    def statement( self , p ) :
        return ( 'strlower' , p.STRING )
        
    #===================================================
    
    @_('NAME "=" NAME "." ISWAYBIG "(" ")"')
    def statement( self , p ) :
        return ( 'isupper' , p.NAME0 , p.NAME1 ) 
        
    @_('NAME "." ISWAYBIG "(" ")"')
    def statement( self , p ) :
        return ( 'isupperwon' , p.NAME )
        
    @_('STRING "." ISWAYBIG "(" ")"')
    def statement( self , p ) :
        return ( 'strisupper' , p.STRING )
        
    #--------------------------------------------
    
    @_('NAME "=" NAME "." ISNANOMECH "(" ")"')
    def statement( self , p ) :
        return ( 'islower' , p.NAME0 , p.NAME1 )
        
    @_('NAME "." ISNANOMECH "(" ")"')
    def statement( self , p ) :
        return ( 'islowerwon' , p.NAME )
        
    @_('STRING "." ISNANOMECH "(" ")"')
    def statement( self , p ) :
        return ( 'strislower' , p.STRING )
        
    #------------------------------------------------
    
    @_('BRAINSTORM "." READ "(" NAME ")"')
    def statement( self , p ) :
        return ( 'listadd' , p.NAME )
        
    @_('BRAINSTORM "." WRITE "(" NAME IN NAME ")"')
    def statement( self , p ) :
        return ( 'listwrite' , p.NAME0 , p.NAME1 )
        
    @_('BRAINSTORM "." WRITE "(" NAME ")"')
    def statement( self , p ) :
        return ( 'listwrite1' , p.NAME )
        
    @_('BRAINSTORM "." STORE "(" NAME ")"')
    def statement( self , p ) :
        return ( 'listadd' , p.NAME )
        
    @_('BRAINSTORM "." GET "(" ")"')
    def statement( self , p ) :
        return ( 'list' , 1 )
        
    #-----------------------------------------------------
    
    @_('JETRAY "(" NAME ")"')
    def statement( self , p ) :
        return ( 'jetray' , p.NAME )
        
    #WEB_SEARCH ------------------------------------------
    
    @_('PRINT "(" "@" WEB_SEARCH STRING ")"')
    def statement( self , p ) :
        return ( 'web_search' , p.STRING )
        
    #AI --------------------------------------------------
    
    @_('PRINT "(" "@" AI STRING ")"')
    def statement( self , p ) :
        return ( 'ai_search' , p.STRING )
        
    # ----------------------------------------------------
    
    @_('BREAK')
    def statement( self , p ) :
        return ('break' , 1 )
        
    
        
        
#MAIN =========================================================================================================================


if __name__ == '__main__':
    print("NAME : " , __name__ )
    print("MAIN : " , '__main__' )
    print("\n")
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('basic > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
            
            
            
