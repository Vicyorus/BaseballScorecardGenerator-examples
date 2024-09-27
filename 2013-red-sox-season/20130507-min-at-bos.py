import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2013-05-07
# https://www.baseball-reference.com/boxes/BOS/BOS201305070.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2013/05/07/347230/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-07 19:10-22:11",
        "at": "Fenway Park, Boston, MA",
        "att": "30,549",
        "temp": "64F, Partly Cloudy",
        "wind": "14mph, In From RF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 58,
            "roster": {
                # Lineup
                8: "Jamey Carroll",
                7: "Joe Mauer",
                16: "Josh Willingham",
                33: "Justin Morneau",
                24: "Trevor Plouffe",
                9: "Ryan Doumit",
                27: "Chris Parmelee",
                22: "Wilkin Ramirez",
                2: "Brian Dozier",
                # Starting pitcher
                58: "Scott Diamond",
                # Bench
                5: "Eduardo Escobar",
                32: "Aaron Hicks",
                31: "Oswaldo Arcia",
                25: "Pedro Florimón",
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
                [8, "6"],
                [7, "0"],
                [16, "7"],
                [33, "3"],
                [24, "5"],
                [9, "2"],
                [27, "9"],
                [22, "8"],
                [2, "4"],
            ],
            "bench": [
                [5, "3B"],
                [32, "RF"],
                [31, "LF"],
                [25, "SS"],
            ],
            "bullpen": [15, 30, 60, 20, 50, 61, 37, 52, 57, 51, 49],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 41, 30, 32, 31, 59, 36, 11, 64, 19, 22],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "Ed Hickox",
            "2B": "Lance Barksdale",
            "3B": "Cory Blaser",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. MIN #8  Jamey Carroll (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("G3-1")

# 2. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("c f b f s")
t1.out("K")

# 3. MIN #16 Josh Willingham (X - X - X)
t1.new_ab()
t1.pitch_list("c f b b s")
t1.out("K")


# Bot 1st
# Pitching: MIN #58 Scott Diamond
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c b")
b1.hit(1)
b1.thrown_out(2, "15 DP6-4-3", 2, 58)

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("1 c f 1 1 f")
b1.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("c 1 s f")
b1.out("DP6-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 4. MIN #33 Justin Morneau (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b")
t2.hit(1)

# 5. MIN #24 Trevor Plouffe (X - X - 33)
t2.new_ab()
t2.pitch_list("s")
t2.out("F9")

# 6. MIN #9  Ryan Doumit (X - X - 33)
t2.new_ab()
t2.pitch_list("l b")
t2.out("F7")

# 7. MIN #27 Chris Parmelee (X - X - 33)
t2.new_ab()
t2.pitch_list("f b c f f b s")
t2.out("K")


# Bot 2nd
# Pitching: MIN #58 Scott Diamond
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b f")
b2.hit(1)
b2.thrown_out(2, "12 FC1-4", 1, 58)

# 5. BOS #12 Mike Napoli (X - X - 34)
b2.new_ab()
b2.pitch_list("f c b f f d f")
b2.reach("FC1-4")

# 6. BOS #5  Jonny Gomes (X - X - 12)
b2.new_ab()
b2.pitch_list("c c 1 b")
b2.out("F9")

# 7. BOS #16 Will Middlebrooks (X - X - 12)
b2.new_ab()
b2.pitch_list("1 c c s")
b2.out("K2-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 8. MIN #22 Wilkin Ramirez (X - X - X)
t3.new_ab()
t3.pitch_list("f b s")
t3.out("G4-3")

# 9. MIN #2  Brian Dozier (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b c")
t3.out("!K")

# 1. MIN #8  Jamey Carroll (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G4-3")


# Bot 3rd
# Pitching: MIN #58 Scott Diamond
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)

# 9. BOS #3  David Ross (X - X - 7)
b3.new_ab()
b3.pitch_list("b 1 b f 1 1 b")
b3.out("P3")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b3.new_ab()
b3.pitch_list("1 f f")
b3.out("(F)P5")

