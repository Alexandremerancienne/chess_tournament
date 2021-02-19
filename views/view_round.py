class ViewRound():

    line = (100*"*")

    @staticmethod
    def start_round(i):
        round_i = (f" ROUND {i} ").center(100,"*")
        print(round_i)
        print("Number of matches : 4")
        input("Press Enter to start the round").center(100," ")
        print(ViewRound.line)

    @staticmethod
    def end_round():
        print(ViewRound.line)
        input("Press Enter to end the round")    	
        print(ViewRound.line)


    @staticmethod
    def print_round_results(i, start_date, end_date, list_of_matches):
        print(f"ROUND {i} RESULTS")
        print(f"Start: {start_date}")        
        print(f"End: {end_date}")
        print(f"Matches: {list_of_matches}")
