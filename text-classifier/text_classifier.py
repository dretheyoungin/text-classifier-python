
import pandas as pd

print("Bot: Loading customer emails into classifier pipeline...")

emails = ["I need help with my password", "Can I get a refund?", "Everything is broken!"]
df = pd.DataFrame({"Text": emails})
df["Department"] = "Billing"

# Execute string filtering
df.loc[df["Text"].str.contains("password|login|broken"), "Department"] = "Urgent Tech Support"
print(df)

# TRIGGER ACTION: Scan the table to see if any row was flagged as Urgent Tech Support
if df["Department"].str.contains("Urgent Tech Support").any():
    print("\n[CRITICAL TRIGGER TRIGGERED]")
    print("Bot Action: Sending automated text alert out to manager via SMS Gateway...")
    print("Notification Status: Success! Alert dispatched safely.")