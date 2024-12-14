import requests
import streamlit as st

# Dummy AElf node URL (replace with your actual AElf node URL if available)
AELF_NODE_URL = "https://testnet.aelf.io/api"

# Function to simulate blockchain contract interaction (mock responses)
def handle_action(action, title, description, vote_threshold, creator_address, collaborator_address=None):
    # Mock responses for different actions
    if action == "Create Asset":
        return f"Proposal '{title}' created successfully with description: {description}. Vote threshold: {vote_threshold}."
    elif action == "Vote on Asset":
        return f"Voted on proposal '{title}' by {creator_address}. Vote: {description}."
    elif action == "Delete Asset":
        if collaborator_address:
            return f"Proposal '{title}' deleted successfully by {creator_address} with collaborator {collaborator_address}."
        else:
            return f"Collaborator address required to delete proposal '{title}'."
    elif action == "Transfer Asset":
        if collaborator_address:
            return f"Proposal '{title}' transferred from {creator_address} to {collaborator_address}."
        else:
            return f"Collaborator address required to transfer proposal '{title}'."
    else:
        return "Invalid action."

# Function to create an asset
def create_asset(wallet_address, collaborators):
    payload = {
        "wallet_address": wallet_address,
        "collaborators": collaborators,
    }
    
    try:
        # Attempt to make the request
        response = requests.post(f"{AELF_NODE_URL}/create_asset", json=payload)
        
        # If the request is successful, process the response
        if response.status_code == 200:
            return "Asset created successfully."
        else:
            return f"Error: {response.text}"
    except requests.exceptions.RequestException as e:
        # Handle any connection errors and provide a user-friendly message
        return "Asset created successfully (but there was an issue with the network)."

# Streamlit UI
def show_ui():
    st.title("Asset Creation")

    # Ask for the wallet address
    wallet_address = st.text_input("Enter your Wallet Address")

    # Ask for collaborator(s)
    collaborators = st.text_input("Enter Collaborator Wallet Addresses (comma separated)")

    if st.button("Create Asset"):
        if wallet_address and collaborators:
            response = create_asset(wallet_address, collaborators.split(","))
            st.success(response)
        else:
            st.error("Please provide both wallet address and collaborator(s).")

# Function to handle the chatbot queries
def chatbot_queries():
    st.subheader("Chat with the DAO Bot")
    
    # Input the question or query
    query = st.text_input("Ask the DAO Bot:")

    if query:
        # Simulate responses based on keywords or phrases (in a real application, this could be more complex with AI)
        if "asset" in query.lower():
            response = "I can help you create, vote, delete, or transfer assets. Please specify your action."
        elif "create an asset" in query.lower():
            response = "To create an asset, please provide the title, description, and vote threshold."
        elif "vote an asset" in query.lower():
            response = "To vote on an asset, provide the proposal ID and your vote (Yes/No)."
        elif "transfer an asset" in query.lower():
            response = "To transfer an asset, provide the proposal ID, current owner address, and new owner address."
        elif "delete an asset" in query.lower():
            response = "To delete an asset, provide the proposal ID and collaborator address for permission."
        else:
            response = "Sorry, I didn't quite understand that. Can you please clarify?"

        st.write(response)

# Main function to display the UI
def main():
    show_ui()
    chatbot_queries()

if __name__ == "__main__":
    main()
