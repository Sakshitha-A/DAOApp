import streamlit as st

# Correct wallet password and wallet address
CORRECT_PASSWORD = "$@K$#!@two504"
WALLET_ADDRESS = "sfhPfB3Dd1G8RdJjsaQx1G6zicQXHE6psDmJtLfJAiHzrNcea"
CONTRACT_ADDRESS = "2Z6mvXDLVuRzSEFUXwraF9zE3wUkEbJ42SQGmFrPbNQViDFw4e"  # Example contract address

# Function to simulate blockchain contract interaction (mock responses)
def handle_action(action, title, description, vote_threshold, creator_address, collaborator_address=None, vote=None):
    # Mock responses for different actions
    if action == "Create Asset":
        return f"Proposal '{title}' created successfully with description: {description}. Vote threshold: {vote_threshold}."
    elif action == "Vote on Asset":
        return f"Voted on proposal '{title}' by {creator_address}. Vote: {vote}."
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

# Streamlit UI for the chatbot interface
def show_ui():
    st.title("Asset Chatbot")

    # Ask the user for the wallet address first
    wallet_address = st.text_input("Enter your Wallet Address", value=WALLET_ADDRESS)

    # If the wallet address is entered, proceed to password entry
    if wallet_address:
        # Ask the user for the wallet password
        password = st.text_input("Enter your Wallet Password", type="password")

        if password == CORRECT_PASSWORD:
            # Once the correct password is entered, show the action selection
            st.success("Password correct! You now have access to your assets.")

            # Display the wallet address as disabled (for reference)
            st.text_input("Wallet Address (Locked)", value=wallet_address, disabled=True)

            # Input for action choice (Create, Vote, Delete, Transfer)
            action = st.selectbox("Choose an action:", ["Create Asset", "Vote on Asset", "Delete Asset", "Transfer Asset"])

            # Inputs that might vary based on the action
            title = st.text_input("Title of Asset")
            description = st.text_area("Description of Asset")
            vote_threshold = st.number_input("Vote Threshold", min_value=1, step=1)
            creator_address = wallet_address  # Set the wallet address to the one entered above
            collaborator_address = None
            vote = None

            if action in ["Delete Asset", "Transfer Asset"]:
                # For Delete and Transfer actions, prompt for collaborator address
                collaborator_address = st.text_input("Collaborator Wallet Address (Required for Delete/Transfer)")

            if action == "Vote on Asset":
                # For Vote action, prompt for the vote (Yes/No)
                vote = st.selectbox("Vote on Proposal (Yes/No)", ["Yes", "No"])

            if st.button("Submit Action"):
                # Handle the action
                response = handle_action(action, title, description, vote_threshold, creator_address, collaborator_address, vote)
                st.success(response)

                # Show details in the sidebar for the respective actions
                if action == "Create Asset":
                    with st.sidebar:
                        st.header("Asset Created")
                        st.subheader("Asset Name:")
                        st.write(title)
                        st.subheader("Description:")
                        st.write(description)
                        st.subheader("Vote Threshold:")
                        st.write(vote_threshold)
                        st.subheader("Creator Address:")
                        st.write(creator_address)
                        if collaborator_address:
                            st.subheader("Collaborator Address:")
                            st.write(collaborator_address)

                elif action == "Vote on Asset":
                    with st.sidebar:
                        st.header("Vote on Asset")
                        st.subheader("Asset Name:")
                        st.write(title)
                        st.subheader("Your Vote:")
                        st.write(vote)
                        st.subheader("Creator Address:")
                        st.write(creator_address)

                elif action == "Delete Asset":
                    with st.sidebar:
                        st.header("Asset Deleted")
                        st.subheader("Asset Name:")
                        st.write(title)
                        st.subheader("Collaborator Address:")
                        st.write(collaborator_address)
                        st.subheader("Creator Address:")
                        st.write(creator_address)

                elif action == "Transfer Asset":
                    with st.sidebar:
                        st.header("Asset Transferred")
                        st.subheader("Asset Name:")
                        st.write(title)
                        st.subheader("Collaborator Address:")
                        st.write(collaborator_address)
                        st.subheader("Creator Address:")
                        st.write(creator_address)

        else:
            if password:
                st.error("Incorrect password. Please try again.")

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
