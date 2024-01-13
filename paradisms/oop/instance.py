# Define a class named 'Payslip'
class Payslip:
    # Constructor method to initialize instance variables
    def __init__(self, name, payment_status, amount) -> None:
        self.name = name
        self.payment_status = payment_status
        self.amount = amount
    
    # Method to update the payment status to "yes"
    def mark_as_paid(self):
        """Mark the payslip as paid."""
        self.payment_status = "yes"
    
    # Method to update the payment status to "no"
    def mark_as_unpaid(self):
        """Mark the payslip as unpaid."""
        self.payment_status = "no"
    
    # Method to get the payment status
    def get_payment_status(self):
        """Get the payment status of the payslip."""
        return self.payment_status
    
    # Method to calculate the total payment including any bonuses
    def calculate_total_payment(self, bonus=0):
        """Calculate the total payment, including any bonuses."""
        total_payment = self.amount + bonus
        return total_payment
    
    # Method to display the payslip information
    def display_payslip_info(self):
        """Display information about the payslip."""
        return f"{self.name}'s payslip - Amount: ${self.amount}, Payment Status: {self.payment_status}"

# Create instances of the 'Payslip' class
nathan = Payslip("Nathan", "no", 1000)
roger = Payslip("Roger", "no", 2000)

# Display the initial payslip information
print("Initial Payslip Information:")
print(nathan.display_payslip_info())
print(roger.display_payslip_info())

# Update the payment status for 'Nathan' instance
nathan.mark_as_paid()

# Display payslip information after updating for 'Nathan' instance
print("\nAfter Payment for Nathan:")
print(nathan.display_payslip_info())
print(roger.display_payslip_info())

# Calculate total payment for 'Roger' with a bonus
roger_bonus = 500
total_payment_roger = roger.calculate_total_payment(bonus=roger_bonus)
print(f"\nTotal payment for Roger (with bonus): ${total_payment_roger}")
