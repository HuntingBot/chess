# chess

An attempt at a chess variant engine (now only supports antichess)

Generate moves brute forcely and brute forcely DFS until reaches depth limit, then evaluate. The evaluation function is `(opponent piece count - own piece count) + 0.01 * mobility` (mobility is possible number of moves)

## Classes

### `Position`

Describes a position.

#### Attributes

`board`: Which pieces are on which squares.

`color`: Which side is it to play.

`ep_square`: Which square can be the destination of an en passant capture (if possible). **Currently unused.**

`halfmove_clock`: 50-move rule counter. **Currently unused.**

#### Functions

`to_FEN`: Convert position to Forsyth-Edwards Notation. **Incomplete** (flags missing).

`from_FEN`: Create position from Forsyth-Edwards Notation. **TODO.**

`get_all_moves`: Return a list of all legal moves in the current position.

`evaluate`: Evaluate the current position statically.

`make_move`: Execute a move and return the position after the move.

`search`: A simple Negamax search.

`random_move`: Return a random move from all legal moves.

`good_move`: Return the best move determined by the `search` function.

---

## Functions

`fromNotation`: Convert notation like `e2e4` to move

`toNotation`: Convert move to notation like `e2e4`
