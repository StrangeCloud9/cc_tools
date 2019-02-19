import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    for single_game_info in json_data:
        #Create a new Game object from the json_data by reading
        #  title
        title = single_game_info['title']
        #  year
        year = single_game_info['year']
        #  platform (which requires reading name and launch_year)
        platform_name = single_game_info['platform']['name']
        platform_launch_year = single_game_info['platform']['launch year']
        platform = test_data.Platform(platform_name, platform_launch_year)
        #Add that Game object to the game_library
        game = test_data.Game(title, platform, year)
        game_library.add_game(game)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"
### Begin Add Code Here ###
#Open the file specified by input_json_file
str_content = open(input_json_file, "rb").read()
#Use the json module to load the data from the file
json_obj = json.loads(str_content)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library = make_game_library_from_json(json_obj)
#Print out the resulting GameLibrary data using print()
print (game_library)
### End Add Code Here ###
