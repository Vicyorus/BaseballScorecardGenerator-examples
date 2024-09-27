import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2013-06-23
# https://www.baseball-reference.com/boxes/DET/DET201306230.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2013/06/23/347872/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-23 13:09-16:56",
        "at": "Comerica Park, Detroit, MI",
        "att": "41,507",
        "temp": "86F, Sunny",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                # Bullpen
                64: "Allen Webster",
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [7, "6"],
                [20, "2"],
                [10, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [16, "3B"],
                [29, "LF"],
            ],
            "bullpen": [64, 63, 40, 41, 30, 32, 19, 31, 36, 46],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 35,
            "roster": {
                # Lineup
                14: "Austin Jackson",
                48: "Torii Hunter",
                24: "Miguel Cabrera",
                28: "Prince Fielder",
                41: "Victor Martinez",
                27: "Jhonny Peralta",
                4: "Omar Infante",
                34: "Avisaíl García",
                50: "Bryan Holaday",
                # Starting pitcher
                35: "Justin Verlander",
                # Bench
                39: "Ramon Santiago",
                32: "Don Kelly",
                12: "Andy Dirks",
                55: "Brayan Peña",
                # Bullpen
                40: "Phil Coke",
                33: "Drew Smyly",
                53: "Joaquín Benoit",
                21: "Rick Porcello",
                36: "Luke Putkonen",
                52: "Jose Alvarez",
                38: "Darin Downs",
                37: "Max Scherzer",
                62: "Al Alburquerque",
                58: "Doug Fister",
                57: "Evan Reed",
            },
            "lefties": [40, 33, 52, 38],
            "lineup": [
                [14, "8"],
                [48, "9"],
                [24, "5"],
                [28, "0"],
                [41, "3"],
                [27, "6"],
                [4, "4"],
                [34, "7"],
                [50, "2"],
            ],
            "bench": [
                [39, "SS"],
                [32, "LF"],
                [12, "LF"],
                [55, "C"],
            ],
            "bullpen": [40, 33, 53, 21, 36, 52, 38, 37, 62, 58, 57],
        },
        "umpires": {
            "HP": "Alfonso Márquez",
            "1B": "Scott Barry",
            "2B": "Mike DiMuro",
            "3B": "Ted Barrett",
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
# Pitching: DET #35 Justin Verlander
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b f")
t1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b c f b b b")
t1.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("1 b s f t")
t1.out("KT")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f b b f b")
b1.reach("BB")
b1.advance(2, "48 BB")
b1.advance(4, "24 2B")

# 2. DET #48 Torii Hunter (X - X - 14)
b1.new_ab()
b1.pitch_list("b b 1 b c f b")
b1.reach("BB")
b1.advance(3, "24 2B")
b1.advance(4, "28 G3")

# 3. DET #24 Miguel Cabrera (X - 14 - 48)
b1.new_ab()
b1.pitch_list("b b f b")
b1.hit(2, rbis=1)
b1.advance(3, "28 G3")

# 4. DET #28 Prince Fielder (48 - 24 - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("G3", rbis=1)

# 5. DET #41 Victor Martinez (24 - X - X)
b1.new_ab()
b1.pitch_list("b c c f f")
b1.out("G5-3")

# 6. DET #27 Jhonny Peralta (24 - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #35 Justin Verlander
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b")
t2.hit(1)
t2.advance(2, "7 BB")
t2.advance(4, "20 1B")

# 6. BOS #5  Jonny Gomes (X - X - 12)
t2.new_ab()
t2.pitch_list("b")
t2.out("F8")

# 7. BOS #7  Stephen Drew (X - X - 12)
t2.new_ab()
t2.pitch_list("1 b f s b b f f b")
t2.reach("BB")
t2.advance(2, "20 1B")
t2.advance(3, "10 HBP")
t2.advance(4, "2 SF8")

# 8. BOS #20 Ryan Lavarnway (X - 12 - 7)
t2.new_ab()
t2.pitch_list("b c f")
t2.hit(1, rbis=1)
t2.advance(2, "10 HBP")

# 9. BOS #10 Jose Iglesias (X - 7 - 20)
t2.new_ab()
t2.pitch_list("l b f")
t2.reach("HBP")

# 1. BOS #2  Jacoby Ellsbury (7 - 20 - 10)
t2.new_ab()
t2.pitch_list("f b b")
t2.out("SF8", rbis=1)

# 2. BOS #18 Shane Victorino (X - 20 - 10)
t2.new_ab()
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 7. DET #4  Omar Infante (X - X - X)
b2.new_ab()
b2.pitch_list("b b f f b")
b2.hit(1)
b2.thrown_out(2, "50 POCS", 2, 22)

# 8. DET #34 Avisaíl García (X - X - 4)
b2.new_ab()
b2.pitch_list("b 1 b s b s")
b2.out("F9")

# 9. DET #50 Bryan Holaday (X - X - 4)
b2.new_ab()
b2.pitch_list("f b f f f 1")
b2.hit(1)
b2.advance(3, "14 2B")
b2.advance("U", "48 PB")

# 1. DET #14 Austin Jackson (X - X - 50)
b2.new_ab()
b2.pitch_list("b f b d")
b2.hit(2)
b2.advance(3, "48 PB")

# 2. DET #48 Torii Hunter (50 - 14 - X)
b2.new_ab()
b2.pitch_list("f c b f s")
b2.pb()
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #35 Justin Verlander
t3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b c b c b")
t3.hit(1)
t3.advance(3, "34 1B")
t3.advance(4, "12 FC6-4")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("1 c 1 b b")
t3.hit(1)
t3.thrown_out(2, "12 FC6-4", 1, 35)

# 5. BOS #12 Mike Napoli (15 - X - 34)
t3.new_ab()
t3.pitch_list("c b f f b f f f b f")
t3.reach("FC6-4", rbis=1)

# 6. BOS #5  Jonny Gomes (X - X - 12)
t3.new_ab()
t3.pitch_list("c s b s")
t3.out("K")

# 7. BOS #7  Stephen Drew (X - X - 12)
t3.new_ab()
t3.pitch_list("c f f t")
t3.out("KT")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 3. DET #24 Miguel Cabrera (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")

# 4. DET #28 Prince Fielder (X - X - X)
b3.new_ab()
b3.out("G4-3")

# 5. DET #41 Victor Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #35 Justin Verlander
t4 = game.new_inning()

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b b")
t4.reach("BB")
t4.advance(3, "2 2B")
t4.advance(4, "18 G6-3")

# 9. BOS #10 Jose Iglesias (X - X - 20)
t4.new_ab()
t4.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - 20)
t4.new_ab()
t4.pitch_list("f b f d f b f f f")
t4.hit(2)
t4.advance(3, "18 G6-3")

