import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIN, 2013-05-18
# https://www.baseball-reference.com/boxes/MIN/MIN201305180.shtml
# https://www.mlb.com/gameday/red-sox-vs-twins/2013/05/18/347371/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-18 19:11-23:04",
        "at": "Target Field, Minneapolis, MN",
        "att": "36,967",
        "temp": "81F, Partly Cloudy",
        "wind": "11mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                20: "Ryan Lavarnway",
                23: "Pedro Ciriaco",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                18: "Shane Victorino",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [16, "5"],
                [20, "2"],
                [23, "6"],
            ],
            "bench": [
                [7, "SS"],
                [39, "C"],
                [37, "1B"],
                [18, "CF"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 31, 59, 36, 11, 19, 22],
        },
        "home": {
            "team": "Minnesota Twins",
            "starter": 58,
            "roster": {
                # Lineup
                8: "Jamey Carroll",
                7: "Joe Mauer",
                33: "Justin Morneau",
                16: "Josh Willingham",
                9: "Ryan Doumit",
                31: "Oswaldo Arcia",
                24: "Trevor Plouffe",
                32: "Aaron Hicks",
                25: "Pedro Florimón",
                # Starting pitcher
                58: "Scott Diamond",
                # Bench
                27: "Chris Parmelee",
                22: "Wilkin Ramirez",
                5: "Eduardo Escobar",
                2: "Brian Dozier",
                # Bullpen
                15: "Glen Perkins",
                30: "Kevin Correia",
                60: "Pedro Hernandez",
                20: "Josh Roenicke",
                50: "Casey Fien",
                61: "Jared Burton",
                37: "Mike Pelfrey",
                52: "Brian Duensing",
                57: "Ryan Pressly",
                51: "Anthony Swarzak",
                49: "Vance Worley",
            },
            "lefties": [58, 15, 60, 52],
            "lineup": [
                [8, "4"],
                [7, "0"],
                [33, "3"],
                [16, "7"],
                [9, "2"],
                [31, "9"],
                [24, "5"],
                [32, "8"],
                [25, "6"],
            ],
            "bench": [
                [27, "1B"],
                [22, "LF"],
                [5, "3B"],
                [2, "2B"],
            ],
            "bullpen": [15, 30, 60, 20, 50, 61, 37, 52, 57, 51, 49],
        },
        "umpires": {
            "HP": "Paul Schrieber",
            "1B": "Chad Fairchild",
            "2B": "Jeff Kellogg",
            "3B": "Eric Cooper",
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
# Pitching: MIN #58 Scott Diamond
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.hit(1)
t1.advance(2, "15 BB")
t1.advance(4, "34 HR")

# 2. BOS #5  Jonny Gomes (X - X - 2)
t1.new_ab()
t1.pitch_list("b 1 f 1 1 b b 1 1")
t1.out("(F)P4")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t1.new_ab()
t1.pitch_list("1 b b b c 1 b")
t1.reach("BB")
t1.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - 2 - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("b f b f")
t1.hit(4, rbis=3)

# 5. BOS #12 Mike Napoli (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.thrown_out(2, "29 DP4-6-3", 2, 58)

# 6. BOS #29 Daniel Nava (X - X - 12)
t1.new_ab()
t1.pitch_list("c c d f f b")
t1.out("DP4-6-3")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. MIN #8  Jamey Carroll (X - X - X)
b1.new_ab()
b1.pitch_list("c b f s")
b1.out("K")

# 2. MIN #7  Joe Mauer (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("F7")

# 3. MIN #33 Justin Morneau (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.hit(1)

# 4. MIN #16 Josh Willingham (X - X - 33)
b1.new_ab()
b1.pitch_list("d c b f b f")
b1.out("P4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIN #58 Scott Diamond
t2 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("c s b f b f")
t2.hit(1)
t2.thrown_out(2, "20 DP4-6-3", 1, 58)

# 8. BOS #20 Ryan Lavarnway (X - X - 16)
t2.new_ab()
t2.pitch_list("b b")
t2.out("DP4-6-3")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 5. MIN #9  Ryan Doumit (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b f d")
b2.reach("BB")
b2.advance(2, "31 BB")
b2.advance(3, "24 G5-3")
b2.thrown_out(4, "32 FC5-2-6-1", 2, 46)

# 6. MIN #31 Oswaldo Arcia (X - X - 9)
b2.new_ab()
b2.pitch_list("b b c f d b")
b2.reach("BB")
b2.advance(2, "24 G5-3")
b2.advance(4, "25 1B")

# 7. MIN #24 Trevor Plouffe (X - 9 - 31)
b2.new_ab(is_risp=True)
b2.out("G5-3")

# 8. MIN #32 Aaron Hicks (9 - 31 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b s c f b")
b2.reach("FC5-2-6-1")
b2.advance(3, "25 1B")

# 9. MIN #25 Pedro Florimón (X - 31 - 32)
b2.new_ab(is_risp=True)
b2.pitch_list("s")
b2.hit(1, rbis=1)
b2.advance(2, "8 BB")

# 1. MIN #8  Jamey Carroll (32 - X - 25)
b2.new_ab(is_risp=True)
b2.pitch_list("b 1 b c b b")
b2.reach("BB")

# 2. MIN #7  Joe Mauer (32 - 25 - 8)
b2.new_ab(is_risp=True)
b2.pitch_list("f b f t")
b2.out("KT")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIN #58 Scott Diamond
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s")
t3.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b b")
t3.reach("BB")
t3.advance(2, "15 1B")
t3.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t3.new_ab()
t3.pitch_list("c d c 1")
t3.hit(1)
t3.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - 5 - 15)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.hit(1, rbis=1)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("b c f f s")
t3.out("K")

# 6. BOS #29 Daniel Nava (X - 15 - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 3. MIN #33 Justin Morneau (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("F8")

# 4. MIN #16 Josh Willingham (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(2)
b3.advance(3, "9 G1-3")

# 5. MIN #9  Ryan Doumit (X - 16 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b b")
b3.out("G1-3")

# 6. MIN #31 Oswaldo Arcia (16 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b s s d b f f f b")
b3.reach("BB")
b3.advance(2, "24 BB")

# 7. MIN #24 Trevor Plouffe (16 - X - 31)
b3.new_ab(is_risp=True)
b3.pitch_list("b d b f b")
b3.reach("BB")

# 8. MIN #32 Aaron Hicks (16 - 31 - 24)
b3.new_ab(is_risp=True)
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIN #58 Scott Diamond
t4 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")
t4.thrown_out(2, "2 FC6", 3, 58)

# 8. BOS #20 Ryan Lavarnway (X - X - 16)
t4.new_ab()
t4.pitch_list("d c b 1 f")
t4.out("L8")

# 9. BOS #23 Pedro Ciriaco (X - X - 16)
t4.new_ab()
t4.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
t4.new_ab()
t4.pitch_list("b b c c f f")
t4.reach("FC6")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
b4.new_ab()
b4.pitch_list("b t b c b")
b4.out("F7")

# 1. MIN #8  Jamey Carroll (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.out("G6-3")

# 2. MIN #7  Joe Mauer (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f")
b4.hit(2)
b4.advance(4, "33 1B")

# 3. MIN #33 Justin Morneau (X - 7 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c b b s f")
b4.hit(1, rbis=1)

# 4. MIN #16 Josh Willingham (X - X - 33)
b4.new_ab()
b4.pitch_list("b b b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIN #58 Scott Diamond
t5 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(4, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - 5 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c l b b")
t5.hit(2, rbis=1)
t5.advance(3, "34 G6-3")
t5.advance(4, "29 SF7")

# 4. BOS #34 David Ortiz (X - 15 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("t b s d")
t5.out("G6-3")

# Pitching change (MIN): #51 Anthony Swarzak replaces #58 Scott Diamond
t5.pitching_substitution(51)

# 5. BOS #12 Mike Napoli (15 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b d b b")
t5.reach("BB")
t5.advance(2, "16 1B")
t5.advance(4, "20 1B")

# 6. BOS #29 Daniel Nava (15 - X - 12)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c")
t5.out("SF7", rbis=1)

# 7. BOS #16 Will Middlebrooks (X - X - 12)
t5.new_ab()
t5.hit(1)
t5.advance(2, "20 1B")
t5.thrown_out(3, "20 7-2-6", 3, 51)

# 8. BOS #20 Ryan Lavarnway (X - 12 - 16)
t5.new_ab(is_risp=True)
t5.hit(1, rbis=1)


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 5. MIN #9  Ryan Doumit (X - X - X)
b5.new_ab()
b5.pitch_list("c f f b b b f")
b5.hit(2)
b5.advance(3, "31 G4-3")
b5.advance(4, "24 G6-3")

# 6. MIN #31 Oswaldo Arcia (X - 9 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s d")
b5.out("G4-3")

# 7. MIN #24 Trevor Plouffe (9 - X - X)
b5.new_ab(is_risp=True)
b5.out("G6-3", rbis=1)

# 8. MIN #32 Aaron Hicks (X - X - X)
b5.new_ab()
b5.pitch_list("b b f b c b")
b5.reach("BB")
b5.advance(2, "25 SB")
b5.advance(4, "25 1B")

# 9. MIN #25 Pedro Florimón (X - X - 32)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b f 1 f b")
b5.hit(1, rbis=1)
b5.advance(2, "8 SB")
b5.advance(4, "8 1B")

# 1. MIN #8  Jamey Carroll (X - X - 25)
b5.new_ab(is_risp=True)
b5.pitch_list("c f d d")
b5.hit(1, rbis=1)
b5.advance(2, "7 1B")

# Pitching change (BOS): #59 Clayton Mortensen replaces #46 Ryan Dempster
b5.pitching_substitution(59)

# 2. MIN #7  Joe Mauer (X - X - 8)
b5.new_ab()
b5.pitch_list("1 1 b b")
b5.hit(1)

# 3. MIN #33 Justin Morneau (X - 8 - 7)
b5.new_ab(is_risp=True)
b5.pitch_list("b b b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIN #51 Anthony Swarzak
t6 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t6.new_ab()
t6.pitch_list("b c b")
t6.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b")
t6.out("F9")

# 2. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F8")


# Bot 6th
# Pitching: BOS #59 Clayton Mortensen
b6 = game.new_inning()

# 4. MIN #16 Josh Willingham (X - X - X)
b6.new_ab()
b6.pitch_list("c s b f f b b")
b6.out("F8")

# 5. MIN #9  Ryan Doumit (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(2, "31 BB")
b6.advance(3, "24 BB")
b6.thrown_out(4, "32 DP4-2", 3, 32)

# 6. MIN #31 Oswaldo Arcia (X - X - 9)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(2, "24 BB")

# Pitching change (BOS): #32 Craig Breslow replaces #59 Clayton Mortensen
b6.pitching_substitution(32)

# 7. MIN #24 Trevor Plouffe (X - 9 - 31)
b6.new_ab(is_risp=True)
b6.pitch_list("b b b c b")
b6.reach("BB")

# 8. MIN #32 Aaron Hicks (9 - 31 - 24)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.out("DP4-2")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIN #51 Anthony Swarzak
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b f b")
t7.reach("BB")
t7.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("b f b")
t7.hit(4, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c b b s b f d")
t7.reach("BB")
t7.advance(4, "29 HR")

# Pitching change (MIN): #50 Casey Fien replaces #51 Anthony Swarzak
t7.pitching_substitution(50)

# 6. BOS #29 Daniel Nava (X - X - 12)
t7.new_ab()
t7.pitch_list("c b b c")
t7.hit(4, rbis=2)

# 7. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b b f c b")
t7.out("G5-3")

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t7.new_ab()
t7.pitch_list("b s s b f s")
t7.out("K")

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t7.new_ab()
t7.out("P3")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G1-3")

# 1. MIN #8  Jamey Carroll (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
b7.thrown_out(2, "7 FC3-6", 2, 32)

# 2. MIN #7  Joe Mauer (X - X - 8)
b7.new_ab()
b7.pitch_list("b b c b")
b7.reach("FC3-6")

# 3. MIN #33 Justin Morneau (X - X - 7)
b7.new_ab()
b7.out("(F)P2")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIN #57 Ryan Pressly
t8 = game.new_inning()

# Pitching change (MIN): #57 Ryan Pressly replaces #50 Casey Fien
t8.pitching_substitution(57)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("F9")

# 2. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #63 Alex Wilson
b8 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #32 Craig Breslow
b8.pitching_substitution(63)

# 4. MIN #16 Josh Willingham (X - X - X)
b8.new_ab()
b8.pitch_list("c b c s")
b8.out("K")

# 5. MIN #9  Ryan Doumit (X - X - X)
b8.new_ab()
b8.pitch_list("b c s b f")
b8.out("G1-3")

# 6. MIN #31 Oswaldo Arcia (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIN #57 Ryan Pressly
t9 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b b c t b d")
t9.reach("BB")
t9.advance(2, "12 BB")
t9.advance(3, "29 1B")
t9.advance(4, "20 SF9")

# 5. BOS #12 Mike Napoli (X - X - 34)
t9.new_ab()
t9.pitch_list("b c f d f b d")
t9.reach("BB")
t9.advance(2, "29 1B")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b c")
t9.hit(1)

# 7. BOS #16 Will Middlebrooks (34 - 12 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("b f b c s")
t9.out("K")

# 8. BOS #20 Ryan Lavarnway (34 - 12 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("d f s")
t9.out("SF9", rbis=1)

# 9. BOS #23 Pedro Ciriaco (X - 12 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("F9")


# Bot 9th
# Pitching: BOS #63 Alex Wilson
b9 = game.new_inning()

# 7. MIN #24 Trevor Plouffe (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.hit(1)
b9.thrown_out(2, "25 DP4-6-3", 2, 63)

# 8. MIN #32 Aaron Hicks (X - X - 24)
b9.new_ab()
b9.pitch_list("c b c s")
b9.out("K")

# 9. MIN #25 Pedro Florimón (X - X - 24)
b9.new_ab()
b9.pitch_list("b c")
b9.out("DP4-6-3")

# Winning team: BOS
# WP: BOS #32 Craig Breslow
game.winning_pitcher(32, is_away_team=True)

# Loser team: MIN
# LP: MIN #58 Scott Diamond
game.losing_pitcher(58)

# print(game)
game.generate_scorecard()
