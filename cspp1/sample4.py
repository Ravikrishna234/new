varA=123
varB="hello"
if type(varA)==str or type(varB)==str:
    print("string is involved")
elif varA>varB:
    print("bigger")
elif varA<varB:
    print("smaller")
else:
    print("equal")
