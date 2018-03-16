# Avan .txt file
File = open("temperatures.txt")
Text = File.read()

# Eraldan temperatuurid üksteisest
List_Of_Temperatures = Text.split()

# Muudan kõik temperatuurid floatiks
Float_Temperatures = [float(Temperature) for Temperature in List_Of_Temperatures]

# Arvutamine
Temperatures_Addition = sum(Float_Temperatures)

Temperatures_Lenght = len(Float_Temperatures)

Temperatures_Average = Temperatures_Addition / Temperatures_Lenght

# Lõpptulemus
print(Temperatures_Average)
