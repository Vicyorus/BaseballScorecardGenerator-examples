import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ OAK, 2013-07-14
# https://www.baseball-reference.com/boxes/OAK/OAK201307140.shtml
# https://www.mlb.com/gameday/red-sox-vs-athletics/2013/07/14/348155/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-14 16:08-19:42",
        "at": "O.co Coliseum, Oakland, CA",
        "att": "31,417",
        "temp": "61F, Sunny",
        "wind": "12mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 67,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                37: "Mike Carp",
                20: "Ryan Lavarnway",
                26: "Brock Holt",
                10: "Jose Iglesias",
                # Starting pitcher
                67: "Brandon Workman",
                # Bench
                39: "Jarrod Saltalamacchia",
                18: "Shane Victorino",
                12: "Mike Napoli",
                23: "Brandon Snyder",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [37, "3"],
                [20, "2"],
                [26, "5"],
                [10, "6"],
            ],
            "bench": [
                [39, "C"],
                [18, "CF"],
                [12, "1B"],
                [23, "1B"],
            ],
            "bullpen": [40, 41, 32, 66, 31, 36, 19, 38, 54, 22, 46],
        },
        "home": {
            "team": "Oakland Athletics",
            "starter": 40,
            "roster": {
                # Lineup
                4: "Coco Crisp",
                5: "John Jaso",
                20: "Josh Donaldson",
                8: "Jed Lowrie",
                52: "Yoenis Cespedes",
                16: "Josh Reddick",
                37: "Brandon Moss",
                15: "Seth Smith",
                28: "Eric Sogard",
                # Starting pitcher
                40: "Bartolo Colon",
                # Bench
                36: "Derek Norris",
                7: "Nate Freiman",
                35: "Grant Green",
                25: "Chris Young",
                # Bullpen
                50: "Grant Balfour",
                64: "A.J. Griffin",
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
                [4, "8"],
                [5, "2"],
                [20, "5"],
                [8, "6"],
                [52, "7"],
                [16, "9"],
                [37, "3"],
                [15, "0"],
                [28, "4"],
            ],
            "bench": [
                [36, "C"],
                [7, "1B"],
                [35, "2B"],
                [25, "CF"],
            ],
            "bullpen": [50, 64, 60, 11, 48, 54, 62, 57, 47, 61, 13],
        },
        "umpires": {
            "HP": "Todd Tichenor",
            "1B": "Mike Muchlinski",
            "2B": "Bill Miller",
            "3B": "Adam Hamari",
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
# Pitching: OAK #40 Bartolo Colon
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b")
t1.hit(1)
t1.thrown_out(2, "29 DP4-3", 1, 40)

# 2. BOS #29 Daniel Nava (X - X - 2)
t1.new_ab()
t1.pitch_list("c")
t1.out("DP4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c c f f f b f f")
t1.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
t1.new_ab()
t1.pitch_list("c f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #67 Brandon Workman
b1 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b f b c")
b1.out("!K")

# 2. OAK #5  John Jaso (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("F7")

# 3. OAK #20 Josh Donaldson (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: OAK #40 Bartolo Colon
t2 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(2)
t2.advance(3, "20 G5-3")

# 6. BOS #37 Mike Carp (X - 5 - X)
t2.new_ab()
t2.out("L6")

# 7. BOS #20 Ryan Lavarnway (X - 5 - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G5-3")

# 8. BOS #26 Brock Holt (5 - X - X)
t2.new_ab()
t2.pitch_list("b s b b")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #67 Brandon Workman
b2 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
b2.new_ab()
b2.pitch_list("c b c b s")
b2.out("K")

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("(F)P2")

# 6. OAK #16 Josh Reddick (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: OAK #40 Bartolo Colon
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("b c c b")
t3.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b")
t3.out("L9")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b")
t3.out("G3-1")


# Bot 3rd
# Pitching: BOS #67 Brandon Workman
b3 = game.new_inning()

# 7. OAK #37 Brandon Moss (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.out("G6-3")

# 8. OAK #15 Seth Smith (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f f b f")
b3.out("F8")

# 9. OAK #28 Eric Sogard (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: OAK #40 Bartolo Colon
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b f f b b f f")
t4.out("G2-3")

# 5. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("f b f b c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #67 Brandon Workman
b4 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F7")

# 2. OAK #5  John Jaso (X - X - X)
b4.new_ab()
b4.pitch_list("c c b f b f f b f b")
b4.reach("BB")
b4.thrown_out(2, "20 CS", 3, 67)

# 3. OAK #20 Josh Donaldson (X - X - 5)
b4.new_ab()
b4.pitch_list("b c b f f f f b f c")
b4.out("KDP2-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: OAK #40 Bartolo Colon
t5 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t5.new_ab()
t5.pitch_list("b s b s b f")
t5.out("L8")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t5.new_ab()
t5.pitch_list("c b f t")
t5.out("KT")

# 8. BOS #26 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("c s")
t5.out("F7")


# Bot 5th
# Pitching: BOS #67 Brandon Workman
b5 = game.new_inning()

# 4. OAK #8  Jed Lowrie (X - X - X)
b5.new_ab()
b5.pitch_list("b f b")
b5.out("F8")

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f")
b5.out("F8")

# 6. OAK #16 Josh Reddick (X - X - X)
b5.new_ab()
b5.pitch_list("b b s s b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: OAK #40 Bartolo Colon
t6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("f b f f")
t6.hit(1)
t6.advance(3, "29 1B")
t6.advance(4, "15 1B")

# 2. BOS #29 Daniel Nava (X - X - 2)
t6.new_ab()
t6.pitch_list("b 1 b s 1 f")
t6.hit(1)
t6.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t6.new_ab()
t6.pitch_list("b c f b")
t6.hit(1, rbis=1)

# 4. BOS #34 David Ortiz (X - 29 - 15)
t6.new_ab()
t6.out("F7")

# 5. BOS #5  Jonny Gomes (X - 29 - 15)
t6.new_ab()
t6.pitch_list("f c c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #67 Brandon Workman
b6 = game.new_inning()

# 7. OAK #37 Brandon Moss (X - X - X)
b6.new_ab()
b6.pitch_list("b c c b")
b6.out("(F)P2")

# 8. OAK #15 Seth Smith (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("F7")

# 9. OAK #28 Eric Sogard (X - X - X)
b6.new_ab()
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: OAK #40 Bartolo Colon
t7 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f")
t7.hit(2)
t7.advance(3, "20 G6-3")
t7.advance(4, "26 1B")

# 7. BOS #20 Ryan Lavarnway (X - 37 - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("G6-3")

# 8. BOS #26 Brock Holt (37 - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(1, rbis=1)
t7.advance(2, "2 SB")

# Pitching change (OAK): #62 Sean Doolittle replaces #40 Bartolo Colon
t7.pitching_substitution(62)

# 9. BOS #10 Jose Iglesias (X - X - 26)
t7.new_ab()
t7.pitch_list("c 1")
t7.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - X - 26)
t7.new_ab()
t7.pitch_list("s b")
t7.out("(F)P5")


# Bot 7th
# Pitching: BOS #67 Brandon Workman
b7 = game.new_inning()

# 1. OAK #4  Coco Crisp (X - X - X)
b7.new_ab()
b7.pitch_list("b f s f")
b7.hit(1)
b7.advance(4, "20 HR")

# 2. OAK #5  John Jaso (X - X - 4)
b7.new_ab()
b7.pitch_list("c b 1")
b7.out("P6")

# 3. OAK #20 Josh Donaldson (X - X - 4)
b7.new_ab()
b7.pitch_list("b d c s f b 1")
b7.hit(4, rbis=2)

# Pitching change (BOS): #32 Craig Breslow replaces #67 Brandon Workman
b7.pitching_substitution(32)

# 4. OAK #8  Jed Lowrie (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.out("G1-3")

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")

# 6. OAK #16 Josh Reddick (X - X - 52)
b7.new_ab()
b7.pitch_list("f s b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: OAK #62 Sean Doolittle
t8 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c f")
t8.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b b")
t8.reach("BB")
t8.thrown_out(2, "34 DP4-6-3", 2, 62)

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab()
t8.pitch_list("f b s")
t8.out("DP4-6-3")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Offensive change (OAK): Pinch-hitter #7 Nate Freiman replaces #37 Brandon Moss, batting 7th
b8.offensive_substitution(7, 7, "PH")

# 7. OAK #7  Nate Freiman (X - X - X)
b8.new_ab()
b8.hit(1)
b8.thrown_out(2, "28 FC4-6", 2, 32)

# 8. OAK #15 Seth Smith (X - X - 7)
b8.new_ab()
b8.pitch_list("b l b c")
b8.out("L7")

# 9. OAK #28 Eric Sogard (X - X - 7)
b8.new_ab()
b8.reach("FC4-6")

# 1. OAK #4  Coco Crisp (X - X - 28)
b8.new_ab()
b8.pitch_list("c f 1 1 1 d b")
b8.out("L6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: OAK #50 Grant Balfour
t9 = game.new_inning()

# Pitching change (OAK): #50 Grant Balfour replaces #62 Sean Doolittle
t9.pitching_substitution(50)

# Defensive switch (OAK): #7 Nate Freiman moves to 1B
t9.defensive_switch(7, "3")

# 5. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("f b f f f f s")
t9.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("c s b c")
t9.out("!K")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t9.new_ab()
t9.pitch_list("f b s s")
t9.out("K")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b9.pitching_substitution(19)

# Defensive change (BOS): #12 Mike Napoli replaces #5 Jonny Gomes (LF), playing 1B, batting 5th
b9.defensive_substitution(5, 12, "3")

# Defensive switch (BOS): #37 Mike Carp moves to LF
b9.defensive_switch(37, "7")

# 2. OAK #5  John Jaso (X - X - X)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# 3. OAK #20 Josh Donaldson (X - X - X)
b9.new_ab()
b9.pitch_list("b b f s")
b9.out("G5-3")

# 4. OAK #8  Jed Lowrie (X - X - X)
b9.new_ab()
b9.out("B1-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: OAK #48 Ryan Cook
t10 = game.new_inning()

# Pitching change (OAK): #48 Ryan Cook replaces #50 Grant Balfour
t10.pitching_substitution(48)

# 8. BOS #26 Brock Holt (X - X - X)
t10.new_ab()
t10.pitch_list("b c")
t10.out("G3-1")

# 9. BOS #10 Jose Iglesias (X - X - X)
t10.new_ab()
t10.out("P4")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t10.new_ab()
t10.pitch_list("b")
t10.hit(1)

# 2. BOS #29 Daniel Nava (X - X - 2)
t10.new_ab()
t10.pitch_list("f")
t10.out("G4-3")


# Bot 10th
# Pitching: BOS #19 Koji Uehara
b10 = game.new_inning()

# 5. OAK #52 Yoenis Cespedes (X - X - X)
b10.new_ab()
b10.pitch_list("f")
b10.hit(1)
b10.error(6)
b10.advance(2, "E6")
b10.thrown_out(3, "7 CS", 2, 19)

# 6. OAK #16 Josh Reddick (X - 52 - X)
b10.new_ab()
b10.pitch_list("f s b s")
b10.out("K")

# 7. OAK #7  Nate Freiman (X - 52 - X)
b10.new_ab()
b10.pitch_list("2 c c b f b")
b10.out("G6-3")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: OAK #48 Ryan Cook
t11 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t11.new_ab()
t11.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
t11.new_ab()
t11.pitch_list("b b b b")
t11.reach("BB")
t11.advance(2, "37 BB")
# Offensive change (BOS): Pinch-runner #23 Brandon Snyder replaces #34 David Ortiz
t11.offensive_substitution(4, 23, "PR")
t11.atbase("PR")
t11.advance(3, "20 HBP")

# 5. BOS #12 Mike Napoli (X - X - 34)
t11.new_ab()
t11.pitch_list("s b s f c")
t11.out("!K")

# 6. BOS #37 Mike Carp (X - X - 34)
t11.new_ab()
t11.pitch_list("b c b b c b")
t11.reach("BB")
t11.advance(2, "20 HBP")

# 7. BOS #20 Ryan Lavarnway (X - 34 - 37)
t11.new_ab()
t11.reach("HBP")

# 8. BOS #26 Brock Holt (23 - 37 - 20)
t11.new_ab()
t11.pitch_list("c s f c")
t11.out("!K")


# Bot 11th
# Pitching: BOS #38 Matt Thornton
b11 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #19 Koji Uehara
b11.pitching_substitution(38)

# Defensive switch (BOS): #23 Brandon Snyder moves to DH
b11.defensive_switch(23, "0")

# Offensive change (OAK): Pinch-hitter #25 Chris Young replaces #15 Seth Smith, batting 8th
b11.offensive_substitution(8, 25, "PH")

# 8. OAK #25 Chris Young (X - X - X)
b11.new_ab()
b11.pitch_list("b b c f b b")
b11.reach("BB")
b11.advance(2, "28 SAC3-4")
b11.advance(4, "20 1B")

# 9. OAK #28 Eric Sogard (X - X - 25)
b11.new_ab()
b11.pitch_list("b")
b11.out("SAC3-4")

# 1. OAK #4  Coco Crisp (X - 25 - X)
b11.new_ab()
b11.out("G5-3")

# Offensive change (OAK): Pinch-hitter #36 Derek Norris replaces #5 John Jaso, batting 2nd
b11.offensive_substitution(2, 36, "PH")

# 2. OAK #36 Derek Norris (X - 25 - X)
b11.new_ab()
b11.pitch_list("c b b f b d")
b11.reach("BB")
b11.advance(3, "20 1B")

# 3. OAK #20 Josh Donaldson (X - 25 - 36)
b11.new_ab()
b11.pitch_list("b")
b11.hit(1, rbis=1)

# Winning team: OAK
# WP: OAK #48 Ryan Cook
game.winning_pitcher(48)

# Loser team: BOS
# LP: BOS #38 Matt Thornton
game.losing_pitcher(38, is_away_team=True)

# print(game)
game.generate_scorecard()
