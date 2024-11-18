Vignesh,Charan=input().split()
if Vignesh==Charan:
    print("NULL")
elif (Vignesh=="R" and Charan=="P") or (Vignesh=="P" and Charan=="S") or (Vignesh=="S" and Charan=="R"):
    print("Charan")
else:
    print("Vignesh")
