from hw05_task01 import *

"""
Test functions (defined in hw05_task01):

table_from_string(S)
pretty_print(M)
row_average(M,r_idx)
smallest_1(M, c_idx)
smallest_all(M)
insert_row(M, r_idx)
insert_column_zero(M, c_idx)
insert_column_data_modify(M, c_idx, new_column)
insert_column_data_return(M, c_idx, new_column)
"""

def print_header(fct_name):
    message = "\n\n--------------  TEST: " + fct_name + " -------------\n"
    print(message)

    
def get_M_list():
    """ Returns a list of nested lists."""
    
    M_all =[ [[0.84,0.76,0.42,0.26], [0.51,0.40,0.78,0.30]],
         [[0.48,0.58,0.91],[0.50,0.28,0.76],[0.62,0.25,0.91]],
         [[0.84,0.76,0.42,0.26]],
         [[0.84],[0.76],[0.42],[0.26]],
         [[]]]
    return M_all


def pretty_print_test():
    print_header ("pretty_print")
    
    M = [[0.3101475693193326, 0.7298317482601286, 0.8988382879679935, 0.6839839319154413, 0.47214271545271336],
         [0.1007012080683658, 0.4341718354537837, 0.6108869734438016, 0.9130110532378982, 0.9666063677707588],
         [0.47700977655271704, 0.8653099277716401, 0.2604923103919594, 0.8050278270130223, 0.5486993038355893],
         [0.014041700164018955, 0.7197046864039541, 0.39882354222426875, 0.824844977148233, 0.6681532012318508],
         [0.0011428193144282783, 0.49357786646532464, 0.8676027754927809, 0.24391087688713198, 0.32520436274739006],
         [0.8704712321086546, 0.19106709150239054, 0.5675107406206719, 0.23861592861522019, 0.9675402502901433],
         [0.80317946927987, 0.44796957143557037, 0.08044581855253541, 0.32005460467254576, 0.5079406425205739]]
    S = """--------------------------------------------------------- 
|     |       0 |       1 |       2 |       3 |       4 |  
---------------------------------------------------------   
|   0 |    0.31 |    0.73 |    0.90 |    0.68 |    0.47 |
|   1 |    0.10 |    0.43 |    0.61 |    0.91 |    0.97 |
|   2 |    0.48 |    0.87 |    0.26 |    0.81 |    0.55 |
|   3 |    0.01 |    0.72 |    0.40 |    0.82 |    0.67 |
|   4 |    0.00 |    0.49 |    0.87 |    0.24 |    0.33 |
|   5 |    0.87 |    0.19 |    0.57 |    0.24 |    0.97 |
|   6 |    0.80 |    0.45 |    0.08 |    0.32 |    0.51 |
---------------------------------------------------------"""
    print("The next 2 tables should be identical.")
    print("EXPECTED:")
    print(S)
    print("GOT:")
    pretty_print(M)


    
def table_from_string_test():
    """ Tests the table_from_string function.

    tests:
    - output type: nested of floats, check by equality (==)
    - different matrix sizes
    - bad input string    
    """

    print_header ("table_from_string")

    S_all = ["0.84 0.76 0.42 0.26;0.51 0.40 0.78 0.30", 
             '0.48 0.58 0.91;0.50 0.28 0.76;0.62 0.25 0.91',
             "0.84 0.76 0.42 0.26",
             "0.84;0.76;0.42;0.26",
             '9.2 3.4;1 2 3;4 5 6']

    M_all =[ [[0.84,0.76,0.42,0.26], [0.51,0.40,0.78,0.30]],
             [[0.48,0.58,0.91],[0.50,0.28,0.76],[0.62,0.25,0.91]],
             [[0.84,0.76,0.42,0.26]],
             [[0.84],[0.76],[0.42],[0.26]],
             [[]]]

    if len(S_all) != len(M_all):
        print("table_from_string_test: Can not perform the tests: str != matrices")

    passed = 0
    i = 0
    while i < len(S_all):        
        S = S_all[i]
        M_good = M_all[i]
        M = table_from_string(S)
        if M != M_good:
            print("table_from_string_test: Failed test", i+1)
            print("expected:", M_good)
            print("got:", M)
        else:
            passed += 1
        i = i + 1

    print("table_from_string_test: PASSED:", passed, "out of:", len(S_all))
    
    
def test_general(command_list, fct_name = ""):
    """ Generic test function.

    Tests function fct_name, using data, commands, and expected relusts from command_list.
    command_list is a list where each item is another list with the data needed to run one test:
    - data string
    - command string (calls teh desired function, MUST use name M for the nested list.
    - expected result
    Example of one item in the command_list:
    ["[[1,2,3],[1,2],[1,2,3]]","smallest_1(M,1)", -1]
    """
          
    if len(command_list) == 0:
        print("\n No tests to run.")
        return 0

    # get the function name and print it
    if fct_name == "":
        temp_str = command_list[0][1]
        idx = temp_str.find('(')
        print_header(temp_str[0:idx])


    passed = 0
    i = 0
    while i < len(command_list):
        init_data = command_list[i][0]
        command = command_list[i][1]
        exp_res = command_list[i][2]
        if len(init_data) != 0:
            #print(init_data)
            M = eval(init_data)  #reinitialize M
        comp_res = eval(command)  #evaluate the command instruction
        if exp_res != comp_res:
             print("Failed: ")
             print("Expected: ", exp_res)
             print("Got:", comp_res)
        else:
            #print("Passed")
            passed += 1
        i = i + 1
        
    total = len(command_list)
    print("Passed:", passed, "out of", total)
    return [passed,total]