# 2. BOS #18 Shane Victorino (X - X - 7)
b3.new_ab()
b3.pitch_list("b c b 1 f")
b3.out("G3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "16 BB")
t4.advance(3, "33 DP1-6-3")

# 3. MIN #16 Josh Willingham (X - X - 7)
t4.new_ab()
t4.pitch_list("b f b f b b")
t4.reach("BB")
t4.thrown_out(2, "33 DP1-6-3", 1, 46)

# 4. MIN #33 Justin Morneau (X - 7 - 16)
t4.new_ab()
t4.pitch_list("b c f")
t4.out("DP1-6-3")

# 5. MIN #24 Trevor Plouffe (7 - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G5-3")


# Bot 4th
# Pitching: MIN #58 Scott Diamond
b4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("s c f b")
b4.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("f b f")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 6. MIN #9  Ryan Doumit (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(3, "27 BLK")
t5.advance(4, "22 1B")

# 7. MIN #27 Chris Parmelee (X - 9 - X)
t5.new_ab()
t5.pitch_list("b n s b b")
t5.balk()
t5.out("(F)P5")

# 8. MIN #22 Wilkin Ramirez (9 - X - X)
t5.new_ab()
t5.hit(1, rbis=1)

# Defensive change (BOS): #39 Jarrod Saltalamacchia replaces #3 David Ross (C), playing C, batting 9th
t5.defensive_substitution(9, 39, "2")

# 9. MIN #2  Brian Dozier (X - X - 22)
t5.new_ab()
t5.pitch_list("1 b l s s")
t5.out("K")

# 1. MIN #8  Jamey Carroll (X - X - 22)
t5.new_ab()
t5.pitch_list("f 1 c b 1 f s")
t5.out("K")


# Bot 5th
# Pitching: MIN #58 Scott Diamond
b5 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F7")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("s c b")
b5.out("G4-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b b")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t6.new_ab()
t6.pitch_list("c s b")
t6.out("P6")

# 3. MIN #16 Josh Willingham (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G6-3")

# 4. MIN #33 Justin Morneau (X - X - X)
t6.new_ab()
t6.pitch_list("s f f f c")
t6.out("!K")


# Bot 6th
# Pitching: MIN #58 Scott Diamond
b6 = game.new_inning()

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c c")
b6.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #46 Ryan Dempster
t7 = game.new_inning()

# Defensive change (BOS): #23 Pedro Ciriaco replaces #16 Will Middlebrooks (3B), playing 3B, batting 7th
t7.defensive_substitution(7, 23, "5")

# 5. MIN #24 Trevor Plouffe (X - X - X)
t7.new_ab()
t7.pitch_list("c f s")
t7.out("K")

# 6. MIN #9  Ryan Doumit (X - X - X)
t7.new_ab()
t7.pitch_list("b c f f f b")
t7.hit(4)

# 7. MIN #27 Chris Parmelee (X - X - X)
t7.new_ab()
t7.pitch_list("c s b")
t7.out("G3")

# 8. MIN #22 Wilkin Ramirez (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("F9")


# Bot 7th
# Pitching: MIN #58 Scott Diamond
b7 = game.new_inning()

# Defensive change (MIN): #32 Aaron Hicks replaces #22 Wilkin Ramirez (CF), playing CF, batting 8th
b7.defensive_substitution(8, 32, "8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("c b b s b f f f")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #46 Ryan Dempster
t8 = game.new_inning()

# 9. MIN #2  Brian Dozier (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b")
t8.error(5)
t8.reach("E5")
t8.advance(3, "8 E5")
t8.advance("U", "7 2B")

# 1. MIN #8  Jamey Carroll (X - X - 2)
t8.new_ab()
t8.pitch_list("d 1")
t8.error(5)
t8.reach("E5")
t8.advance(3, "7 2B")
t8.advance("U", "33 1B")

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
t8.pitching_substitution(32)

# 2. MIN #7  Joe Mauer (2 - X - 8)
t8.new_ab()
t8.pitch_list("s")
t8.hit(2, rbis=1)
t8.advance(3, "33 1B")
t8.advance(4, "24 1B")

# 3. MIN #16 Josh Willingham (8 - 7 - X)
t8.new_ab()
t8.pitch_list("b f b s f b b")
t8.reach("BB")
t8.advance(2, "33 1B")
t8.advance(3, "24 1B")
t8.thrown_out(4, "9 FC3-2", 1, 63)

# 4. MIN #33 Justin Morneau (8 - 7 - 16)
t8.new_ab()
t8.pitch_list("d b f b")
t8.hit(1, rbis=1)
t8.advance(2, "24 1B")
t8.error(2)
t8.advance("U", "9 E2")

# 5. MIN #24 Trevor Plouffe (7 - 16 - 33)
t8.new_ab()
t8.hit(1, rbis=1)
t8.advance(3, "9 E2")

# Pitching change (BOS): #63 Alex Wilson replaces #32 Craig Breslow
t8.pitching_substitution(63)

# 6. MIN #9  Ryan Doumit (16 - 33 - 24)
t8.new_ab()
t8.reach("FC3-2")

# 7. MIN #27 Chris Parmelee (24 - X - 9)
t8.new_ab()
t8.pitch_list("f")
t8.out("F7")

# 8. MIN #32 Aaron Hicks (24 - X - 9)
t8.new_ab()
t8.pitch_list("b")
t8.out("L6")


# Bot 8th
# Pitching: MIN #20 Josh Roenicke
b8 = game.new_inning()

# Pitching change (MIN): #20 Josh Roenicke replaces #58 Scott Diamond
b8.pitching_substitution(20)

# 6. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("F8")

# 7. BOS #23 Pedro Ciriaco (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #63 Alex Wilson
t9 = game.new_inning()

# 9. MIN #2  Brian Dozier (X - X - X)
t9.new_ab()
t9.pitch_list("b b f c f f c")
t9.out("!K")

# 1. MIN #8  Jamey Carroll (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G6-3")

# 2. MIN #7  Joe Mauer (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b b")
t9.reach("BB")

# 3. MIN #16 Josh Willingham (X - X - 7)
t9.new_ab()
t9.pitch_list("b b")
t9.out("F8")


# Bot 9th
# Pitching: MIN #20 Josh Roenicke
b9 = game.new_inning()

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("b b")
b9.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b9.new_ab()
b9.pitch_list("b b f b b")
b9.reach("BB")
b9.thrown_out(2, "18 DP3-6-3", 1, 20)

# 2. BOS #18 Shane Victorino (X - X - 2)
b9.new_ab()
b9.pitch_list("c")
b9.out("DP3-6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("b f b b b")
b9.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b9.new_ab()
b9.pitch_list("b")
b9.out("L8")

# Winning team: MIN
# WP: MIN #58 Scott Diamond
game.winning_pitcher(58, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
