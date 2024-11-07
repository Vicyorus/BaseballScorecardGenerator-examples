import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CLE, 2013-04-16
# https://www.baseball-reference.com/boxes/CLE/CLE201304160.shtml
# https://www.mlb.com/gameday/red-sox-vs-indians/2013/04/16/346938/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-16 19:06-22:36",
        "at": "Progressive Field, Cleveland, OH",
        "att": "9,143",
        "temp": "50F, Overcast",
        "wind": "2mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                44: "Jackie Bradley Jr.",
                # Bullpen
                63: "Alex Wilson",
                35: "Steven Wright",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [16, "5"],
                [29, "7"],
                [5, "0"],
                [3, "2"],
                [23, "6"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [44, "CF"],
            ],
            "bullpen": [63, 35, 40, 30, 91, 31, 59, 36, 11, 19, 46],
        },
        "home": {
            "team": "Cleveland Indians",
            "starter": 30,
            "roster": {
                # Lineup
                11: "Drew Stubbs",
                13: "Asdrúbal Cabrera",
                41: "Carlos Santana",
                33: "Nick Swisher",
                12: "Mark Reynolds",
                23: "Michael Brantley",
                4: "Mike Aviles",
                8: "Lonnie Chisenhall",
                9: "Ryan Raburn",
                # Starting pitcher
                30: "Ubaldo Jiménez",
                # Bench
                25: "Jason Giambi",
                46: "Cord Phelps",
                10: "Yan Gomes",
                22: "Jason Kipnis",
                # Bullpen
                34: "Zach McAllister",
                54: "Chris Perez",
                53: "Rich Hill",
                38: "Joe Smith",
                37: "Cody Allen",
                50: "Nick Hagadone",
                39: "Brett Myers",
                52: "Vinnie Pestano",
                63: "Justin Masterson",
                27: "Bryan Shaw",
            },
            "lefties": [53, 50],
            "lineup": [
                [11, "8"],
                [13, "6"],
                [41, "2"],
                [33, "3"],
                [12, "0"],
                [23, "7"],
                [4, "4"],
                [8, "5"],
                [9, "9"],
            ],
            "bench": [
                [25, "1B"],
                [46, "2B"],
                [10, "C"],
                [22, "2B"],
            ],
            "bullpen": [34, 54, 53, 38, 37, 50, 39, 52, 63, 27],
        },
        "umpires": {
            "HP": "Laz Diaz",
            "1B": "Tim Timmons",
            "2B": "Mike Winters",
            "3B": "Mark Wegner",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: CLE #30 Ubaldo Jiménez
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b f c")
t1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c c")
t1.out("G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. CLE #11 Drew Stubbs (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b c")
b1.out("F9")

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("F8")

# 3. CLE #41 Carlos Santana (X - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CLE #30 Ubaldo Jiménez
t2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b")
t2.hit(2)
t2.advance(3, "5 BB")
t2.advance(4, "3 BB")

# 5. BOS #16 Will Middlebrooks (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b s b s b")
t2.reach("BB")
t2.advance(2, "5 BB")
t2.advance(3, "3 BB")
t2.advance(4, "23 SF9")

# 6. BOS #29 Daniel Nava (X - 12 - 16)
t2.new_ab(is_risp=True)
t2.pitch_list("f b b c s")
t2.out("K")

# 7. BOS #5  Jonny Gomes (X - 12 - 16)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c d b")
t2.reach("BB")
t2.advance(2, "3 BB")
t2.advance(4, "2 1B")

# 8. BOS #3  David Ross (12 - 16 - 5)
t2.new_ab(is_risp=True)
t2.pitch_list("b c f b b b")
t2.reach("BB", rbis=1)
t2.advance(3, "2 1B")
t2.advance(4, "15 BB")

# 9. BOS #23 Pedro Ciriaco (16 - 5 - 3)
t2.new_ab(is_risp=True)
t2.pitch_list("c f")
t2.out("SF9", rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - 5 - 3)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.hit(1, rbis=1)
t2.advance(2, "18 SB")
t2.advance(3, "15 BB")
t2.advance(4, "12 2B")

# 2. BOS #18 Shane Victorino (3 - X - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c d b")
t2.reach("BB")
t2.advance(2, "15 BB")
t2.advance(4, "12 2B")

# 3. BOS #15 Dustin Pedroia (3 - 2 - 18)
t2.new_ab(is_risp=True)
t2.pitch_list("c c d b f d b")
t2.reach("BB", rbis=1)
t2.advance(4, "12 2B")

# Pitching change (CLE): #37 Cody Allen replaces #30 Ubaldo Jiménez
t2.pitching_substitution(37)

# 4. BOS #12 Mike Napoli (2 - 18 - 15)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b b f")
t2.hit(2, rbis=3)

# 5. BOS #16 Will Middlebrooks (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("s c d f b c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 4. CLE #33 Nick Swisher (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1)
b2.advance(3, "23 1B")
b2.advance(4, "4 SF9")

# 5. CLE #12 Mark Reynolds (X - X - 33)
b2.new_ab()
b2.pitch_list("c f b b d f f s")
b2.out("K")

# 6. CLE #23 Michael Brantley (X - X - 33)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 7. CLE #4  Mike Aviles (33 - X - 23)
b2.new_ab(is_risp=True)
b2.pitch_list("c d")
b2.out("SF9", rbis=1)

# 8. CLE #8  Lonnie Chisenhall (X - X - 23)
b2.new_ab()
b2.pitch_list("1 b b b c f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CLE #37 Cody Allen
t3 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("b c c s")
t3.out("K")

# 7. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.pitch_list("b c c")
t3.hit(1)
t3.advance(3, "3 1B")

# 8. BOS #3  David Ross (X - X - 5)
t3.new_ab()
t3.hit(1)

# 9. BOS #23 Pedro Ciriaco (5 - X - 3)
t3.new_ab(is_risp=True)
t3.pitch_list("c s s")
t3.out("K")

# 1. BOS #2  Jacoby Ellsbury (5 - X - 3)
t3.new_ab(is_risp=True)
t3.pitch_list("b b")
t3.out("G3")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 9. CLE #9  Ryan Raburn (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f f c")
b3.out("!K")

# 1. CLE #11 Drew Stubbs (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b s b")
b3.reach("BB")

# 2. CLE #13 Asdrúbal Cabrera (X - X - 11)
b3.new_ab()
b3.pitch_list("c c b f c")
b3.out("!K")

# 3. CLE #41 Carlos Santana (X - X - 11)
b3.new_ab()
b3.pitch_list("b b f f b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CLE #37 Cody Allen
t4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c f b")
t4.hit(1)

# 4. BOS #12 Mike Napoli (X - X - 15)
t4.new_ab()
t4.out("F9")

# 5. BOS #16 Will Middlebrooks (X - X - 15)
t4.new_ab()
t4.pitch_list("f b s c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 4. CLE #33 Nick Swisher (X - X - X)
b4.new_ab()
b4.out("F9")

# 5. CLE #12 Mark Reynolds (X - X - X)
b4.new_ab()
b4.pitch_list("b b s b b")
b4.reach("BB")

# 6. CLE #23 Michael Brantley (X - X - 12)
b4.new_ab()
b4.pitch_list("b c b b")
b4.out("L7")

# 7. CLE #4  Mike Aviles (X - X - 12)
b4.new_ab()
b4.pitch_list("c b s c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CLE #37 Cody Allen
t5 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("b c s s")
t5.out("K")

# 7. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")

# 8. BOS #3  David Ross (X - X - 5)
t5.new_ab()
t5.pitch_list("c s b f s")
t5.out("K")

# Pitching change (CLE): #50 Nick Hagadone replaces #37 Cody Allen
t5.pitching_substitution(50)

# 9. BOS #23 Pedro Ciriaco (X - X - 5)
t5.new_ab()
t5.pitch_list("f f d b 1")
t5.out("F9")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 8. CLE #8  Lonnie Chisenhall (X - X - X)
b5.new_ab()
b5.pitch_list("b f b")
b5.out("F7")

# 9. CLE #9  Ryan Raburn (X - X - X)
b5.new_ab()
b5.pitch_list("b f s b")
b5.hit(1)
b5.advance(2, "11 BB")
b5.advance(3, "13 1B")
b5.advance(4, "33 PB")

# 1. CLE #11 Drew Stubbs (X - X - 9)
b5.new_ab()
b5.pitch_list("b f b b b")
b5.reach("BB")
b5.advance(2, "13 1B")
b5.advance(3, "33 PB")

# 2. CLE #13 Asdrúbal Cabrera (X - 9 - 11)
b5.new_ab(is_risp=True)
b5.pitch_list("f d")
b5.hit(1)
b5.advance(2, "33 PB")

# 3. CLE #41 Carlos Santana (9 - 11 - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("c d f s")
b5.out("K")

# 4. CLE #33 Nick Swisher (9 - 11 - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("b f c b f b b")
b5.pb()
b5.reach("BB")

# 5. CLE #12 Mark Reynolds (11 - 13 - 33)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CLE #50 Nick Hagadone
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b c f f b")
t6.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "12 WP")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t6.new_ab()
t6.pitch_list("c 1 s 1 f b 1 f c")
t6.out("!K")

# 4. BOS #12 Mike Napoli (X - X - 18)
t6.new_ab(is_risp=True)
t6.pitch_list("b b 1 s s c")
t6.wp()
t6.out("!K")


# Bot 6th
# Pitching: BOS #59 Clayton Mortensen
b6 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #22 Felix Doubront
b6.pitching_substitution(59)

# 6. CLE #23 Michael Brantley (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(1)
b6.advance(2, "9 BB")

# 7. CLE #4  Mike Aviles (X - X - 23)
b6.new_ab()
b6.pitch_list("1 b b")
b6.out("F9")

# 8. CLE #8  Lonnie Chisenhall (X - X - 23)
b6.new_ab()
b6.pitch_list("b")
b6.out("F7")

# 9. CLE #9  Ryan Raburn (X - X - 23)
b6.new_ab()
b6.pitch_list("b b 1 b c f b")
b6.reach("BB")

# 1. CLE #11 Drew Stubbs (X - 23 - 9)
b6.new_ab(is_risp=True)
b6.pitch_list("b c c c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CLE #50 Nick Hagadone
t7 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G5-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("f f s")
t7.out("K")

# 7. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b c f b")
t7.reach("BB")
t7.advance(2, "3 WP")

# Pitching change (CLE): #53 Rich Hill replaces #50 Nick Hagadone
t7.pitching_substitution(53)

# 8. BOS #3  David Ross (X - X - 5)
t7.new_ab(is_risp=True)
t7.pitch_list("c s b b s")
t7.wp()
t7.out("K")


# Bot 7th
# Pitching: BOS #59 Clayton Mortensen
b7 = game.new_inning()

# 2. CLE #13 Asdrúbal Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G3-1")

# 3. CLE #41 Carlos Santana (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G4-3")

# 4. CLE #33 Nick Swisher (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.out("G2-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CLE #53 Rich Hill
t8 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t8.new_ab()
t8.pitch_list("b f b c b b")
t8.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
t8.new_ab()
t8.pitch_list("c c c")
t8.out("!K")

# 2. BOS #18 Shane Victorino (X - X - 23)
t8.new_ab()
t8.pitch_list("1 b f c f f f f")
t8.out("F8")

# Pitching change (CLE): #27 Bryan Shaw replaces #53 Rich Hill
t8.pitching_substitution(27)

# 3. BOS #15 Dustin Pedroia (X - X - 23)
t8.new_ab()
t8.pitch_list("c s b b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #63 Alex Wilson
b8 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #59 Clayton Mortensen
b8.pitching_substitution(63)

# 5. CLE #12 Mark Reynolds (X - X - X)
b8.new_ab()
b8.pitch_list("b c c b b b")
b8.reach("BB")
b8.thrown_out(2, "23 DP1-6-3", 1, 63)

# 6. CLE #23 Michael Brantley (X - X - 12)
b8.new_ab()
b8.pitch_list("f b")
b8.out("DP1-6-3")

# 7. CLE #4  Mike Aviles (X - X - X)
b8.new_ab()
b8.pitch_list("c s b c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CLE #27 Bryan Shaw
t9 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f s")
t9.out("K")

# 5. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b b s")
t9.out("K")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #29 Daniel Nava, batting 6th
t9.offensive_substitution(6, 37, "PH")

# 6. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")


# Bot 9th
# Pitching: BOS #63 Alex Wilson
b9 = game.new_inning()

# Defensive change (BOS): #44 Jackie Bradley Jr. replaces #37 Mike Carp (PH), playing LF, batting 6th
b9.defensive_substitution(6, 44, "7")

# 8. CLE #8  Lonnie Chisenhall (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("G4-3")

# Offensive change (CLE): Pinch-hitter #46 Cord Phelps replaces #9 Ryan Raburn, batting 9th
b9.offensive_substitution(9, 46, "PH")

# 9. CLE #46 Cord Phelps (X - X - X)
b9.new_ab()
b9.pitch_list("b c f")
b9.out("G1-3")

# 1. CLE #11 Drew Stubbs (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.hit(1)
b9.advance(2, "13 DI")

# 2. CLE #13 Asdrúbal Cabrera (X - X - 11)
b9.new_ab(is_risp=True)
b9.pitch_list("b b f b")
b9.out("G3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22, is_away_team=True)

# Loser team: CLE
# LP: CLE #30 Ubaldo Jiménez
game.losing_pitcher(30)

# print(game)
game.generate_scorecard()
