#Ledger payments
ldg_pmt1=1000;
ldg_pmt2=2000;
ldg_pmt3=4000;
print("Ledger payments:",ldg_pmt1,ldg_pmt2,ldg_pmt3);

#Statement Payments
stmt_pmt1=2000;
stmt_pmt2=3000;
stmt_pmt3=1000;
print("Statement payments:",stmt_pmt1,stmt_pmt2,stmt_pmt3);

#Ledger total
ldg_tot=ldg_pmt1+ldg_pmt2+ldg_pmt3;
print("Sum of ledger payments is:",ldg_tot);

#Statement total
stmt_tot=stmt_pmt1+stmt_pmt2+stmt_pmt3;
print("Sum of statemet payments is:",stmt_tot)

#Proofing by comparison
if ldg_tot == stmt_tot:
    print("Payments reconciled, ledger and statement totals match")
elif ldg_tot > stmt_tot:
    print("Not reconciled, Ledger shows excess by: ",ldg_tot-stmt_tot)
else:
    print("Not reconciled, Statement shows excess by: ",stmt_tot-ldg_tot)
