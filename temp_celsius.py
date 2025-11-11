import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp=sys.argv[1]
else:
    script_name = sys.argv[0]
    temp=25
    print("Input not provided. Using default temperature.")

print("Script Name:", script_name)
print("Temperature:", temp,"*C")

if int(temp) > 30:
    print("Hot")
elif int(temp)<=30 and int(temp)>=15:
    print("Normal")
else:
    print("Cold")
