import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2013-05-06
# https://www.baseball-reference.com/boxes/BOS/BOS201305060.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2013/05/06/347219/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-06 19:11-23:55",
        "at": "Fenway Park, Boston, MA",
        "att": "31,088",
        "temp": "53F, Partly Cloudy",
        "wind": "12mph, In From RF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 49,
            "roster": {
                # Lineup
                2: "Brian Dozier",
                7: "Joe Mauer",
                16: "Josh Willingham",
                33: "Justin Morneau",
                27: "Chris Parmelee",
                24: "Trevor Plouffe",
                31: "Oswaldo Arcia",
                32: "Aaron Hicks",
                25: "Pedro Florimón",
                # Starting pitcher
                49: "Vance Worley",
                # Bench
                22: "Wilkin Ramirez",
                8: "Jamey Carroll",
                5: "Eduardo Escobar",
                9: "Ryan Doumit",
                # Bullpen
                15: "Glen Perkins",
                30: "Kevin Correia",
                58: "Scott Diamond",
                60: "Pedro Hernandez",
                20: "Josh Roenicke",
                50: "Casey Fien",
                61: "Jared Burton",
                37: "Mike Pelfrey",
                52: "Brian Duensing",
                57: "Ryan Pressly",
                51: "Anthony Swarzak",
            },
            "lefties": [15, 58, 60, 52],
            "lineup": [
                [2, "4"],
                [7, "2"],
                [16, "7"],
                [33, "3"],
                [27, "9"],
                [24, "5"],
                [31, "0"],
                [32, "8"],
                [25, "6"],
            ],
            "bench": [
                [22, "LF"],
                [8, "2B"],
                [5, "3B"],
                [9, "C"],
            ],
            "bullpen": [15, 30, 58, 60, 20, 50, 61, 37, 52, 57, 51],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
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
                [29, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 41, 30, 32, 52, 31, 59, 36, 19, 22, 46],
        },
        "umpires": {
            "HP": "Cory Blaser",
            "1B": "Jeff Nelson",
            "2B": "Ed Hickox",
            "3B": "Lance Barksdale",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. MIN #2  Brian Dozier (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F8")

# 2. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(2)
t1.advance(4, "16 2B")

# 3. MIN #16 Josh Willingham (X - 7 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c t b")
t1.hit(2, rbis=1)
t1.advance(4, "33 1B")

# 4. MIN #33 Justin Morneau (X - 16 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c f")
t1.hit(1, rbis=1)
t1.advance(2, "27 BB")
t1.advance(3, "24 BB")

# 5. MIN #27 Chris Parmelee (X - X - 33)
t1.new_ab()
t1.pitch_list("c b b 1 b f b")
t1.reach("BB")
t1.advance(2, "24 BB")

# 6. MIN #24 Trevor Plouffe (X - 33 - 27)
t1.new_ab(is_risp=True)
t1.pitch_list("b f b f d f b")
t1.reach("BB")

# 7. MIN #31 Oswaldo Arcia (33 - 27 - 24)
t1.new_ab(is_risp=True)
t1.pitch_list("b b s s b f f s")
t1.out("K")

# 8. MIN #32 Aaron Hicks (33 - 27 - 24)
t1.new_ab(is_risp=True)
t1.pitch_list("c f s")
t1.out("K")


# Bot 1st
# Pitching: MIN #49 Vance Worley
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(1)
b1.thrown_out(2, "15 DP4-6-3", 2, 49)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("b c 1 f")
b1.out("DP4-6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
t2.new_ab()
t2.pitch_list("c c b c")
t2.out("!K")

# 1. MIN #2  Brian Dozier (X - X - X)
t2.new_ab()
t2.pitch_list("c s b c")
t2.out("!K")

# 2. MIN #7  Joe Mauer (X - X - X)
t2.new_ab()
t2.pitch_list("c s")
t2.out("G3-1")


# Bot 2nd
# Pitching: MIN #49 Vance Worley
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("c c f")
b2.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b f b s b")
b2.out("G5-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 3. MIN #16 Josh Willingham (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F9")

# 4. MIN #33 Justin Morneau (X - X - X)
t3.new_ab()
t3.pitch_list("b s c f f b t")
t3.out("KT")

# 5. MIN #27 Chris Parmelee (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s b f t")
t3.out("KT")


# Bot 3rd
# Pitching: MIN #49 Vance Worley
b3 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(2)
b3.advance(3, "16 G6-3")

# 8. BOS #16 Will Middlebrooks (X - 39 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c c")
b3.out("G6-3")

# 9. BOS #7  Stephen Drew (39 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b f c c")
b3.out("!K")

# 1. BOS #2  Jacoby Ellsbury (39 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 6. MIN #24 Trevor Plouffe (X - X - X)
t4.new_ab()
t4.pitch_list("c s c")
t4.out("!K")

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t4.new_ab()
t4.pitch_list("c s f b f b f")
t4.hit(2)
t4.advance(4, "32 2B")

# 8. MIN #32 Aaron Hicks (X - 31 - X)
t4.new_ab(is_risp=True)
t4.hit(2, rbis=1)

# 9. MIN #25 Pedro Florimón (X - 32 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b s b s c")
t4.out("!K")

# 1. MIN #2  Brian Dozier (X - 32 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b c b")
t4.out("G6-3")


# Bot 4th
# Pitching: MIN #49 Vance Worley
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c t")
b4.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.thrown_out(2, "34 DP1-6-3", 1, 49)

# 4. BOS #34 David Ortiz (X - X - 15)
b4.new_ab()
b4.pitch_list("c")
b4.out("DP1-6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("f c f b f b b")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t5.new_ab()
t5.hit(2)
t5.advance(3, "16 1B")
t5.advance(4, "33 SF7")

# 3. MIN #16 Josh Willingham (X - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b f")
t5.hit(1)
t5.advance(2, "27 G4-1")

# 4. MIN #33 Justin Morneau (7 - X - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("f s")
t5.out("SF7", rbis=1)

# 5. MIN #27 Chris Parmelee (X - X - 16)
t5.new_ab()
t5.pitch_list("f s b b")
t5.out("G4-1")

# 6. MIN #24 Trevor Plouffe (X - 16 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("d f c b")
t5.error(3)
t5.out("F8")


# Bot 5th
# Pitching: MIN #49 Vance Worley
b5 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b c s f f b f b")
b5.hit(2)
b5.advance(4, "7 1B")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b s b s")
b5.out("K")

# 8. BOS #16 Will Middlebrooks (X - 29 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f t s")
b5.out("K")

# 9. BOS #7  Stephen Drew (X - 29 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.hit(1, rbis=1)
b5.advance(3, "2 2B")
b5.thrown_out(4, "2 8-6-2", 3, 49)

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b5.new_ab()
b5.pitch_list("1 b b b c")
b5.hit(2)


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t6.new_ab()
t6.pitch_list("b f s b f s")
t6.out("K")

# 8. MIN #32 Aaron Hicks (X - X - X)
t6.new_ab()
t6.pitch_list("c m f b")
t6.out("G4-3")

# 9. MIN #25 Pedro Florimón (X - X - X)
t6.new_ab()
t6.out("G4-3")


# Bot 6th
# Pitching: MIN #49 Vance Worley
b6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f b")
b6.hit(1)
b6.advance(2, "15 1B")
b6.advance(3, "34 DP3-6-1")
b6.advance(4, "12 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b6.new_ab()
b6.pitch_list("b 1 f f f 1")
b6.hit(1)
b6.thrown_out(2, "34 DP3-6-1", 1, 52)

# Pitching change (MIN): #52 Brian Duensing replaces #49 Vance Worley
b6.pitching_substitution(52)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b6.new_ab(is_risp=True)
b6.pitch_list("d b")
b6.out("DP3-6-1")

# 5. BOS #12 Mike Napoli (18 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f b d f")
b6.hit(1, rbis=1)
b6.advance(2, "29 WP")

# 6. BOS #29 Daniel Nava (X - X - 12)
b6.new_ab(is_risp=True)
b6.pitch_list("b b f d b")
b6.wp()
b6.reach("BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
b6.new_ab(is_risp=True)
b6.pitch_list("b b b c s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #63 Alex Wilson
t7 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #11 Clay Buchholz
t7.pitching_substitution(63)

# 1. MIN #2  Brian Dozier (X - X - X)
t7.new_ab()
t7.pitch_list("c f b f b f f")
t7.hit(1)
t7.advance(2, "7 BB")

# 2. MIN #7  Joe Mauer (X - X - 2)
t7.new_ab()
t7.pitch_list("b c b b b")
t7.reach("BB")

# 3. MIN #16 Josh Willingham (X - 2 - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("f f b b s")
t7.out("K")

# Pitching change (BOS): #30 Andrew Miller replaces #63 Alex Wilson
t7.pitching_substitution(30)

# 4. MIN #33 Justin Morneau (X - 2 - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("b c f f f s")
t7.out("K")

# 5. MIN #27 Chris Parmelee (X - 2 - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("c c d s")
t7.out("K")


# Bot 7th
# Pitching: MIN #50 Casey Fien
b7 = game.new_inning()

# Pitching change (MIN): #50 Casey Fien replaces #52 Brian Duensing
b7.pitching_substitution(50)

# 8. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("f c b f")
b7.out("G5-3")

# 9. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b b f b")
b7.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("f b s b b f f")
b7.out("G3-1")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #30 Andrew Miller
t8.pitching_substitution(32)

# 6. MIN #24 Trevor Plouffe (X - X - X)
t8.new_ab()
t8.out("F9")

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t8.new_ab()
t8.pitch_list("c f b f s")
t8.out("K")

# 8. MIN #32 Aaron Hicks (X - X - X)
t8.new_ab()
t8.pitch_list("s c f f b")
t8.out("F8")


# Bot 8th
# Pitching: MIN #50 Casey Fien
b8 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("f b f b f b f f f")
b8.hit(4)

# Pitching change (MIN): #51 Anthony Swarzak replaces #50 Casey Fien
b8.pitching_substitution(51)

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("t c")
b8.hit(2)
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #34 David Ortiz
b8.offensive_substitution(4, 23, "PR")
b8.atbase("PR")
b8.thrown_out(3, "39 CS", 3, 51)

# 5. BOS #12 Mike Napoli (X - 34 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c")
b8.out("L3")

# 6. BOS #29 Daniel Nava (X - 34 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b s c b f b c")
b8.out("!K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 23 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c f f b f f f b b")
b8.reach("BB")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #52 Joel Hanrahan
t9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #32 Craig Breslow
t9.pitching_substitution(52)

# Defensive switch (BOS): #23 Pedro Ciriaco moves to DH
t9.defensive_switch(23, "0")

# Offensive change (MIN): Pinch-hitter #9 Ryan Doumit replaces #25 Pedro Florimón, batting 9th
t9.offensive_substitution(9, 9, "PH")

# 9. MIN #9  Ryan Doumit (X - X - X)
t9.new_ab()
t9.pitch_list("b c b")
t9.out("F7")

# 1. MIN #2  Brian Dozier (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b c")
t9.hit(4)

# 2. MIN #7  Joe Mauer (X - X - X)
t9.new_ab()
t9.pitch_list("c c f s")
t9.out("K")

# 3. MIN #16 Josh Willingham (X - X - X)
t9.new_ab()
t9.pitch_list("b f b b b")
t9.reach("BB")
# Offensive change (MIN): Pinch-runner #5 Eduardo Escobar replaces #16 Josh Willingham
t9.offensive_substitution(3, 5, "PR")
t9.atbase("PR")

# Pitching change (BOS): #59 Clayton Mortensen replaces #52 Joel Hanrahan
t9.pitching_substitution(59)

# 4. MIN #33 Justin Morneau (X - X - 16)
t9.new_ab()
t9.pitch_list("1 b")
t9.out("G5-3")


# Bot 9th
# Pitching: MIN #51 Anthony Swarzak
b9 = game.new_inning()

# Defensive switch (MIN): #5 Eduardo Escobar moves to SS
b9.defensive_switch(5, "6")

# Defensive switch (MIN): #9 Ryan Doumit moves to LF
b9.defensive_switch(9, "7")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b9.new_ab()
b9.pitch_list("b b b s s s")
b9.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("b s s f f b")
b9.hit(1)
b9.thrown_out(2, "2 DP4-6-3", 2, 51)

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b9.new_ab()
b9.out("DP4-6-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #59 Clayton Mortensen
t10 = game.new_inning()

# 5. MIN #27 Chris Parmelee (X - X - X)
t10.new_ab()
t10.pitch_list("b")
t10.out("G4-3")

# 6. MIN #24 Trevor Plouffe (X - X - X)
t10.new_ab()
t10.pitch_list("c b b b f b")
t10.reach("BB")
t10.advance(2, "31 BB")

# 7. MIN #31 Oswaldo Arcia (X - X - 24)
t10.new_ab()
t10.pitch_list("b f 1 f b 1 f 1 f b b")
t10.reach("BB")

# Offensive change (MIN): Pinch-hitter #22 Wilkin Ramirez replaces #32 Aaron Hicks, batting 8th
t10.offensive_substitution(8, 22, "PH")

# 8. MIN #22 Wilkin Ramirez (X - 24 - 31)
t10.new_ab(is_risp=True)
t10.pitch_list("b c c")
t10.out("P4")

# 9. MIN #9  Ryan Doumit (X - 24 - 31)
t10.new_ab(is_risp=True)
t10.pitch_list("c")
t10.out("G3-1")


# Bot 10th
# Pitching: MIN #51 Anthony Swarzak
b10 = game.new_inning()

# Defensive switch (MIN): #22 Wilkin Ramirez moves to CF
b10.defensive_switch(22, "8")

# 2. BOS #18 Shane Victorino (X - X - X)
b10.new_ab()
b10.pitch_list("c b b c")
b10.out("L8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b10.new_ab()
b10.pitch_list("b c f f b s")
b10.out("K")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #23 Pedro Ciriaco, batting 4th
b10.offensive_substitution(4, 37, "PH")

# 4. BOS #37 Mike Carp (X - X - X)
b10.new_ab()
b10.pitch_list("b b c b f s")
b10.out("K")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #59 Clayton Mortensen
t11 = game.new_inning()

# Defensive switch (BOS): #37 Mike Carp moves to DH
t11.defensive_switch(37, "0")

# 1. MIN #2  Brian Dozier (X - X - X)
t11.new_ab()
t11.pitch_list("b c b f t")
t11.out("KT")

# 2. MIN #7  Joe Mauer (X - X - X)
t11.new_ab()
t11.pitch_list("b f")
t11.out("G4-3")

# 3. MIN #5  Eduardo Escobar (X - X - X)
t11.new_ab()
t11.pitch_list("f b f")
t11.hit(1)

# 4. MIN #33 Justin Morneau (X - X - 5)
t11.new_ab()
t11.pitch_list("t 1 1 1 f d d 1 f 1 f")
t11.out("F7")


# Bot 11th
# Pitching: MIN #61 Jared Burton
b11 = game.new_inning()

# Pitching change (MIN): #61 Jared Burton replaces #51 Anthony Swarzak
b11.pitching_substitution(61)

# 5. BOS #12 Mike Napoli (X - X - X)
b11.new_ab()
b11.pitch_list("s f")
b11.out("G5-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b11.new_ab()
b11.pitch_list("b b")
b11.out("F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b11.new_ab()
b11.pitch_list("c f")
b11.hit(1)
b11.advance(2, "16 1B")
b11.advance(4, "7 2B")

# 8. BOS #16 Will Middlebrooks (X - X - 39)
b11.new_ab()
b11.pitch_list("c")
b11.hit(1)
b11.advance(3, "7 2B")

# 9. BOS #7  Stephen Drew (X - 39 - 16)
b11.new_ab(is_risp=True)
b11.pitch_list("c")
b11.hit(2, rbis=1)

# Winning team: BOS
# WP: BOS #59 Clayton Mortensen
game.winning_pitcher(59)

# Loser team: MIN
# LP: MIN #61 Jared Burton
game.losing_pitcher(61, is_away_team=True)

# print(game)
game.generate_scorecard()