# 2. BOS #18 Shane Victorino (20 - 2 - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("G6-3", rbis=1)

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t4.new_ab()
t4.out("L9")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 6. DET #27 Jhonny Peralta (X - X - X)
b4.new_ab()
b4.out("F9")

# 7. DET #4  Omar Infante (X - X - X)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.error(6)
b4.advance(2, "34 E6")
b4.advance(3, "14 BB")

# 8. DET #34 Avisaíl García (X - X - 4)
b4.new_ab()
b4.reach("FC6")
b4.advance(2, "14 BB")

# 9. DET #50 Bryan Holaday (X - 4 - 34)
b4.new_ab()
b4.out("F9")

# 1. DET #14 Austin Jackson (X - 4 - 34)
b4.new_ab()
b4.pitch_list("b b b c c f b")
b4.reach("BB")

# 2. DET #48 Torii Hunter (4 - 34 - 14)
b4.new_ab()
b4.pitch_list("b s f f")
b4.out("(F)F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #35 Justin Verlander
t5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b b b f")
t5.hit(1)
t5.advance(2, "7 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
t5.new_ab()
t5.pitch_list("b f")
t5.out("L9")

# 6. BOS #5  Jonny Gomes (X - X - 34)
t5.new_ab()
t5.pitch_list("b c 1 b")
t5.out("F9")

# 7. BOS #7  Stephen Drew (X - X - 34)
t5.new_ab()
t5.hit(1)

# 8. BOS #20 Ryan Lavarnway (X - 34 - 7)
t5.new_ab()
t5.pitch_list("c c d d f f c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 3. DET #24 Miguel Cabrera (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b")
b5.out("P4")

# 4. DET #28 Prince Fielder (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f s")
b5.out("K")

# 5. DET #41 Victor Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b b c c b f f f")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #33 Drew Smyly
t6 = game.new_inning()

# Pitching change (DET): #33 Drew Smyly replaces #35 Justin Verlander
t6.pitching_substitution(33)

# 9. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G3-1")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #36 Junichi Tazawa
b6 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #22 Felix Doubront
b6.pitching_substitution(36)

# 6. DET #27 Jhonny Peralta (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b b b")
b6.reach("BB")

# 7. DET #4  Omar Infante (X - X - 27)
b6.new_ab()
b6.pitch_list("f s f s")
b6.out("K")

# 8. DET #34 Avisaíl García (X - X - 27)
b6.new_ab()
b6.pitch_list("b c s")
b6.out("F9")

# 9. DET #50 Bryan Holaday (X - X - 27)
b6.new_ab()
b6.pitch_list("c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #33 Drew Smyly
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)
t7.advance(2, "34 1B")
t7.advance(3, "12 F7")

# 4. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("1 1 c 1")
t7.hit(1)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t7.new_ab()
t7.pitch_list("f b s f")
t7.out("F7")

# 6. BOS #5  Jonny Gomes (15 - X - 34)
t7.new_ab()
t7.pitch_list("b")
t7.out("(F)P3")

# 7. BOS #7  Stephen Drew (15 - X - 34)
t7.new_ab()
t7.pitch_list("c")
t7.out("P6")


# Bot 7th
# Pitching: BOS #40 Andrew Bailey
b7 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa
b7.pitching_substitution(40)

# 1. DET #14 Austin Jackson (X - X - X)
b7.new_ab()
b7.pitch_list("b c b f")
b7.hit(1)
b7.advance(2, "24 1B")
b7.advance(3, "28 1B")
b7.advance(4, "27 HBP")

# 2. DET #48 Torii Hunter (X - X - 14)
b7.new_ab()
b7.pitch_list("1 s")
b7.out("L4-3")

# 3. DET #24 Miguel Cabrera (X - X - 14)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1)
b7.advance(2, "28 1B")
b7.advance(3, "27 HBP")

# Pitching change (BOS): #30 Andrew Miller replaces #40 Andrew Bailey
b7.pitching_substitution(30)

# 4. DET #28 Prince Fielder (X - 14 - 24)
b7.new_ab()
b7.pitch_list("b f b")
b7.hit(1)
b7.advance(2, "27 HBP")

# 5. DET #41 Victor Martinez (14 - 24 - 28)
b7.new_ab()
b7.pitch_list("f f f f t")
b7.out("KT")

# 6. DET #27 Jhonny Peralta (14 - 24 - 28)
b7.new_ab()
b7.pitch_list("s s")
b7.reach("HBP", rbis=1)
b7.thrown_out(2, "4 FC5-4", 3, 30)

# 7. DET #4  Omar Infante (24 - 28 - 27)
b7.new_ab()
b7.pitch_list("b c f")
b7.reach("FC5-4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #33 Drew Smyly
t8 = game.new_inning()

# 8. BOS #20 Ryan Lavarnway (X - X - X)
t8.new_ab()
t8.pitch_list("b c c f b b f")
t8.out("L7")

# 9. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b")
t8.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.hit(1)
t8.advance(2, "29 SB")

# Pitching change (DET): #53 Joaquín Benoit replaces #33 Drew Smyly
t8.pitching_substitution(53)

# Offensive change (BOS): Pinch-hitter #29 Daniel Nava replaces #18 Shane Victorino, batting 2nd
t8.offensive_substitution(2, 29, "PH")

# 2. BOS #29 Daniel Nava (X - X - 2)
t8.new_ab()
t8.pitch_list("d c s f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #30 Andrew Miller
b8 = game.new_inning()

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b8.defensive_switch(29, "9")

# 8. DET #34 Avisaíl García (X - X - X)
b8.new_ab()
b8.error(9)
b8.reach("E9", end_base=2)
b8.advance(3, "50 SAC1")
b8.advance("U", "48 SF8")

# 9. DET #50 Bryan Holaday (X - 34 - X)
b8.new_ab()
b8.pitch_list("c")
b8.error(1)
b8.reach("SAC1")
b8.advance(2, "14 BB")
b8.advance(3, "48 SF8")
b8.advance("U", "28 1B")

# 1. DET #14 Austin Jackson (34 - X - 50)
b8.new_ab()
b8.pitch_list("b b c b b")
b8.reach("BB")
b8.advance(2, "24 IBB")
b8.advance("U", "28 1B")

# Pitching change (BOS): #63 Alex Wilson replaces #30 Andrew Miller
b8.pitching_substitution(63)

# 2. DET #48 Torii Hunter (34 - 50 - 14)
b8.new_ab()
b8.pitch_list("f f b")
b8.out("SF8", rbis=1)

# 3. DET #24 Miguel Cabrera (50 - X - 14)
b8.new_ab()
b8.pitch_list("b b i i")
b8.reach("IBB")
b8.advance(2, "28 1B")

# Pitching change (BOS): #32 Craig Breslow replaces #63 Alex Wilson
b8.pitching_substitution(32)

# 4. DET #28 Prince Fielder (50 - 14 - 24)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1, rbis=2)
b8.thrown_out(2, "41 DP1-6-4-3", 2, 32)

# 5. DET #41 Victor Martinez (X - 24 - 28)
b8.new_ab()
b8.pitch_list("b d s")
b8.out("DP1-6-4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #53 Joaquín Benoit
t9 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b c b t")
t9.hit(1)
t9.advance(2, "34 DI")
t9.advance(4, "5 2B")

# 4. BOS #34 David Ortiz (X - X - 15)
t9.new_ab()
t9.pitch_list("c b f b s")
t9.out("K")

# 5. BOS #12 Mike Napoli (X - 15 - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("L8")

# 6. BOS #5  Jonny Gomes (X - 15 - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(2, rbis=1)

# 7. BOS #7  Stephen Drew (X - 5 - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("L9")

# Winning team: DET
# WP: DET #53 Joaquín Benoit
game.winning_pitcher(53)

# Loser team: BOS
# LP: BOS #30 Andrew Miller
game.losing_pitcher(30, is_away_team=True)

# print(game)
game.generate_scorecard()
