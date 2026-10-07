def player(prev_play, opponent_history=[], play_order={}):
    # Reset history when starting a new match against a new bot
    if prev_play == "":
        opponent_history.clear()
        play_order.clear()

    # Store opponent's last move
    opponent_history.append(prev_play)

    # Default move for initial rounds
    guess = "R"

    # Pattern length to track (N-gram size)
    n = 4

    # We need at least n + 1 moves to record a full pattern -> next move transition
    if len(opponent_history) > n:
        # Get the previous n-length pattern and the move that followed it
        prev_pattern = "".join(opponent_history[-(n + 1) : -1])
        last_move = opponent_history[-1]

        # Update pattern frequency count
        if prev_pattern not in play_order:
            play_order[prev_pattern] = {"R": 0, "P": 0, "S": 0}
        play_order[prev_pattern][last_move] += 1

        # Current n-length pattern to find predictions for
        current_pattern = "".join(opponent_history[-n:])

        # Predict opponent's next move based on current pattern history
        if current_pattern in play_order:
            predict_counts = play_order[current_pattern]
            predicted_move = max(predict_counts, key=predict_counts.get)
        else:
            predicted_move = "R"

        # Play counter-move (R beats S, P beats R, S beats P)
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[predicted_move]

    return guess