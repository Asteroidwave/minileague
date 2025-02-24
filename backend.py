import streamlit as st

# Define players and starting balances
players = {"Hans": 0, "Rich": 0, "MAlls": 0}
tracks = ["PARX", "TP", "DD", "GP", "PENN", "AQU", "SA", "LRL", "OP"]


def update_balances(winner, selected_tracks):
    """Update balances based on race results."""
    entry_fee = 40
    total_pool = 120  # Three players contribute $40 each
    profit = total_pool - entry_fee  # Winner takes home $80 per track

    for track in selected_tracks:
        for player in players:
            if player == winner:
                players[player] += profit
            else:
                players[player] -= entry_fee


def main():
    st.title("Fantasy Horse Racing Tracker")
    st.subheader("Enter Daily Race Results")

    selected_tracks = st.multiselect("Select Tracks Raced Today:", tracks)

    if selected_tracks:
        winner = st.selectbox("Select the Winner:", ["Hans", "Rich", "Ralls"])

        if st.button("Submit Results"):
            update_balances(winner, selected_tracks)
            st.success(f"Updated balances! {winner} won at {', '.join(selected_tracks)}")

    st.subheader("Current Balances")
    for player, balance in players.items():
        st.write(f"{player}: ${balance}")

    st.subheader("Performance Stats")
    total_wins = {player: sum([1 for bal in players.values() if bal > 0]) for player in players}
    for player, wins in total_wins.items():
        st.write(f"{player} Wins: {wins}")


if __name__ == "__main__":
    main()
