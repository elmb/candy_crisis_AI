from utils import menu, game_lib
import heapq
import timeit

def start_game():
    for file_number in range(1,5):
        games = game_lib.load_all_games_from_data_file ('input{}.txt'.format(file_number))
        # features' weights
        i = 1
        k = 5
        j = 5
        z = 1
        total_solution_paths_length = 0
        for game in games:
            start = timeit.default_timer ()
            total_number_of_visited_nodes = 0
            # set up root node (a node is a state of the game, ie. position of candies on the board, id of this node, id of the parent node that led to this state, position of the slider on this board)
            node = {'board': [[], [], []], 'id': 0,'parent_id': 0, 'heuristic_value': 0, 'parent_move': None, 'slider_pos': None, 'cost': 0}
            game_lib.populate_board (node['board'], game)
            current_slider_position = game_lib.get_starting_position (node['board'])
            node['slider_pos'] = current_slider_position
            # start game
            currently_visited_node = node
            # open list is a priority queue ordered based on heuristic value
            open_list = []
            closed_list = []
            while (not game_lib.goal_state (currently_visited_node['board'])):
                children_nodes = game_lib.get_children_nodes(currently_visited_node, i, j, k, z, total_number_of_visited_nodes)
                game_lib.add_children_to_open_list(children_nodes, open_list, closed_list)
                closed_list.append(currently_visited_node)
                currently_visited_node = heapq.heappop(open_list)[2]
                total_number_of_visited_nodes += 1

            goal_state = currently_visited_node
            solution_path = game_lib.get_solution_path(closed_list, goal_state)
            total_solution_paths_length += len (solution_path)
            end = timeit.default_timer()

            with open('output{}.txt'.format(file_number), "a+") as text_file:
                text_file.write(''.join(solution_path) + '\n' + str(int((end-start)*1000)) + 'ms' + '\n')

            display_moves_of_solved_game (game, solution_path)

        with open('output{}.txt'.format(file_number), "a+") as text_file:
            text_file.write(str(total_solution_paths_length))

    menu.handle_end_of_game()

def display_moves_of_solved_game(game, solution_path):
    board_game = [[], [], []]
    game_lib.populate_board (board_game, game)
    print ('\nStarting board: ')
    game_lib.print_board (board_game)
    for move in solution_path:
        print ('\nMove to play: ' + move)
        slider_position = game_lib.letter_to_coordinates (move)
        game_lib.update_board_positions (board_game, slider_position, move)
        game_lib.print_board (board_game)
    print ('\nCONGRATULATIONS!!!\nSequence Of Moves: {}'.format(solution_path))
