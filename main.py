import simulation
total = int(input("How many participants should be there : "))
selects = int(input("How many participants should be selected : "))
luck = int(input("What is the max percentage of luck one can have : "))

x = simulation.run(luck_percentage_max=luck,total_participants=total,selects=selects)
print(f"""
Out of the {total} participants,
only {x[2]} would be selected if luck didnt play a role
although luck was only {luck} percent of the total score
{((x[2]/selects)*100)}% of the participants were selected becuase they were lucky """)
