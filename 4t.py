print("Medical Diagnosis System") 
print("Answer with yes or no.\n") 
fever = input("Do you have a fever? ").lower() 
cough = input("Do you have a cough? ").lower() 
sore_throat = input("Do you have a sore throat? ").lower()
body_ache = input("Do you have body Aches? ").lower()
rn_nose = input("Do you have a Running Nose? ").lower()
if fever == "yes" and cough == "yes" and body_ache == "yes": 
    Diagnosis = "Viral infection"
elif cough=="yes" and fever=="yes":
      Diagnosis = "illness"
else: Diagnosis = "Please Provide much detail........."
print("\t\tResult") 
print("Diagnosis:", Diagnosis) 
print("Please consult  for an actual diagnosis.") 