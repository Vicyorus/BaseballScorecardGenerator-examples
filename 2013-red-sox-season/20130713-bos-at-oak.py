import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ OAK, 2013-07-13
# https://www.baseball-reference.com/boxes/OAK/OAK201307130.shtml
# https://www.mlb.com/gameday/red-sox-vs-athletics/2013/07/13/348141/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-13 22:07-00:56 +1",
        "at": "O.co Coliseum, Oakland, CA",
        "att": "36,067",
        "temp": "62F, Clear",
        "wind": "5mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
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
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                44: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 32, 38, 22],
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
            "bullpen": [40, 41, 67, 32, 36, 19, 38, 54, 22, 46],
        },
        "home": {
            "team": "Oakland Athletics",
            "starter": 64,
            "roster": {
                # Lineup
                4: "Coco Crisp",
                8: "Jed Lowrie",
                20: "Josh Donaldson",
                52: "Yoenis Cespedes",
                7: "Nate Freiman",
                25: "Chris Young",
                16: "Josh Reddick",
                36: "Derek Norris",
                35: "Grant Green",
                # Starting pitcher
                64: "A.J. Griffin",
                # Bench
                37: "Brandon Moss",
                15: "Seth Smith",
                28: "Eric Sogard",
                5: "John Jaso",
                # Bullpen
                50: "Grant Balfour",
                40: "Bartolo Colon",
                60: "Jesse Chavez",
                11: "Jarrod Parker",
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
                [4, "0"],
                [8, "6"],
                [20, "5"],
                [52, "7"],
                [7, "3"],
                [25, "8"],
                [16, "9"],
                [36, "2"],
                [35, "4"],
            ],
            "bench": [
                [37, "1B"],
                [15, "LF"],
                [28, "2B"],
                [5, "C"],
            ],
            "bullpen": [50, 40, 60, 11, 48, 54, 62, 57, 47, 61, 13],
        },
        "umpires": {
            "HP": "Adam Hamari",
            "1B": "Todd Tichenor",
            "2B": "Mike Muchlinski",
            "3B": "Bill Miller",
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
# Pitching: OAK #64 A.J. Griffin
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("f c s")
t1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b f")
t1.hit(1)
t1.advance(2, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c b")
t1.out("P6")

# 4. BOS #34 David Ortiz (X - X - 18)
t1.new_ab()
t1.pitch_list("b b b c")
t1.hit(1)

# 5. BOS #12 Mike Napoli (X - 18 - 34)
t1.new_ab()
t1.pitch_list("b s b c f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c b c")
b1.out("!K")

# 2. OAK #8  Jed Lowrie (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("(F)P3")

# 3. OAK #20 Josh Donaldson (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b")
b1.out("L4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: OAK #64 A.J. Griffin
t2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c c b b")
t2.out("P5")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b b f b f b")
t2.reach("BB")
t2.thrown_out(2, "10 DP4-3", 2, 64)

# 8. BOS #10 Jose Iglesias (X - X - 39)
t2.new_ab()
t2.pitch_list("c")
t2.out("DP4-3")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. OAK #52 Yoenis Cespedes (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.thrown_out(2, "7 DP6-4-3", 1, 31)

# 5. OAK #7  Nate Freiman (X - X - 52)
b2.new_ab()
b2.pitch_list("c b b s f d")
b2.out("DP6-4-3")

# 6. OAK #25 Chris Young (X - X - X)
b2.new_ab()
b2.pitch_list("l")
b2.hit(1)
b2.advance(2, "16 1B")

# 7. OAK #16 Josh Reddick (X - X - 25)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 8. OAK #36 Derek Norris (X - 25 - 16)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G3-1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: OAK #64 A.J. Griffin
t3 = game.new_inning()

# 9. BOS #26 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.out("F9")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.hit(1)
t3.advance(2, "15 SB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t3.new_ab()
t3.pitch_list("c f f")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 9. OAK #35 Grant Green (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f b c")
b3.out("!K")

# 1. OAK #4  Coco Crisp (X - X - X)
b3.new_ab()
b3.pitch_list("s f")
b3.out("F7")

# 2. OAK #8  Jed Lowrie (X - X - X)
b3.new_ab()
b3.out("L9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: OAK #64 A.J. Griffin
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("s b s")
t4.out("F7")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.hit(2)

# 6. BOS #29 Daniel Nava (X - 12 - X)
t4.new_ab()
t4.pitch_list("b c d b")
t4.out("L7")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F8")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 3. OAK #20 Josh Donaldson (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F7")

# 4. OAK #52 Yoenis Cespedes (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L8")

# 5. OAK #7  Nate Freiman (X - X - X)
b4.new_ab()
b4.pitch_list("f s b f b f b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: OAK #64 A.J. Griffin
t5 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("b b c c f f")
t5.out("G5-3")

# 9. BOS #26 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 26)
t5.new_ab()
t5.pitch_list("b 1 1")
t5.out("F8")

# 2. BOS #18 Shane Victorino (X - X - 26)
t5.new_ab()
t5.pitch_list("1 c b 1")
t5.out("G3")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 6. OAK #25 Chris Young (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("F9")

# 7. OAK #16 Josh Reddick (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 8. OAK #36 Derek Norris (X - X - X)
b5.new_ab()
b5.pitch_list("s f")
b5.hit(4)

# 9. OAK #35 Grant Green (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: OAK #64 A.J. Griffin
t6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c b b")
t6.out("F7")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.error(4)
t6.reach("E4")
t6.advance(3, "29 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
t6.new_ab()
t6.pitch_list("b c c s")
t6.out("K")

# 6. BOS #29 Daniel Nava (X - X - 34)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (34 - X - 29)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F7")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s c")
b6.out("!K")

# 2. OAK #8  Jed Lowrie (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b b b")
b6.reach("BB")
b6.advance(2, "20 1B")
b6.advance(4, "52 1B")

# 3. OAK #20 Josh Donaldson (X - X - 8)
b6.new_ab()
b6.pitch_list("c f")
b6.hit(1)
b6.advance(2, "52 1B")

# 4. OAK #52 Yoenis Cespedes (X - 8 - 20)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(1, rbis=1)

# 5. OAK #7  Nate Freiman (X - 20 - 52)
b6.new_ab()
b6.out("P4")

# 6. OAK #25 Chris Young (X - 20 - 52)
b6.new_ab()
b6.pitch_list("c f")
b6.out("(F)P3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: OAK #64 A.J. Griffin
t7 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G1-6-3")

# 9. BOS #26 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("b b f")
t7.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("b f c b")
t7.out("L8")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 7. OAK #16 Josh Reddick (X - X - X)
b7.new_ab()
b7.pitch_list("b c c b b")
b7.hit(1)
b7.advance(2, "36 BB")
b7.advance(3, "35 (F)F9")
b7.advance(4, "4 1B")

# 8. OAK #36 Derek Norris (X - X - 16)
b7.new_ab()
b7.pitch_list("c d b b b")
b7.reach("BB")
b7.advance(2, "4 1B")

# 9. OAK #35 Grant Green (X - 16 - 36)
b7.new_ab()
b7.pitch_list("b c s b")
b7.out("(F)F9")

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
b7.pitching_substitution(36)

# 1. OAK #4  Coco Crisp (16 - X - 36)
b7.new_ab()
b7.hit(1, rbis=1)

# 2. OAK #8  Jed Lowrie (X - 36 - 4)
b7.new_ab()
b7.pitch_list("f c d f f s")
b7.out("K")

# 3. OAK #20 Josh Donaldson (X - 36 - 4)
b7.new_ab()
b7.pitch_list("b c f f b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: OAK #64 A.J. Griffin
t8 = game.new_inning()

# Defensive change (OAK): #28 Eric Sogard replaces #35 Grant Green (2B), playing 2B, batting 9th
t8.defensive_substitution(9, 28, "4")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("P5")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("b c s")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# 4. OAK #52 Yoenis Cespedes (X - X - X)
b8.new_ab()
b8.pitch_list("b b s t f f")
b8.hit(1)
b8.thrown_out(2, "7 DP6-4-3", 1, 36)

# 5. OAK #7  Nate Freiman (X - X - 52)
b8.new_ab()
b8.pitch_list("b f f d")
b8.out("DP6-4-3")

# 6. OAK #25 Chris Young (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: OAK #50 Grant Balfour
t9 = game.new_inning()

# Pitching change (OAK): #50 Grant Balfour replaces #64 A.J. Griffin
t9.pitching_substitution(50)

# Defensive change (OAK): #37 Brandon Moss replaces #7 Nate Freiman (1B), playing 1B, batting 5th
t9.defensive_substitution(5, 37, "3")

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c c b")
t9.hit(1)
t9.thrown_out(2, "29 FC3-6", 1, 50)

# 6. BOS #29 Daniel Nava (X - X - 12)
t9.new_ab()
t9.pitch_list("b b c")
t9.reach("FC3-6")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t9.new_ab()
t9.pitch_list("d b c b s s")
t9.out("K")

# 8. BOS #10 Jose Iglesias (X - X - 29)
t9.new_ab()
t9.pitch_list("b b c f")
t9.out("(F)P3")

# Winning team: OAK
# WP: OAK #64 A.J. Griffin
game.winning_pitcher(64)
# SV: OAK #50 Grant Balfour
game.save_pitcher(50)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
