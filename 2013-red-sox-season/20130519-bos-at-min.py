import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIN, 2013-05-19
# https://www.baseball-reference.com/boxes/MIN/MIN201305190.shtml
# https://www.mlb.com/gameday/red-sox-vs-twins/2013/05/19/347386/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-19 14:12-20:27 (3:00 delay)",
        "at": "Target Field, Minneapolis, MN",
        "att": "33,042",
        "temp": "80F, Partly Cloudy",
        "wind": "13mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                39: "Jarrod Saltalamacchia",
                23: "Pedro Ciriaco",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                7: "Stephen Drew",
                2: "Jacoby Ellsbury",
                37: "Mike Carp",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [18, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [16, "5"],
                [39, "2"],
                [23, "6"],
            ],
            "bench": [
                [7, "SS"],
                [2, "CF"],
                [37, "1B"],
                [20, "C"],
            ],
            "bullpen": [63, 65, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Minnesota Twins",
            "starter": 60,
            "roster": {
                # Lineup
                8: "Jamey Carroll",
                7: "Joe Mauer",
                33: "Justin Morneau",
                24: "Trevor Plouffe",
                31: "Oswaldo Arcia",
                22: "Wilkin Ramirez",
                27: "Chris Parmelee",
                32: "Aaron Hicks",
                25: "Pedro Florimón",
                # Starting pitcher
                60: "Pedro Hernandez",
                # Bench
                16: "Josh Willingham",
                5: "Eduardo Escobar",
                9: "Ryan Doumit",
                2: "Brian Dozier",
                # Bullpen
                15: "Glen Perkins",
                30: "Kevin Correia",
                58: "Scott Diamond",
                20: "Josh Roenicke",
                50: "Casey Fien",
                61: "Jared Burton",
                37: "Mike Pelfrey",
                52: "Brian Duensing",
                57: "Ryan Pressly",
                51: "Anthony Swarzak",
                49: "Vance Worley",
            },
            "lefties": [60, 15, 58, 52],
            "lineup": [
                [8, "4"],
                [7, "2"],
                [33, "3"],
                [24, "5"],
                [31, "0"],
                [22, "7"],
                [27, "9"],
                [32, "8"],
                [25, "6"],
            ],
            "bench": [
                [16, "LF"],
                [5, "3B"],
                [9, "C"],
                [2, "2B"],
            ],
            "bullpen": [15, 30, 58, 20, 50, 61, 37, 52, 57, 51, 49],
        },
        "umpires": {
            "HP": "Chad Fairchild",
            "1B": "Jeff Kellogg",
            "2B": "Eric Cooper",
            "3B": "Paul Schrieber",
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
# Pitching: MIN #60 Pedro Hernandez
t1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b s f")
t1.hit(1)
t1.advance(2, "34 SB")

# 2. BOS #5  Jonny Gomes (X - X - 18)
t1.new_ab()
t1.pitch_list("1 b s s 1 d")
t1.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c 1")
t1.out("L9")

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("s f b b")
t1.out("G1-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. MIN #8  Jamey Carroll (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b f")
b1.out("F8")

# 2. MIN #7  Joe Mauer (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b s")
b1.out("K")

# 3. MIN #33 Justin Morneau (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIN #60 Pedro Hernandez
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G6-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b c f")
t2.out("G6-3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("f b b")
t2.hit(4)

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("s f b b s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. MIN #24 Trevor Plouffe (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("L9")

# 5. MIN #31 Oswaldo Arcia (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G4-3")

# 6. MIN #22 Wilkin Ramirez (X - X - X)
b2.new_ab()
b2.pitch_list("b f f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIN #60 Pedro Hernandez
t3 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G6-3")

# 1. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b c f f f f b")
t3.reach("BB")
t3.advance(3, "5 1B")
t3.advance(4, "15 FC5")

# 2. BOS #5  Jonny Gomes (X - X - 18)
t3.new_ab()
t3.pitch_list("1 1 1 c f b 1 b 1")
t3.hit(1)
t3.error(5)
t3.advance(2, "15 FC5")
t3.advance(3, "15 E5")

# 3. BOS #15 Dustin Pedroia (18 - X - 5)
t3.new_ab()
t3.pitch_list("b b")
t3.reach("FC5", rbis=1)

# 4. BOS #34 David Ortiz (5 - X - 15)
t3.new_ab()
t3.pitch_list("f f c")
t3.out("!K")

# 5. BOS #12 Mike Napoli (5 - X - 15)
t3.new_ab()
t3.pitch_list("1 c b b b f f")
t3.out("F9")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 7. MIN #27 Chris Parmelee (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F8")

# 8. MIN #32 Aaron Hicks (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b c")
b3.out("G4-3")

# 9. MIN #25 Pedro Florimón (X - X - X)
b3.new_ab()
b3.pitch_list("c c b b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIN #60 Pedro Hernandez
t4 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("c f b f")
t4.hit(1)
t4.advance(2, "16 G5-3")
t4.advance(3, "39 1B")

# 7. BOS #16 Will Middlebrooks (X - X - 29)
t4.new_ab()
t4.pitch_list("b b 1 c f f b 1")
t4.out("G5-3")

# 8. BOS #39 Jarrod Saltalamacchia (X - 29 - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.advance(2, "23 B1-3")

# 9. BOS #23 Pedro Ciriaco (29 - X - 39)
t4.new_ab()
t4.pitch_list("f")
t4.out("B1-3")

# 1. BOS #18 Shane Victorino (29 - 39 - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("L5")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 1. MIN #8  Jamey Carroll (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")

# 2. MIN #7  Joe Mauer (X - X - X)
b4.new_ab()
b4.pitch_list("b c f f b")
b4.out("F8")

# 3. MIN #33 Justin Morneau (X - X - X)
b4.new_ab()
b4.pitch_list("b c b f")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIN #60 Pedro Hernandez
t5 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b b c c")
t5.hit(1)
t5.advance(3, "34 1B")
t5.advance(4, "12 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t5.new_ab()
t5.pitch_list("c 1 b 1 b s 1")
t5.hit(1)
t5.advance(2, "12 1B")
t5.advance(3, "29 1B")

# 5. BOS #12 Mike Napoli (15 - X - 34)
t5.new_ab()
t5.pitch_list("c f b f")
t5.hit(1, rbis=1)
t5.advance(2, "29 1B")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t5.new_ab()
t5.pitch_list("c f f b")
t5.hit(1)

# Pitching change (MIN): #20 Josh Roenicke replaces #60 Pedro Hernandez
t5.pitching_substitution(20)

# 7. BOS #16 Will Middlebrooks (34 - 12 - 29)
t5.new_ab()
t5.pitch_list("b b s f d")
t5.out("IF4")

# 8. BOS #39 Jarrod Saltalamacchia (34 - 12 - 29)
t5.new_ab()
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 4. MIN #24 Trevor Plouffe (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(2)
b5.error(6)
b5.advance("U", "27 E6")

# 5. MIN #31 Oswaldo Arcia (X - 24 - X)
b5.new_ab()
b5.pitch_list("b f b s")
b5.reach("HBP")
b5.thrown_out(2, "27 FC4-6", 2, 41)

# 6. MIN #22 Wilkin Ramirez (X - 24 - 31)
b5.new_ab()
b5.pitch_list("f s s")
b5.out("K")

# 7. MIN #27 Chris Parmelee (X - 24 - 31)
b5.new_ab()
b5.reach("FC4-6")

# 8. MIN #32 Aaron Hicks (X - X - 27)
b5.new_ab()
b5.pitch_list("b b f b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIN #20 Josh Roenicke
t6 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("(F)P3")

# 1. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G1-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("P4")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b b")
b6.out("G4-3")

# 1. MIN #8  Jamey Carroll (X - X - X)
b6.new_ab()
b6.pitch_list("b c b c")
b6.out("G6-3")

# 2. MIN #7  Joe Mauer (X - X - X)
b6.new_ab()
b6.pitch_list("b c f b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIN #20 Josh Roenicke
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c s s")
t7.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("b b s b c s")
t7.out("K")


# Bot 7th
# Pitching: BOS #30 Andrew Miller
b7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #41 John Lackey
b7.pitching_substitution(30)

# 3. MIN #33 Justin Morneau (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.out("G3-1")

# 4. MIN #24 Trevor Plouffe (X - X - X)
b7.new_ab()
b7.pitch_list("c s b c")
b7.out("!K")

# 5. MIN #31 Oswaldo Arcia (X - X - X)
b7.new_ab()
b7.pitch_list("s f b")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIN #52 Brian Duensing
t8 = game.new_inning()

# Pitching change (MIN): #52 Brian Duensing replaces #20 Josh Roenicke
t8.pitching_substitution(52)

# 6. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c b b c s")
t8.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("b s s b f b s")
t8.out("K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b f b b c f b")
t8.reach("BB")

# 9. BOS #23 Pedro Ciriaco (X - X - 39)
t8.new_ab()
t8.out("F9")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
b8.pitching_substitution(19)

# 6. MIN #22 Wilkin Ramirez (X - X - X)
b8.new_ab()
b8.hit(2)
b8.advance(3, "8 1B")

# 7. MIN #27 Chris Parmelee (X - 22 - X)
b8.new_ab()
b8.pitch_list("c f s")
b8.out("K")

# Offensive change (MIN): Pinch-hitter #16 Josh Willingham replaces #32 Aaron Hicks, batting 8th
b8.offensive_substitution(8, 16, "PH")

# 8. MIN #16 Josh Willingham (X - 22 - X)
b8.new_ab()
b8.pitch_list("b b b s c s")
b8.out("K")

# 9. MIN #25 Pedro Florimón (X - 22 - X)
b8.new_ab()
b8.pitch_list("b b f b f b")
b8.reach("BB")
b8.advance(2, "8 1B")

# 1. MIN #8  Jamey Carroll (X - 22 - 25)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)

# 2. MIN #7  Joe Mauer (22 - 25 - 8)
b8.new_ab()
b8.pitch_list("d f f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIN #61 Jared Burton
t9 = game.new_inning()

# Pitching change (MIN): #61 Jared Burton replaces #52 Brian Duensing
t9.pitching_substitution(61)

# Defensive switch (MIN): #22 Wilkin Ramirez moves to CF
t9.defensive_switch(22, "8")

# Defensive switch (MIN): #16 Josh Willingham moves to LF
t9.defensive_switch(16, "7")

# 1. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G2-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("s b b b c b")
t9.reach("BB")
t9.advance(4, "15 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t9.new_ab()
t9.pitch_list("c c b 1")
t9.hit(4, rbis=2)

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("s b")
t9.hit(1)
t9.advance(2, "12 BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
t9.new_ab()
t9.pitch_list("c s f b b b b")
t9.reach("BB")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t9.new_ab()
t9.pitch_list("c f f f d")
t9.out("F7")

# 7. BOS #16 Will Middlebrooks (X - 34 - 12)
t9.new_ab()
t9.pitch_list("f b f d f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #36 Junichi Tazawa
b9 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
b9.pitching_substitution(36)

# 3. MIN #33 Justin Morneau (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "24 1B")

# 4. MIN #24 Trevor Plouffe (X - X - 33)
b9.new_ab()
b9.pitch_list("b")
b9.hit(1)

# 5. MIN #31 Oswaldo Arcia (X - 33 - 24)
b9.new_ab()
b9.pitch_list("s f s")
b9.out("K")

# 6. MIN #22 Wilkin Ramirez (X - 33 - 24)
b9.new_ab()
b9.pitch_list("b f d s s")
b9.out("K")

# 7. MIN #27 Chris Parmelee (X - 33 - 24)
b9.new_ab()
b9.pitch_list("c f b")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41, is_away_team=True)

# Loser team: MIN
# LP: MIN #60 Pedro Hernandez
game.losing_pitcher(60)

# print(game)
game.generate_scorecard()
