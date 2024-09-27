import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2013-05-09
# https://www.baseball-reference.com/boxes/BOS/BOS201305090.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2013/05/09/347257/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-09 19:10-22:14",
        "at": "Fenway Park, Boston, MA",
        "att": "31,571",
        "temp": "57F, Cloudy",
        "wind": "6mph, R To L",
        "away": {
            "team": "Minnesota Twins",
            "starter": 30,
            "roster": {
                # Lineup
                2: "Brian Dozier",
                7: "Joe Mauer",
                16: "Josh Willingham",
                33: "Justin Morneau",
                24: "Trevor Plouffe",
                9: "Ryan Doumit",
                31: "Oswaldo Arcia",
                32: "Aaron Hicks",
                25: "Pedro Florimón",
                # Starting pitcher
                30: "Kevin Correia",
                # Bench
                27: "Chris Parmelee",
                22: "Wilkin Ramirez",
                8: "Jamey Carroll",
                5: "Eduardo Escobar",
                # Bullpen
                15: "Glen Perkins",
                58: "Scott Diamond",
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
            "lefties": [15, 58, 60, 52],
            "lineup": [
                [2, "4"],
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
                [8, "2B"],
                [5, "3B"],
            ],
            "bullpen": [15, 58, 60, 20, 50, 61, 37, 52, 57, 51, 49],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                5: "Jonny Gomes",
                23: "Pedro Ciriaco",
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
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [5, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 65, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Lance Barksdale",
            "1B": "Cory Blaser",
            "2B": "Jeff Nelson",
            "3B": "Ed Hickox",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. MIN #2  Brian Dozier (X - X - X)
t1.new_ab()
t1.pitch_list("c s b s")
t1.out("K")

# 2. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("c c f s")
t1.out("K")

# 3. MIN #16 Josh Willingham (X - X - X)
t1.new_ab()
t1.pitch_list("c f c")
t1.out("!K")


# Bot 1st
# Pitching: MIN #30 Kevin Correia
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c c")
b1.hit(1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F7")

# 4. BOS #34 David Ortiz (X - X - 18)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. MIN #33 Justin Morneau (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F9")

# 5. MIN #24 Trevor Plouffe (X - X - X)
t2.new_ab()
t2.pitch_list("f b t f s")
t2.out("K")

# 6. MIN #9  Ryan Doumit (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("F9")


# Bot 2nd
# Pitching: MIN #30 Kevin Correia
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b f")
b2.out("G4-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F8")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2)

# 8. BOS #7  Stephen Drew (X - 16 - X)
b2.new_ab()
b2.pitch_list("c b f b b")
b2.out("G3-1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.out("F7")

# 8. MIN #32 Aaron Hicks (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c t f f")
t3.out("L1")

# 9. MIN #25 Pedro Florimón (X - X - X)
t3.new_ab()
t3.hit(1)
t3.advance(2, "2 SB")

# 1. MIN #2  Brian Dozier (X - X - 25)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G3")


# Bot 3rd
# Pitching: MIN #30 Kevin Correia
b3 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("f b b f b")
b3.out("(F)P2")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("L8")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b f")
b3.hit(2)
b3.advance(4, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b3.new_ab()
b3.hit(1, rbis=1)

# 4. BOS #34 David Ortiz (X - X - 15)
b3.new_ab()
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t4.new_ab()
t4.pitch_list("c c b f s")
t4.out("K")

# 3. MIN #16 Josh Willingham (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.out("G5-3")

# 4. MIN #33 Justin Morneau (X - X - X)
t4.new_ab()
t4.hit(1)

# 5. MIN #24 Trevor Plouffe (X - X - 33)
t4.new_ab()
t4.pitch_list("c c")
t4.out("F9")


# Bot 4th
# Pitching: MIN #30 Kevin Correia
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("f b c")
b4.out("G5-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b f")
b4.hit(1)
b4.advance(2, "16 G6-3")
b4.advance(4, "7 1B")

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b4.new_ab()
b4.pitch_list("b f c f b")
b4.out("G6-3")

# 8. BOS #7  Stephen Drew (X - 29 - X)
b4.new_ab()
b4.pitch_list("s b")
b4.hit(1, rbis=1)

# 9. BOS #3  David Ross (X - X - 7)
b4.new_ab()
b4.pitch_list("b b t s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 6. MIN #9  Ryan Doumit (X - X - X)
t5.new_ab()
t5.pitch_list("c s b")
t5.out("G4-3")

# 7. MIN #31 Oswaldo Arcia (X - X - X)
t5.new_ab()
t5.pitch_list("f b b f b f")
t5.hit(3)
t5.advance(4, "32 2B")

# 8. MIN #32 Aaron Hicks (31 - X - X)
t5.new_ab()
t5.pitch_list("b 3 s")
t5.hit(2, rbis=1)

# 9. MIN #25 Pedro Florimón (X - 32 - X)
t5.new_ab()
t5.pitch_list("b c b c b f t")
t5.out("KT")

# 1. MIN #2  Brian Dozier (X - 32 - X)
t5.new_ab()
t5.pitch_list("d f b f c")
t5.out("!K")


# Bot 5th
# Pitching: MIN #30 Kevin Correia
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b")
b5.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
b5.new_ab()
b5.pitch_list("c b b b")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 2. MIN #7  Joe Mauer (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.hit(1)
t6.advance(2, "33 BB")
t6.error(1)
t6.advance(3, "24 FC1")
t6.advance("U", "24 E1")

# 3. MIN #16 Josh Willingham (X - X - 7)
t6.new_ab()
t6.out("F8")

# 4. MIN #33 Justin Morneau (X - X - 7)
t6.new_ab()
t6.pitch_list("c b b f b f b")
t6.reach("BB")
t6.advance(3, "24 E1")
t6.advance("U", "9 SF9")

# 5. MIN #24 Trevor Plouffe (X - 7 - 33)
t6.new_ab()
t6.pitch_list("s")
t6.reach("FC1")
t6.advance("U", "31 HR")

# 6. MIN #9  Ryan Doumit (33 - X - 24)
t6.new_ab()
t6.pitch_list("b 1")
t6.out("SF9", rbis=1)

# 7. MIN #31 Oswaldo Arcia (X - X - 24)
t6.new_ab()
t6.pitch_list("1")
t6.hit("U", rbis=2)

# 8. MIN #32 Aaron Hicks (X - X - X)
t6.new_ab()
t6.out("L9")


# Bot 6th
# Pitching: MIN #30 Kevin Correia
b6 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f b f")
b6.hit(2)
b6.advance(4, "29 1B")

# 6. BOS #29 Daniel Nava (X - 12 - X)
b6.new_ab()
b6.pitch_list("f")
b6.hit(1, rbis=1)
b6.thrown_out(2, "16 FC6-4", 1, 30)

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b6.new_ab()
b6.pitch_list("b c")
b6.reach("FC6-4")

# Pitching change (MIN): #52 Brian Duensing replaces #30 Kevin Correia
b6.pitching_substitution(52)

# 8. BOS #7  Stephen Drew (X - X - 16)
b6.new_ab()
b6.pitch_list("c b")
b6.out("L7")

# 9. BOS #3  David Ross (X - X - 16)
b6.new_ab()
b6.pitch_list("b b s c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 9. MIN #25 Pedro Florimón (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("B1-3")

# 1. MIN #2  Brian Dozier (X - X - X)
t7.new_ab()
t7.pitch_list("m c f")
t7.out("G5-3")

# 2. MIN #7  Joe Mauer (X - X - X)
t7.new_ab()
t7.pitch_list("b f f s")
t7.out("K")


# Bot 7th
# Pitching: MIN #52 Brian Duensing
b7 = game.new_inning()

# Defensive change (MIN): #5 Eduardo Escobar replaces #25 Pedro Florimón (SS), playing SS, batting 9th
b7.defensive_substitution(9, 5, "6")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b f f c")
b7.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.out("P3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b7.new_ab()
b7.pitch_list("b b")
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #41 John Lackey
t8.pitching_substitution(19)

# 3. MIN #16 Josh Willingham (X - X - X)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")

# 4. MIN #33 Justin Morneau (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b b f t")
t8.out("KT")

# 5. MIN #24 Trevor Plouffe (X - X - X)
t8.new_ab()
t8.pitch_list("s c s")
t8.out("K")


# Bot 8th
# Pitching: MIN #61 Jared Burton
b8 = game.new_inning()

# Pitching change (MIN): #61 Jared Burton replaces #52 Brian Duensing
b8.pitching_substitution(61)

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("b b b d")
b8.reach("BB")
b8.advance(2, "16 E6")

# 7. BOS #16 Will Middlebrooks (X - X - 29)
b8.new_ab()
b8.pitch_list("c b 1 b f f f f f b")
b8.error(6)
b8.reach("E6")

# 8. BOS #7  Stephen Drew (X - 29 - 16)
b8.new_ab()
b8.pitch_list("c b f c")
b8.out("!K")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #3 David Ross, batting 9th
b8.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (X - 29 - 16)
b8.new_ab()
b8.pitch_list("c c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Craig Breslow
t9 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #19 Koji Uehara
t9.pitching_substitution(32)

# Defensive change (BOS): #39 Jarrod Saltalamacchia replaces #37 Mike Carp (PH), playing C, batting 9th
t9.defensive_substitution(9, 39, "2")

# 6. MIN #9  Ryan Doumit (X - X - X)
t9.new_ab()
t9.pitch_list("b b b")
t9.error(5)
t9.reach("E5")
t9.advance(2, "31 G5-3")

# 7. MIN #31 Oswaldo Arcia (X - X - 9)
t9.new_ab()
t9.pitch_list("s d b f")
t9.out("G5-3")

# 8. MIN #32 Aaron Hicks (X - 9 - X)
t9.new_ab()
t9.pitch_list("b c d")
t9.out("G6-3")

# 9. MIN #5  Eduardo Escobar (X - 9 - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G1-3")


# Bot 9th
# Pitching: MIN #15 Glen Perkins
b9 = game.new_inning()

# Pitching change (MIN): #15 Glen Perkins replaces #61 Jared Burton
b9.pitching_substitution(15)

# Defensive change (MIN): #27 Chris Parmelee replaces #31 Oswaldo Arcia (RF), playing RF, batting 7th
b9.defensive_substitution(7, 27, "9")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b9.new_ab()
b9.pitch_list("c f b b f b b")
b9.reach("BB")

# 2. BOS #18 Shane Victorino (X - X - 2)
b9.new_ab()
b9.pitch_list("c b f f c")
b9.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b9.new_ab()
b9.pitch_list("f s b d f f f b c")
b9.out("!K")

# 4. BOS #34 David Ortiz (X - X - 2)
b9.new_ab()
b9.pitch_list("b b")
b9.out("G3")

# Winning team: MIN
# WP: MIN #30 Kevin Correia
game.winning_pitcher(30, is_away_team=True)
# SV: MIN #15 Glen Perkins
game.save_pitcher(15, is_away_team=True)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41)

# print(game)
game.generate_scorecard()
