from MVC.models.model_match import ModelMatch
from MVC.views.view_match import ViewMatch


class ControllerMatch:

    """A Controller for Match Class.

    The controller can perform the following actions :

    - Start a match ;
    - Print the winner and the score of a match."""

    def __init__(self, model, view):
        self.model = ModelMatch
        self.view = ViewMatch

    def start_match(first_player, second_player):

        """A function to start a match."""

        first_player_name = first_player.last_name
        second_player_name = second_player.last_name
        return ViewMatch.start_match(first_player_name, second_player_name)

    def print_winner_and_score(first_player, second_player):

        """A function to print the winner and the score of a match."""

        match = ModelMatch("", "", "", "")

        f_p = first_player.last_name
        s_p = second_player.last_name

        result = ViewMatch.get_match_result(f_p)

        if result in "wW":
            result = ModelMatch.first_player_wins(match)
            first_player.score += 1
            match = ModelMatch(f_p, 1, s_p, 0)
            ViewMatch.print_first_player_wins_and_score(f_p, s_p)
            return match

        elif result in "lL":
            result = ModelMatch.second_player_wins(match)
            second_player.score += 1
            match = ModelMatch(f_p, 0, s_p, 1)
            ViewMatch.print_first_player_wins_and_score(s_p, f_p)
            return match

        elif result in "dD":
            result = ModelMatch.draw(match)
            first_player.score += 0.5
            second_player.score += 0.5
            match = ModelMatch(f_p, 0.5, s_p, 0.5)
            ViewMatch.print_draw(f_p, s_p)
            return match