def test_general_modify(command_list, fct_name = ""):
    """ Generic test function.

    Same as test_general, but used for testing functions that modify M.

    Tests function fct_name, using data, commands, and expected relusts from command_list.
    command_list is a list where each item is another list with the data needed to run one test:
    - data string
    - command string (calls teh desired function, MUST use name M for the nested list.
    - expected result
    Example of one item in the command_list:
    ["[[1,2,3],[1,2],[1,2,3]]","smallest_1(M,1)", -1]
    """
    
#    print_header(fct_name)    
    if len(command_list) == 0:
        print("\n No tests to run.")
        return 0

    # get the function name and print it
    if fct_name == "":
        temp_str = command_list[0][1]
        idx = temp_str.find('(')
        print_header(temp_str[0:idx])

    
    passed = 0
    i = 0
    while i < len(command_list):
        init_data = command_list[i][0]
        command = command_list[i][1]
        exp_res = command_list[i][2]
        if len(init_data) != 0:
            #print(init_data)
            M = eval(init_data)  #reinitialize M        
        eval(command)  #evaluate the command instruction        
        if exp_res != M:  # DIFFERENCE: compare with M not with comp_res
             print("Failed: ")
             print("Expected: ", exp_res)
             print("Got:", M)
        else:
            #print("Passed")
            passed += 1
        i = i + 1
        
    total = len(command_list)
    print("Passed:", passed, "out of", total)
    return [passed,total]


def main():
    
    table_from_string_test()

    pretty_print_test()
    
    # row_average
    command_list = [["get_M_list()[0]","row_average(M, 1)", 0.4975]]    
    test_general(command_list)


    # smallest_1 
    command_list = [[" [[3,1,6,8], [5, 9, 4, 2], [7, 5, 0, 5]]", "smallest_1(M, 0)", -1],
                    ["",     "smallest_1(M,1)", 1],
                    ["[[]]", "smallest_1(M,0)", -1],
                    ["[]",   "smallest_1(M,1)", -1],
                    ["[[9999999999999999999999,6],[9999999999999999999900,-3],[9999999999999999999990,2]]","smallest_1(M,0)", 9999999999999999999900],
                    ["[[1,2,3],[1,2],[1,2,3]]", "smallest_1(M,1)", -1]
                    ]            
    test_general(command_list)


    # smallest_
    command_list = [[" [[3,1,6,8], [5, 9, 4, 2], [7, 5, 0, 5]]","smallest_all(M)", [-1, 1, 0, 5]]]
    test_general(command_list)

    # insert_row
    command_list = [[" [[3,1], [5, 9], [7, 5]]", "insert_row(M,1)", [[3,1], [0,0], [5,9], [7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_row(M,0)", [[0,0], [3,1], [5,9], [7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_row(M,3)", [[3,1], [5,9], [7,5], [0,0]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_row(M,7)", [[3,1], [5,9], [7,5], [0,0]]],
                    [" [[]]", "insert_row(M,0)", [[],[]] ],
                    [" []", "insert_row(M,0)", [] ],
                    ]
    test_general_modify(command_list)

    # insert_column_zero
    command_list = [[" [[3,1], [5, 9], [7, 5]]", "insert_column_zero(M,1)", [[3,0,1], [5,0,9], [7,0,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_zero(M,0)", [[0,3,1], [0,5,9], [0,7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_zero(M,4)", [[3,1,0], [5,9,0], [7,5,0]]],
                    [" [[]]", "insert_column_zero(M,0)", [[0]] ],
                    [" []", "insert_column_zero(M,0)", [] ],
                    ]
    test_general_modify(command_list)

    # insert_column_data_modify
    command_list = [[" [[3,1], [5, 9], [7, 5]]", "insert_column_data_modify(M,1,[15,89, -3.5])", [[3,15,1], [5,89,9], [7,-3.5,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_modify(M,0,[6,1,90])", [[6,3,1], [1,5,9], [90,7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_modify(M,4,[90,40,80])", [[3,1,90], [5,9,40], [7,5,80]]],
                    [" [[]]", "insert_column_data_modify(M,0,[4.4])", [[4.4]] ],
                    [" []", "insert_column_data_modify(M,0,[])", [] ],
                    [" []", "insert_column_data_modify(M,0,[9])", [] ],  # should not be able to insert for this test and for those below
                    [" [[]]", "insert_column_data_modify(M,0,[4.4, 5])", [[]] ], 
                    [" [[]]", "insert_column_data_modify(M,0,[])", [[]] ],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_modify(M,1,[15,89])", [[3,1], [5,9], [7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_modify(M,1,[1,2,3,4])", [[3,1], [5,9], [7,5]]],
                    ]
    test_general_modify(command_list)    

    # insert_column_data_return
    command_list = [[" [[3,1], [5, 9], [7, 5]]", "insert_column_data_return(M,1,[15,89, -3.5])", [[3,15,1], [5,89,9], [7,-3.5,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_return(M,0,[6,1,90])", [[6,3,1], [1,5,9], [90,7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_return(M,4,[90,40,80])", [[3,1,90], [5,9,40], [7,5,80]]],
                    [" [[]]", "insert_column_data_return(M,0,[4.4])", [[4.4]] ],
                    [" []", "insert_column_data_return(M,0,[])", [] ],
                    [" []", "insert_column_data_return(M,0,[9])", [] ],  # should not be able to add
                    [" [[]]", "insert_column_data_return(M,0,[4.4, 5])", [[]] ],
                    [" [[]]", "insert_column_data_return(M,0,[])", [[]] ],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_return(M,1,[15,89])", [[3,1], [5,9], [7,5]]],
                    [" [[3,1], [5, 9], [7, 5]]", "insert_column_data_return(M,1,[1,2,3,4])", [[3,1], [5,9], [7,5]]],
                    ]
    test_general(command_list)    

main()
