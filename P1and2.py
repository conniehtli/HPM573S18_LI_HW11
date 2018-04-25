import math as math
#_________________________Problem 1_________________________

print("__Problem 1__")
print("Part 1")
print("Annual mortality = ", -(math.log(1-(18/1000))))
print("Stroke mortality = ", -(math.log(1-(36.2/100000))))
print("Background mortality = ", 0.01816-0.00036)
print("")

print("Part 2")
print("Annual rate of first stroke = ", -(math.log(1-(15/1000))))
print("")

print("Part 3")
print("Annual rate of transition from 'Well' to 'Stroke' = ", -(math.log(1-(15/1000)))*0.9)
print("Annual rate of transition from 'Well' to 'Stroke Death' = ", -(math.log(1-(15/1000)))*0.1)
print("")

print("Part 4")
print("Annual rate of recurrent stroke  = ", (-(math.log(1-(17/100))))/5)
print("")

print("Part 5")
print("Annual rate of transition from 'Post-Stroke' to 'Stroke'  = ", 0.0372659*0.8)
print("Annual rate of transition from 'Post-Stroke' to 'Stroke Death'  = ", 0.0372659*0.2)
print("")

print("Part 6")
print("Annual rate of transition from 'Stroke' to 'Post-Stroke'  = ", 52)
print("")

print("__Problem 2__")
NO_Rate_Matrix = [# NO TREATMENT
[0,     0.0136,    0,   0.00151], # Well
[0,     0,         52,  0.00745], # Stroke
[0,     0.0298,    0,   0.00745], # Post-Stroke
[0,     0,         0,   0      ], # Stroke Death
]

AG_Rate_Matrix = [# ANTICOAGULANT
[0,     0.0136,    0,   0.00159], # Well
[0,     0,         52,  0.00745], # Stroke
[0,     0.0223,    0,   0.00782], # Post-Stroke
[0,     0,         0,   0      ], # Stroke Death
]

print(NO_Rate_Matrix, AG_Rate_Matrix)
