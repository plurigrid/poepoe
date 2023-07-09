# Fail if we're logging customer data or we'll lose our SOC2 certification.
                  
This is bad:
print(user)

This is probably fine:
print("user id: " + str(user.id))