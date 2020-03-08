import module_mycalc_1,module_mycalc_2

op1, op2 =2, 3

result = module_mycalc_1.plus(op1,op2)
print("plus({0}, {1}) => {2}".format(op1,op2,result))

result = module_mycalc_1.minus(op1,op2)
print("minus({0}, {1}) => {2}".format(op1,op2,result))

result = module_mycalc_2.multiply(op1,op2)
print("multiply({0}, {1}) => {2}".format(op1,op2,result))

result = module_mycalc_2.divide(op1,op2)
print("divide({0}, {1}) => {2}".format(op1,op2,result))
print("divide({0}, {1}) => {2:.2}".format(op1,op2,result))


