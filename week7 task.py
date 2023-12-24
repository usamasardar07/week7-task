#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Charity:
    def __init__(self, name, total):
        self.name = name
        self.total = total

def display_charities(charities):
    print(f"{'Charity Number':<25}{'Charity Name':<25}")
    for i, charity in enumerate(charities, 1):
        print(f"{i:<25}{charity.name:<25}")

def display_totals(charities):
    print("\nCharity Totals (Descending Order):\n")
    print(f"{'Charity Name':<25}{'Total Donated':<25}")
    sorted_charities = sorted(charities, key=lambda x: x.total, reverse=True)
    for charity in sorted_charities:
        print(f"{charity.name:<25}${charity.total:<25}")

def main():
    charities = [Charity("Charity 1", 0.0), Charity("Charity 2", 0.0), Charity("Charity 3", 0.0)]
    grand_total = 0.0

    print("Welcome to the Charity Donation System!\n")

    # TASK 1: Set up the donation system
    for charity in charities:
        charity.name = input(f"Enter the name of {charity.name}: ")

    # TASK 2 and TASK 3: Record and total each donation and Show the totals so far
    while True:
        print("\n")
        display_charities(charities)

        choice = int(input("\nEnter your choice (1, 2, 3) or -1 to show totals: "))

        if choice == -1:
            print("\n")
            display_totals(charities)

            grand_total = sum(charity.total for charity in charities)
            donation_from_total = 0.01 * grand_total

            print(f"\nGRAND TOTAL DONATED TO CHARITIES: ${grand_total}")
            print(f"Your donation also contributes to the grand total. From the total amount, ${donation_from_total} will be donated to all charities collectively.\n")

            break

        if choice < 1 or choice > 3:
            print("Invalid choice. Please choose 1, 2, 3, or -1 to show totals.")
            continue

        shopping_bill = float(input("Enter your shopping bill amount: $"))
        donation = 0.01 * shopping_bill

        charities[choice - 1].total += donation

        print(f"\nThank you for your donation of ${donation} to {charities[choice - 1].name}.")

if __name__ == "__main__":
    main()


# In[ ]:




