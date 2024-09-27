import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ OAK, 2013-07-12
# https://www.baseball-reference.com/boxes/OAK/OAK201307120.shtml
# https://www.mlb.com/gameday/red-sox-vs-athletics/2013/07/12/348125/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-12 22:09-01:15 +1",
        "at": "O.co Coliseum, Oakland, CA",
        "att": "27,084",
        "temp": "61F, Clear",
        "wind": "7mph, Out To RF",
        "away": {
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
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                26: "Brock Holt",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                44: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                40: "Andrew Bailey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [10, "6"],
                [26, "5"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [44, "CF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 40, 67, 32, 31, 36, 19, 54, 22, 46],
        },
        "home": {
            "team": "Oakland Athletics",
            "starter": 11,
            "roster": {
                # Lineup
                4: "Coco Crisp",
                5: "John Jaso",
                20: "Josh Donaldson",
                8: "Jed Lowrie",
                52: "Yoenis Cespedes",
                37: "Brandon Moss",
                16: "Josh Reddick",
                15: "Seth Smith",
                28: "Eric Sogard",
                # Starting pitcher
                11: "Jarrod Parker",
                # Bench
                36: "Derek Norris",
                7: "Nate Freiman",
                35: "Grant Green",
                25: "Chris Young",
                # Bullpen
                50: "Grant Balfour",
                64: "A.J. Griffin",
                40: "Bartolo Colon",
                60: "Jesse Chavez",
                48: "Ryan Cook",
                54: "Sonny Gray",
                62: "Sean Doolittle",
                57: "Tommy Milone",
                47: "Pat Neshek",
                61: "Dan Otero",
                13: "Jerry Blevins",
            },
            "lefties": [62, 57, 13],
            "lineup": [
                [4, "8"],
                [5, "2"],
                [20, "5"],
                [8, "6"],
                [52, "7"],
                [37, "3"],
                [16, "9"],
                [15, "0"],
                [28, "4"],
            ],
            "bench": [
                [36, "C"],
                [7, "1B"],
                [35, "2B"],
                [25, "CF"],
            ],
            "bullpen": [50, 64, 40, 60, 48, 54, 62, 57, 47, 61, 13],
        },
        "umpires": {
            "HP": "CB Bucknor",
            "1B": "Adam Hamari",
            "2B": "Bill Miller",
            "3B": "Todd Tichenor",
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
# Pitching: OAK #11 Jarrod Parker
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c c f")
t1.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("b 1 b b")
t1.out("F8")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3")

# 2. OAK #5  John Jaso (X - X - X)
b1.new_ab()
b1.pitch_list("c f b s")
b1.out("K")

# 3. OAK #20 Josh Donaldson (X - X - X)
b1.new_ab()
b1.pitch_list("c t b b f f b")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: OAK #11 Jarrod Parker
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b c b")
t2.hit(1)
t2.error(5)
t2.advance(2, "E5")
t2.advance(3, "39 F7")
t2.advance(4, "26 E2")

# 6. BOS #29 Daniel Nava (X - 12 - X)
t2.new_ab()
t2.pitch_list("b c")
t2.reach("HBP")
t2.advance(2, "39 F7")
t2.advance(4, "26 E2")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
t2.new_ab()
t2.pitch_list("f c b b f")
t2.out("F7")

# 8. BOS #10 Jose Iglesias (12 - 29 - X)
t2.new_ab()
t2.pitch_list("c f f b d b f")
t2.out("F9")

# 9. BOS #26 Brock Holt (12 - 29 - X)
t2.new_ab()
t2.pitch_list("b s b b f")
t2.hit(1, rbis=2)
t2.error(2)
t2.advance(2, "E2")
t2.advance(3, "T")

# 1. BOS #2  Jacoby Ellsbury (26 - X - X)
t2.new_ab()
t2.pitch_list("c b c d")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b2.new_ab()
b2.pitch_list("b f s b b d")
b2.reach("BB")
b2.advance(2, "16 SB")
b2.advance(3, "16 SB")

# 6. OAK #37 Brandon Moss (X - X - 52)
b2.new_ab()
b2.pitch_list("c")
b2.out("L8")

# 7. OAK #16 Josh Reddick (X - X - 52)
b2.new_ab()
b2.pitch_list("b c s b f d b")
b2.reach("BB")

# 8. OAK #15 Seth Smith (52 - X - 16)
b2.new_ab()
b2.pitch_list("d b f")
b2.out("G3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: OAK #11 Jarrod Parker
t3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c s b b")
t3.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b")
t3.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.out("L9")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 9. OAK #28 Eric Sogard (X - X - X)
b3.new_ab()
b3.pitch_list("c f f f f f")
b3.out("G4-3")

# 1. OAK #4  Coco Crisp (X - X - X)
b3.new_ab()
b3.pitch_list("b s b f c")
b3.out("!K")

# 2. OAK #5  John Jaso (X - X - X)
b3.new_ab()
b3.pitch_list("b b f")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: OAK #11 Jarrod Parker
t4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("t f b b c")
t4.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G3-1")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.out("F8")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 3. OAK #20 Josh Donaldson (X - X - X)
b4.new_ab()
b4.pitch_list("c s b b c")
b4.out("!K")

# 4. OAK #8  Jed Lowrie (X - X - X)
b4.new_ab()
b4.out("P6")

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.reach("HBP")
b4.advance(2, "37 BB")

# 6. OAK #37 Brandon Moss (X - X - 52)
b4.new_ab()
b4.pitch_list("s b f b d b")
b4.reach("BB")

# 7. OAK #16 Josh Reddick (X - 52 - 37)
b4.new_ab()
b4.pitch_list("b c s f f b f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: OAK #11 Jarrod Parker
t5 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")

# 9. BOS #26 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("c b c b b")
t5.out("L7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.out("F7")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 8. OAK #15 Seth Smith (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b")
b5.hit(2)
b5.advance(3, "28 G4-3")
b5.advance(4, "5 1B")

# 9. OAK #28 Eric Sogard (X - 15 - X)
b5.new_ab()
b5.pitch_list("s b f")
b5.out("G4-3")

# 1. OAK #4  Coco Crisp (15 - X - X)
b5.new_ab()
b5.pitch_list("b b b c f b")
b5.reach("BB")
b5.error(9)
b5.advance(2, "5 1B")
b5.advance(3, "5 E9")

# 2. OAK #5  John Jaso (15 - X - 4)
b5.new_ab()
b5.hit(1, rbis=1)
b5.thrown_out(2, "20 DP4-6-3", 2, 41)

# 3. OAK #20 Josh Donaldson (4 - X - 5)
b5.new_ab()
b5.out("DP4-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: OAK #11 Jarrod Parker
t6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b")
t6.out("G1-6-3")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4)

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f f")
b6.out("G6-3")

# 6. OAK #37 Brandon Moss (X - X - X)
b6.new_ab()
b6.out("G5-3")

# 7. OAK #16 Josh Reddick (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: OAK #11 Jarrod Parker
t7 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c s b c")
t7.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("G3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 8. OAK #15 Seth Smith (X - X - X)
b7.new_ab()
b7.pitch_list("b f c")
b7.out("G6-3")

# 9. OAK #28 Eric Sogard (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F7")

# 1. OAK #4  Coco Crisp (X - X - X)
b7.new_ab()
b7.pitch_list("b b s")
b7.out("G3-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: OAK #62 Sean Doolittle
t8 = game.new_inning()

# Pitching change (OAK): #62 Sean Doolittle replaces #11 Jarrod Parker
t8.pitching_substitution(62)

# 8. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("b c b")
t8.hit(1)
t8.advance(2, "26 SAC1-4")
t8.advance(3, "2 G4-3")
t8.advance(4, "15 1B")

# 9. BOS #26 Brock Holt (X - X - 10)
t8.new_ab()
t8.pitch_list("c b")
t8.out("SAC1-4")

# 1. BOS #2  Jacoby Ellsbury (X - 10 - X)
t8.new_ab()
t8.pitch_list("s b f b f b")
t8.out("G4-3")

# 2. BOS #18 Shane Victorino (10 - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.reach("HBP")
t8.advance(2, "15 SB")
t8.advance(4, "15 1B")

# Pitching change (OAK): #48 Ryan Cook replaces #62 Sean Doolittle
t8.pitching_substitution(48)

# 3. BOS #15 Dustin Pedroia (10 - X - 18)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1, rbis=2)

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab()
t8.pitch_list("1 f 1 b f b 1 b f c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #40 Andrew Bailey
b8 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #41 John Lackey
b8.pitching_substitution(40)

# 2. OAK #5  John Jaso (X - X - X)
b8.new_ab()
b8.pitch_list("c b b c b b")
b8.reach("BB")

# 3. OAK #20 Josh Donaldson (X - X - 5)
b8.new_ab()
b8.pitch_list("f")
b8.out("F7")

# 4. OAK #8  Jed Lowrie (X - X - 5)
b8.new_ab()
b8.pitch_list("f f b s")
b8.out("K")

# 5. OAK #52 Yoenis Cespedes (X - X - 5)
b8.new_ab()
b8.pitch_list("c s b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: OAK #60 Jesse Chavez
t9 = game.new_inning()

# Pitching change (OAK): #60 Jesse Chavez replaces #48 Ryan Cook
t9.pitching_substitution(60)

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("s b c b f f")
t9.hit(3)
# Offensive change (BOS): Pinch-runner #44 Jackie Bradley Jr. replaces #12 Mike Napoli
t9.offensive_substitution(5, 44, "PR")
t9.atbase("PR")
t9.thrown_out(4, "10 FC3-2", 2, 60)

# 6. BOS #29 Daniel Nava (12 - X - X)
t9.new_ab()
t9.pitch_list("c c f f")
t9.out("G6-3")

# 7. BOS #39 Jarrod Saltalamacchia (44 - X - X)
t9.new_ab()
t9.pitch_list("f f b b b b")
t9.reach("BB")
t9.advance(2, "10 FC3-2")

# 8. BOS #10 Jose Iglesias (44 - X - 39)
t9.new_ab()
t9.pitch_list("b")
t9.reach("FC3-2")

# 9. BOS #26 Brock Holt (X - 39 - 10)
t9.new_ab()
t9.pitch_list("c f")
t9.out("G6-3")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #40 Andrew Bailey
b9.pitching_substitution(19)

# Defensive switch (BOS): #44 Jackie Bradley Jr. moves to LF
b9.defensive_switch(44, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b9.defensive_switch(29, "3")

# 6. OAK #37 Brandon Moss (X - X - X)
b9.new_ab()
b9.pitch_list("s b s t")
b9.out("KT")

# 7. OAK #16 Josh Reddick (X - X - X)
b9.new_ab()
b9.pitch_list("s f f b b c")
b9.out("!K")

# 8. OAK #15 Seth Smith (X - X - X)
b9.new_ab()
b9.pitch_list("f b s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: OAK
# LP: OAK #62 Sean Doolittle
game.losing_pitcher(62)

# print(game)
game.generate_scorecard()
