import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2013-05-08
# https://www.baseball-reference.com/boxes/BOS/BOS201305080.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2013/05/08/347245/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-08 19:10-22:52",
        "at": "Fenway Park, Boston, MA",
        "att": "29,969",
        "temp": "63F, Cloudy",
        "wind": "17mph, In From RF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 60,
            "roster": {
                # Lineup
                8: "Jamey Carroll",
                7: "Joe Mauer",
                16: "Josh Willingham",
                33: "Justin Morneau",
                24: "Trevor Plouffe",
                9: "Ryan Doumit",
                31: "Oswaldo Arcia",
                32: "Aaron Hicks",
                25: "Pedro Florimón",
                # Starting pitcher
                60: "Pedro Hernandez",
                # Bench
                27: "Chris Parmelee",
                22: "Wilkin Ramirez",
                5: "Eduardo Escobar",
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
                [16, "7"],
                [33, "3"],
                [24, "5"],
                [9, "0"],
                [31, "9"],
                [32, "8"],
                [25, "6"],
            ],
            "bench": [
                [27, "1B"],
                [22, "LF"],
                [5, "3B"],
                [2, "2B"],
            ],
            "bullpen": [15, 30, 58, 20, 50, 61, 37, 52, 57, 51, 49],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 64,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                23: "Pedro Ciriaco",
                # Starting pitcher
                64: "Allen Webster",
                # Bench
                37: "Mike Carp",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                3: "David Ross",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
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
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [23, "5"],
            ],
            "bench": [
                [37, "1B"],
                [16, "3B"],
                [29, "LF"],
                [3, "C"],
            ],
            "bullpen": [63, 41, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Ed Hickox",
            "1B": "Lance Barksdale",
            "2B": "Cory Blaser",
            "3B": "Jeff Nelson",
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
# Pitching: BOS #64 Allen Webster
t1 = game.new_inning()

# 1. MIN #8  Jamey Carroll (X - X - X)
t1.new_ab()
t1.pitch_list("c c f s")
t1.out("K")

# 2. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c b")
t1.reach("BB")
t1.advance(2, "16 BB")
t1.advance(4, "33 2B")

# 3. MIN #16 Josh Willingham (X - X - 7)
t1.new_ab()
t1.pitch_list("f d b b b")
t1.reach("BB")
t1.advance(3, "33 2B")
t1.advance(4, "24 SF8")

# 4. MIN #33 Justin Morneau (X - 7 - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("b b")
t1.hit(2, rbis=1)
t1.advance(3, "24 SF8")
t1.advance(4, "9 HR")

# 5. MIN #24 Trevor Plouffe (16 - 33 - X)
t1.new_ab(is_risp=True)
t1.out("SF8", rbis=1)

# 6. MIN #9  Ryan Doumit (33 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c s b")
t1.hit(4, rbis=2)

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t1.new_ab()
t1.pitch_list("s f b")
t1.hit(1)

# 8. MIN #32 Aaron Hicks (X - X - 31)
t1.new_ab()
t1.pitch_list("b s b 1 f s")
t1.out("K")


# Bot 1st
# Pitching: MIN #60 Pedro Hernandez
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f c")
b1.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(3, "15 1B")
b1.advance(4, "5 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("c f d 1 1")
b1.hit(1)
b1.advance(2, "12 BB")
b1.advance(4, "5 HR")

# 4. BOS #34 David Ortiz (18 - X - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b 1 s f s")
b1.out("K")

# 5. BOS #12 Mike Napoli (18 - X - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("1 b b b b")
b1.reach("BB")
b1.advance(4, "5 HR")

# 6. BOS #5  Jonny Gomes (18 - 15 - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.hit(4, rbis=4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.hit(2)
b1.advance(4, "7 1B")

# 8. BOS #7  Stephen Drew (X - 39 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("f c")
b1.hit(1, rbis=1)
b1.thrown_out(2, "9-6", 3, 60)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #64 Allen Webster
t2 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
t2.new_ab()
t2.pitch_list("b c b c b")
t2.hit(4)

# 1. MIN #8  Jamey Carroll (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b b")
t2.reach("BB")
t2.advance(3, "7 2B")
t2.advance(4, "33 SF8")

# 2. MIN #7  Joe Mauer (X - X - 8)
t2.new_ab()
t2.pitch_list("c")
t2.hit(2)
t2.advance(3, "33 SF8")
t2.advance(4, "24 2B")

# 3. MIN #16 Josh Willingham (8 - 7 - X)
t2.new_ab(is_risp=True)
t2.out("P4")

# 4. MIN #33 Justin Morneau (8 - 7 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b f")
t2.out("SF8", rbis=1)

# 5. MIN #24 Trevor Plouffe (7 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c s")
t2.hit(2, rbis=1)
t2.advance(3, "31 1B")
t2.advance(4, "32 1B")

# Pitching change (BOS): #22 Felix Doubront replaces #64 Allen Webster
t2.pitching_substitution(22)

# 6. MIN #9  Ryan Doumit (X - 24 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(2, "31 1B")
t2.advance(4, "32 1B")

# 7. MIN #31 Oswaldo Arcia (X - 24 - 9)
t2.new_ab(is_risp=True)
t2.pitch_list("b b f")
t2.hit(1)
t2.advance(2, "32 1B")
t2.advance(4, "25 2B")

# 8. MIN #32 Aaron Hicks (24 - 9 - 31)
t2.new_ab(is_risp=True)
t2.pitch_list("b c f")
t2.hit(1, rbis=2)
t2.advance(4, "25 2B")

# 9. MIN #25 Pedro Florimón (X - 31 - 32)
t2.new_ab(is_risp=True)
t2.pitch_list("b d")
t2.hit(2, rbis=2)

# 1. MIN #8  Jamey Carroll (X - 25 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b c s f b s")
t2.out("K")


# Bot 2nd
# Pitching: MIN #60 Pedro Hernandez
b2 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b2.new_ab()
b2.pitch_list("c b s f f")
b2.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("L8")

# 2. BOS #18 Shane Victorino (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b2.new_ab()
b2.pitch_list("b b f c f b")
b2.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c s b")
b2.out("G1-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t3.new_ab()
t3.pitch_list("b f c b")
t3.out("G4-3")

# 3. MIN #16 Josh Willingham (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c c")
t3.out("!K")

# 4. MIN #33 Justin Morneau (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "24 FC5-4", 3, 22)

# 5. MIN #24 Trevor Plouffe (X - X - 33)
t3.new_ab()
t3.pitch_list("s")
t3.reach("FC5-4")


# Bot 3rd
# Pitching: MIN #57 Ryan Pressly
b3 = game.new_inning()

# Pitching change (MIN): #57 Ryan Pressly replaces #60 Pedro Hernandez
b3.pitching_substitution(57)

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.out("G6-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("s c s")
b3.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(1)

# 8. BOS #7  Stephen Drew (X - X - 39)
b3.new_ab()
b3.pitch_list("b b s")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 6. MIN #9  Ryan Doumit (X - X - X)
t4.new_ab()
t4.pitch_list("b f f")
t4.hit(1)
t4.advance(2, "31 1B")
t4.advance(3, "32 PB")
t4.advance(4, "25 DP4-6-3")

# 7. MIN #31 Oswaldo Arcia (X - X - 9)
t4.new_ab()
t4.pitch_list("c f d")
t4.hit(1)
t4.advance(2, "32 PB")
t4.advance(3, "25 DP4-6-3")

# 8. MIN #32 Aaron Hicks (X - 9 - 31)
t4.new_ab(is_risp=True)
t4.pitch_list("d b b c b")
t4.pb()
t4.reach("BB")
t4.thrown_out(2, "25 DP4-6-3", 1, 22)

# 9. MIN #25 Pedro Florimón (9 - 31 - 32)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.out("DP4-6-3")

# 1. MIN #8  Jamey Carroll (31 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c b f")
t4.out("G5-3")


# Bot 4th
# Pitching: MIN #57 Ryan Pressly
b4 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(2, "2 BB")
b4.advance(3, "18 FC4-6")

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
b4.new_ab()
b4.pitch_list("b b b c f b")
b4.reach("BB")
b4.thrown_out(2, "18 FC4-6", 1, 57)

# 2. BOS #18 Shane Victorino (X - 23 - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b b c")
b4.reach("FC4-6")
b4.advance(2, "15 G3")

# 3. BOS #15 Dustin Pedroia (23 - X - 18)
b4.new_ab(is_risp=True)
b4.pitch_list("c f")
b4.out("G3")

# 4. BOS #34 David Ortiz (23 - 18 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b f f")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.hit(2)
t5.advance(3, "33 G4-3")
t5.advance(4, "24 1B")

# 3. MIN #16 Josh Willingham (X - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c c b f f b f c")
t5.out("!K")

# 4. MIN #33 Justin Morneau (X - 7 - X)
t5.new_ab(is_risp=True)
t5.out("G4-3")

# 5. MIN #24 Trevor Plouffe (7 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("d b")
t5.hit(1, rbis=1)
t5.advance(2, "9 1B")
t5.advance(4, "31 2B")

# 6. MIN #9  Ryan Doumit (X - X - 24)
t5.new_ab()
t5.hit(1)
t5.advance(3, "31 2B")

# 7. MIN #31 Oswaldo Arcia (X - 24 - 9)
t5.new_ab(is_risp=True)
t5.pitch_list("c s f")
t5.hit(2, rbis=1)

# 8. MIN #32 Aaron Hicks (9 - 31 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c b t")
t5.out("G6-3")


# Bot 5th
# Pitching: MIN #57 Ryan Pressly
b5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c b c")
b5.hit(1)

# 6. BOS #5  Jonny Gomes (X - X - 12)
b5.new_ab()
b5.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b5.new_ab()
b5.pitch_list("c s b c")
b5.out("!K")

# 8. BOS #7  Stephen Drew (X - X - 12)
b5.new_ab()
b5.pitch_list("b b c")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 1. MIN #8  Jamey Carroll (X - X - X)
t6.new_ab()
t6.pitch_list("c b f f")
t6.out("G4-3")

# 2. MIN #7  Joe Mauer (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f f s")
t6.out("K")


# Bot 6th
# Pitching: MIN #57 Ryan Pressly
b6 = game.new_inning()

# 9. BOS #23 Pedro Ciriaco (X - X - X)
b6.new_ab()
b6.pitch_list("c c f t")
b6.out("KT")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f b f")
b6.out("F7")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c f f")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# Defensive change (BOS): #29 Daniel Nava replaces #18 Shane Victorino (RF), playing RF, batting 2nd
t7.defensive_substitution(2, 29, "9")

# 3. MIN #16 Josh Willingham (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.error(5)
t7.reach("E5")
t7.advance(2, "24 1B")

# 4. MIN #33 Justin Morneau (X - X - 16)
t7.new_ab()
t7.pitch_list("b f b f f")
t7.out("F8")

# 5. MIN #24 Trevor Plouffe (X - X - 16)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.thrown_out(2, "9 DP8-6-4-3", 2, 22)

# 6. MIN #9  Ryan Doumit (X - 16 - 24)
t7.new_ab(is_risp=True)
t7.pitch_list("f")
t7.reach("DP8-6-4-3")
t7.thrown_out(2, "XXXXX4", 3, 22)


# Bot 7th
# Pitching: MIN #50 Casey Fien
b7 = game.new_inning()

# Pitching change (MIN): #50 Casey Fien replaces #57 Ryan Pressly
b7.pitching_substitution(50)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(2, "34 G1")
b7.advance(3, "12 1B")
b7.advance(4, "5 SF7")

# 4. BOS #34 David Ortiz (X - X - 15)
b7.new_ab()
b7.pitch_list("b b b c")
b7.out("G1")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b s")
b7.hit(1)
# Offensive change (BOS): Pinch-runner #37 Mike Carp replaces #12 Mike Napoli
b7.offensive_substitution(5, 37, "PR")
b7.atbase("PR")

# 6. BOS #5  Jonny Gomes (15 - X - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("s b b")
b7.out("SF7", rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b7.new_ab()
b7.pitch_list("b b b c f")
b7.out("P6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #30 Andrew Miller
t8 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #22 Felix Doubront
t8.pitching_substitution(30)

# Defensive switch (BOS): #37 Mike Carp moves to 1B
t8.defensive_switch(37, "3")

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t8.new_ab()
t8.pitch_list("b f b c s")
t8.out("K")

# 8. MIN #32 Aaron Hicks (X - X - X)
t8.new_ab()
t8.pitch_list("s c b s")
t8.out("K")

# 9. MIN #25 Pedro Florimón (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b c")
t8.out("!K")


# Bot 8th
# Pitching: MIN #52 Brian Duensing
b8 = game.new_inning()

# Pitching change (MIN): #52 Brian Duensing replaces #50 Casey Fien
b8.pitching_substitution(52)

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c b f")
b8.hit(1)
b8.advance(2, "23 BB")
b8.advance(3, "2 FC4-6")
b8.advance(4, "29 SF8")

# 9. BOS #23 Pedro Ciriaco (X - X - 7)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.thrown_out(2, "2 FC4-6", 1, 52)

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 23)
b8.new_ab(is_risp=True)
b8.pitch_list("f f f")
b8.reach("FC4-6")

# 2. BOS #29 Daniel Nava (7 - X - 2)
b8.new_ab(is_risp=True)
b8.pitch_list("f")
b8.out("SF8", rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b8.new_ab()
b8.pitch_list("b")
b8.out("(F)P3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #36 Junichi Tazawa
t9 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #30 Andrew Miller
t9.pitching_substitution(36)

# 1. MIN #8  Jamey Carroll (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(3, "7 1B")
t9.advance(4, "33 SF8")

# 2. MIN #7  Joe Mauer (X - X - 8)
t9.new_ab()
t9.pitch_list("b f b s f")
t9.hit(1)
t9.advance(2, "16 HBP")
t9.advance(3, "33 SF8")

# 3. MIN #16 Josh Willingham (8 - X - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.reach("HBP")
# Offensive change (MIN): Pinch-runner #22 Wilkin Ramirez replaces #16 Josh Willingham
t9.offensive_substitution(3, 22, "PR")
t9.atbase("PR")

# 4. MIN #33 Justin Morneau (8 - 7 - 16)
t9.new_ab(is_risp=True)
t9.pitch_list("b f s")
t9.out("SF8", rbis=1)

# 5. MIN #24 Trevor Plouffe (7 - X - 22)
t9.new_ab(is_risp=True)
t9.pitch_list("c s c")
t9.out("!K")

# 6. MIN #9  Ryan Doumit (7 - X - 22)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("F7")


# Bot 9th
# Pitching: MIN #15 Glen Perkins
b9 = game.new_inning()

# Pitching change (MIN): #15 Glen Perkins replaces #52 Brian Duensing
b9.pitching_substitution(15)

# Defensive switch (MIN): #22 Wilkin Ramirez moves to LF
b9.defensive_switch(22, "7")

# 4. BOS #34 David Ortiz (X - X - X)
b9.new_ab()
b9.pitch_list("c b s f f b s")
b9.out("K")

# 5. BOS #37 Mike Carp (X - X - X)
b9.new_ab()
b9.pitch_list("c f b s")
b9.out("K")

# 6. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("b c b")
b9.out("(F)P2")

# Winning team: MIN
# WP: MIN #57 Ryan Pressly
game.winning_pitcher(57, is_away_team=True)

# Loser team: BOS
# LP: BOS #64 Allen Webster
game.losing_pitcher(64)

# print(game)
game.generate_scorecard()
