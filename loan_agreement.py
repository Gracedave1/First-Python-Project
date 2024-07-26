# LOAN AGREEMENT PROJECT

def title_case_name():
    first_name = input("Please enter your first name: ").title()
    last_name = input("Please enter your last name: ").title()
    return first_name, last_name
first_name, last_name = title_case_name()

bank_name = input("Please enter the bank name: ")
bank_name_upper_case = bank_name.upper()
principal = float(input("Please enter the amount of money loaned: "))
rate = float(input("Please, enter the rate: "))
time = int(input("Please, enter the duration: "))
interest = principal * rate * time / 100

loan_agreement =  (
    f"I, {first_name} {last_name}, hereby agree to accept the loan of ₦{principal} for the period of {time} years \n"
     f"at a rate of {rate}% from {bank_name_upper_case} Ltd. \n" 
     f"\n" 
     f"I, oblige of my own free will to comply with all the CBN rules and regulations guiding loan contracts \n" 
     f"and will not hold the lending party, {bank_name_upper_case} Ltd responsible for confiscating all designated \n"
     f"collateral should I not pay the requisite return of ₦{interest} at the end of the loaning term."
     )
print(loan_agreement)
message_sender = f"Signed: {first_name} { last_name}"
print(message_sender)