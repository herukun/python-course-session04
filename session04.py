# Condition

user_name="faisal"
password='54442544'

input_username=input('Please enter your name : ').lower()
input_password=input('please enter your password : ')

if input_username == user_name and input_password == password:
    print('Login scsses')
elif input_username == user_name or input_password == password :
     print('username Or password not correct')
else:
    print('ERROR')
#============== Python single if example =========================================

age = 38
if age == 38 : print('age == 38')
#============== Python single if else example ====================================

age = 38
print('age == 38')if age == 38 else print('age != 38')
#============== Useing (in and not in) ============================================
liverpool={"mane":10,"salah":11,"tiago":6}
if "mane" in liverpool:
    print('mane Play for liverpool')
#============================================
if "messi" not in liverpool:
    print('messi player for another Team')
#============ all() and any() Function ============================================
name='faisal'
hight = 175

if all([name=='faisa',hight==175]):
    print('correct name and hight')
elif any([name=='faisa',hight==175]):
    print('one value is Correct')
else:
    print('ERROR')



