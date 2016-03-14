
def get_expression_string(given_number, cur_state, exp):

    if(cur_state > given_number):
        return (False, '')
    elif(cur_state == given_number):
        return (True, exp)

    (res_mult_3, exp1) = get_expression_string(given_number, cur_state*3, '( ' + exp + '* 3 )')
    if(res_mult_3):
        return (True, exp1)

    (res_add_5, exp2) = get_expression_string(given_number, cur_state + 5, '( ' + exp + '+ 5 )')
    if(res_add_5):
        return (True, exp2)

    return (False, '')



# num = 13
(res_state, res_exp) = get_expression_string(102, 1, '1')

if(res_state):
    print res_exp
else:
    print "Not possible"
