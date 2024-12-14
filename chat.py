import streamlit as st
import requests

# Hardcoded wallet address and password for authentication (for demo purposes)
auth_wallet_address = "sfhPfB3Dd1G8RdJjsaQx1G6zicQXHE6psDmJtLfJAiHzrNcea"
auth_password = "$@K$#!@two504"

# Function to authenticate the user
def authenticate_user(wallet_address, password):
    if wallet_address == auth_wallet_address and password == auth_password:
        return True
    return False

# Function to simulate asset creation (no real AElf interaction)
def create_asset(wallet_address, collaborators):
    # Simulate asset creation by returning a success message
    return {"message": f"Asset created by {wallet_address} with collaborators: {', '.join(collaborators) if collaborators else 'None'}"}

# Function to simulate asset update (no real AElf interaction)
def update_asset(wallet_address, proposal_id, vote):
    # Simulate asset update action
    return {"message": f"Voted on proposal {proposal_id} by {wallet_address}. Vote: {'Yes' if vote else 'No'}"}

# Function to simulate asset deletion (no real AElf interaction)
def delete_asset(wallet_address, proposal_id, vote):
    # Simulate asset deletion action
    return {"message": f"Voted to delete proposal {proposal_id} by {wallet_address}. Vote: {'Yes' if vote else 'No'}"}

# Function to simulate asset transfer (no real AElf interaction)
def transfer_asset(wallet_address, recipient_address, asset_id):
    # Simulate asset transfer action
    return {"message": f"Asset {asset_id} transferred from {wallet_address} to {recipient_address}"}

# Streamlit UI
st.title("Builders DAO Chatbot")

# Step 1: Wallet Authentication
st.subheader("Step 1: Authenticate")
wallet_address = st.text_input("Enter your wallet address:")
wallet_password = st.text_input("Enter your wallet password:", type="password")

if st.button("Authenticate"):
    if authenticate_user(wallet_address, wallet_password):
        st.success("Authentication successful!")
        st.session_state.authenticated = True
    else:
        st.error("Invalid wallet address or password.")
        st.session_state.authenticated = False

# Step 2: Display options for actions (only if authenticated)
if "authenticated" in st.session_state and st.session_state.authenticated:
    action = st.selectbox("Choose an action:", ["Create Asset", "Update Asset", "Delete Asset", "Transfer Asset"])

    if action == "Create Asset":
        st.subheader("Create Asset")

        # Step 3: Collaborator input for asset creation
        collaborators = []
        collaborator_address = st.text_input("Enter collaborator wallet address (leave empty for no collaborator):")
        if collaborator_address:
            collaborators.append(collaborator_address)

        # Step 4: Upload file (if needed)
        uploaded_file = st.file_uploader("Upload a file for the asset", type=["jpg", "png", "pdf", "txt", "docx"])
        if uploaded_file:
            st.write(f"File '{uploaded_file.name}' uploaded successfully!")

        if st.button("Create Asset"):
            response = create_asset(wallet_address, collaborators)
            st.write(response["message"])

    elif action == "Update Asset":
        st.subheader("Update Asset")

        proposal_id = st.text_input("Enter proposal ID to update:")
        vote = st.radio("Vote on proposal:", ["Yes", "No"])

        if st.button("Vote on Update"):
            response = update_asset(wallet_address, proposal_id, vote == "Yes")
            st.write(response["message"])

    elif action == "Delete Asset":
        st.subheader("Delete Asset")

        proposal_id = st.text_input("Enter proposal ID to delete:")
        vote = st.radio("Vote on proposal:", ["Yes", "No"])

        if st.button("Vote on Deletion"):
            response = delete_asset(wallet_address, proposal_id, vote == "Yes")
            st.write(response["message"])

    elif action == "Transfer Asset":
        st.subheader("Transfer Asset")

        recipient_address = st.text_input("Enter recipient wallet address:")
        asset_id = st.text_input("Enter asset ID:")

        if st.button("Transfer Asset"):
            response = transfer_asset(wallet_address, recipient_address, asset_id)
            st.write(response["message"])

else:
    st.info("Please authenticate to proceed with the actions.")

# Chatbot Section for general queries
st.subheader("Chat with DAO Bot")

# Input the question or query
query = st.text_input("Ask the DAO Bot:")

if query:
    # Simulate responses based on keywords or phrases (in a real application, this could be more complex with AI)
    if "create an asset" in query.lower():
        collaborators = []
        collaborator_address = st.text_input("Enter collaborator wallet address (leave empty for no collaborator):")
        if collaborator_address:
            collaborators.append(collaborator_address)

        uploaded_file = st.file_uploader("Upload a file for the asset", type=["jpg", "png", "pdf", "txt", "docx"])
        if uploaded_file:
            st.write(f"File '{uploaded_file.name}' uploaded successfully!")

        if st.button("Create Asset"):
            response = create_asset(wallet_address, collaborators)
            st.write(response["message"])

    elif "update an asset" in query.lower():
        proposal_id = st.text_input("Enter proposal ID to update:")
        vote = st.radio("Vote on proposal:", ["Yes", "No"])

        if st.button("Vote on Update"):
            response = update_asset(wallet_address, proposal_id, vote == "Yes")
            st.write(response["message"])

    elif "delete an asset" in query.lower():
        proposal_id = st.text_input("Enter proposal ID to delete:")
        vote = st.radio("Vote on proposal:", ["Yes", "No"])

        if st.button("Vote on Deletion"):
            response = delete_asset(wallet_address, proposal_id, vote == "Yes")
            st.write(response["message"])

    elif "transfer an asset" in query.lower():
        recipient_address = st.text_input("Enter recipient wallet address:")
        asset_id = st.text_input("Enter asset ID:")

        if st.button("Transfer Asset"):
            response = transfer_asset(wallet_address, recipient_address, asset_id)
            st.write(response["message"])

    else:
        st.write("Sorry, I didn't quite understand that. Can you please clarify?")
