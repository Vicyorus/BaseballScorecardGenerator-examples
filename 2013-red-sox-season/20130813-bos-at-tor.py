import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-08-13
# https://www.baseball-reference.com/boxes/TOR/TOR201308130.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/08/13/348526/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-13 19:07-22:44",
        "at": "Rogers Centre, Toronto, ON",
        "att": "32,816",
        "temp": "69F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                26: "Brock Holt",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [12, "3"],
                [7, "6"],
                [39, "2"],
                [16, "5"],
            ],
            "bench": [
                [37, "1B"],
                [26, "2B"],
                [5, "LF"],
                [20, "C"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 19, 62, 22],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 58,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                19: "José Bautista",
                10: "Edwin Encarnación",
                26: "Adam Lind",
                13: "Brett Lawrie",
                3: "Maicer Izturis",
                9: "J.P. Arencibia",
                1: "Emilio Bonifácio",
                # Starting pitcher
                58: "Todd Redmond",
                # Bench
                22: "Josh Thole",
                16: "Mark DeRosa",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                49: "Brad Lincoln",
                62: "Aaron Loup",
                51: "Thad Weber",
                56: "Mark Buehrle",
                37: "Mickey Storey",
                27: "Brett Cecil",
                21: "Sergio Santos",
                44: "Casey Janssen",
                32: "Esmil Rogers",
                38: "Darren Oliver",
            },
            "lefties": [62, 56, 27, 38],
            "lineup": [
                [7, "6"],
                [11, "7"],
                [19, "9"],
                [10, "3"],
                [26, "0"],
                [13, "5"],
                [3, "4"],
                [9, "2"],
                [1, "8"],
            ],
            "bench": [
                [22, "C"],
                [16, "3B"],
            ],
            "bullpen": [43, 45, 49, 62, 51, 56, 37, 27, 21, 44, 32, 38],
        },
        "umpires": {
            "HP": "Tom Hallion",
            "1B": "Phil Cuzzi",
            "2B": "Chris Guccione",
            "3B": "Ron Kulpa",
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
# Pitching: TOR #58 Todd Redmond
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b c f")
t1.out("G6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b f f b f f f")
t1.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
t1.new_ab()
t1.pitch_list("b b c b f f f b")
t1.reach("BB")

# 5. BOS #29 Daniel Nava (X - 15 - 34)
t1.new_ab()
t1.pitch_list("c f")
t1.out("F8")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K")

# 2. TOR #11 Rajai Davis (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F8")

# 3. TOR #19 José Bautista (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("P3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #58 Todd Redmond
t2 = game.new_inning()

# 6. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("P3")

# 7. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f b f c")
t2.out("!K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b s s b f f b")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b c b")
b2.reach("BB")
b2.advance(2, "13 1B")

# 5. TOR #26 Adam Lind (X - X - 10)
b2.new_ab()
b2.out("F8")

# 6. TOR #13 Brett Lawrie (X - X - 10)
b2.new_ab()
b2.hit(1)
b2.thrown_out(2, "3 DP6-4-3", 2, 46)

# 7. TOR #3  Maicer Izturis (X - 10 - 13)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("DP6-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #58 Todd Redmond
t3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b s s f s")
t3.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c s f b c")
t3.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b")
t3.out("P5")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 8. TOR #9  J.P. Arencibia (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("G6-3")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b3.new_ab()
b3.pitch_list("b c f")
b3.out("G4-3")

# 1. TOR #7  José Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("L5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #58 Todd Redmond
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b f c")
t4.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("s c f s")
t4.out("K")

# 5. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b c b f f")
t4.hit(1)

# 6. BOS #12 Mike Napoli (X - X - 29)
t4.new_ab()
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 2. TOR #11 Rajai Davis (X - X - X)
b4.new_ab()
b4.pitch_list("b c f b b f s")
b4.out("K")

# 3. TOR #19 José Bautista (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("(F)P2")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b4.new_ab()
b4.pitch_list("f b f")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #58 Todd Redmond
t5 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("c f b s")
t5.out("K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.hit(2)

# 9. BOS #16 Will Middlebrooks (X - 39 - X)
t5.new_ab()
t5.pitch_list("b c b")
t5.out("G1-3")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - X)
t5.new_ab()
t5.out("F7")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
b5.new_ab()
b5.pitch_list("b c s")
b5.out("G6-3")

# 6. TOR #13 Brett Lawrie (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)
b5.advance(3, "3 L9")
b5.advance(4, "9 1B")

# 7. TOR #3  Maicer Izturis (X - 13 - X)
b5.new_ab()
b5.pitch_list("f c b b b")
b5.out("L9")

# 8. TOR #9  J.P. Arencibia (13 - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1, rbis=1)

# 9. TOR #1  Emilio Bonifácio (X - X - 9)
b5.new_ab()
b5.pitch_list("b c f s")
b5.out("K2-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #58 Todd Redmond
t6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b f b f f")
t6.reach("HBP")
t6.advance(2, "34 1B")
t6.advance(3, "5 BB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t6.new_ab()
t6.pitch_list("c 1 1")
t6.out("F9")

# Pitching change (TOR): #27 Brett Cecil replaces #58 Todd Redmond
t6.pitching_substitution(27)

# 4. BOS #34 David Ortiz (X - X - 18)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.advance(2, "5 BB")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #29 Daniel Nava, batting 5th
t6.offensive_substitution(5, 5, "PH")

# 5. BOS #5  Jonny Gomes (X - 18 - 34)
t6.new_ab()
t6.pitch_list("c f b f b b b")
t6.reach("BB")

# 6. BOS #12 Mike Napoli (18 - 34 - 5)
t6.new_ab()
t6.pitch_list("b s f f c")
t6.out("!K")

# 7. BOS #7  Stephen Drew (18 - 34 - 5)
t6.new_ab()
t6.out("F8")


# Bot 6th
# Pitching: BOS #46 Ryan Dempster
b6 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b6.defensive_switch(5, "7")

# 1. TOR #7  José Reyes (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "11 G1-3")
b6.thrown_out(4, "10 9-2", 3, 46)

# 2. TOR #11 Rajai Davis (X - X - 7)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G1-3")

# 3. TOR #19 José Bautista (X - 7 - X)
b6.new_ab()
b6.pitch_list("f 2 2 b b s s")
b6.out("K")

# 4. TOR #10 Edwin Encarnación (X - 7 - X)
b6.new_ab()
b6.pitch_list("b d c b")
b6.hit(1)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #27 Brett Cecil
t7 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("f f f b f s")
t7.out("K")

# Pitching change (TOR): #21 Sergio Santos replaces #27 Brett Cecil
t7.pitching_substitution(21)

# 9. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(2)
t7.advance(4, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
t7.new_ab()
t7.pitch_list("b s")
t7.hit(1, rbis=1)
t7.advance(2, "18 SB")
t7.advance(3, "18 G6-3")
t7.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t7.new_ab()
t7.pitch_list("1 b f f f")
t7.out("G6-3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1, rbis=1)
t7.advance(2, "34 SB")

# 4. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("c b i i i")
t7.reach("IBB")

# 5. BOS #5  Jonny Gomes (X - 15 - 34)
t7.new_ab()
t7.pitch_list("c b c s")
t7.out("K")


# Bot 7th
# Pitching: BOS #46 Ryan Dempster
b7 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("P6")

# 6. TOR #13 Brett Lawrie (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("F8")

# 7. TOR #3  Maicer Izturis (X - X - X)
b7.new_ab()
b7.pitch_list("c b s")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #45 Neil Wagner
t8 = game.new_inning()

# Pitching change (TOR): #45 Neil Wagner replaces #21 Sergio Santos
t8.pitching_substitution(45)

# 6. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("b s b f s")
t8.out("K")

# 7. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F7")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b c c b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #46 Ryan Dempster
b8.pitching_substitution(36)

# 8. TOR #9  J.P. Arencibia (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b")
b8.hit(4)

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b8.new_ab()
b8.pitch_list("f f b s")
b8.out("K")

# 1. TOR #7  José Reyes (X - X - X)
b8.new_ab()
b8.pitch_list("b s")
b8.out("F8")

# 2. TOR #11 Rajai Davis (X - X - X)
b8.new_ab()
b8.out("B3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #45 Neil Wagner
t9 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("F8")

# Pitching change (TOR): #38 Darren Oliver replaces #45 Neil Wagner
t9.pitching_substitution(38)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("c c b f b")
t9.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c s f")
t9.out("(F)P3")


# Bot 9th
# Pitching: BOS #36 Junichi Tazawa
b9 = game.new_inning()

# 3. TOR #19 José Bautista (X - X - X)
b9.new_ab()
b9.pitch_list("b c b")
b9.hit(1)
b9.advance(2, "10 G5-3")

# 4. TOR #10 Edwin Encarnación (X - X - 19)
b9.new_ab()
b9.pitch_list("b f c f f d")
b9.out("G5-3")

# 5. TOR #26 Adam Lind (X - 19 - X)
b9.new_ab()
b9.pitch_list("i i i i")
b9.reach("IBB")

# 6. TOR #13 Brett Lawrie (X - 19 - 26)
b9.new_ab()
b9.out("(F)P3")

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b9.pitching_substitution(32)

# Offensive change (TOR): Pinch-hitter #16 Mark DeRosa replaces #3 Maicer Izturis, batting 7th
b9.offensive_substitution(7, 16, "PH")

# 7. TOR #16 Mark DeRosa (X - 19 - 26)
b9.new_ab()
b9.pitch_list("b c s b s")
b9.out("K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TOR #44 Casey Janssen
t10 = game.new_inning()

# Pitching change (TOR): #44 Casey Janssen replaces #38 Darren Oliver
t10.pitching_substitution(44)

# Defensive switch (TOR): #16 Mark DeRosa moves to 2B
t10.defensive_switch(16, "4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t10.new_ab()
t10.pitch_list("b b b c")
t10.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t10.new_ab()
t10.pitch_list("c b")
t10.hit(2)
# Offensive change (BOS): Pinch-runner #26 Brock Holt replaces #34 David Ortiz
t10.offensive_substitution(4, 26, "PR")
t10.atbase("PR")

# 5. BOS #5  Jonny Gomes (X - 34 - X)
t10.new_ab()
t10.out("G1-3")

# 6. BOS #12 Mike Napoli (X - 26 - X)
t10.new_ab()
t10.pitch_list("c s d d c")
t10.out("!K")


# Bot 10th
# Pitching: BOS #32 Craig Breslow
b10 = game.new_inning()

# Defensive switch (BOS): #26 Brock Holt moves to DH
b10.defensive_switch(26, "0")

# 8. TOR #9  J.P. Arencibia (X - X - X)
b10.new_ab()
b10.pitch_list("b")
b10.out("L1")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b10.new_ab()
b10.pitch_list("c f b s")
b10.out("K")

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b10.pitching_substitution(19)

# 1. TOR #7  José Reyes (X - X - X)
b10.new_ab()
b10.pitch_list("s f f f s")
b10.out("K")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: TOR #62 Aaron Loup
t11 = game.new_inning()

# Pitching change (TOR): #62 Aaron Loup replaces #44 Casey Janssen
t11.pitching_substitution(62)

# 7. BOS #7  Stephen Drew (X - X - X)
t11.new_ab()
t11.pitch_list("c")
t11.out("F7")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t11.new_ab()
t11.pitch_list("b b f b b")
t11.reach("BB")
t11.advance(2, "16 1B")
t11.advance(3, "2 FC6-4")
t11.advance(4, "18 1B")

# 9. BOS #16 Will Middlebrooks (X - X - 39)
t11.new_ab()
t11.pitch_list("b b")
t11.hit(1)
t11.thrown_out(2, "2 FC6-4", 2, 62)

# 1. BOS #2  Jacoby Ellsbury (X - 39 - 16)
t11.new_ab()
t11.pitch_list("b")
t11.reach("FC6-4")
t11.advance(2, "18 SB")
t11.advance(4, "18 1B")

# 2. BOS #18 Shane Victorino (39 - X - 2)
t11.new_ab()
t11.pitch_list("c b c")
t11.hit(1, rbis=2)
t11.error(2)
t11.advance(2, "15 SB")
t11.advance(3, "15 E2")

# Pitching change (TOR): #49 Brad Lincoln replaces #62 Aaron Loup
t11.pitching_substitution(49)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t11.new_ab()
t11.pitch_list("c b b")
t11.out("F8")


# Bot 11th
# Pitching: BOS #19 Koji Uehara
b11 = game.new_inning()

# 2. TOR #11 Rajai Davis (X - X - X)
b11.new_ab()
b11.pitch_list("b c f f")
b11.out("(F)P3")

# 3. TOR #19 José Bautista (X - X - X)
b11.new_ab()
b11.pitch_list("s b f")
b11.out("G5-3")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b11.new_ab()
b11.pitch_list("b c b f f")
b11.out("G5-3")

# Winning team: BOS
# WP: BOS #19 Koji Uehara
game.winning_pitcher(19, is_away_team=True)

# Loser team: TOR
# LP: TOR #62 Aaron Loup
game.losing_pitcher(62)

# print(game)
game.generate_scorecard()
