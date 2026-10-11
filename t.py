print("=" *30) 
print("     AI-BASED HEALTHCARE SYSTEM") 
print("=" *30) 
Name = input("Enter Patient Name: ") 
Age = int(input("Enter Patient Age: ")) 
Symptom = input("Enter Symptom: ").lower() 
print("-" * 20) 
print("Patient Name :", Name) 
print("Patient Age  :", Age) 
print("Main Symptom :", Symptom.title()) 
print("-" * 20) 
# Special advice for children below 5 years 
if Age <=5: 
    rec = "Strict Advice: Please consult a doctor promptly" 
elif "fever" in Symptom: 
    re = "Take adequate rest, drink plenty of water, and monitor your temperature." 
elif "headache" in Symptom: 
    rec = "Stay hydrated, take adequate rest, and consult a doctor if the headache continues." 
elif "cough" in Symptom: 
    rec = "Drink warm fluids, take rest, and consult a  doctor if symptoms become severe." 
elif "stomach" in Symptom: 
    rec = "Eat light food, drink sufficient water, and  consult a doctor if the problem continues." 
elif "cold" in Symptom: 
   rec = "Take rest, drink warm fluids, and consult a doctor if symptoms worsen." 
else: 
   rec = "Please consult a qualified healthcare professional for proper evaluation." 
   print("\nRecommendation:") 
   print(rec) 
print( "=" *30) 
print("Thank you,", Name) 
print("=" * 30) 
