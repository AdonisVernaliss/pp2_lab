def sti2(st):
    st=st.replace("ONE", '1')
    st=st.replace("TWO", '2')
    st=st.replace("THR", '3')
    st=st.replace("FOU", '4')
    st=st.replace("FIV", '5')
    st=st.replace("SIX", '6')
    st=st.replace("SEV", '7')
    st=st.replace("EIG", '8')
    st=st.replace("NIN", '9')
    st=st.replace("ZER", '0')
    return st

def its2(st):
    st=st.replace('1',"ONE")
    st=st.replace('2',"TWO")
    st=st.replace('3',"THR")
    st=st.replace('4',"FOU")
    st=st.replace('5',"FIV")
    st=st.replace('6',"SIX")
    st=st.replace('7',"SEV")
    st=st.replace('8',"EIG")
    st=st.replace('9',"NIN")
    st=st.replace('0',"ZER")
    return st



n = input()
s = ''
r = 0
n=sti2(n)

for i in n:
    if i.isdigit():
        s+=i
    else:
        r=int(s,base = 10)
        s=''
r+=int(s)
n = str(r)

n = its2(n)

print(n)