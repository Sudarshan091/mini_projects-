total_seats=243

bjp=int(input("enter winned seats by BJP:"))
congress=int(input("enter the winned seats by CONGRESS:"))
jansuraj=int(input("enter the winned seats by JANSURAJ:"))
rjd=int(input("enter the winned seats by RJD:"))
majority= 122
if(bjp>=majority):
    print("PHIR EK BAAR NITISH KUMAR")

elif(congress>=122):
    print("🤚🏼 BADLEGA HALAT ")    
elif(jansuraj>=122):
    print("daaru badnam kardi ")   
elif(rjd>=122):
    print("lagal lagal jhulaniya me dhakka balam kalkatta chali")
else:
    print("tejpratap bhaiya jindabad ")    
